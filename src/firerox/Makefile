# --------------------------------------------------- -*- Makefile -*- --
# $Id: Makefile,v 1.27 2012/11/27 00:48:35 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 
# Copyright (c) 2000 - 2014 The Regents of the University of California.
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
# $Log: Makefile,v $
# Revision 1.27  2012/11/27 00:48:35  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.26  2012/05/06 05:48:42  phil
# Copyright Storm for Mamba
#
# Revision 1.25  2012/04/04 15:51:04  phil
# Hmmm... Trying another combination to see if we can get a common build
# for 5 and 6.
#
# Revision 1.24  2012/03/27 18:38:28  phil
# For 5, revert to older version of firefox
#
# Revision 1.23  2012/03/21 16:51:42  phil
# Updated firefox to build on Centos6 32-bit. Needs testing.
#
# Revision 1.22  2011/07/23 02:30:44  phil
# Viper Copyright
#
# Revision 1.21  2010/09/07 23:53:06  bruno
# star power for gb
#
# Revision 1.20  2010/06/22 21:26:23  mjk
# Build env is now from src/devel package, nothing outside of base roll.
#
# Revision 1.19  2009/10/28 22:28:03  bruno
# add user.js
#
# Revision 1.18  2009/10/25 18:36:38  bruno
# make sure firefox builds for i386 too
#
# Revision 1.17  2009/10/16 17:15:47  bruno
# really get rid of the tab bar
#
# Revision 1.16  2009/10/08 20:55:41  bruno
# make prettier
#
# Revision 1.15  2009/10/07 17:41:47  bruno
# don't patch
#
# Revision 1.14  2009/10/05 21:29:41  bruno
# fixes to build new version of firefox
#
# Revision 1.13  2009/10/03 00:19:40  bruno
# can build compute nodes with RHEL 5.4
#
# Revision 1.12  2009/05/01 19:07:05  mjk
# chimi con queso
#
# Revision 1.11  2008/10/18 00:55:59  mjk
# copyright 5.1
#
# Revision 1.10  2008/03/06 23:41:41  mjk
# copyright storm on
#
# Revision 1.9  2007/08/14 22:07:32  bruno
# update firefox for RHEL 5
#
# Revision 1.8  2007/06/23 04:03:22  mjk
# mars hill copyright
#
# Revision 1.7  2006/12/06 00:20:20  anoop
# All the Makefiles get a bit of an overhaul
#
# $(INSTALL) is used instead of install
# $(MAKE) is used instead of make or gmake
# $(TAR) is used instead of tar of gtar
#
# The mode argument for the $(INSTALL) command needs to be numeric and
# follow the convention of
#
# install [-cs] [-g group] [-m mode] [-o owner] file ...  destination
# install  -d   [-g group] [-m mode] [-o owner] dir
#
# This is portable across solaris and linux.
#
# Finally "tar xzf $TARFILE.tar.gz" is replaced with "gunzip -c $TARFILE.tar.gz | tar -xf -"
# This is again done for portability.
#
# This needs to be the convention from now on.
#
# Revision 1.6  2006/12/02 01:04:54  anoop
# Ridiculously big ass commit.
# Also known as the week after thanksgiving 2006. Or "The day Anoop
# broke Rocks".
#
# Main Changes.
#
# 1. Added a roll-profile.mk file. This is meant as a makefile for building
# the profile rpm containing all the XML files meant for the roll. This is a
# breakaway from the spec.in file method of building the profile RPM.
#
# 2. The variable PWD is now changed to CURDIR. The main reason for this is
# PWD is supplied by the shell. CURDIR is the variable supplied by gmake itself.
# This means we can have a slightly more platform independant way of doing things.
# Also Solaris was failing to set PWD correctly in the source directories, wreaking
# havoc on the location of the BUILD and PKG directories.
#
# Revision 1.5  2006/09/11 22:47:09  mjk
# monkey face copyright
#
# Revision 1.4  2006/08/10 00:09:32  mjk
# 4.2 copyright
#
# Revision 1.3  2006/06/05 17:57:37  bruno
# first steps towards 4.2 beta
#
# Revision 1.2  2006/03/16 17:34:00  bruno
# added preferences to remove toolbars and to not warn about insecure form
# posting
#
# Revision 1.1  2006/02/02 03:54:46  bruno
# the installer web browser is ready
#
# Revision 1.1  2005/12/31 07:50:53  mjk
# build python from source
#

PKGROOT		= /opt/rocks
REDHAT.ROOT     = $(CURDIR)/../../
ROCKSROOT       = ../devel/devel
NATIVEARCH	= $(shell /bin/arch)

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk


build:
	$(TAR) jfx firefox-$(FIREFOX_VERSION).source.tar.bz2
	( 								\
		cd mozilla-$(MOZILLA_VERSION);				\
		cp ../mozconfig .mozconfig;				\
		$(MAKE) -j 4 -f client.mk build;				\
	)

install::
	(								\
		cd mozilla-$(MOZILLA_VERSION);				\
		$(MAKE) -j 4  package;					\
	)
	mkdir -p $(ROOT)/$(PKGROOT)
	(								\
		cd mozilla-$(MOZILLA_VERSION)/dist;			\
		tar jxf 						\
		 firefox-$(FIREFOX_VERSION).en-US.linux-$(NATIVEARCH).tar.bz2 \
			-C $(ROOT)/$(PKGROOT)/;				\
	)
	cp userChrome.css $(ROOT)/$(PKGROOT)/firefox/defaults/profile/chrome
	cp user.js $(ROOT)/$(PKGROOT)/firefox/defaults/profile
	mv $(ROOT)/$(PKGROOT)/firefox $(ROOT)/$(PKGROOT)/firerox


clean::
	rm -rf mozilla-$(MOZILLA_VERSION)
	rm -f $(NAME).spec.in

