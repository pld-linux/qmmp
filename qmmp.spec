# TODO: Output/oss4 plugin (R: soundcard.h from OSS 4)
#
# Conditional build:
%bcond_with	jack1	# JACK1 (0.12x) instead of JACK2 (1.9.x)

Summary:	XMMS like audio player based on Qt
Summary(hu.UTF-8):	XMMS-szerű Qt alapú audio-lejátszó
Summary(pl.UTF-8):	Odtwarzacz muzyki w stylu XMMS oparty na Qt
Name:		qmmp
Version:	1.6.5
Release:	5
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://qmmp.ylsoftware.com/files/qmmp/1.6/%{name}-%{version}.tar.bz2
# Source0-md5:	15443877d70916f968fa798ab866bfd7
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
BuildRequires:	libmms-devel >= 0.4
BuildRequires:	libmodplug-devel >= 0.8.4
BuildRequires:	libogg-devel
BuildRequires:	libprojectM-devel >= 2.0.0
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libshout-devel
BuildRequires:	libsidplayfp-devel >= 1.0.3
BuildRequires:	libsndfile-devel >= 1.0.21
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxmp-devel >= 4.2.0
BuildRequires:	musepack-devel
BuildRequires:	opus-devel >= 1.0.2
BuildRequires:	opusfile-devel >= 0.2
BuildRequires:	pipewire-devel
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
Obsoletes:	qmmp-input-xmp < 1.6.0
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

%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/56x56

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.CC-by-sa_V4 ChangeLog ChangeLog.svn README
%lang(ru) %doc ChangeLog.rus README.RUS
%lang(uk) %doc README.UKR
%attr(755,root,root) %{_bindir}/qmmp-1
%dir %{_libdir}/qmmp-1.6
%dir %{_libdir}/qmmp-1.6/CommandLineOptions
%attr(755,root,root) %{_libdir}/qmmp-1.6/CommandLineOptions/lib*option.so
%dir %{_libdir}/qmmp-1.6/Effect
# R: libbs2b
%attr(755,root,root) %{_libdir}/qmmp-1.6/Effect/libbs2b.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Effect/libcrossfade.so
# R: libogg libvorbis
%attr(755,root,root) %{_libdir}/qmmp-1.6/Effect/libfilewriter.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Effect/libladspa.so
# R: soxr
%attr(755,root,root) %{_libdir}/qmmp-1.6/Effect/libsoxr.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Effect/libstereo.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Effect/libmonotostereo.so
%dir %{_libdir}/qmmp-1.6/Engines
%attr(755,root,root) %{_libdir}/qmmp-1.6/Engines/libmplayer.so
%dir %{_libdir}/qmmp-1.6/FileDialogs
%attr(755,root,root) %{_libdir}/qmmp-1.6/FileDialogs/lib*dialog.so
%dir %{_libdir}/qmmp-1.6/General
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/liblibrary.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/liblistenbrainz.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libsleepinhibitor.so
# R: taglib
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libconverter.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libcopypaste.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libcovermanager.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libfileops.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libgnomehotkey.so
# R: Qt5DBus
#%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libhal.so
# R: libX11
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libhotkey.so
# R: Qt5DBus
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libkdenotify.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/liblyrics.so
# R: Qt5DBus
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libmpris.so
# R: Q5X11Extras libX11
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libnotifier.so
# R: taglib
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/librgscan.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libscrobbler.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libstatusicon.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libstreambrowser.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libtrackchange.so
# R: Qt5DBus
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libudisks.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/General/libhistory.so
%dir %{_libdir}/qmmp-1.6/Input
# R: faad2 taglib
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libaac.so
# R: libarchive
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libarchive.so
# R: libcddb libcdio libcdio-paranoia
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libcdaudio.so
# R: enca-libs
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libcue.so
# R: ffmpeg-libs
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libffmpeg.so
# R: flac taglib
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libflac.so
# R: game-music-emu
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libgme.so
# R: libmpcdec taglib
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libmpc.so
# R: opus opusfile taglib
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libopus.so
# R: libsidplayfp
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libsid.so
# R: libsndfile
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libsndfile.so
# R: libvorbis taglib
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libvorbis.so
# R: wavpack
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libwavpack.so
# R: libxmp
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libxmp.so
# R: wildmidi
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libwildmidi.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Input/libmpeg.so
%dir %{_libdir}/qmmp-1.6/Output
# R: alsa-lib
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/libalsa.so
# R: jack-audio-connection-kit-libs soxr
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/libjack.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/libnull.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/liboss.so
# R: pipewire-devel
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/libpipewire.so
# R: pulseaudio-libs
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/libpulseaudio.so
# R: QtMultimedia
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/libqtmultimedia.so
# R: libogg libshout libvorbis soxr
%attr(755,root,root) %{_libdir}/qmmp-1.6/Output/libshout.so
%dir %{_libdir}/qmmp-1.6/PlayListFormats
%attr(755,root,root) %{_libdir}/qmmp-1.6/PlayListFormats/lib*playlistformat.so
%dir %{_libdir}/qmmp-1.6/Transports
# R: curl-libs enca-libs
%attr(755,root,root) %{_libdir}/qmmp-1.6/Transports/libhttp.so
# R: libmms
%attr(755,root,root) %{_libdir}/qmmp-1.6/Transports/libmms.so
%dir %{_libdir}/qmmp-1.6/Ui
%attr(755,root,root) %{_libdir}/qmmp-1.6/Ui/libqsui.so
# R: libX11
%attr(755,root,root) %{_libdir}/qmmp-1.6/Ui/libskinned.so
%dir %{_libdir}/qmmp-1.6/Visual
%attr(755,root,root) %{_libdir}/qmmp-1.6/Visual/libanalyzer.so
%attr(755,root,root) %{_libdir}/qmmp-1.6/Visual/libprojectm.so
%{_desktopdir}/qmmp-1.desktop
%{_desktopdir}/qmmp-dir-1.desktop
%{_desktopdir}/qmmp-enqueue-1.desktop
%dir %{_datadir}/qmmp-1
%dir %{_datadir}/qmmp-1/images
%{_datadir}/qmmp-1/images/*.png
%dir %{_datadir}/qmmp-1/scripts
%attr(755,root,root) %{_datadir}/qmmp-1/scripts/kwin.sh
%{_iconsdir}/hicolor/*x*/apps/qmmp-1.png
%{_iconsdir}/hicolor/scalable/apps/qmmp-1.svgz
%{_iconsdir}/hicolor/scalable/apps/qmmp-simple-1.svgz
%{_metainfodir}/qmmp-1.appdata.xml
%{_datadir}/solid/actions/qmmp-opencda-1.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqmmp-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmp-1.so.1
%attr(755,root,root) %{_libdir}/libqmmpui-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmpui-1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqmmp-1.so
%attr(755,root,root) %{_libdir}/libqmmpui-1.so
%{_includedir}/qmmp-1
%{_pkgconfigdir}/qmmp-1.pc
%{_pkgconfigdir}/qmmpui-1.pc
