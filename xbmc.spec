
%define name	xbmc
%define branch	pvr-testing2
%define version	9.11
# the svn revision of the end-result:
%define svnsnap	28014
# the svn revision of the tarball:
%define basesnap 28000
%define rel	2

Summary:	XBMC Media Center - media player and home entertainment system
Name:		%{name}
Version:	%{version}
%define branchr	%(echo %branch | tr - _)
Release:	%mkrel 1.svn%svnsnap.%branchr.%rel
URL:		http://xbmc.org/
# URL=https://xbmc.svn.sourceforge.net/svnroot/xbmc/branches/pvr-testing2
# REV=$(svn info $URL| sed -ne 's/^Last Changed Rev: //p')
# svn export -r $REV $URL xbmc-pvr-testing2-$REV
# tar -cJf xbmc-pvr-testing2-$REV.tar.xz xbmc-pvr-testing2-$REV
# or
# git archive --prefix=xbmc-pvr-testing2-$REV/ origin/pvr-testing2 |
# xz > xbmc-pvr-testing2-$REV.tar.xz
Source:		%{name}-%{branch}-%basesnap.tar.xz

# Patches from upstream and related patches resolving merge conflicts
# =================================
# bring snapshot up-to-date with pvr-testing2 branch:
# already up-to-date
# Patch0:		xbmc-pvr-testing2-%basesnap-to-27596.patch
# bring snapshot up-to-date with trunk:
# git diff -a ffae046521a2e408..9663680e8808c55d4e2d
Patch1:		xbmc-pvr-testing2-merge-trunk-27946-27976.patch
# resolve merge issues in addon code:
Patch2:		xbmc-pvr-testing2-merge-actions.patch
# git diff -a 9663680e8808c55d4e2d..ced60f8a3b1fdf66828ef
Patch3:		xbmc-pvr-testing2-merge-trunk-27976-27986.patch
# git diff -a ced60f8a3b1fdf66828ef..80cbed7072a761ca39f976d1
Patch4:		xbmc-pvr-testing2-merge-trunk-27986-28007.patch
# drop httpapi support from unused ExecuteHttpApi() method, as it has not
# been updated for the switch to microhttpd yet
Patch5:		xbmc-addon-httpapi.patch
# git diff -a 80cbed7072a761ca39f976d1..088a1f046d68e5161
Patch6:		xbmc-pvr-testing2-merge-trunk-28007-28014.patch

# Upstreamable patches fixing upstream bugs
# ===============================
# better OpenGL visual selection routine
# submitted in http://trac.xbmc.org/ticket/8661
Patch20:	xbmc-glxvisuals.patch
# fix saving addon settings
# submitted as http://trac.xbmc.org/ticket/8836
Patch21:	xbmc-pvr-testing2-fix-save-settings.patch
# fix non-literal format strings in goom
# submitted in http://trac.xbmc.org/ticket/8661
Patch23:	xbmc-goom-strfmt.patch
# workaround usage of 'byte' in glib2 headers
Patch24:        xbmc-fix-glib2.23.4.patch

# Non-upstreamable patches for upstream bugs
# =============================
# fix addon library sonames:
Patch40:	xbmc-pvr-testing2-addon-sonames.patch
# code assumes 4 byte unicode on linux, while our python has 2 byte unicode
# hack, reported as http://xbmc.org/trac/ticket/8430
Patch41:	xbmc-python-unicode-2byte.patch
# add missing stsound source files
# partial revert of http://xbmc.svn.sourceforge.net/viewvc/xbmc?view=rev&revision=14069
# and fix it for 64bit; still doesn't seem to work, though
Patch42:	xbmc-stsound-fix-missing-files.patch
# load global default-addons.xml if there is no local one yet
# allows loading non-pvr addons by default as per trunk behaviour
# (FIXME: what about added addons on upgrade? should we parse default-addons.xml always,
#  while keeping a list of previously added addons?)
Patch43:	xbmc-default-addons.patch

