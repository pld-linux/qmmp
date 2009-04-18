Summary:	XMMS like audio player written in Qt
Summary(pl.UTF-8):	Odtwarzacz muzyki w stylu XMMS napisany w Qt
Name:		qmmp
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://qmmp.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	8b25c607e345fba27829f7ea41ae37ba
URL:		http://code.google.com/p/qmmp/
BuildRequires:	QtCore-devel >= 4.3
BuildRequires:	QtGui-devel >= 4.3
BuildRequires:	alsa-lib-devel >= 1.0.1
BuildRequires:	cmake
BuildRequires:	curl >= 7.16
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	gettext-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.102.5
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel >= 0.8.4
BuildRequires:	libmpcdec-devel >= 1.2.6
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libsndfile-devel >= 1.0.17
BuildRequires:	libvorbis-devel
BuildRequires:	pulseaudio-devel >= 0.9.9
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	taglib-devel >= 1.4.0
BuildRequires:	wavpack-devel >= 4.41
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio player that supports:
- file formats among: Vorbis, FLAC, MPEG1, WMA, WAV,
- plugins,
- Winamp and XMMS skins and more.

%description -l pl.UTF-8
Odtwarzacz audio wspierający:
- formaty plikow m.in.: Vorbis, Flac, MPEG1, WMA, WAW, i inne,
- system wtyczek,
- skórki z XMMS i Winampa, i więcej.

%package devel
Summary:	Header files for qmmp
Summary(pl.UTF-8):	Pliki nagłówkowe qmmp
License:	GPL v2.1+
Group:		Development/Libraries

%description devel
Header files for qmmp

%description -l pl.UTF-8
Pliki nagłówkowe qmmp


%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir} \
        kde_libs_htmldir=%{_kdedocdir}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libqmmp.so.0.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmp.so.0
%attr(755,root,root) %{_libdir}/libqmmpui.so.0.*.*
%attr(755,root,root) %ghost %{_libdir}/libqmmpui.so.0
%attr(755,root,root) %{_libdir}/qmmp/
%{_desktopdir}/qmmp.desktop
%{_iconsdir}/hicolor/*/apps/qmmp.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/qmmp
%{_includedir}/qmmpui
%attr(755,root,root) %{_libdir}/libqmmp.so
%attr(755,root,root) %{_libdir}/libqmmpui.so