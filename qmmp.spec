# TODO: Output/oss4 plugin (R: soundcard.h from OSS 4)
Summary:	XMMS like audio player based on Qt
Summary(hu.UTF-8):	XMMS-szerű Qt alapú audio-lejátszó
Summary(pl.UTF-8):	Odtwarzacz muzyki w stylu XMMS oparty na Qt
Name:		qmmp
Version:	0.10.8
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	5504999a4a0ee477367871ff181be4d6
URL:		http://qmmp.ylsoftware.com/
BuildRequires:	Qt3Support-devel >= 4.6
BuildRequires:	QtCore-devel >= 4.6
BuildRequires:	QtDBus-devel >= 4.6
BuildRequires:	QtGui-devel >= 4.6
BuildRequires:	QtMultimedia-devel >= 4.6
BuildRequires:	QtNetwork-devel >= 4.6
BuildRequires:	QtOpenGL-devel >= 4.6
BuildRequires:	alsa-lib-devel >= 1.0.1
BuildRequires:	cmake >= 2.8.6
BuildRequires:	curl-devel >= 7.16
BuildRequires:	enca-devel >= 1.9
BuildRequires:	faad2-devel >= 2.6.1
# libavcodec>=53.34.0 libavformat>=53.20.0 libavutil>=51.21.0
BuildRequires:	ffmpeg-devel >= 0.9.1
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	game-music-emu-devel >= 0.5.5
BuildRequires:	gettext-tools
BuildRequires:	jack-audio-connection-kit-devel >= 0.102.5
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
BuildRequires:	libsidplayfp-devel >= 1.0.3
BuildRequires:	libsndfile-devel >= 1.0.17
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	opus-devel >= 1.0.2
BuildRequires:	opusfile-devel >= 0.2
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.15
BuildRequires:	qt4-build >= 4.6.0
BuildRequires:	qt4-linguist >= 4.6.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	soxr-devel >= 0.1.0
BuildRequires:	taglib-devel >= 1.6
BuildRequires:	wavpack-devel >= 4.41
BuildRequires:	wildmidi-devel >= 0.2.3.4
BuildRequires:	xorg-lib-libX11-devel
Requires:	Qt3Support >= 4.6
Requires:	QtCore >= 4.6
Requires:	QtDBus >= 4.6
Requires:	QtGui >= 4.6
Requires:	QtMultimedia >= 4.6
Requires:	QtNetwork >= 4.6
Requires:	QtOpenGL >= 4.6
Requires:	curl-libs >= 7.16
Requires:	enca-libs >= 1.9
Requires:	faad2-libs >= 2.6.1
Requires:	ffmpeg-libs >= 0.9.1
Requires:	flac >= 1.1.3
Requires:	game-music-emu >= 0.5.5
Requires:	jack-audio-connection-kit-libs >= 0.102.5
Requires:	libbs2b >= 3.0.0
Requires:	libcddb >= 1.3.1
Requires:	libcdio >= 0.80
Requires:	libcdio-paranoia >= 0.90_10.2
Requires:	libmms >= 0.4
Requires:	libmodplug >= 0.8.4
Requires:	libmpcdec >= 1.2.6
Requires:	libprojectM >= 2.0.0
Requires:	libsidplayfp >= 1.0.3
Requires:	libsndfile >= 1.0.17
Requires:	opus >= 1.0.2
Requires:	opusfile >= 0.2
Requires:	pulseaudio-libs >= 0.9.15
Requires:	soxr >= 0.1.0
Requires:	taglib >= 1.6
Requires:	wavpack >= 4.41
Requires:	wildmidi >= 0.2.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio player that supports:
- file formats among: Vorbis, FLAC, MPEG1, WMA, WAV...
- plugins,
- Winamp and XMMS skins and more.

%description -l hu.UTF-8
A lejátszó a következőket támogatja:
- fájlformátumok: Vorbis, FLAC, MPEG1, WMA, WAV
- pluginok
- Wnamp és XMMS szkinek és még sok mást.

%description -l pl.UTF-8
Odtwarzacz audio obsługujący m.in.:
- formaty plikow m.in.: Vorbis, FLAC, MPEG1, WMA, WAV i inne,
- system wtyczek,
- skórki z XMMS i Winampa.

%package devel
Summary:	Header files for qmmp
Summary(pl.UTF-8):	Pliki nagłówkowe qmmp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.6
Requires:	QtGui-devel >= 4.6
Requires:	QtNetwork-devel >= 4.6

%description devel
Header files for qmmp.

%description devel -l pl.UTF-8
Pliki nagłówkowe qmmp.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.CC-by-sa_V4 ChangeLog ChangeLog.svn README
%lang(ru) %doc ChangeLog.rus README.RUS
%lang(uk) %doc README.UKR
%attr(755,root,root) %{_bindir}/qmmp
%attr(755,root,root) %{_libdir}/libqmmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmp.so.0
%attr(755,root,root) %{_libdir}/libqmmpui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmpui.so.0
%dir %{_libdir}/qmmp/CommandLineOptions
%attr(755,root,root) %{_libdir}/qmmp/CommandLineOptions/lib*option.so
%dir %{_libdir}/qmmp/Effect
# R: libbs2b
%attr(755,root,root) %{_libdir}/qmmp/Effect/libbs2b.so
%attr(755,root,root) %{_libdir}/qmmp/Effect/libcrossfade.so
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
# R: QtDBus
%attr(755,root,root) %{_libdir}/qmmp/General/libhal.so
# R: libX11
%attr(755,root,root) %{_libdir}/qmmp/General/libhotkey.so
# R: QtDBus
%attr(755,root,root) %{_libdir}/qmmp/General/libkdenotify.so
%attr(755,root,root) %{_libdir}/qmmp/General/liblyrics.so
# R: QtDBus
%attr(755,root,root) %{_libdir}/qmmp/General/libmpris.so
%attr(755,root,root) %{_libdir}/qmmp/General/libnotifier.so
# R: taglib
%attr(755,root,root) %{_libdir}/qmmp/General/librgscan.so
%attr(755,root,root) %{_libdir}/qmmp/General/libscrobbler.so
%attr(755,root,root) %{_libdir}/qmmp/General/libstatusicon.so
%attr(755,root,root) %{_libdir}/qmmp/General/libstreambrowser.so
%attr(755,root,root) %{_libdir}/qmmp/General/libtrackchange.so
# R: QtDBus
%attr(755,root,root) %{_libdir}/qmmp/General/libudisks2.so
%dir %{_libdir}/qmmp/Input
# R: faad2 taglib
%attr(755,root,root) %{_libdir}/qmmp/Input/libaac.so
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
# R: pulseaudio-libs
%attr(755,root,root) %{_libdir}/qmmp/Output/libpulseaudio.so
# R: QtMultimedia
%attr(755,root,root) %{_libdir}/qmmp/Output/libqtmultimedia.so
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqmmp.so
%attr(755,root,root) %{_libdir}/libqmmpui.so
%{_includedir}/qmmp
%{_includedir}/qmmpui
%{_pkgconfigdir}/qmmp.pc
%{_pkgconfigdir}/qmmpui.pc
