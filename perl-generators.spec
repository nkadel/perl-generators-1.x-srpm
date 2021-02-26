Name:           perl-generators
Version:        1.08
#Release:        7%%{?dist}
Release:        0.7%{?dist}
Summary:        RPM Perl dependencies generators
Group:          Development/Libraries
License:        GPL+
URL:            http://jplesnik.fedorapeople.org/generators/
BuildArch:      noarch
Requires:       perl-macros
Requires:       rpm-build

%description
This package provides RPM Perl dependencies generators which are used for
getting provides and requires from Perl binaries and modules.

This is a dummy package for compatibility with Fedora source packages. The
Perl dependenciss generators are provided by rpm-build package. See
<https://fedoraproject.org/wiki/Changes/Build_Root_Without_Perl> and
<https://fedoraproject.org/wiki/Packaging:Perl#Build_Dependencies>.

%prep

%build

%install

%check

%files

%changelog
* Mon Jan 07 2019 Petr Pisar <ppisar@redhat.com> - 1.08-7
- Remove perl-interpreter package (bug #1663304)

* Mon Aug 28 2017 Petr Pisar <ppisar@redhat.com> - 1.08-6
- Add epoch to perl-interpreter version.

* Mon Aug 28 2017 Petr Pisar <ppisar@redhat.com> - 1.08-5
- Provide perl-interpreter (bug #1410347)

* Wed Jun 22 2016 Petr Pisar <ppisar@redhat.com> - 1.08-4
- Provide this dummy package to ease porting Fedora packages to EPEL

