%define build_cec 0
%define codename Jarvis

Summary:	XBMC Media Center - media player and home entertainment system
Name:		kodi
Version:	16.1
Release:	1
# nosefart audio plugin and RSXS-0.9 based screensavers are GPLv2 only
# several eventclients are GPLv3+ (in subpackages)
# libhdhomerun is LGPLv3+ with an exception (always ok to link against it)
# the rest is GPLv2+
# both GPLv2+ and GPLv2 are mentioned because plugins are not part of core
# xbmc and therefore e.g. /usr/bin/kodi is GPLv2+ with LGPLv3+ part
# as allowed by a license exception
License:	GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
Group:		Video
Url:		http://kodi.tv/
%define	srcver	17.0b5
Source0:	http://mirrors.kodi.tv/releases/source/%{version}-%{codename}.tar.gz
Source1:	kodi.rpmlintrc
# (cg) From https://github.com/opdenkamp/xbmc-pvr-addons.xz
# ./bootstrap && ./configure && make dist-xz
# commit 1db308ba7db2aa5ecea22cb032ec20e04e4e6730
# 20140529
Source2:	kodi-pvr-addons-78397afa33774b484a1649c379d9b5e6eb3180c0.tar.xz

#Patch1:		xbmc-13.0-no-win32.patch
Patch2:		kodi-14.0-EventClients-python-override.patch
Patch3:		xbmc-14.0-remove-usage-of-dead-internal-ffmpeg-function.patch
Patch4:		0001-fix-some-merory-errors-in-kodi-wiiremote.patch
# This will disable console screen blanking and cursor blinking on arm, where
# kodi will rather run on console using OpenGL ES, hence the need to disable
# features such as console blanking and cursor blinking as they'll interfer.
Patch5:		kodi-16.1-disable-console-cursor-and-blanking-on-arm.patch

# Hack to workaround upgrading from our old hack... see patch header for more
# details and an upstreaming plan.
#Patch213:	0001-hack-workaround-for-old-incompatible-PVR-addon-datab.patch

# https://bugs.mageia.org/show_bug.cgi?id=2331
# TODO: needs changes for upstreaming
#Patch214:	xbmc-13.1-Gotham-Fix-handling-of-filenames-with-spaces-in-wrapper-she.patch

# debian patches
#Patch101:	0001-Don-t-enter-ffmpeg-dir-when-using-external-ffmpeg-li.patch
#Patch102:	0002-Fix-compilation-with-libav-10-beta1.patch
#Patch103:	0004-Disable-static-ffmpeg-when-using-external-ffmpeg-liba.patch
#Patch104:	0005-Fix-av_stream_get_r_frame_rate-Libav-hack-accessor.patch
#Patch105:	0006-Define-AV_CODEC_ID_SUBRIP-to-AV_CODEC_ID_TEXT-in-lib.patch
#Patch106:	0007-Enable-using-external-ffmpeg-in-.-configure.patch
#Patch107:	04-differentiate-from-vanilla-XBMC.patch
#Patch108:	05-Fix-GLES-with-X11.patch
#Patch109:	06-use-external-libraries.patch
#FIXME: later...
#Patch110:	07-use-system-groovy.patch
#Patch111:	08-armel.patch
#Patch112:	09-use-correct-ftgl.h
#Patch113:	10-configure-all-arches.patch

