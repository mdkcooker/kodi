
%define name	xbmc
%define branch_release	dharma
%define extra_feature	pvr
%define version	10.1
%define snap	0
%define rel	2

%if %snap
%define branch	%branch_release.%extra_feature
%else
%define branch	%extra_feature
%endif

%define branchr	%([ "%branch" ] && echo .%branch | tr - _)

# There are some compatibility issues with the various python addons which
# are mostly tested against bundled python only, and there are too many of
# them to be checked out and fixed by us for system python compatibility.
# Additional issues are caused by the bundled python having several system
# calls redirected through xbmc VFS layer, which doesn't currently work when
# using the system python. Usage of system python can probably be safely
# re-enabled when XBMC upstream migrates away from python 2.4 and fixes the
# issues regarding external python (this is planned). -Anssi 11/2010
%define system_python	0

%if %mdkversion >= 201100
# using system python2.7+ reportedly causes problems with 
# getcwd() and chdir() calls from python
# http://trac.xbmc.org/ticket/8658
%define system_python	0
%endif

Summary:	XBMC Media Center - media player and home entertainment system
Name:		%{name}
Version:	%{version}
%if %snap
Release:	%mkrel 0.svn%snap%branchr.%rel
# REV=$(git log -1 origin/Dharma | grep git-svn-id | sed -ne 's,^.*@\([^ ]\+\).*$,\1,p')
# git archive --prefix=xbmc-dharma-$REV/ origin/Dharma | xz > xbmc-dharma-$REV.tar.xz
Source:		%{name}-%branch_release-%snap.tar.xz
%else
Release:	%mkrel 1.%branch.%rel
Source:		%{name}-%{version}.tar.gz
%endif
URL:		http://xbmc.org/

# needed modules when using bundled python (versions are those expected by the Makefiles):
Source11:	http://www.effbot.org/downloads/Imaging-1.1.7.tar.gz
Source12:	http://pysqlite.googlecode.com/files/pysqlite-2.5.6.tar.gz

# bring snapshot up-to-date with pvr branch
# https://github.com/opdenkamp/xbmc/tree/Dharma-pvr
Patch0:		xbmc-10.0-opdenkamp-pvr-fdb057b7754.patch

# bring snapshot up-to-date with main branch (patches rediffed for pvr):
# already up-to-date
#Patch18:	xbmc-dharma-r35305-r%svnsnap.patch

# VDPAU backports from upstream master
Patch31:	0001-changed-split-CDVDVideoCodecFFmpeg-GetPicture.patch
Patch32:	0002-fixed-VDPAU-temporal-deinterlacer-was-not-provided-e.patch
Patch33:	0003-changed-allow-VDPAU-reverse-telecine-when-deinterlac.patch
Patch34:	0004-fixed-VDPAU-reverse-telecine.patch
Patch35:	0005-changed-enable-VDPAU-temporal-deinterlacer-when-temp.patch
Patch36:	0006-fixed-flush-VDPAU-video-surfaces-and-picture-queue-w.patch
Patch37:	0007-fixed-picture.iDuration-0-comparison.patch
Patch38:	0008-fixed-vdpau-needs-to-memset-its-DVDVideoPicture-stru.patch

# backports from upstream master
Patch40:	0001-added-note-in-linux-crashlog-if-gdb-is-not-installed.patch
Patch41:	0001-Added-9763-Fix-64-bit-WiiRemote-connection-issues-Th.patch

# backports from upstream stable branch
Patch51:	0001-dvdplayer-fix-build-with-gcc-4.6.-Flags-to-the-Linke.patch

# Disable updates of the default skin. Our one is the PVR version, while the
# one in the XBMC.org addon repository would be the vanilla one (Confluence
# is currently not in the addon repository, though, as of 2010-10).
Patch60:	xbmc-disable-confluence-update.patch

# Workaround http://www.nvnews.net/vbulletin/showthread.php?t=156665
# by forcing SDL to use alsa when pulse is disabled and nvidia proprietary
# driver version 260.x.y older than 260.19.21 is active.
Patch61:	0001-added-workaround-for-crash-with-nonpulse-nvidia260.patch

