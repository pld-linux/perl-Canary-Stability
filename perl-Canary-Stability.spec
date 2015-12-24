#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Canary
%define		pnam	Stability
%include	/usr/lib/rpm/macros.perl
Summary:	Canary::Stability - canary to check Perl compatibility for Schmorp's modules
Summary(pl.UTF-8):	Canary::Stability - kanarek do sprawdzania zgodności Perla z modułami Schmorpa
Name:		perl-Canary-Stability
Version:	2006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/Canary-Stability-2006.tar.gz
# Source0-md5:	570ffd5fd8a399b6ba392c8451c8f5ab
URL:		http://search.cpan.org/dist/Canary-Stability/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is used by Schmorp's modules during configuration stage to
test the installed Perl for compatibility with his modules.

It's not, at this stage, meant as a tool for other module authors,
although in principle nothing prevents them from subscribing to the
same ideas.

%description -l pl.UTF-8
Ten moduł jest używany przez moduły Schmorpa na etapie konfiguracji
do sprawdzenia zainstalowanej wersji Perla pod kątem zgodności z
modułami tego autora.

Na tym etapie nie jest przeznaczony dla modułów innych autorów, ale
zasadniczo nie ma przeszkód do korzystania z tych samych idei.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%dir %{perl_vendorlib}/Canary
%{perl_vendorlib}/Canary/Stability.pm
%{_mandir}/man3/Canary::Stability.3pm*
