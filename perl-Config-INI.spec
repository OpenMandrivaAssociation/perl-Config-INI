
%define realname   Config-INI
%define version    0.014
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A subclassable .ini-file emitter
Source:     http://www.cpan.org/modules/by-module/Config/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Mixin::Linewise::Readers)
BuildRequires: perl(Mixin::Linewise::Writers)

BuildArch: noarch

%description
Config::INI::Reader is _yet another_ config module implementing _yet
another_ slightly different take on the undeniably easy to read the ".ini"
file format|Config::INI manpage. Its default behavior is quite similar to
that of the Config::Tiny manpage, on which it is based.

The chief difference is that Config::INI::Reader is designed to be
subclassed to allow for side-effects and self-reconfiguration to occur
during the course of reading its input.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


