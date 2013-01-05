Summary:	libXTrap library - client API for the DEC-XTRAP extension
Summary(pl.UTF-8):	Biblioteka libXTrap - API klienckie rozszerzenia DEC-XTRAP
Name:		xorg-lib-libXTrap
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXTrap-%{version}.tar.bz2
# Source0-md5:	076ff6279d202f19421b51af4f723935
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-trapproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libXTrap library is the Xlib-based client API for the DEC-XTRAP
extension.

XTrap was a proposed standard extension for X11R5 which facilitated
the capturing of server protocol and synthesizing core input events.

Digital participated in the X Consortium's xtest working group which
chose to evolve XTrap functionality into the XTEST & RECORD extensions
for X11R6.

As X11R6 was released in 1994, XTrap has now been deprecated for over 15
years, and uses of it should be quite rare.

%description -l pl.UTF-8
Biblioteka libXTrap to oparte na bibliotece Xlib API klienckie dla
rozszerzenia DEC-XTRAP.

XTrap było proponowanym standardowym rozszerzeniem dla X11R5,
ułatwiającym przechwytywanie protokołu serwera i sztuczne tworzenie
zdarzeń wejściowych.

Digital brał udział w grupie roboczej X Consortium xtest, która
zdecydowała o ewolucji funkcjonalności XTrap w rozszerzenia XTEST oraz
RECORD dla X11R6.

Jako że X11R6 zostało wydane w 1994, XTrap jest przestarzałe od ponad 15
lat i jego użycie powinno być raczej rzadkie.

%package devel
Summary:	Development files for libXTrap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXTrap
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXt-devel
Requires:	xorg-proto-trapproto-devel

%description devel
This package contains the development files needed to compile programs
that use libXTrap.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne niezbędne do kompilowania
programów używających biblioteki libXTrap.

%package static
Summary:	Static libXTrap library
Summary(pl.UTF-8):	Biblioteka statyczna libXTrap
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libXTrap library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę libXTrap.

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXTrap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXTrap.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXTrap.so
%{_libdir}/libXTrap.la
%{_pkgconfigdir}/xtrap.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXTrap.a
