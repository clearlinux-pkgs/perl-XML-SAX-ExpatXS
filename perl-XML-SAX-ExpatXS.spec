#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-XML-SAX-ExpatXS
Version  : 1.33
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/P/PC/PCIMPRICH/XML-SAX-ExpatXS-1.33.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PC/PCIMPRICH/XML-SAX-ExpatXS-1.33.tar.gz
Summary  : Perl SAX 2 XS extension to Expat parser
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-XML-SAX-ExpatXS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : expat-dev
BuildRequires : perl(XML::SAX)
BuildRequires : perl(XML::SAX::Base)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
================================================
1. Introduction
2. Dependencies
3. Installation
4. Callbacks
5. Encoding

%package dev
Summary: dev components for the perl-XML-SAX-ExpatXS package.
Group: Development
Provides: perl-XML-SAX-ExpatXS-devel = %{version}-%{release}
Requires: perl-XML-SAX-ExpatXS = %{version}-%{release}

%description dev
dev components for the perl-XML-SAX-ExpatXS package.


%package perl
Summary: perl components for the perl-XML-SAX-ExpatXS package.
Group: Default
Requires: perl-XML-SAX-ExpatXS = %{version}-%{release}

%description perl
perl components for the perl-XML-SAX-ExpatXS package.


%prep
%setup -q -n XML-SAX-ExpatXS-1.33
cd %{_builddir}/XML-SAX-ExpatXS-1.33

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
/usr/share/man/man3/XML::SAX::ExpatXS.3
/usr/share/man/man3/XML::SAX::ExpatXS::Encoding.3
/usr/share/man/man3/XML::SAX::ExpatXS::Preload.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