# Patches for policy compatibility, not necessarily "real" upstream bugs
# ================================
# do not use --as-needed for python module, as that breaks loading
# system libpython via the module
Patch60:	xbmc-python-module-no-as-needed.patch
# fix various undefined symbols in submodules
# quick hacks, not proper fixes (also, normally upstream links many unneeded
# libs into the main executable so that the dependencies of submodules are
# satisfied; this doesn't happen with our --as-needed)
Patch61:	xbmc-fix-undefined-symbols.patch
# same as above but for PVR symbols:
Patch62:	xbmc-pvr-testing2-underlinking.patch
# hacks to load modules from @XBMCLIBS@ (set in %%prep)
Patch63:	xbmc-fhs-hack.patch
Patch64:	xbmc-addons-fhs-hack.patch
# build faad,dca support with internal headers, but do not build the
# libraries themselves; use system copies with dlopen instead;
# this allows keeping them as optional external libraries
# (nb. dca is no longer used in favor of ffmpeg, but faad part is still useful)
Patch65:	xbmc-hack-ext-libs-with-int-headers.patch

License:	GPLv3+
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
BuildRequires:	a52dec-devel
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
%ifarch %ix86
BuildRequires:	nasm
%endif
BuildRequires:	imagemagick
# presently unpackaged:
# BuildRequires:	libass-devel
# dts and faad support use internal headers as per above patch
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-skin-confluence
Requires:	%{name}-skin-pm3-hd
Requires:	%{name}-screensavers-default = %{version}-%{release}
Suggests:	%{name}-nosefart = %{version}-%{release}

%description
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

While XBMC functions very well as a standard media player application
for your computer, it has been designed to be the perfect companion
for your HTPC. Supporting an almost endless range of remote controls,
and combined with its beautiful interface and powerful skinning
engine, XBMC feels very natural to use from the couch and is the
ideal solution for your home theater.

This is the development version of XBMC from pvr-testing2 branch,
with VDR streamdev support. Support for RAR files and XBMS protocol
is not included due to license issues.

This package provides the standard XBMC suite.

%package	core
Summary:	XBMC Media Center - core files
Group:		Video
Requires:	lsb-release
# dlopened: (see prep stage for changing sonames in xbmc/DllPaths_generated.h.in)
Requires:	%{_lib}curl4
Requires:	%{_lib}flac8
Requires:	%{_lib}vorbisfile3
Requires:	%{_lib}mad0
Requires:	%{_lib}ogg0
Requires:	%{_lib}vorbisenc2
Requires:	%{_lib}vorbis0
Requires:	%{_lib}modplug0
# not nearly as common as the above, so suggest instead for now:
Suggests:	%{_lib}crystalhd1
Requires:	xbmc-skin
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
# Packages not shipped by Mandriva:
Suggests:	%{_lib}faad2_2
Suggests:	%{_lib}lame0
Suggests:	%{_lib}dca0
Suggests:	%{_lib}dvdcss2
Obsoletes:	xbmc-script-examples < 9.11-1.svn27796
Obsoletes:	xbmc-web-pm3 < 9.11-1.svn27796

%description	core
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the core files of XBMC from pvr-testing2
branch, with VDR streamdev support. See package 'xbmc' for the full
suite.

Support for RAR files and XBMS protocol is not included due to
license issues.

%package	devel
Summary:	XBMC addon development files
Group:		Development/C++
Requires:	%{name}-core = %{version}-%{release}

%description	devel
Development headers and library symlinks needed for building XBMC
addons. This package is not needed for normal XBMC usage.

%package	skin-confluence
Summary:	Confluence skin for XBMC
Group:		Video
Requires:	%{name}-core = %{version}-%{release}
Provides:	xbmc-skin

%description	skin-confluence
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains the Confluence skin for XBMC.

%package	skin-pm3-hd
Summary:	Project Mayhem III HD skin for XBMC
Group:		Video
Requires:	%{name}-core = %{version}-%{release}
Provides:	xbmc-skin

%description	skin-pm3-hd
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains the PM3.HD (Project Mayhem III High Definition)
skin for XBMC.

%package	nosefart
Summary:	NSF audio support for XBMC
Group:		Video
License:	GPLv2
Requires:	%{name}-core = %{version}-%{release}

%description	nosefart
NSF audio support for XBMC PVR testing version, via nosefart library.

%package	screensavers-default
Summary:	Default screensavers for XBMC
Group:		Video
License:	GPLv2
Requires:	%{name}-core = %{version}-%{release}

%description	screensavers-default
Default screensavers for XBMC PVR testing version, based on RSXS.

