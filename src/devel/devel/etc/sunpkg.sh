## $(#) i.template.sh 1.7 02/05/13 SMI

NAME="i.none"
FILELIST=${PKGSAV:?undefined}/filelist
BD=${BASEDIR:-/}


is_an_archive=0
is_a_filelist=0
list_empty=1
local_install=0
Spcl_init=0
Rm_alt_sav=0
Tmp_xpath=/usr/tmp$$dir

MV_xpath=/usr/bin
MV_cmd=$MV_xpath/mv
CPIO_xpath=/usr/bin
CPIO_cmd=$CPIO_xpath/cpio
UNZIP_xpath=/usr/bin
UNZIP_cmd=$UNZIP_xpath/unzip
BZCAT_xpath=/usr/bin
BZCAT_cmd=$BZCAT_xpath/bzcat
ZCAT_xpath=/usr/bin
ZCAT_cmd=$ZCAT_xpath/zcat
LN_xpath=/usr/bin
LN_cmd=$LN_xpath/ln
NAWK_xpath=/usr/bin
NAWK_cmd=$NAWK_xpath/nawk
RM_xpath=/usr/bin
RM_cmd=$RM_xpath/rm



eval_pkg() {
	read path	# get the package source directory

	if [ ${path:-NULL} != NULL ]; then
		PKGSRC=${path:?undefined}

		

		if [ -r $PKGSRC/archive/none -o \
			-r $PKGSRC/archive/none.Z -o \
			-r $PKGSRC/archive/none.bz2 ]; then
			is_an_archive=1
		fi
	else
		exit 0	# empty pipe, we're done
	fi

}


eval_pkg

if [ "$is_an_archive" -eq 0 ]; then
	echo "ERROR : $NAME cannot find archived files in $PKGSRC/archive."
	exit 1
fi

Reloc_Arch=$PKGSRC/archive/none

if [ ! -d "$PKGSAV" ]; then
	echo "WARNING : $NAME cannot find save directory $PKGSAV."
	PKGSAV=$Tmp_xpath/$PKG.sav

	if [ ! -d "$PKGSAV" ]; then
		/usr/bin/mkdir $PKGSAV
	fi

	if [ $? -eq 0 ]; then
		echo "  Using alternate save directory" $PKGSAV
		FILELIST=$PKGSAV/filelist
		Rm_alt_sav=1
	else
		echo "ERROR : cannot create alternate save directory" $PKGSAV
		exit 1
	fi
fi

if [ -f "$FILELIST" ]; then
	rm $FILELIST
fi

cd $BD

if [ ${PKG_INIT_INSTALL:-null} = null ]; then
	is_a_filelist=1
	while	read path
	do
		
		echo $path >> $FILELIST
		list_empty=0
	done
fi


if [ ! -x "$BZCAT_cmd" ]; then
	echo "Cannot find required executable $BZCAT_cmd"
	exit 1
fi
if [ "$is_a_filelist" -eq 1 ]; then
	$BZCAT_cmd "$Reloc_Arch".bz2 | $CPIO_cmd -C 512 -idukm -E $FILELIST
	status=$?
	if [ "$status" -ne 0 ]; then
		echo "Unarchiving of $Reloc_Arch failed with error $status"
		exit 1
	fi
else
	$BZCAT_cmd "$Reloc_Arch".bz2 | $CPIO_cmd -C 512 -idukm
	status=$?
	if [ "$status" -ne 0 ]; then
		echo "Unarchiving of $Reloc_Arch failed with error $status"
		exit 1
	fi
fi


if [ -f "$FILELIST" ]; then
	$RM_cmd $FILELIST
fi

if [ "$Rm_alt_sav" -eq 1 ]; then
	$RM_cmd -r $PKGSAV
fi


exit 0
