%define build_cec 1
%define codename Gotham

Summary:	XBMC Media Center - media player and home entertainment system
Name:		xbmc
Version:	13.1
Release:	1
# nosefart audio plugin and RSXS-0.9 based screensavers are GPLv2 only
# several eventclients are GPLv3+ (in subpackages)
# libhdhomerun is LGPLv3+ with an exception (always ok to link against it)
# the rest is GPLv2+
# both GPLv2+ and GPLv2 are mentioned because plugins are not part of core
# xbmc and therefore e.g. /usr/bin/xbmc is GPLv2+ with LGPLv3+ part
# as allowed by a license exception
License:	GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
Group:		Video
Url:		http://xbmc.org/
Source0:	http://mirrors.xbmc.org/releases/source/%{name}-%{version}.tar.gz
Source1:	xbmc.rpmlintrc
# (cg) From https://github.com/opdenkamp/xbmc-pvr-addons
# ./bootstrap && ./configure && make dist-xz
# commit 1db308ba7db2aa5ecea22cb032ec20e04e4e6730
# 20140529
Source2:	xbmc-pvr-addons-1db308ba7db2aa5ecea22cb032ec20e04e4e6730.tar.xz

Patch0:		xbmc-13.0-external-ffmpeg.patch
Patch1:		xbmc-13.0-no-win32.patch
# Display Music Videos in "Artist - Name" format instead of just "Name"
Patch2:		xbmc-13.0-upnp-musicvideos-artist.patch
# Fix bug with UPnP playback for Playlists
Patch3:		xbmc-13.0-upnp-playlists.patch

# work around weird gold output redirection weirdness...
Patch4:		xbmc-13.1-try-work-around-gold-linker-output-fd-weirdness.patch
# Fix bootstrap script return value on error
Patch5:		xbmc-bootstrap-return-value.patch

# Hack to workaround upgrading from our old hack... see patch header for more
# details and an upstreaming plan.
#Patch213:	0001-hack-workaround-for-old-incompatible-PVR-addon-datab.patch

# https://bugs.mageia.org/show_bug.cgi?id=2331
# TODO: needs changes for upstreaming
Patch214:	xbmc-13.1-Gotham-Fix-handling-of-filenames-with-spaces-in-wrapper-she.patch

# debian patches
Patch101:	0001-Don-t-enter-ffmpeg-dir-when-using-external-ffmpeg-li.patch
Patch102:	0002-Fix-compilation-with-libav-10-beta1.patch
Patch103:	0004-Disable-static-ffmpeg-when-using-external-ffmpeg-liba.patch
Patch104:	0005-Fix-av_stream_get_r_frame_rate-Libav-hack-accessor.patch
Patch105:	0006-Define-AV_CODEC_ID_SUBRIP-to-AV_CODEC_ID_TEXT-in-lib.patch
#Patch106:	0007-Enable-using-external-ffmpeg-in-.-configure.patch
Patch107:	04-differentiate-from-vanilla-XBMC.patch
Patch108:	05-Fix-GLES-with-X11.patch
Patch109:	06-use-external-libraries.patch
Patch110:	07-use-system-groovy.patch
Patch111:	08-armel.patch
Patch112:	09-use-correct-ftgl.h
Patch113:	10-configure-all-arches.patch

BuildRequires:	afpclient-devel
BuildRequires:	avahi-common-devel
BuildRequires:	boost-devel
BuildRequires:	cap-devel
BuildRequires:	bzip2-devel
BuildRequires:	crystalhd-devel
BuildRequires:	cwiid-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	hdhomerun-devel
BuildRequires:	jpeg-devel
BuildRequires:	lzo-devel
BuildRequires:	mariadb-devel
BuildRequires:	rtmp-devel
BuildRequires:	rsxs
BuildRequires:	ssh-devel
BuildRequires:	tiff-devel
BuildRequires:	tinyxml-devel
BuildRequires:	yajl-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gl)
#BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libcdio)
%if %{build_cec}
BuildRequires:	pkgconfig(libcec) >= 2:1:0
%else
BuildConflicts:	pkgconfig(libcec)
%endif
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmicrohttpd)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	pkgconfig(libnfs)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsidplay2)
BuildRequires:	pkgconfig(libshairport)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libprojectM)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
%if "%{disttag}" == "mdk"
BuildRequires:	lame-devel
%endif
%ifarch %{ix86} x86_64
BuildRequires:	nasm
%endif
Requires:	lsb-release
# for codegenrator
BuildRequires:	doxygen
BuildRequires:	java-rpmbuild
BuildRequires:	swig
%if "%{distepoch}" >= "2014.0"
BuildRequires:	groovy
%endif
BuildRequires:	apache-commons-lang

