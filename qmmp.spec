# TODO: Output/oss4 plugin (R: soundcard.h from OSS 4)
#
# Conditional build:
%bcond_with	jack1	# JACK1 (0.12x) instead of JACK2 (1.9.x)

Summary:	XMMS like audio player based on Qt
Summary(hu.UTF-8):	XMMS-szerű Qt alapú audio-lejátszó
Summary(pl.UTF-8):	Odtwarzacz muzyki w stylu XMMS oparty na Qt
Name:		qmmp
Version:	1.2.0
Release:	4
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	cc3468fe610412e2db5113d8ce0a379e
Patch0:		ffmpeg4.patch
URL:		http://qmmp.ylsoftware.com/
BuildRequires:	Qt5Core-devel >= 5.4.0
BuildRequires:	Qt5DBus-devel >= 5.4.0
BuildRequires:	Qt5Gui-devel >= 5.4.0
BuildRequires:	Qt5Multimedia-devel >= 5.4.0
BuildRequires:	Qt5Network-devel >= 5.4.0
BuildRequires:	Qt5Widgets-devel >= 5.4.0
BuildRequires:	Qt5X11Extras-devel >= 5.4.0
BuildRequires:	alsa-lib-devel >= 1.0.1
BuildRequires:	cmake >= 2.8.11
BuildRequires:	curl-devel >= 7.16
BuildRequires:	enca-devel >= 1.9
BuildRequires:	faad2-devel >= 2.6.1
# libavcodec>=55.18.102 libavformat>=55.12.1000 libavutil>=52.38.100
BuildRequires:	ffmpeg-devel >= 2.0
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	game-music-emu-devel >= 0.5.5
BuildRequires:	gettext-tools
%{?with_jack1:BuildRequires:	jack-audio-connection-kit-devel >= 0.122.0}
%{!?with_jack1:BuildRequires:	jack-audio-connection-kit-devel >= 1.9.8}
BuildRequires:	libarchive-devel >= 3.2.0
BuildRequires:	libbs2b-devel >= 3.0.0
BuildRequires:	libcddb-devel >= 1.3.1
BuildRequires:	libcdio-devel >= 0.80
BuildRequires:	libcdio-paranoia-devel >= 0.90_10.2
BuildRequires:	libmad-devel
BuildRequires:	libmms-devel >= 0.4
BuildRequires:	libmodplug-devel >= 0.8.4
BuildRequires:	libmpcdec-devel >= 1.2.6
BuildRequires:	libogg-devel
BuildRequires:	libprojectM-devel >= 2.0.0
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libshout-devel
BuildRequires:	libsidplayfp-devel >= 1.0.3
BuildRequires:	libsndfile-devel >= 1.0.21
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	opus-devel >= 1.0.2
BuildRequires:	opusfile-devel >= 0.2
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.15
BuildRequires:	qt5-build >= 5.4.0
BuildRequires:	qt5-linguist >= 5.4.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	soxr-devel >= 0.1.0
BuildRequires:	taglib-devel >= 1.11
BuildRequires:	wavpack-devel >= 4.41
BuildRequires:	wildmidi-devel >= 0.2.3.4
BuildRequires:	xorg-lib-libX11-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	Qt5Core >= 5.4.0
Requires:	Qt5DBus >= 5.4.0
Requires:	Qt5Gui >= 5.4.0
Requires:	Qt5Multimedia >= 5.4.0
Requires:	Qt5Network >= 5.4.0
Requires:	Qt5Widgets >= 5.4.0
Requires:	Qt5X11Extras >= 5.4.0
Requires:	curl-libs >= 7.16
Requires:	enca-libs >= 1.9
Requires:	faad2-libs >= 2.6.1
Requires:	ffmpeg-libs >= 2.0
Requires:	flac >= 1.1.3
Requires:	game-music-emu >= 0.5.5
%{?with_jack1:Requires:	jack-audio-connection-kit-libs >= 0.102.5}
%{!?with_jack1:Requires:	jack-audio-connection-kit-libs >= 1.9.8}
Requires:	libarchive >= 3.2.0
Requires:	libbs2b >= 3.0.0
Requires:	libcddb >= 1.3.1
Requires:	libcdio >= 0.80
Requires:	libcdio-paranoia >= 0.90_10.2
Requires:	libmms >= 0.4
Requires:	libmodplug >= 0.8.4
Requires:	libmpcdec >= 1.2.6
Requires:	libprojectM >= 2.0.0
Requires:	libsidplayfp >= 1.0.3
Requires:	libsndfile >= 1.0.21
Requires:	opus >= 1.0.2
Requires:	opusfile >= 0.2
Requires:	pulseaudio-libs >= 0.9.15
Requires:	soxr >= 0.1.0
Requires:	taglib >= 1.11
Requires:	wavpack-libs >= 4.41
Requires:	wildmidi >= 0.2.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qmmp (Qt-based Multimedia Player) is an audio player that supports:
- file formats among: Vorbis, FLAC, MPEG1, WMA, WAV...
- plugins,
- Winamp and XMMS skins and more.

