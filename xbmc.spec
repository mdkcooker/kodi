
%define name	xbmc
%define branch	pvr-testing2
%define version	9.11
%define svnsnap	26907
%define rel	1

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
Source:		%{name}-%{branch}-%svnsnap.tar.xz
# weather.rar in zip format:
# rm -f ../xbmc-weather.zip && unrar x ../xbmc-foo/media/weather.rar &&
# md5sum ../xbmc-foo/media/weather.rar | cut -d" " -f1 | zip -0rz ../xbmc-weather.zip *
Source1:	xbmc-weather.zip
# fix GPL compatibility issues, from gpl-compat branch, as of r26893:
Patch0:		xbmc-pvr-testing-26907-gpl-compat-26893.patch
# fix crash if reading VDR response fails
# submitted as http://xbmc.org/trac/ticket/8542
Patch1:		xbmc-pvr-testing-fix-crash.patch
# fix a mistake in trunk => pvr-testing2 merge; fixes build
# already fixed upstream
Patch2:		xbmc-pvr-testing2-fix-trunk-merge.patch
# format strings in embedded timidity
Patch3:		xbmc-timidity-format-strings.patch
# do not use --as-needed for python module, as that breaks loading
# system libpython via the module
Patch4:		xbmc-python-module-no-as-needed.patch
# format strings in xbmc itself
# submitted as http://xbmc.org/trac/ticket/8543
Patch5:		xbmc-format-strings.patch
# code assumes 4 byte unicode on linux, while our python has 2 byte unicode
# hack, reported as http://xbmc.org/trac/ticket/8430
Patch6:		xbmc-python-unicode-2byte.patch
# fix various undefined symbols in submodules
# quick hacks, not proper fixes
Patch7:		xbmc-fix-undefined-symbols.patch
# add missing stsound source files
# partial revert of http://xbmc.svn.sourceforge.net/viewvc/xbmc?view=rev&revision=14069
# and fix it for 64bit; still doesn't seem to work, though
Patch8:		xbmc-stsound-fix-missing-files.patch
# use weather.zip instead of weather.rar, as our rar support is disabled
# this simply uncomments .zip defines and comments .rar defines
Patch9:		xbmc-pvr-testing2-use-weatherzip-not-rar.patch
# hacks to load modules from @XBMCLIBS@ (set in %%prep)
Patch10:	xbmc-fhs-hack.patch
# build faad,dca support with internal headers, but do not build the
# libraries themselves; use system copies with dlopen instead
Patch11:	xbmc-hack-ext-libs-with-int-headers.patch
License:	GPLv3+
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	boost-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	a52dec-devel
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
BuildRequires:	cmake
BuildRequires:	gperf
%ifarch %ix86
BuildRequires:	nasm
%endif
BuildRequires:	imagemagick
# presently unpackaged:
# BuildRequires:	libass-devel
# BuildRequires:	crystalhd-devel
# dts and faad support use internal headers as per above patch
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-skin-confluence
Requires:	%{name}-skin-pm3-hd
Requires:	%{name}-web-pm3
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
with VDR streamdev support.

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
Requires:	xbmc-skin
# Packages not shipped by Mandriva:
Suggests:	%{_lib}faad2_2
Suggests:	%{_lib}lame0
Suggests:	%{_lib}dca0
Suggests:	%{_lib}dvdcss2

%description	core
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media. 

This package contains the core files of XBMC from pvr-testing2
branch, with VDR streamdev support. See package 'xbmc' for the full
suite.

%package	script-examples
Summary:	XBMC example python scripts
Group:		Video
Requires:	%{name}-core = %{version}-%{release}

%description	script-examples
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media. 

This is the version from pvr-testing2 branch, with VDR support.

This package contains the example scripts that are shipped with XBMC.

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

%package	web-pm3
Summary:	Project Mayhem III skin for web server of XBMC
Group:		Video
Requires:	%{name}-core = %{version}-%{release}