Requires:	%{dlopen_req curl}
Requires:	%{dlopen_req FLAC}
Requires:	%{dlopen_req mad}
Requires:	%{dlopen_req ogg}
Requires:	%{dlopen_req vorbis}
Requires:	%{dlopen_req vorbisenc}
Requires:	%{dlopen_req vorbisfile}
Requires:	%{dlopen_req modplug}
Requires:	%{dlopen_req rtmp}
Requires:	%{dlopen_req mpeg2}
Requires:	%{dlopen_req ass}
Requires:	%{dlopen_req bluray}
Requires:	%{dlopen_req nfs}
Requires:	%{dlopen_req afpclient}
Requires:	%{dlopen_req plist}
Requires:	%{dlopen_req shairport}
%if %{build_cec}
Requires:	%{dlopen_req cec}
%endif
# not nearly as common as the above, so just suggest instead for now:
Suggests:	%{dlopen_req crystalhd}
# TODO: FEH.py is useless nowadays, drop it here and upstream.
# for FEH.py, to check current configuration is ok for xbmc:
Requires:	xdpyinfo
Requires:	glxinfo
# for FEH.py to allow it to give an error message (should be available already
# on most systems):
Requires:	pygtk2
# for xbmc python scripts:
Requires:	python-imaging
# Packages not shipped in core:
Suggests:	%{_lib}lame0
Suggests:	%{_lib}dvdcss2

%description
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

While XBMC functions very well as a standard media player application
for your computer, it has been designed to be the perfect companion
for your HTPC. Supporting an almost endless range of remote controls,
and combined with its beautiful interface and powerful skinning
engine, XBMC feels very natural to use from the couch and is the
ideal solution for your home theater.

Support for RAR files is not included due to license issues.

%package	devel
Summary:	Development files for XBMC
License:	GPLv2+
Group:		Development/C
Provides:	xbmc-eventclients-devel = %{EVRD}
Conflicts:	xbmc-eventclients-devel < 13.0
Obsoletes:	xbmc-eventclients-devel < 13.0

%description	devel
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build addons and eventclients.

%package	eventclients-common
Summary:	Common files for XBMC eventclients
License:	GPLv2+
Group:		Video

%description	eventclients-common
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains common files for eventclients.

%package	eventclient-wiiremote
Summary:	Wii Remote eventclient for XBMC
License:	GPLv3+
Group:		Video
Requires:	%{name}-eventclients-common = %{EVRD}

%description	eventclient-wiiremote
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%package	eventclient-j2me
Summary:	J2ME eventclient for XBMC
License:	GPLv2+
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{EVRD}

%description	eventclient-j2me
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the J2ME eventclient, providing a bluetooth
server that can communicate with a mobile tool supporting J2ME.

%package	eventclient-ps3
Summary:	PS3 eventclients for XBMC
License:	GPLv2+
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{EVRD}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:	python-gobject avahi-python python-dbus

%description	eventclient-ps3
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%package	eventclient-xbmc-send
Summary:	PS3 eventclient for XBMC
License:	GPLv2+
Group:		Video
Requires:	%{name}-eventclients-common = %{EVRD}

%description	eventclient-xbmc-send
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the xbmc-send eventclient.
#----------------------------------------------------------------------------

%prep
%setup -q -a 2 -n %{name}-%{version}%{?codename:-%{codename}}
%apply_patches
%if "%{distepoch}" <= "2014.0"
#%patch107 -p1 -R
%endif

find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" -o -name "missing" -o -name "bootstrap*" |xargs sed -i -e 's,configure.in,configure.ac,g'
cp configure.in configure.ac

# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete

# GPLv2 only
rm -r lib/cmyth/Win32/include/mysql

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

