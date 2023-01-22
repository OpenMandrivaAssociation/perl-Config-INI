%define upstream_name    Config-INI

Name:		perl-%{upstream_name}
Version:	0.029
Release:	1

Summary:	A subclassable .ini-file emitter

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Config::INI
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Mixin::Linewise::Readers)
BuildRequires:	perl(Mixin::Linewise::Writers)
BuildRequires:	perl(PerlIO::utf8_strict)
BuildRequires:	perl(Test::More)

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
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*