BuildRequires:	afpclient-devel
BuildRequires:	avahi-common-devel
BuildRequires:	boost-devel
BuildRequires:	cap-devel
BuildRequires:	bzip2-devel
%ifarch %{ix86} x32 x86_64
BuildRequires:	crystalhd-devel
%endif
BuildRequires:	pkgconfig(cwiid)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavfilter)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	lzo-devel
BuildRequires:	pkgconfig(mariadb)
BuildRequires:	rtmp-devel
%ifnarch %{armx}
BuildRequires:	rsxs
%endif
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
%ifarch armv7hl
BuildRequires:	libgpu-viv-bin-mx6q-devel
Provides:	kodi(wandboard) = %{EVRD}
%endif
%ifarch %{armx}
BuildRequires:	pkgconfig(glesv2)
%else
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
%endif
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
%ifarch armv7hl armv7hnl
BuildRequires:	pkgconfig(libfslvpuwrap)
%endif
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
%ifnarch %{armx}
BuildRequires:	pkgconfig(libva)
%endif
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openssl)
%ifnarch %{armx}
BuildRequires:	pkgconfig(libprojectM)
%endif
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(udev)
%ifnarch %{armx}
BuildRequires:	pkgconfig(vdpau)
%endif
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
%ifnarch armv7hl
BuildRequires:	pkgconfig(x11)
%endif
%ifnarch %{armx}
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
%endif
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
%ifarch %{ix86}
BuildRequires:	nasm
%endif
Requires:	lsb-release
# for codegenrator
BuildRequires:	doxygen
BuildRequires:	java-devel
BuildRequires:	swig
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
# for FEH.py, to check current configuration is ok for kodi:
Requires:	xdpyinfo
%ifarch %{armx}
# can run without X on arm...
Suggests:	glxinfo
%else
Requires:	glxinfo
%endif
# for FEH.py to allow it to give an error message (should be available already
# on most systems):
Requires:	pygtk2
# for kodi python scripts:
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
Conflicts:	xbmc-eventclients-devel < 13.1
Obsoletes:	xbmc-eventclients-devel < 13.1

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

%prep
%setup -q -a 2 -n xbmc-%{version}%{?codename:-%{codename}}
%apply_patches
%if "%{distepoch}" <= "2014.0"
#%patch107 -p1 -R
%endif


# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

export PKG_CONFIG_PATH=%{_libdir}/pkgconfig
./bootstrap

%build
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig

# due to kodi modules that use symbols from kodi binary
# and are not using libtool
%define _disable_ld_no_undefined 1

%global debugcflags %{debugcflags}
%global optflags %{optflags} -Ofast
%configure \
	--disable-debug \
%ifarch %{armx}
	--enable-neon	\
%endif
	--with-ffmpeg=shared \
%if "%{disttag}" == "mdk"
	--enable-non-free \
%else
	--disable-non-free \
	--disable-dvdcss \
%endif
	--with-lirc-device=%{_varrun}/lirc/lircd \
	--enable-pulse \
	--enable-libcap \
	--enable-texturepacker \
	--enable-avahi \
	--disable-hal \
	--enable-mid \
	--enable-nfs \
	--enable-upnp \
%ifarch %{armx}
	--disable-gl \
	--disable-projectm \
	--disable-sdl \
	--disable-joystick \
	--disable-vdpau \
	--disable-vaapi \
	--enable-gles \
	--disable-x11 \
	--disable-xrandr \
%else
	--enable-gl \
	--enable-projectm \
	--enable-sdl \
	--enable-joystick \
	--enable-x11 \
	--enable-xrandr \
	--enable-vdpau \
	--enable-vaapi \
	--disable-gles \
	--enable-rsxs \
%endif
	--enable-libbluray \
	--disable-openmax \
	--disable-glew  \
%ifarch armv7hl
	--enable-codec=imxvpu \
%endif
	--disable-wayland \
	PYTHON=%{__python2} \
	PYTHON_VERSION=%{py2_ver}

# non-free = unrar
# dvdcss is handled via dlopen when disabled

%make V=1

%install
%makeinstall_std
%makeinstall_std -C tools/EventClients

# unused
rm %{buildroot}%{_datadir}/xsessions/{kodi,xbmc}.desktop

# our version of the above:
install -d -m755 %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/15XBMC <<EOF
NAME=Kodi
ICON=kodi.png
DESC=Kodi Media Center
EXEC=%{_bindir}/kodi-standalone
SCRIPT:
exec %{_bindir}/kodi-standalone
EOF

# unused files, TODO fix this upstream:
find %{buildroot}%{_datadir}/kodi/addons/skin.*/media -name '*.png' -delete

%check
exit 0
# for IFS and +x
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