%package	eventclients-common
Summary:	Common files for XBMC eventclients
Group:		Video
%py_requires
# required by zeroconf.py, only used by PS3 sixaxis client,
# not installed by default:
# Requires:	python-gobject avahi-python python-dbus

%description	eventclients-common
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains common files for eventclients.

%package	eventclients-devel
Summary:	Development files for XBMC eventclients
Group:		Development/C

%description	eventclients-devel
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains files needed to build eventclients.

%package	eventclient-wiiremote
Summary:	Wii Remote eventclient for XBMC
Group:		Video
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-wiiremote
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains the Wii Remote eventclient.

%package	eventclient-j2me
Summary:	J2ME eventclient for XBMC
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-j2me
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains the J2ME eventclient, providing a bluetooth
server that can communicate with a mobile tool supporting J2ME.

%package	eventclient-ps3remote
Summary:	PS3 Remote eventclient for XBMC
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-ps3remote
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains the PS3 Remote eventclient.

%package	eventclient-xbmc-send
Summary:	PS3 eventclient for XBMC
Group:		Video
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-xbmc-send
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This is the version from pvr-testing2 branch, with VDR support.

This package contains the xbmc-send eventclient.

%prep
%setup -q -n %name-%{branch}-%basesnap
# make the patches affecting strings.xml from git apply to sources from svn:
sed -i 's,^<!--\$Revision: [0-9]* \$-->$,<!--\$Revision\$-->,' language/*/strings.xml

%apply_patches
# otherwise backups end up in binary rpms
find -type f -name '*.00??' -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete

sed -i 's,special://xbmc/system,%{_libdir}/xbmc/system,g' xbmc/DllPaths_generated.h.in
sed -i 's,getenv("XBMC_HOME"),"%{_libdir}/xbmc",g' xbmc/linux/XRandR.cpp
sed -i 's,@XBMCLIBS@,%{_libdir}/xbmc,g' tools/Linux/xbmc.sh.in
sed -i 's,@XBMCLIBS@,"%{_libdir}/xbmc",g' \
	xbmc/cores/DllLoader/DllLoaderContainer.cpp \
	xbmc/lib/libPython/XBPython.cpp \
	xbmc/utils/AddonDll.h

# adapt sonames for dlopen:
grep -q \"libfaad.so.0\" xbmc/DllPaths_generated.h.in
sed -i 's,"libfaad.so.0","libfaad.so.2",' xbmc/DllPaths_generated.h.in
grep -q libcrystalhd.so\" xbmc/DllPaths_generated.h.in
sed -i 's,"libcrystalhd.so","libcrystalhd.so.1",' xbmc/DllPaths_generated.h.in

# GPLv2 only
rm -r xbmc/lib/cmyth/Win32/include/mysql
# BSD 4-clause
rm -r xbmc/cores/DllLoader/exports/emu_socket

# fix python directory
sed -i 's,python.\../site,python%py_ver/site,' tools/EventClients/Makefile

%build
export SVN_REV=%svnsnap
./bootstrap
# fixes build
autoreconf -vif lib/libmodplug

# due to xbmc modules that use symbols from xbmc binary
%define _disable_ld_no_undefined 1

# some parts are compiled/linked without $C(XX)FLAGS and linked without $LDFLAGS,
# workaround it by adding those into $CC and $CXX (as of 2010-01):
export CC="gcc %optflags %{?ldflags}"
export CXX="g++ %optflags %{?ldflags}"

%configure2_5x \
	--disable-ccache \
	--enable-external-libraries \
	--disable-non-free \
	--disable-dvdcss \
	--disable-faac \
	--enable-goom

# non-free = unrar + xbms
# dvdcss is handled via dlopen when disabled
# faac is always handled via libavcodec

# parallel build broken as of 03/2010
make

%make -C tools/EventClients wiimote WII_EXTRA_OPTS="%{optflags} %{?ldflags}" prefix=%{_prefix}
# prevent recompilation in install stage:
touch tools/EventClients/wiimote

%install
rm -rf %{buildroot}
%makeinstall
%makeinstall -C tools/EventClients

# in %%doc already:
rm %{buildroot}%{_datadir}/xbmc/{*.txt,LICENSE.GPL,README.linux}

# we already have shared ones
rm %{buildroot}%{_libdir}/libXBMC_*.a

# unused
rm %{buildroot}%{_datadir}/xsessions/XBMC.desktop
# our version:
install -d -m755 %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/15XBMC <<EOF
NAME=XBMC
ICON=xbmc.png
DESC=XBMC Media Center
EXEC=%{_bindir}/xbmc-standalone
SCRIPT:
exec %{_bindir}/xbmc-standalone
EOF

# mediaportal client is not built on linux yet
grep -q '<library>XBMC_MPTV.pvr</library>' %{buildroot}%{_datadir}/xbmc/addons/pvr/MediaPortal/description.xml
[ ! -e %{buildroot}%{_datadir}/xbmc/addons/pvr/MediaPortal/XBMC_MPTV.pvr ]
rm -rf %{buildroot}%{_datadir}/xbmc/addons/pvr/MediaPortal

# create default-addons.xml file, loading non-PVR addons by default as per trunk behaviour
echo "<addons>" > %{buildroot}%{_datadir}/xbmc/default-addons.xml
for type in visualization screensaver; do
	echo "<$type>"
	for file in %{buildroot}%{_datadir}/xbmc/addons/${type}s/*/description.xml; do
		uuid=$(sed -ne 's,^.*<uuid>\(.*\)</uuid>.*$,\1,p' $file)
		echo "<addon>"
		echo "<uuid>$uuid</uuid>"
		echo "</addon>"
	done
	echo "</$type>"
