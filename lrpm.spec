Name:       lrpm
Summary:    Log wrapper for rpm
Version:    0.1.1
Release:    1%{org_tag}
Group:      Applications/System
License:    GPL
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
BuildArch:  noarch
BuildRequires: /usr/bin/pod2man

%description
lrpm is a simple rpm wrapper that logs successful rpm transactions to 
/var/log/yum.log.

%prep
%setup

%build
pod2man %{name} > %{name}.1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install %{name} $RPM_BUILD_ROOT%{_bindir}
install -m0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%changelog

* Mon Feb 22 2010 Gavin Carr <gavin@openfusion.com.au> 0.1.1-1
- Fix buglet with timestamp format.

* Mon Feb 22 2010 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial spec file

