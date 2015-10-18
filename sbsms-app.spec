Summary:	Program for high quality time stretching and pitch scaling
Summary(pl.UTF-8):	Program do wysokiej jakości zmiany szybkości i wysokości dźwięku
Name:		sbsms-app
Version:	0.0.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sbsms/%{name}-%{version}.tar.gz
# Source0-md5:	37bea968c52ad775c9724687093f3fd5
Patch0:		%{name}-link.patch
URL:		http://sbsms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmad-devel >= 0.15.1
BuildRequires:	libsbsms2-devel >= 2.0.2
BuildRequires:	libsndfile-devel >= 1.0.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libsbsms2 >= 2.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sbsms is a tool for high quality time and pitch scale modification. It
uses octave subband sinusoidal modeling implemented in libsbsms.

%description -l pl.UTF-8
sbsms to narzędzie do wysokiej jakości modyfikowania szybkości i
wysokości dźwięku. Wykorzystuje modelowanie sinusoidalne
zaimplementowane w bibliotece libsbsms.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsbsmsx.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/sbsms