done >> %{buildroot}%{_datadir}/xbmc/default-addons.xml
echo "</addons>" >> %{buildroot}%{_datadir}/xbmc/default-addons.xml

# when adding files here remember to make sure they are handled in fhs-hack.patch!
for file in \
	%{buildroot}%{_datadir}/xbmc/xbmc.bin \
	%{buildroot}%{_datadir}/xbmc/xbmc-xrandr \
	%{buildroot}%{_datadir}/xbmc/system/*.so \
	%{buildroot}%{_datadir}/xbmc/system/players/dvdplayer/*.so \
	%{buildroot}%{_datadir}/xbmc/system/players/paplayer/*.so \
	%{buildroot}%{_datadir}/xbmc/system/python/*.so \
	%{buildroot}%{_datadir}/xbmc/addons/pvr/*/*.pvr \
	%{buildroot}%{_datadir}/xbmc/addons/screensavers/*/*.xbs \
	%{buildroot}%{_datadir}/xbmc/addons/visualizations/*/*.vis \
	; do
	dirname="$(dirname "$file")"
	dirname="${dirname#%{buildroot}%{_datadir}/xbmc}"
	install -d -m755 "%{buildroot}%{_libdir}/xbmc$dirname"
	mv "$file" "%{buildroot}%{_libdir}/xbmc/$dirname/"
done

# icons
file %{buildroot}%{_datadir}/pixmaps/xbmc.png | grep -q 256 || exit 1
install -m644 -D %{buildroot}%{_datadir}/pixmaps/xbmc.png %{buildroot}%{_iconsdir}/hicolor/256x256/apps/xbmc.png
for size in 64 48 32 16; do
	install -d -m755 %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps
	convert %{buildroot}%{_datadir}/pixmaps/xbmc.png -resize $size %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/xbmc.png
done

# implement the above disabled --no-undefined ourselves, taking symbols in
# xbmc.bin into account
undefined=
fhserr=
echo Silencing output of ELF verification
set +x
for file in $(find %{buildroot} -type f -not -name '* *'); do
	type="$(file "$file")"
	echo "$type" | grep -q "ELF" || continue
	echo "$file" | grep -q "%{_datadir}" && fhserr="${fhserr}$file\n"
	echo "$type" | grep -q "shared object" || continue
	for symbol in $(LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} ldd -r "$file" 2>&1 | grep undefined | awk '{ print $3 }'); do
		nm -f posix -D --defined-only --no-demangle %{buildroot}%{_libdir}/xbmc/xbmc.bin | grep -q "^$symbol " && continue
		undefined="${undefined}$file: $symbol\n"
	done
