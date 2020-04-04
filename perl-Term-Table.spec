%{?scl:%scl_package perl-Term-Table}

%if ! (0%{?scl:1})
# Recognize terminal size
%bcond_without perl_Term_Table_enables_terminal
# Respect Unicode rules when breaking lines
%bcond_without perl_Term_Table_enables_unicode
%else
%bcond_with perl_Term_Table_enables_terminal
%bcond_with perl_Term_Table_enables_unicode
%endif

Name:           %{?scl_prefix}perl-Term-Table
Version:        0.015
Release:        3%{?dist}
Summary:        Format a header and rows into a table
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Term-Table
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Term-Table-%{version}.tar.gz
# Unbundle Object::HashBase
Patch0:         Term-Table-0.015-Use-system-Object-HashBase.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(:VERSION) >= 5.8.1
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Importer) >= 0.024
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(Object::HashBase) >= 0.008
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# Optional run-time:
%if %{with perl_Term_Table_enables_terminal}
# Term::ReadKey 2.32 not used if Term::Size::Any is available
# Prefer Term::Size::Any over Term::ReadKey
BuildRequires:  %{?scl_prefix}perl(Term::Size::Any) >= 0.002
%endif
%if %{with perl_Term_Table_enables_unicode}
BuildRequires:  %{?scl_prefix}perl(Unicode::GCString) >= 2013.10
%endif
# Tests:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Test2::API)
BuildRequires:  %{?scl_prefix}perl(Test2::Tools::Tiny) >= 1.302097
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(utf8)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Importer) >= 0.024
%if %{with perl_Term_Table_enables_terminal}
Requires:       %{?scl_prefix}perl(Term::ReadKey) >= 2.32
# Prefer Term::Size::Any over Term::ReadKey
Requires:       %{?scl_prefix}perl(Term::Size::Any) >= 0.002
%endif
%if %{with perl_Term_Table_enables_unicode}
Requires:       %{?scl_prefix}perl(Unicode::GCString) >= 2013.10
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^%{?scl_prefix}perl\\(Importer\\)$

%description
This Perl module is able to format rows of data into tables.

%prep
%setup -q -n Term-Table-%{version}
%patch0 -p1
# Delete bundled Object::HashBase
for F in lib/Term/Table/HashBase.pm t/HashBase.t; do
    rm "$F"
    sed -i -e '\|^'"$F"'|d' MANIFEST
done

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TABLE_TERM_SIZE
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jan 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-3
- SCL

* Thu Nov 21 2019 Petr Pisar <ppisar@redhat.com> - 0.015-2
- Unbundle Object::HashBase

* Tue Nov 19 2019 Petr Pisar <ppisar@redhat.com> - 0.015-1
- 0.015 bump

* Wed Oct 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-1
- 0.014 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Petr Pisar <ppisar@redhat.com> - 0.013-1
- 0.013 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.012-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.012-1
- 0.012 bump

* Wed Oct 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-1
- 0.011 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-2
- Perl 5.26 rebuild

* Mon Mar 20 2017 Petr Pisar <ppisar@redhat.com> - 0.008-1
- 0.008 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Petr Pisar <ppisar@redhat.com> - 0.006-1
- 0.006 bump

* Mon Jan 02 2017 Petr Pisar <ppisar@redhat.com> - 0.005-1
- 0.005 bump

* Wed Dec 21 2016 Petr Pisar <ppisar@redhat.com> - 0.004-1
- 0.004 bump

* Tue Dec 20 2016 Petr Pisar <ppisar@redhat.com> 0.002-1
- Specfile autogenerated by cpanspec 1.78.