%ifnarch %{armx}
# XXX: /usr/bin/nm terminated with signal 13 [Broken pipe]
	# check for undefined symbols in XBMC modules
	echo "$type" | grep -q "shared object" || continue
	for symbol in $(LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} ldd -r "$file" 2>&1 | grep undefined | awk '{ print $3 }'); do
		# undefined symbols may also be provided by XBMC:
		nm -f posix -D --no-demangle --defined-only %{buildroot}%{_libdir}/kodi/kodi.bin | grep -q "^$symbol " && continue
		# The symbol was not provided by XBMC.
		# Check if it is available through its dependencies:
		for filename in $(objdump -p %{buildroot}%{_libdir}/kodi/kodi.bin | grep NEEDED | awk '{ print $2 }'); do
			depfile="/%{_lib}/$filename"
			[ -e "$depfile" ] || depfile="%{_libdir}/$filename"
			nm -f posix -D --no-demangle --defined-only $depfile | grep -q "^$symbol " && continue 2
		done
		# Euphoria references rsxs PNG class, but it is never used at runtime,
		# so it results in no errors due to RTLD_LAZY being used by kodi module loader.
		case $file:$symbol in */Euphoria.xbs:_ZN3PNG*) continue; esac
		# the symbol was not found
		undefined="${undefined}$file: $symbol\n"
	done
done
%endif
ok=1
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols!" && ok=
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && ok=
[ -n "$ok" ]
%files
%doc %{_docdir}/kodi
%{_sysconfdir}/X11/wmsession.d/15XBMC
%{_bindir}/kodi
%{_bindir}/kodi-standalone
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%dir %{_libdir}/kodi
%dir %{_libdir}/kodi/addons
%dir %{_libdir}/kodi/system
%dir %{_libdir}/kodi/system/players
%dir %{_libdir}/kodi/system/players/dvdplayer
%dir %{_libdir}/kodi/system/players/paplayer
%{_libdir}/kodi/kodi.bin
%ifnarch %{armx}
%{_libdir}/kodi/kodi-xrandr
%endif
%dir %{_libdir}/kodi/addons/*
%{_libdir}/kodi/addons/*/*.so
%{_libdir}/kodi/addons/*/*.vis
#%{_libdir}/kodi/addons/*/*.xbs
%{_libdir}/kodi/addons/*/*.pvr
%{_libdir}/kodi/system/ImageLib-*.so
%{_libdir}/kodi/system/libcmyth-*.so
%{_libdir}/kodi/system/libcpluff-*.so
%{_libdir}/kodi/system/libexif-*.so
%{_libdir}/kodi/system/players/dvdplayer/libdvdcss-*.so
%{_libdir}/kodi/system/players/dvdplayer/libdvdnav-*.so
#%{_libdir}/kodi/system/players/paplayer/adpcm-*.so
%{_libdir}/kodi/system/players/paplayer/nosefart-*.so
%{_libdir}/kodi/system/players/paplayer/stsoundlibrary-*.so
%{_libdir}/kodi/system/players/paplayer/timidity-*.so
%{_libdir}/kodi/system/players/paplayer/vgmstream-*.so
%ifarch %{ix86}
%{_libdir}/kodi/system/players/paplayer/SNESAPU-*.so
%endif
%{_libdir}/xbmc
%dir %{_datadir}/kodi
%{_datadir}/kodi/addons
%{_datadir}/kodi/FEH.py
%{_datadir}/kodi/language
%{_datadir}/kodi/media
%{_datadir}/kodi/sounds
%{_datadir}/kodi/system
%{_datadir}/kodi/userdata
%{_datadir}/xbmc
%{_datadir}/applications/kodi.desktop
%{_iconsdir}/hicolor/*/apps/kodi.png

%files eventclients-common
%{python2_sitelib}/kodi
%dir %{_datadir}/pixmaps/kodi
%{_datadir}/pixmaps/kodi/*.png

%files devel
%dir %{_includedir}/kodi
%{_includedir}/kodi/*
%{_includedir}/xbmc
%{_libdir}/kodi/*.cmake

%files eventclient-j2me
%{_bindir}/kodi-j2meremote

%files eventclient-ps3
%{_bindir}/kodi-ps3d
%{_bindir}/kodi-ps3remote

%files eventclient-xbmc-send
%{_bindir}/kodi-send

%files eventclient-wiiremote
%{_bindir}/kodi-wiiremote