done
set -x
ok=1
# fix-undefined-symbols.patch
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols, update fix-undefined-symbols.patch!" && ok=
# fhs-hack.patch
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && ok=
[ -n "$ok" ]

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%files core
%defattr(-,root,root)
%doc README.linux LICENSE.GPL copying.txt keymapping.txt
%{_sysconfdir}/X11/wmsession.d/15XBMC
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%dir %{_libdir}/xbmc
%dir %{_libdir}/xbmc/addons
%dir %{_libdir}/xbmc/addons/pvr
%dir %{_libdir}/xbmc/addons/pvr/*
%dir %{_libdir}/xbmc/addons/screensavers
%dir %{_libdir}/xbmc/addons/visualizations
%dir %{_libdir}/xbmc/addons/visualizations/*
%dir %{_libdir}/xbmc/system
%dir %{_libdir}/xbmc/system/players
%dir %{_libdir}/xbmc/system/players/dvdplayer
%dir %{_libdir}/xbmc/system/players/paplayer
%dir %{_libdir}/xbmc/system/python
%{_libdir}/xbmc/xbmc.bin
%{_libdir}/xbmc/xbmc-xrandr
%{_libdir}/xbmc/addons/pvr/*/*.pvr
%{_libdir}/xbmc/addons/visualizations/*/*.vis
%{_libdir}/xbmc/system/ImageLib-*-linux.so
%{_libdir}/xbmc/system/hdhomerun-*-linux.so
%{_libdir}/xbmc/system/libexif-*-linux.so
%{_libdir}/xbmc/system/libid3tag-*-linux.so
%{_libdir}/xbmc/system/players/dvdplayer/libass-*-linux.so
%{_libdir}/xbmc/system/players/dvdplayer/libdvdnav-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/ac3codec-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/adpcm-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/gensapu-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/libsidplay2-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/stsoundlibrary-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/timidity-*-linux.so
%{_libdir}/xbmc/system/players/paplayer/vgmstream-*-linux.so
%ifarch %ix86
%{_libdir}/xbmc/system/players/paplayer/SNESAPU-*-linux.so
%endif
%{_libdir}/xbmc/system/python/python*-*-linux.so
# Not libified as they are completely useless without XBMC, and there is no
# need to have multiple copies installed. - Anssi 02/2010
%{_libdir}/libXBMC_*.so.*
%dir %{_datadir}/xbmc
%{_datadir}/xbmc/addons
%{_datadir}/xbmc/default-addons.xml
%{_datadir}/xbmc/FEH.py
%{_datadir}/xbmc/language
%{_datadir}/xbmc/media
%dir %{_datadir}/xbmc/scripts
%{_datadir}/xbmc/scripts/autoexec.py
%dir %{_datadir}/xbmc/skin
%{_datadir}/xbmc/sounds
# FIXME: there are bundled fontconfig config files in xbmc/system/players/dvdplayer.
# they are probably unused already, but this has to be confirmed
%{_datadir}/xbmc/system
%{_datadir}/xbmc/userdata
%{_datadir}/xbmc/web
%{_datadir}/applications/xbmc.desktop
%{_datadir}/pixmaps/xbmc.png
%{_iconsdir}/hicolor/*/apps/xbmc.png

%files devel
%defattr(-,root,root)
%dir %{_includedir}/xbmc
%doc %{_includedir}/xbmc/NOTE
%{_includedir}/xbmc/libXBMC_*.h
%{_includedir}/xbmc/xbmc_*.h
%{_libdir}/libXBMC_*.so

%files skin-confluence
%defattr(-,root,root)
%{_datadir}/xbmc/skin/Confluence

%files skin-pm3-hd
%defattr(-,root,root)
%{_datadir}/xbmc/skin/PM3.HD

%files screensavers-default
%defattr(-,root,root)
%dir %{_libdir}/xbmc/addons/screensavers/*
%{_libdir}/xbmc/addons/screensavers/*/*.xbs

%files nosefart
%defattr(-,root,root)
%{_libdir}/xbmc/system/players/paplayer/nosefart-*-linux.so

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

%files eventclient-ps3remote
%defattr(-,root,root)
%{_bindir}/xbmc-ps3remote

%files eventclient-xbmc-send
%defattr(-,root,root)
%{_bindir}/xbmc-send

%files eventclient-wiiremote
%defattr(-,root,root)
%{_bindir}/xbmc-wiiremote
