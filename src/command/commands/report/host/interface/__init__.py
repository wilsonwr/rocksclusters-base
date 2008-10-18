# $Id: __init__.py,v 1.2 2008/10/18 00:55:56 mjk Exp $
# 
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		           version 5.1  (VI)
# 
# Copyright (c) 2000 - 2008 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: __init__.py,v $
# Revision 1.2  2008/10/18 00:55:56  mjk
# copyright 5.1
#
# Revision 1.1  2008/09/23 01:10:18  bruno
# moved 'rocks.config.host.interface|network' to
# moved 'rocks.report.host.interface|network'
#
#

import rocks.commands

class Command(rocks.commands.report.host.command):
	"""
	Output the network configuration file for a host's interface.

	<arg type='string' name='host'>
	One host name.
	</arg>

	<param type='string' name='iface'>
	Output a configuration file for this host's interface (e.g. 'eth0').
	If no 'iface' parameter is supplied, then configuration files
	for every interface defined for the host will be output (and each
	file will be delineated by &lt;file&gt; and &lt;/file&gt; tags).
	</param>

	<example cmd='report host interface compute-0-0 iface=eth0'>
	Output a network configuration file for compute-0-0's eth0 interface.
	</example>
	"""

	def isPhysicalHost(self, host):
		#
		# determine if this is 'physical' machine, that is, not a VM.
		#
		rows = self.db.execute("""select vn.id from vm_nodes vn, nodes n
			where n.name = '%s' and vn.node = n.id""" % (host))

		if rows == 0:
			#
			# this host is *not* in the VM nodes table, so it is
			# a physical host
			#
			retval = 1
		else:
			retval = 0

		return retval


	def writeConfig(self, mac, ip, device, gateway, netmask, vlanid, host):
		configured = 0

		self.addOutput('', 'DEVICE=%s' % device)

		if mac:
			self.addOutput('', 'HWADDR=%s' % mac)

		if ip and netmask:
			self.addOutput('', 'IPADDR=%s' % ip)
			self.addOutput('', 'NETMASK=%s' % netmask)
			self.addOutput('', 'BOOTPROTO=static')
			if gateway:
				self.addOutput('', 'GATEWAY=%s' % gateway)
			self.addOutput('', 'ONBOOT=yes')
			configured = 1

		if vlanid and self.isPhysicalHost(host):
			self.addOutput('', 'VLAN=yes')
			self.addOutput('', 'ONBOOT=yes')
			configured = 1

		if not configured:
			self.addOutput('', 'BOOTPROTO=none')
			self.addOutput('', 'ONBOOT=no')
		

	def writeModprobe(self, device, module):
		if not module:
			return

		self.addOutput('', '<![CDATA[')
		self.addOutput('', 'grep -v "\<%s\>" /etc/modprobe.conf > /tmp/modprobe.conf' % (device))
		self.addOutput('', "echo 'alias %s %s' >> /tmp/modprobe.conf" % (device, module))
		self.addOutput('', 'mv /tmp/modprobe.conf /etc/modprobe.conf')
		self.addOutput('', 'chmod 444 /etc/modprobe.conf')
		self.addOutput('', ']]>')


	def run(self, params, args):
		self.iface, = self.fillParams([('iface', ), ])

                hosts = self.getHostnames(args)

		#
		# only takes one host
		#
		if len(hosts) != 1:
			return

		host = hosts[0]

		mac = None
		ip = None
		netmask = None
		bootproto = None
		gateway = None

		self.db.execute("select os from nodes where " +\
				"name='%s'" % (host))
		osname = self.db.fetchone()[0].strip()
		f = getattr(self, 'run_%s' % (osname))
		self.beginOutput()
		f(host)
		self.endOutput()

	def run_sunos(self, host):
		self.db.execute("select networks.ip, networks.device " +\
				"from networks, nodes where "	+\
				"nodes.name='%s' " % (host)	+\
				"and networks.node=nodes.id")

		for row in self.db.fetchall():
			(ip, device) = row
			if ip is not None:
				self.write_host_file_sunos(ip, device)
		
	def write_host_file_sunos(self, ip, device):
		s = '<file name="/etc/hostname.%s">\n' % device
		s += "%s\n" % ip
		s += '</file>\n'
		self.addText(s)
		
	def run_linux(self, host):
		self.db.execute("""select distinctrow net.mac, net.ip,
			net.device, net.gateway,
			if(net.subnet, s.netmask, NULL), net.vlanid,
			net.subnet, net.module from
			networks net, nodes n, subnets s where net.node = n.id
			and if(net.subnet, net.subnet = s.id, true) and
			n.name = "%s" order by net.id""" % (host))


		for row in self.db.fetchall():
			mac,ip,device,gateway,netmask,vlanid,subnetid,module \
				= row

			if device and device[0:4] != 'vlan':
				#
				# output a script to update modprobe.conf
				#
				self.writeModprobe(device, module)

			if vlanid and self.isPhysicalHost(host):
				#
				# look up the name of the interface that
				# maps to this VLAN spec
				#
				rows = self.db.execute("""select net.device from
					networks net, nodes n where
					n.id = net.node and n.name = '%s'
					and net.subnet = %d and
					net.device not like 'vlan%%' """ %
					(host, subnetid))

				if rows:
					dev, = self.db.fetchone()
					#
					# check if already referencing 
					# a physical device
					#
					if dev != device:
						device = '%s.%d' % (dev, vlanid)

			if self.iface:
				if self.iface == device:
					self.writeConfig(mac, ip, device,
						gateway, netmask, vlanid, host)
			else:
				s = '<file name="'
				s += '/etc/sysconfig/network-scripts/ifcfg-'
				s += '%s">' % (device)

				self.addOutput('', s)
				self.writeConfig(mac, ip, device, gateway,
					netmask, vlanid, host)
				self.addOutput('', '</file>')
