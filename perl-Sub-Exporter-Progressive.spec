%define upstream_name Sub-Exporter-Progressive
%define upstream_version 0.001013

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Only use Sub::Exporter if you need it
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Sub::Exporter::Progressive
Source0:	http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.880.0
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
the Sub::Exporter manpage is an incredibly powerful module, but with that
power comes great responsibility, er- as well as some runtime penalties.
This module is a 'Sub::Exporter' wrapper that will let your users just use
the Exporter manpage if all they are doing is picking exports, but use
'Sub::Exporter' if your users try to use 'Sub::Exporter''s more advanced
features features, like renaming exports, if they try to use them.

Note that this module will export '@EXPORT' and '@EXPORT_OK' package
variables for 'Exporter' to work. Additionally, if your package uses
advanced 'Sub::Exporter' features like currying, this module will only ever
use 'Sub::Exporter', so you might as well use it directly.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
make test

%install
%make_install

%files
%doc Changes META.json META.yml README
%{perl_vendorlib}/*
%doc %{_mandir}/man3/*