pushd xbmc/interfaces/python/
doxygen -u
popd
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig
export GIT_REV="tarball"
./bootstrap
ln -s configure.ac configure.in

%build
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig
export GIT_REV="tarball"

# due to xbmc modules that use symbols from xbmc binary
# and are not using libtool
%define _disable_ld_no_undefined 1

# Workaround configure using git to override GIT_REV (TODO: fix it properly)
export ac_cv_prog_HAVE_GIT="no"

%global debugcflags %{debugcflags} -fno-var-tracking-assignments
%configure \
	--disable-debug \
%ifarch %{arm}
	--enable-neon	\
%endif
	--enable-external-libraries \
	--enable-external-ffmpeg \
%if "%{disttag}" == "mdk"
	--enable-non-free \
%else
	--disable-non-free \
	--disable-dvdcss \
%endif
	--enable-goom \
	--enable-pulse \
	--with-lirc-device=%{_varrun}/lirc/lircd \
	--enable-libcap \
	--enable-texturepacker \
	--enable-libusb \
	--enable-libmp3lame \
	--enable-avahi \
	--disable-hal \
	--enable-mid \
	--enable-ffmpeg-libvorbis \
	--enable-nfs \
	--enable-upnp \
	--enable-x11 \
	--enable-projectm \
	--enable-xrandr \
	--enable-gl \
	--enable-sdl \
	--enable-vdpau \
	--enable-vaapi \
	--enable-libbluray \
	--disable-openmax \
	--enable-rsxs \
	--disable-gles \
	--disable-wayland

# non-free = unrar
# dvdcss is handled via dlopen when disabled
# (cg) We cannot enable MythTV support easily via a passthrough configure from above
#      so re-run configure here and explicitly pass the --enable-addons-with-dependencies option
pushd pvr-addons
%configure \
	--enable-addons-with-dependencies \
	--enable-release
%make
popd

%make
%make -C tools/EventClients wiimote

%install
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
echo Silencing output of undefined symbol and FHS conformance checks
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
		case $file:$symbol in */Euphoria.xbs:_ZN3PNG*) continue; esac
		# the symbol was not found
		undefined="${undefined}$file: $symbol\n"
	done
done
ok=1
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols!" && ok=
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && ok=
[ -n "$ok" ]
)

%files
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
%{_libdir}/xbmc/xbmc.bin
%{_libdir}/xbmc/xbmc-xrandr
%dir %{_libdir}/xbmc/addons/*
%{_libdir}/xbmc/addons/*/*.so
%{_libdir}/xbmc/addons/*/*.vis
%{_libdir}/xbmc/addons/*/*.xbs
%{_libdir}/xbmc/addons/*/*.pvr
%{_libdir}/xbmc/system/ImageLib-*.so
%{_libdir}/xbmc/system/libcmyth-*.so
%{_libdir}/xbmc/system/libcpluff-*.so
%{_libdir}/xbmc/system/libexif-*.so
%{_libdir}/xbmc/system/players/dvdplayer/libdvdcss-*.so
%{_libdir}/xbmc/system/players/dvdplayer/libdvdnav-*.so
#%{_libdir}/xbmc/system/players/paplayer/adpcm-*.so
%{_libdir}/xbmc/system/players/paplayer/nosefart-*.so
%{_libdir}/xbmc/system/players/paplayer/stsoundlibrary-*.so
%{_libdir}/xbmc/system/players/paplayer/timidity-*.so
%{_libdir}/xbmc/system/players/paplayer/vgmstream-*.so
%ifarch %{ix86}
%{_libdir}/xbmc/system/players/paplayer/SNESAPU-*.so
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
%{python_sitelib}/xbmc
%dir %{_datadir}/pixmaps/xbmc
%{_datadir}/pixmaps/xbmc/*.png

%files devel
%dir %{_includedir}/xbmc
%{_includedir}/xbmc/*
%{_libdir}/xbmc/*.cmake

%files eventclient-j2me
%{_bindir}/xbmc-j2meremote

%files eventclient-ps3
%{_bindir}/xbmc-ps3d
%{_bindir}/xbmc-ps3remote

%files eventclient-xbmc-send
%{_bindir}/xbmc-send

%files eventclient-wiiremote
%{_bindir}/xbmc-wiiremote
