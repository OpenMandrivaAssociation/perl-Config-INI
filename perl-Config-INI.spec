%define upstream_name    Config-INI
%define upstream_version 0.015

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A subclassable .ini-file emitter
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Mixin::Linewise::Readers)
BuildRequires: perl(Mixin::Linewise::Writers)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