# forkpty and openpty are in -lutil
Patch62:	0001-fixed-undefined-symbols-in-internal-python.patch

# Ensure backward-compatibility with pvr-testing2 and prevent future compatibility
# issues with trunk Addons database format
Patch63:	0001-changed-use-the-legacy-pvr-testing2-addon-database.patch

# Do not use avg_frame_rate for mkv files on 2010.1 and older, instead
# use time_base if needed (fixes MicroDVD subtitles with 23.976 H.264 mkv)
Patch65:	xbmc-old-libavformat-mkv-subs.patch

# build faad support with internal headers, but do not build the
# internal library; use system lib with dlopen instead;
# this allows keeping it as an optional external library
Patch70:	xbmc-hack-ext-faad-with-int-headers.patch

# CVE fixes for the internal python
Patch81:	0001-fixed-CVE-2007-2052-in-internal-python-Mandriva.patch
Patch82:	0002-fixed-CVE-2007-4965-in-internal-python-upstream.patch
Patch83:	0003-fixed-CVE-2008-1679-in-internal-python-upstream.patch
Patch84:	0004-fixed-CVE-2008-1887-in-internal-python-upstream.patch
Patch85:	0005-fixed-CVE-2008-1721-in-internal-python-upstream.patch
Patch86:	0006-fixed-CVE-2008-2315-in-internal-python-Gentoo.patch
Patch87:	0007-fixed-CVE-2008-3142-in-internal-python-Gentoo.patch
Patch88:	0008-fixed-CVE-2008-3144-in-internal-python-Gentoo.patch
Patch89:	0009-fixed-CVE-2008-4864-in-internal-python-Mandriva.patch
Patch90:	0010-fixed-CVE-2008-5031-in-internal-python-upstream.patch
Patch91:	0011-fixed-CVE-2010-1634-in-internal-python-Mandriva.patch
Patch92:	0012-fixed-CVE-2010-2089-in-internal-python-Mandriva.patch
Patch93:	0013-fixed-CVE-2009-2625-in-internal-python-Mandriva.patch
Patch94:	0014-fixed-CVE-2010-3492-in-internal-python-Mandriva.patch
Patch95:	0015-fixed-CVE-2010-3493-in-internal-python-Mandriva.patch