%description -l hu.UTF-8
A lejátszó a következőket támogatja:
- fájlformátumok: Vorbis, FLAC, MPEG1, WMA, WAV
- pluginok
- Wnamp és XMMS szkinek és még sok mást.

%description -l pl.UTF-8
Qmmp (Qt-based Multimedia Player) to odtwarzacz dźwięku obsługujący
m.in.:
- formaty plików: Vorbis, FLAC, MPEG1, WMA, WAV i inne,
- system wtyczek,
- skórki z XMMS i Winampa.

%package libs
Summary:	Qmmp (Qt-based Multimedia Player) shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone odtwarzacza dźwięku Qmmp
Group:		Libraries
Requires:	Qt5Core >= 5.4.0
Requires:	Qt5Gui >= 5.4.0
Requires:	Qt5Network >= 5.4.0
Requires:	Qt5Widgets >= 5.4.0
Conflicts:	qmmp < 1.1.8-3

%description libs
Qmmp (Qt-based Multimedia Player) shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone odtwarzacza dźwięku Qmmp, opartego na Qt.

%package devel
Summary:	Header files for qmmp
Summary(pl.UTF-8):	Pliki nagłówkowe qmmp
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.4.0
Requires:	Qt5Gui-devel >= 5.4.0
Requires:	Qt5Network-devel >= 5.4.0
Requires:	Qt5Widgets-devel >= 5.4.0

%description devel
Header files for qmmp.

