# $Rev: 3272 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	XTrap library
Summary(pl):	libXTrap
Name:		xorg-lib-libXTrap
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXTrap-%{version}.tar.bz2
# Source0-md5:	f71d0ee1dd5a3fe5bc656b8ea06a70c9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto-trapproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXTrap-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XTrap library.

%description -l pl
Biblioteka XTrap.


%package devel
Summary:	Header files libXTrap development
Summary(pl):	Pliki nag��wkowe do biblioteki libXTrap
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXTrap = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXt-devel
Requires:	xorg-proto-trapproto-devel

%description devel
XTrap library.

This package contains the header files needed to develop programs that
use these libXTrap.

%description devel -l pl
Biblioteka XTrap.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libXTrap.


%package static
Summary:	Static libXTrap libraries
Summary(pl):	Biblioteki statyczne libXTrap
Group:		Development/Libraries
Requires:	xorg-lib-libXTrap-devel = %{version}-%{release}

%description static
XTrap library.

This package contains the static libXTrap library.

%description static -l pl
Biblioteka XTrap.

Pakiet zawiera statyczn� bibliotek� libXTrap.


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
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libXTrap.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXTrap.la
%attr(755,root,wheel) %{_libdir}/libXTrap.so
%{_pkgconfigdir}/xtrap.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXTrap.a