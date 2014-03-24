%define upstream_name    Config-INI
%define upstream_version 0.023

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A subclassable .ini-file emitter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Mixin::Linewise::Readers)
BuildRequires:	perl(Mixin::Linewise::Writers)

BuildArch:	noarch

%description
Config::INI::Reader is _yet another_ config module implementing _yet
another_ slightly different take on the undeniably easy to read the ".ini"
file format|Config::INI manpage. Its default behavior is quite similar to
that of the Config::Tiny manpage, on which it is based.

The chief difference is that Config::INI::Reader is designed to be
subclassed to allow for side-effects and self-reconfiguration to occur
during the course of reading its input.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.18.0-1mdv2011.0
+ Revision: 684739
- update to new version 0.018

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.17.0-3
+ Revision: 657770
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Tue Dec 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.0-1mdv2011.0
+ Revision: 621740
- update to new version 0.017

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.16.0-1mdv2011.0
+ Revision: 576293
- update to 0.016

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.15.0-1mdv2011.0
+ Revision: 572698
- update to 0.015

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.014-2mdv2011.0
+ Revision: 375962
- rebuild

* Wed Mar 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.014-1mdv2009.1
+ Revision: 360993
- import perl-Config-INI


* Tue Mar 24 2009 cpan2dist 0.014-1mdv
- initial mdv release, generated with cpan2dist