# nosefart audio plugin and RSXS-0.9 based screensavers are GPLv2 only
# libhts, libhdhomerun and several eventclients are GPLv3+
# the rest is GPLv2+
License:	GPLv3+ and GPLv2+ and GPLv2
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	boost-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libmpeg2dec-devel
BuildRequires:	libogg-devel
BuildRequires:	libwavpack-devel
BuildRequires:	python-devel
BuildRequires:	glew-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	libmad-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libvorbis-devel
BuildRequires:	bzip2-devel
BuildRequires:	mysql-devel
BuildRequires:	liblzo2-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	fontconfig-devel
BuildRequires:	fribidi-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libpng-devel
BuildRequires:	libpcre-devel
BuildRequires:	libcdio-devel
BuildRequires:	libmms-devel
BuildRequires:	freetype2-devel
BuildRequires:	libflac-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libjasper-devel
BuildRequires:	libtiff-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libalsa-devel
BuildRequires:	enca-devel
BuildRequires:	libxt-devel
BuildRequires:	libxtst-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libcurl-devel
BuildRequires:	dbus-devel
BuildRequires:	hal-devel
BuildRequires:	SDL-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	avahi-common-devel
BuildRequires:	avahi-client-devel
BuildRequires:	libxrandr-devel
BuildRequires:	vdpau-devel
BuildRequires:	cwiid-devel
BuildRequires:	libice-devel
BuildRequires:	libx11-devel
BuildRequires:	crystalhd-devel
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libmodplug-devel
BuildRequires:	ssh-devel
BuildRequires:	libva-devel
BuildRequires:	gettext-devel
BuildRequires:	expat-devel
BuildRequires:	libass-devel
BuildRequires:	rtmp-devel
BuildRequires:	bluray-devel
BuildRequires:	bluez-devel
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
%ifarch %ix86
BuildRequires:	nasm
%endif
%if !%system_python
# python-imaging
BuildRequires:	lcms-devel
%endif
Requires:	lsb-release
# dlopened (existence check required by rpm5 as it doesn't use stderr):
%define dlopenreq() %([ -e %{_libdir}/lib%{1}.so ] && rpm -qf --qf '%%{name}' $(readlink -f %{_libdir}/lib%{1}.so) 2>/dev/null || echo %{name})
Requires:	%dlopenreq curl
Requires:	%dlopenreq FLAC
Requires:	%dlopenreq mad
Requires:	%dlopenreq ogg
Requires:	%dlopenreq vorbis
Requires:	%dlopenreq vorbisenc
Requires:	%dlopenreq vorbisfile
Requires:	%dlopenreq modplug
Requires:	%dlopenreq rtmp
# not nearly as common as the above, so just suggest instead for now:
Suggests:	%dlopenreq bluray
Suggests:	%dlopenreq crystalhd
# for FEH.py, to check current configuration is ok for xbmc:
Requires:	xdpyinfo
%if %{mdkversion} >= 201010
Requires:	glxinfo
%else
Requires:	mesa-demos
%endif
# for FEH.py to allow it to give an error message (should be available already
# on most systems):
Requires:	pygtk2
%if %system_python
# for xbmc python scripts:
Requires:	python-imaging
Requires:	python-sqlite2
%endif
# Packages not shipped by Mandriva:
Suggests:	%{_lib}faad2_2
Suggests:	%{_lib}lame0
Suggests:	%{_lib}dca0
Suggests:	%{_lib}dvdcss2

# Packages have been merged
Obsoletes:	xbmc-core < 9.11-1.svn29468
Obsoletes:	xbmc-skin-confluence < 9.11-1.svn29468
Obsoletes:	xbmc-skin-pm3-hd < 9.11-1.svn29468
Obsoletes:	xbmc-nosefart < 9.11-1.svn29468
Obsoletes:	xbmc-screensavers-default < 9.11-1.svn29468
Obsoletes:	xbmc-script-examples < 9.11-1.svn27796
Obsoletes:	xbmc-web-pm3 < 9.11-1.svn27796

%description
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

While XBMC functions very well as a standard media player application
for your computer, it has been designed to be the perfect companion
for your HTPC. Supporting an almost endless range of remote controls,
and combined with its beautiful interface and powerful skinning
engine, XBMC feels very natural to use from the couch and is the
ideal solution for your home theater.

This is the stable version of XBMC from the dharma release branch,
with PVR support added from opdenkamp Dharma-pvr branch. Support for
RAR files and XBMS protocol is not included due to license issues.

%package	eventclients-common
Summary:	Common files for XBMC eventclients
Group:		Video
%py_requires

%description	eventclients-common
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains common files for eventclients.

%package	eventclients-devel
Summary:	Development files for XBMC eventclients
Group:		Development/C

%description	eventclients-devel
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build eventclients.

%package	eventclient-wiiremote
Summary:	Wii Remote eventclient for XBMC
Group:		Video
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-wiiremote
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%package	eventclient-j2me
Summary:	J2ME eventclient for XBMC
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-j2me
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the J2ME eventclient, providing a bluetooth
server that can communicate with a mobile tool supporting J2ME.

%package	eventclient-ps3
Summary:	PS3 eventclients for XBMC
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:	python-gobject avahi-python python-dbus
# TODO merge all these?, and TODO zeroconf.py to a correct package? :)
Obsoletes:	eventclient-ps3remote < 9.11-1.svn31936

%description	eventclient-ps3
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%package	eventclient-xbmc-send
Summary:	PS3 eventclient for XBMC
Group:		Video
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-xbmc-send
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the xbmc-send eventclient.

