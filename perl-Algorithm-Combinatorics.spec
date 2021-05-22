#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Combinatorics
Version  : 0.27
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/F/FX/FXN/Algorithm-Combinatorics-0.27.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FX/FXN/Algorithm-Combinatorics-0.27.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libalgorithm-combinatorics-perl/libalgorithm-combinatorics-perl_0.27-2.debian.tar.xz
Summary  : Efficient generation of combinatorial sequences
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Algorithm-Combinatorics-license = %{version}-%{release}
Requires: perl-Algorithm-Combinatorics-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::More)

%description
NAME
Algorithm::Combinatorics - Efficient generation of combinatorial
sequences
SYNOPSIS
use Algorithm::Combinatorics qw(permutations);

%package dev
Summary: dev components for the perl-Algorithm-Combinatorics package.
Group: Development
Provides: perl-Algorithm-Combinatorics-devel = %{version}-%{release}
Requires: perl-Algorithm-Combinatorics = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-Combinatorics package.


%package license
Summary: license components for the perl-Algorithm-Combinatorics package.
Group: Default

%description license
license components for the perl-Algorithm-Combinatorics package.


%package perl
Summary: perl components for the perl-Algorithm-Combinatorics package.
Group: Default
Requires: perl-Algorithm-Combinatorics = %{version}-%{release}

%description perl
perl components for the perl-Algorithm-Combinatorics package.


%prep
%setup -q -n Algorithm-Combinatorics-0.27
cd %{_builddir}
tar xf %{_sourcedir}/libalgorithm-combinatorics-perl_0.27-2.debian.tar.xz
cd %{_builddir}/Algorithm-Combinatorics-0.27
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Algorithm-Combinatorics-0.27/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Algorithm-Combinatorics
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Algorithm-Combinatorics/4ac3f33934bfa4f4c6997eb59ab63df03f2296b9
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::Combinatorics.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Algorithm-Combinatorics/4ac3f33934bfa4f4c6997eb59ab63df03f2296b9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Algorithm/Combinatorics.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Algorithm/Combinatorics/Combinatorics.so
