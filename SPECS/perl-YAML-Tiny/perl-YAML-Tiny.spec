# Got the intial spec from Fedora and modified it
Summary:        Read/Write YAML files with as little code as possible
Name:           perl-YAML-Tiny
Version:        1.70
Release:        1%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/YAML-Tiny/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/YAML-Tiny-%{version}.tar.gz
%define sha1 YAML-Tiny=ece384991fca135995223d9b4444a5ae325acd64
Vendor:		VMware, Inc.
Distribution:	Photon
BuildArch:      noarch
BuildRequires:  perl
Requires:	perl
%description
YAML::Tiny is a Perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and
memory overhead.

%prep
%setup -q -n YAML-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test

%files
%{perl_vendorlib}/YAML/
%{_mandir}/man3/YAML::Tiny.3*

%changelog
*   Wed Apr 05 2017 Robert Qi <qij@vmware.com> 1.70-1
-   Update version to 1.70
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.69-2
-	GA - Bump release of all rpms
*   Tue Feb 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.69-1
-   Upgraded to version 1.69
*	Fri Apr 3 2015 Divya Thaluru <dthaluru@vmware.com> 1.66-1
-	Initial version.