%prep
%if %snap
%setup -q -n %name-%branch_release-%snap
%else
%setup -q
%endif
%apply_patches
# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete

# GPLv2 only
rm -r xbmc/lib/cmyth/Win32/include/mysql
# BSD 4-clause
rm -r xbmc/cores/DllLoader/exports/emu_socket

# rm disabled stuff to detect possible bugs
rm -rf xbmc/cores/dvdplayer/Codecs/{libdts,liba52} xbmc/cores/paplayer/AC3Codec/liba52

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

%if !%system_python
cp %{SOURCE11} lib/addons/script.module.pil
cp %{SOURCE12} lib/addons/script.module.pysqlite

# we need to fix the lookup directories (otherwise setup.py queries
# incorrect information from the bundled python)
tar -xzf %{SOURCE11} -C lib/addons/script.module.pil
sed -ri 's|^([A-Z0-9]+_ROOT =) None|\1 "%{_libdir}", "%{_includedir}"|' lib/addons/script.module.pil/Imaging-*/setup.py
%endif

%build
%if %snap
export GIT_REV=%snap
%else
export GIT_REV=$(basename %SOURCE0)
%endif
./bootstrap

# due to xbmc modules that use symbols from xbmc binary
# and are not using libtool
%define _disable_ld_no_undefined 1

# Workaround configure using git to override GIT_REV (TODO: fix it properly)
export ac_cv_prog_HAVE_GIT="no"

%configure2_5x \
	--disable-debug \
	--disable-ccache \
	--enable-external-libraries \
%if !%system_python
	--disable-external-python \
%endif
	--disable-non-free \
	--disable-dvdcss \
	--disable-faac \
	--enable-goom \
%if %{mdkversion} <= 201020
	--disable-vaapi \
%endif
%if %{mdkversion} >= 201000
	--with-lirc-device=/var/run/lirc/lircd
%else
	--with-lirc-device=/dev/lircd
%endif

# non-free = unrar + xbms
# dvdcss is handled via dlopen when disabled
# faac is always handled via libavcodec

%make
%make -C tools/EventClients wiimote

%if !%system_python
for dir in lib/addons/script.module.*; do
	%make -C $dir
done
%endif

%install
rm -rf %{buildroot}
%makeinstall_std
%makeinstall_std -C tools/EventClients

# unused
rm %{buildroot}%{_datadir}/xsessions/XBMC.desktop
# our version of the above:
install -d -m755 %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/15XBMC <<EOF
NAME=XBMC
ICON=xbmc.png
DESC=XBMC Media Center
EXEC=%{_bindir}/xbmc-standalone
SCRIPT:
exec %{_bindir}/xbmc-standalone
EOF

# unused files, TODO fix this upstream:
find %{buildroot}%{_datadir}/xbmc/addons/skin.*/media -name '*.png' -delete

( # for IFS and +x
# Check for issues in ELF binaries
undefined=
fhserr=
echo Silencing output of checking symbols and FHS conformance
set +x
IFS=$'\n'
for file in $(find %{buildroot} -type f); do
	type="$(file "$file")"
	echo "$type" | grep -q "ELF" || continue

	# Check that a binary file is not in datadir:
	echo "$file" | grep -q "%{_datadir}" && fhserr="${fhserr}$file\n"

	# check for undefined symbols in XBMC modules
	echo "$type" | grep -q "shared object" || continue
	for symbol in $(LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} ldd -r "$file" 2>&1 | grep undefined | awk '{ print $3 }'); do
		# undefined symbols may also be provided by XBMC:
		nm -f posix -D --no-demangle --defined-only %{buildroot}%{_libdir}/xbmc/xbmc.bin | grep -q "^$symbol " && continue
		# The symbol was not provided by XBMC.
		# Check if it is available through its dependencies:
		for filename in $(objdump -p %{buildroot}%{_libdir}/xbmc/xbmc.bin | grep NEEDED | awk '{ print $2 }'); do
			depfile="/%{_lib}/$filename"
			[ -e "$depfile" ] || depfile="%{_libdir}/$filename"
			nm -f posix -D --no-demangle --defined-only $depfile | grep -q "^$symbol " && continue 2
		done
		# Euphoria references rsxs PNG class, but it is never used at runtime,
		# so it results in no errors due to RTLD_LAZY being used by xbmc module loader.
		# _imaging*.so and _sqlite.so are python modules that exist when using bundled python
		case $file:$symbol in */Euphoria.xbs:_ZN3PNG*|*/_imaging*.so:*|*/_sqlite.so:*) continue; esac
		# the symbol was not found
		undefined="${undefined}$file: $symbol\n"
	done
