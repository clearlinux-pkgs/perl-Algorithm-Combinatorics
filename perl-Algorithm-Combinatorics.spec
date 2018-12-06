#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Combinatorics
Version  : 0.27
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/F/FX/FXN/Algorithm-Combinatorics-0.27.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FX/FXN/Algorithm-Combinatorics-0.27.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libalgorithm-combinatorics-perl/libalgorithm-combinatorics-perl_0.27-2.debian.tar.xz
Summary  : Efficient generation of combinatorial sequences
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Algorithm-Combinatorics-lib = %{version}-%{release}
Requires: perl-Algorithm-Combinatorics-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Algorithm::Combinatorics - Efficient generation of combinatorial
sequences
SYNOPSIS
use Algorithm::Combinatorics qw(permutations);

%package dev
Summary: dev components for the perl-Algorithm-Combinatorics package.
Group: Development
Requires: perl-Algorithm-Combinatorics-lib = %{version}-%{release}
Provides: perl-Algorithm-Combinatorics-devel = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-Combinatorics package.


%package lib
Summary: lib components for the perl-Algorithm-Combinatorics package.
Group: Libraries
Requires: perl-Algorithm-Combinatorics-license = %{version}-%{release}

%description lib
lib components for the perl-Algorithm-Combinatorics package.


%package license
Summary: license components for the perl-Algorithm-Combinatorics package.
Group: Default

%description license
license components for the perl-Algorithm-Combinatorics package.


%prep
%setup -q -n Algorithm-Combinatorics-0.27
cd ..
%setup -q -T -D -n Algorithm-Combinatorics-0.27 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Algorithm-Combinatorics-0.27/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Algorithm-Combinatorics
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Algorithm-Combinatorics/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Algorithm/Combinatorics.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::Combinatorics.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Algorithm/Combinatorics/Combinatorics.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Algorithm-Combinatorics/deblicense_copyright
