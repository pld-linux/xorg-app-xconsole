Summary:	xconsole application
Summary(pl):	Aplikacja xconsole
Name:		xorg-app-xconsole
Version:	1.0.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xconsole-%{version}.tar.bz2
# Source0-md5:	8678ddd23573022d68dcd883ae239be8
Source1:	xconsole.desktop
Source2:	xconsole.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xconsole application.

%description -l pl
Aplikacja xconsole.

%prep
%setup -q -n xconsole-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xconsole.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xconsole.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/X11/app-defaults/*
%{_desktopdir}/xconsole.desktop
%{_pixmapsdir}/xconsole.png
%{_mandir}/man1/*.1x*