done
ok=1
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols!" && ok=
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && ok=
[ -n "$ok" ]
)

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_docdir}/xbmc
%{_sysconfdir}/X11/wmsession.d/15XBMC
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%dir %{_libdir}/xbmc
%dir %{_libdir}/xbmc/addons
%dir %{_libdir}/xbmc/system
%dir %{_libdir}/xbmc/system/players
%dir %{_libdir}/xbmc/system/players/dvdplayer
%dir %{_libdir}/xbmc/system/players/paplayer
%dir %{_libdir}/xbmc/system/python
%{_libdir}/xbmc/xbmc.bin
%{_libdir}/xbmc/xbmc-xrandr
%dir %{_libdir}/xbmc/addons/*
%{_libdir}/xbmc/addons/*/*.so
%{_libdir}/xbmc/addons/*/*.pvr
%{_libdir}/xbmc/addons/*/*.vis
%{_libdir}/xbmc/addons/*/*.xbs
%{_libdir}/xbmc/addons/script.module.*/*.xml
%{_libdir}/xbmc/system/ImageLib-*-linux.so
%{_libdir}/xbmc/system/hdhomerun-*-linux.so
%{_libdir}/xbmc/system/libcpluff-*-linux.so
%{_libdir}/xbmc/system/libexif-*-linux.so
%{_libdir}/xbmc/system/libid3tag-*-linux.so
%{_libdir}/xbmc/system/players/dvdplayer/libdvdnav-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/adpcm-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/libsidplay2-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/nosefart-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/stsoundlibrary-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/timidity-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/vgmstream-*-linux.so
%ifarch %ix86
%{_libdir}/xbmc/system/players/paplayer/SNESAPU-*-linux.so
%endif
%{_libdir}/xbmc/system/python/python*-*-linux.so
%if !%system_python
%{_libdir}/xbmc/addons/script.module.pil/*
%{_libdir}/xbmc/addons/script.module.pysqlite/*
%{_libdir}/xbmc/system/python/python*.zip
%endif
%dir %{_datadir}/xbmc
%{_datadir}/xbmc/addons
%{_datadir}/xbmc/FEH.py
%{_datadir}/xbmc/language
%{_datadir}/xbmc/media
%{_datadir}/xbmc/sounds
%{_datadir}/xbmc/system
%{_datadir}/xbmc/userdata
%{_datadir}/applications/xbmc.desktop
%{_iconsdir}/hicolor/*/apps/xbmc.png

%files eventclients-common
%defattr(-,root,root)
%python_sitelib/xbmc
%dir %{_datadir}/pixmaps/xbmc
%{_datadir}/pixmaps/xbmc/*.png

%files eventclients-devel
%defattr(-,root,root)
%dir %{_includedir}/xbmc
%{_includedir}/xbmc/xbmcclient.h

%files eventclient-j2me
%defattr(-,root,root)
%{_bindir}/xbmc-j2meremote

%files eventclient-ps3
%defattr(-,root,root)
%{_bindir}/xbmc-ps3d
%{_bindir}/xbmc-ps3remote

%files eventclient-xbmc-send
%defattr(-,root,root)
%{_bindir}/xbmc-send

%files eventclient-wiiremote
%defattr(-,root,root)
%{_bindir}/xbmc-wiiremote
