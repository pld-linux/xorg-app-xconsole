Summary:	xconsole application to monitor system console messages with X
Summary(pl.UTF-8):	Aplikacja xconsole do monitorowania komunikatów konsoli systemowej pod X
Name:		xorg-app-xconsole
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xconsole-%{version}.tar.bz2
# Source0-md5:	0e1a3110bebabecc2897d67a973526b0
Source1:	xconsole.desktop
Source2:	xconsole.png
Source3:	xconsole.1x.it
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
The xconsole program displays messages which are usually sent to
/dev/console.

%description -l pl.UTF-8
Program xconsole wyświetla komunikaty, które zwykle są wysyłane na
/dev/console.

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
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/it/man1/xconsole.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xconsole
%{_datadir}/X11/app-defaults/XConsole
%{_desktopdir}/xconsole.desktop
%{_pixmapsdir}/xconsole.png
%{_mandir}/man1/xconsole.1x*
%lang(it) %{_mandir}/it/man1/xconsole.1x*
