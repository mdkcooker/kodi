# Current version 2.0.1 is not supported by XBMC 11.0
%define build_cec	0

%define branch_release	Eden
%define extra_feature	pvr
%define snap	0
%define pre	0
%define rel	4

%if %snap
%define branch	%branch_release.%extra_feature
%else
%define branch	%extra_feature
%endif

%define branchr	%([ "%branch" ] && echo .%branch | tr - _)

Summary:	XBMC Media Center - media player and home entertainment system
Name:		xbmc
Version:	11.0
%if %{snap}
Release:	0.git%{snap}%{branchr}.%{rel}
Source:		%{name}-%{branch_release}-%{snap}.tar.xz
%else
%if %{pre}
Release:	0.%{pre}%{branchr}.%{rel}
Source:		%{name}-%{version}-%{branch_release}_%{pre}.tar.gz
%else
Release:	1.%{branch}.%{rel}
Source:		%{name}-%{version}.tar.gz
%endif
%endif
URL:		http://xbmc.org/

# bring snapshot up-to-date with pvr branch
# https://github.com/opdenkamp/xbmc
# git diff 14feb096bcea1e..opdenkamp/Eden-pvr
Patch0:		xbmc-Eden-pvr-rc1.1+20120324-g6a4c861.patch
# gcc 4.7 support
Patch1:		xbmc-wiiremote-missing-include.patch

# Disable updates of the default skin. Our one is the PVR version, while the
# one in the XBMC.org addon repository would be the vanilla one (Confluence
# is currently not in the addon repository, though, as of 2012-03).
Patch201:	xbmc-disable-confluence-update.patch

# Make the MythTV PVR client buildable (submitted upstream):
Patch211:	0001-fixed-undefined-symbols-in-MythTV-PVR-client.patch

# Hack to workaround upgrading from our old hack... see patch header for more
# details and an upstreaming plan.
Patch213:	0001-hack-workaround-for-old-incompatible-PVR-addon-datab.patch

# New ffmpeg API support

Patch301:	0101-Update-ffmpeg-to-n0.10.2-f139838d6473c7b5152178f602c.patch
Patch302:	0102-Update-patches.patch
Patch303:	0103-Drop-neon-patch-that-doesn-t-apply-anymore.patch
Patch304:	0104-Drop-patch-for-win32-build.patch
Patch305:	0105-Drop-patch-for-cdxa-probe-it-causes-missdetections-o.patch
Patch306:	0106-Drop-now-merged-or-redundant-patches.patch
Patch307:	0107-replace-depreciated-av_open_input_stream-file-with-n.patch
Patch308:	0108-replace-depreciated-ByteIOContext-with-AVIOContext.patch
Patch309:	0109-replace-depreciated-AVMetadata-Tag-with-AVDictionary.patch
Patch310:	0110-Don-t-listen-to-depreciated-return-value-of-av_read_.patch
Patch311:	0111-Don-t-use-depreciated-avcodec_thread_init.patch
Patch312:	0112-Replace-depreciated-av_find_stream_info-with-avforma.patch
Patch313:	0113-Replace-more-depreciated-ffmpeg-functions.patch
Patch314:	0114-Drop-support-for-ffmpeg-version-older-than-our-built.patch
Patch315:	0115-Replace-deprecated-is_streamed-with-new-seekable-fla.patch
Patch316:	0116-Remove-old-code-depending-on-deprecated-file_size.patch
Patch317:	0117-changed-replace-old-libavfilter-integration-with-nul.patch
Patch318:	0118-changed-replace-old-swscale-pixel-format-conversion-.patch
Patch319:	0119-Drop-url_set_interrupt_cb-usage-which-was-removed-in.patch
Patch320:	0120-Do-not-map-url_fdopen-as-it-is-deprecated-and-gone-i.patch
Patch321:	0121-Replace-av_write_header-by-avformat_write_header.patch
Patch322:	0122-Remove-av_set_parameters.patch
Patch323:	0123-Replace-av_metadata_-get-set2-by-av_dict_-get-set.patch
Patch324:	0124-Merge-av_close_input_-file-stream-into-avformat_clos.patch
Patch325:	0125-Replace-init_put_byte-by-avio_alloc_context.patch
Patch326:	0126-Replace-dump_format-by-av_dump_format.patch
Patch327:	0127-Replace-url_-functions-by-their-avio_-counterparts.patch
Patch328:	0128-Remove-av_alloc_put_byte-and-replace-its-occurences-.patch
Patch329:	0129-Include-libavfilter-avcodec.h-for-av_vsrc_buffer_add.patch
Patch330:	0130-Remove-assignment-to-stream_copy-which-is-never-read.patch
Patch331:	0131-Do-not-set-AVFrame.age.patch
Patch332:	0132-Use-av_opt_set-instead-of-av_set_string3-and-drop-su.patch
Patch333:	0133-Replace-deprecated-av_get_bits_per_sample_fmt-by-av_.patch
Patch334:	0134-Convert-to-avcodec_decode_audio4-and-drop-avcodec_de.patch
Patch335:	0135-osx-ios-atv2-build-and-link-static-libs-for-ffmpeg-b.patch
Patch336:	0136-changed-Only-allow-slice-based-parallel-decoding.patch
Patch337:	0137-fixed-crash-if-audio-decoder-for-some-reason-doesn-t.patch
Patch338:	0138-dvdplayer-previous-picture-is-invalidated-by-a-call-.patch
Patch339:	0139-dvdplayer-Recalculate-codecname-when-we-update-based.patch
Patch340:	0140-dvdplayer-avoid-crashing-if-ffmpeg-contains-more-tha.patch
Patch341:	0141-Add-support-for-new-ffmpeg-10-11-api.patch
Patch342:	0142-Bring-av_read_frame_flush-in-line-with-ffmpeg-git.patch
Patch343:	0143-avutil-add-av_get_default_channel_layout-for-later-u.patch
Patch344:	0144-Use-libavutil-av_get_default_channel_layout-instead-.patch
Patch345:	0145-DllAvCodec-Remove-now-unused-private-avcodec_guess_c.patch