%description	web-pm3
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media. 

This is the version from pvr-testing2 branch, with VDR support.

This package contains the PM3 (Project Mayhem III) skin for the web
server of XBMC.

%package	web-iphone
Summary:	iPhone skin for web server of XBMC
Group:		Video
Requires:	%{name}-core = %{version}-%{release}

%description	web-iphone
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media. 

This is the version from pvr-testing2 branch, with VDR support.

This package contains an iPhone skin for the web server of XBMC.

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
%setup -q -n %name-%{branch}-%svnsnap
%apply_patches
# otherwise backups end up in binary rpms
find -type f -name '*.00??' -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -print -delete
# (as of 2010-01 prebuilt wma-i486-linux.so may otherwise get included)

sed -i 's,special://xbmc/system,%{_libdir}/xbmc/system,g' xbmc/DllPaths_generated.h.in
sed -i 's,getenv("XBMC_HOME"),"%{_libdir}/xbmc",g' xbmc/linux/XRandR.cpp
sed -i 's,@XBMCLIBS@,%{_libdir}/xbmc,g' tools/Linux/xbmc.sh.in
sed -i 's,@XBMCLIBS@,"%{_libdir}/xbmc",g' \
	xbmc/cores/DllLoader/DllLoaderContainer.cpp \
	xbmc/visualizations/VisualisationFactory.cpp \
	xbmc/visualizations/Visualisation.cpp \
	xbmc/GUIWindowSettingsCategory.cpp \
	xbmc/GUIWindowScreensaver.cpp \
	xbmc/lib/libPython/XBPython.cpp

# adapt sonames for dlopen:
grep -q libfaad.so.0 xbmc/DllPaths_generated.h.in
sed -i s,libfaad.so.0,libfaad.so.2, xbmc/DllPaths_generated.h.in

