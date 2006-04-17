Summary:	XTrap library
Summary(pl):	Biblioteka XTrap
Name:		xorg-lib-libXTrap
Version:	1.0.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/libXTrap-%{version}.tar.bz2
# Source0-md5:	1e2d966b5b2b89910e418bb0f78e10de
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-trapproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XTrap library.

%description -l pl
Biblioteka XTrap.

%package devel
Summary:	Header files for libXTrap library
Summary(pl):	Pliki nagłówkowe biblioteki libXTrap
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXt-devel
Requires:	xorg-proto-trapproto-devel

%description devel
XTrap library.

This package contains the header files needed to develop programs that
use libXTrap.

%description devel -l pl
Biblioteka XTrap.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXTrap.

%package static
Summary:	Static libXTrap library
Summary(pl):	Biblioteka statyczna libXTrap
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XTrap library.

This package contains the static libXTrap library.

%description static -l pl
Biblioteka XTrap.

Pakiet zawiera statyczną bibliotekę libXTrap.

%prep
%setup -q -n libXTrap-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXTrap.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXTrap.so
%{_libdir}/libXTrap.la
%{_pkgconfigdir}/xtrap.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXTrap.a