Patch360:	xbmc-11.0-more-ffmpeg-fixes.patch

# nosefart audio plugin and RSXS-0.9 based screensavers are GPLv2 only
# several eventclients are GPLv3+ (in subpackages)
# libhdhomerun is LGPLv3+ with an exception (always ok to link against it)
# the rest is GPLv2+
# both GPLv2+ and GPLv2 are mentioned because plugins are not part of core
# xbmc and therefore e.g. /usr/bin/xbmc is GPLv2+ with LGPLv3+ part
# as allowed by a license exception
License:	GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
Group:		Video
BuildRequires:	afpclient-devel
BuildRequires:	avahi-common-devel
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	crystalhd-devel
BuildRequires:	cwiid-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	liblzo2-devel
BuildRequires:	mysql-devel
BuildRequires:	python-devel
BuildRequires:	rtmp-devel
BuildRequires:	ssh-devel
BuildRequires:	tiff-devel
BuildRequires:	yajl-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libcdio)
%if %{build_cec}
BuildRequires:	pkgconfig(libcec)
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
BuildRequires:	pkgconfig(libshairport)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
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
%ifarch %ix86
BuildRequires:	nasm
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
Requires:	%dlopenreq mpeg2
Requires:	%dlopenreq ass
Requires:	%dlopenreq bluray
Requires:	%dlopenreq nfs
Requires:	%dlopenreq afpclient
Requires:	%dlopenreq plist
Requires:	%dlopenreq shairport
%if %{build_cec}
Requires:	%dlopenreq cec
%endif
# not nearly as common as the above, so just suggest instead for now:
Suggests:	%dlopenreq crystalhd
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

This is the stable version of XBMC from the %branch_release release branch,
with PVR support added from opdenkamp %branch_release-pvr branch. Support for
RAR files is not included due to license issues.

%package	eventclients-common
Summary:	Common files for XBMC eventclients
Group:		Video
License:	GPLv2+
%py_requires

%description	eventclients-common
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains common files for eventclients.

%package	eventclients-devel
Summary:	Development files for XBMC eventclients
Group:		Development/C
License:	GPLv2+

%description	eventclients-devel
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build eventclients.

%package	eventclient-wiiremote
Summary:	Wii Remote eventclient for XBMC
Group:		Video
License:	GPLv3+
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-wiiremote
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%package	eventclient-j2me
Summary:	J2ME eventclient for XBMC
Group:		Video
License:	GPLv2+
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
License:	GPLv2+
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:	python-gobject avahi-python python-dbus

%description	eventclient-ps3
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%package	eventclient-xbmc-send
Summary:	PS3 eventclient for XBMC
Group:		Video
License:	GPLv2+
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-xbmc-send
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the xbmc-send eventclient.

%prep
%if %snap
%setup -q -n %{name}-%{branch_release}-%{snap}
%else
%if %pre
%setup -q -n %{name}-%{version}-%{branch_release}_%{pre}
%else
%setup -q
%endif
%endif
%apply_patches
# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete

# GPLv2 only
rm -r lib/cmyth/Win32/include/mysql
# BSD 4-clause
rm -r xbmc/cores/DllLoader/exports/emu_socket

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

%build
%if %snap
export GIT_REV=%snap
%else
export GIT_REV="tarball"
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
	--disable-non-free \
	--disable-dvdcss \
	--enable-goom \
	--with-lirc-device=/var/run/lirc/lircd

# non-free = unrar
# dvdcss is handled via dlopen when disabled

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
%{_libdir}/xbmc/addons/*/*.pvr
%{_libdir}/xbmc/addons/*/*.vis
%{_libdir}/xbmc/addons/*/*.xbs
%{_libdir}/xbmc/system/ImageLib-*-linux.so
%{_libdir}/xbmc/system/hdhomerun-*-linux.so
%{_libdir}/xbmc/system/libcmyth-*-linux.so
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

%files eventclients-devel
%dir %{_includedir}/xbmc
%{_includedir}/xbmc/xbmcclient.h

%files eventclient-j2me
%{_bindir}/xbmc-j2meremote

%files eventclient-ps3
%{_bindir}/xbmc-ps3d
%{_bindir}/xbmc-ps3remote

%files eventclient-xbmc-send
%{_bindir}/xbmc-send

%files eventclient-wiiremote
%{_bindir}/xbmc-wiiremote