# confirm that there are no special://xbmc entries that would have to
# be adapted:
grep -q special: xbmc/screensavers/* && exit 1

# GPLv2 only
rm -r xbmc/lib/cmyth/Win32/include/mysql
# BSD 4-clause
rm -r xbmc/cores/DllLoader/exports/emu_socket

chmod a+x xbmc/lib/libapetag/configure
chmod a+x lib/libmodplug/configure

# fix python directory
sed -i 's,python.\../site,python%py_ver/site,' tools/EventClients/Makefile

# disable FEH.py to avoid dependencies on mesa-demos, xdpyinfo and gnome-python:
sed -i 's,^python,true #&,' tools/Linux/xbmc.sh.in
# this unfortunately disables the warning when using software rendering

# original md5 stored in zip comment, see Source1
current_weather_rar_md5=$(md5sum media/weather.rar | cut -d" " -f1)
original_weather_rar_md5=$(unzip -qz %{_sourcedir}/xbmc-weather.zip)
# if this fails, update Source1
[ "$current_weather_rar_md5" = "$original_weather_rar_md5" ] || exit 1
rm media/weather.rar
install -m644 %{_sourcedir}/xbmc-weather.zip media/weather.zip

%build
export SVN_REV=%svnsnap
./bootstrap
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
	--disable-faac
# non-free = unrar code
# dvdcss is handled via dlopen when disabled
# faac is always handled via libavcodec

# parallel build broken as of 2010-01
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

%if 0
# should we provide this? e.g. Scripts link is broken in the page...
cp -pr web/xbmciphone/iphone %{buildroot}%{_datadir}/xbmc/web/iphone
# .. and the server looks for default.asp, not index.html:
ln -s index.html %{buildroot}%{_datadir}/xbmc/web/iphone/default.asp
%endif

# the example scripts are zipped, but they don't all seem to work like that
# as of 2010-01 - Anssi
# alternatively, we could just remove them and ship in %%doc
mkdir %{buildroot}%{_datadir}/xbmc/scripts/examples
cd %{buildroot}%{_datadir}/xbmc/scripts/examples
for file in ../*.zip; do
	unzip "$file"
	rm "$file"
done
# invalid license
rm -r medusa
cd -

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

# when adding files here remember to make sure they are handled in fhs-hack.patch!
for file in \
	%{buildroot}%{_datadir}/xbmc/xbmc.bin \
	%{buildroot}%{_datadir}/xbmc/xbmc-xrandr \
	%{buildroot}%{_datadir}/xbmc/system/*.so \
	%{buildroot}%{_datadir}/xbmc/system/players/dvdplayer/*.so \
	%{buildroot}%{_datadir}/xbmc/system/players/paplayer/*.so \
	%{buildroot}%{_datadir}/xbmc/system/python/*.so \
	%{buildroot}%{_datadir}/xbmc/screensavers/*.xbs \
	%{buildroot}%{_datadir}/xbmc/visualisations/*.vis \
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
set +x
for file in $(find %{buildroot} -type f -perm /u+x); do
	type="$(file "$file")"
	echo "$type" | grep -q "ELF" || continue
	echo "$file" | grep -q "%{_datadir}" && fhserr="${fhserr}$file\n"
	echo "$type" | grep -q "shared object" || continue
	for symbol in $(ldd -r "$file" 2>&1 | grep undefined | awk '{ print $3 }'); do
		nm -f posix -D --defined-only --no-demangle %{buildroot}%{_libdir}/xbmc/xbmc.bin | grep -q "^$symbol " && continue
		undefined="${undefined}$file: $symbol\n"
	done
done
set -x
# fix-undefined-symbols.patch
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols, update fix-undefined-symbols.patch!" && exit 1
# fhs-hack.patch
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && exit 1

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
%dir %{_libdir}/xbmc/system
%dir %{_libdir}/xbmc/system/players
%dir %{_libdir}/xbmc/system/players/dvdplayer
%dir %{_libdir}/xbmc/system/players/paplayer
%dir %{_libdir}/xbmc/system/python
%dir %{_libdir}/xbmc/screensavers
%dir %{_libdir}/xbmc/visualisations
%{_libdir}/xbmc/xbmc.bin
%{_libdir}/xbmc/xbmc-xrandr
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
%{_libdir}/xbmc/visualisations/*.vis
%dir %{_datadir}/xbmc
%{_datadir}/xbmc/addons
%{_datadir}/xbmc/FEH.py
%{_datadir}/xbmc/language
%{_datadir}/xbmc/media
%dir %{_datadir}/xbmc/screensavers
%dir %{_datadir}/xbmc/scripts
%{_datadir}/xbmc/scripts/autoexec.py
%dir %{_datadir}/xbmc/skin
%{_datadir}/xbmc/sounds
%{_datadir}/xbmc/system
%{_datadir}/xbmc/userdata
%{_datadir}/xbmc/visualisations
%dir %{_datadir}/xbmc/web
%{_datadir}/applications/xbmc.desktop
%{_datadir}/pixmaps/xbmc.png
%{_iconsdir}/hicolor/*/apps/xbmc.png

%files skin-confluence
%defattr(-,root,root)
%{_datadir}/xbmc/skin/Confluence

%files skin-pm3-hd
%defattr(-,root,root)
%{_datadir}/xbmc/skin/PM3.HD

%files screensavers-default
%defattr(-,root,root)
%{_libdir}/xbmc/screensavers/*.xbs

%files nosefart
%defattr(-,root,root)
%{_libdir}/xbmc/system/players/paplayer/nosefart-*-linux.so

%files script-examples
%defattr(-,root,root)
%{_datadir}/xbmc/scripts/examples

%files web-pm3
%defattr(-,root,root)
%{_datadir}/xbmc/web/default.asp
%{_datadir}/xbmc/web/styles

%if 0
%files web-iphone
%defattr(-,root,root)
%doc web/xbmciphone/README
%{_datadir}/xbmc/web/iphone
%endif

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