%description devel -l pl.UTF-8
Pliki nagłówkowe qmmp.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DUSE_OSS=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.CC-by-sa_V4 ChangeLog ChangeLog.svn README
%lang(ru) %doc ChangeLog.rus README.RUS
%lang(uk) %doc README.UKR
%attr(755,root,root) %{_bindir}/qmmp
%dir %{_libdir}/qmmp
%dir %{_libdir}/qmmp/CommandLineOptions
%attr(755,root,root) %{_libdir}/qmmp/CommandLineOptions/lib*option.so
%dir %{_libdir}/qmmp/Effect
# R: libbs2b
%attr(755,root,root) %{_libdir}/qmmp/Effect/libbs2b.so
%attr(755,root,root) %{_libdir}/qmmp/Effect/libcrossfade.so
# R: libogg libvorbis
%attr(755,root,root) %{_libdir}/qmmp/Effect/libfilewriter.so
%attr(755,root,root) %{_libdir}/qmmp/Effect/libladspa.so
# R: soxr
%attr(755,root,root) %{_libdir}/qmmp/Effect/libsoxr.so
%attr(755,root,root) %{_libdir}/qmmp/Effect/libstereo.so
%dir %{_libdir}/qmmp/Engines
%attr(755,root,root) %{_libdir}/qmmp/Engines/libmplayer.so
%dir %{_libdir}/qmmp/FileDialogs
%attr(755,root,root) %{_libdir}/qmmp/FileDialogs/lib*dialog.so
%dir %{_libdir}/qmmp/General
# R: taglib
%attr(755,root,root) %{_libdir}/qmmp/General/libconverter.so
%attr(755,root,root) %{_libdir}/qmmp/General/libcopypaste.so
%attr(755,root,root) %{_libdir}/qmmp/General/libcovermanager.so
%attr(755,root,root) %{_libdir}/qmmp/General/libfileops.so
%attr(755,root,root) %{_libdir}/qmmp/General/libgnomehotkey.so
# R: Qt5DBus
%attr(755,root,root) %{_libdir}/qmmp/General/libhal.so
# R: libX11
%attr(755,root,root) %{_libdir}/qmmp/General/libhotkey.so
# R: Qt5DBus
%attr(755,root,root) %{_libdir}/qmmp/General/libkdenotify.so
%attr(755,root,root) %{_libdir}/qmmp/General/liblyrics.so
# R: Qt5DBus
%attr(755,root,root) %{_libdir}/qmmp/General/libmpris.so
# R: Q5X11Extras libX11
%attr(755,root,root) %{_libdir}/qmmp/General/libnotifier.so
# R: taglib
%attr(755,root,root) %{_libdir}/qmmp/General/librgscan.so
%attr(755,root,root) %{_libdir}/qmmp/General/libscrobbler.so
%attr(755,root,root) %{_libdir}/qmmp/General/libstatusicon.so
%attr(755,root,root) %{_libdir}/qmmp/General/libstreambrowser.so
%attr(755,root,root) %{_libdir}/qmmp/General/libtrackchange.so
# R: Qt5DBus
%attr(755,root,root) %{_libdir}/qmmp/General/libudisks2.so
%dir %{_libdir}/qmmp/Input
# R: faad2 taglib
%attr(755,root,root) %{_libdir}/qmmp/Input/libaac.so
# R: libarchive
%attr(755,root,root) %{_libdir}/qmmp/Input/libarchive.so
# R: libcddb libcdio libcdio-paranoia
%attr(755,root,root) %{_libdir}/qmmp/Input/libcdaudio.so
# R: enca-libs
%attr(755,root,root) %{_libdir}/qmmp/Input/libcue.so
# R: ffmpeg-libs
%attr(755,root,root) %{_libdir}/qmmp/Input/libffmpeg.so
# R: flac taglib
%attr(755,root,root) %{_libdir}/qmmp/Input/libflac.so
# R: game-music-emu
%attr(755,root,root) %{_libdir}/qmmp/Input/libgme.so
# R: libmad taglib
%attr(755,root,root) %{_libdir}/qmmp/Input/libmad.so
# R: libmodplug
%attr(755,root,root) %{_libdir}/qmmp/Input/libmodplug.so
# R: libmpcdec taglib
%attr(755,root,root) %{_libdir}/qmmp/Input/libmpc.so
# R: opus opusfile taglib
%attr(755,root,root) %{_libdir}/qmmp/Input/libopus.so
# R: libsidplayfp
%attr(755,root,root) %{_libdir}/qmmp/Input/libsid.so
# R: libsndfile
%attr(755,root,root) %{_libdir}/qmmp/Input/libsndfile.so
# R: libvorbis taglib
%attr(755,root,root) %{_libdir}/qmmp/Input/libvorbis.so
# R: wavpack
%attr(755,root,root) %{_libdir}/qmmp/Input/libwavpack.so
# R: wildmidi
%attr(755,root,root) %{_libdir}/qmmp/Input/libwildmidi.so
%dir %{_libdir}/qmmp/Output
# R: alsa-lib
%attr(755,root,root) %{_libdir}/qmmp/Output/libalsa.so
# R: jack-audio-connection-kit-libs soxr
%attr(755,root,root) %{_libdir}/qmmp/Output/libjack.so
%attr(755,root,root) %{_libdir}/qmmp/Output/libnull.so
%attr(755,root,root) %{_libdir}/qmmp/Output/liboss.so
# R: pulseaudio-libs
%attr(755,root,root) %{_libdir}/qmmp/Output/libpulseaudio.so
# R: QtMultimedia
%attr(755,root,root) %{_libdir}/qmmp/Output/libqtmultimedia.so
# R: libogg libshout libvorbis soxr
%attr(755,root,root) %{_libdir}/qmmp/Output/libshout.so
%dir %{_libdir}/qmmp/PlayListFormats
%attr(755,root,root) %{_libdir}/qmmp/PlayListFormats/lib*playlistformat.so
%dir %{_libdir}/qmmp/Transports
# R: curl-libs enca-libs
%attr(755,root,root) %{_libdir}/qmmp/Transports/libhttp.so
# R: libmms
%attr(755,root,root) %{_libdir}/qmmp/Transports/libmms.so
%dir %{_libdir}/qmmp/Ui
%attr(755,root,root) %{_libdir}/qmmp/Ui/libqsui.so
# R: libX11
%attr(755,root,root) %{_libdir}/qmmp/Ui/libskinned.so
%dir %{_libdir}/qmmp/Visual
%attr(755,root,root) %{_libdir}/qmmp/Visual/libanalyzer.so
%attr(755,root,root) %{_libdir}/qmmp/Visual/libprojectm.so
%{_desktopdir}/qmmp.desktop
%{_desktopdir}/qmmp_dir.desktop
%{_desktopdir}/qmmp_enqueue.desktop
%dir %{_datadir}/qmmp
%dir %{_datadir}/qmmp/images
%{_datadir}/qmmp/images/*.png
%{_iconsdir}/hicolor/*x*/apps/qmmp.png
%{_iconsdir}/hicolor/scalable/apps/qmmp.svgz
%{_iconsdir}/hicolor/scalable/apps/qmmp-simple.svgz

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqmmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmp.so.1
%attr(755,root,root) %{_libdir}/libqmmpui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmpui.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqmmp.so
%attr(755,root,root) %{_libdir}/libqmmpui.so
%{_includedir}/qmmp
%{_includedir}/qmmpui
%{_pkgconfigdir}/qmmp.pc
%{_pkgconfigdir}/qmmpui.pc
