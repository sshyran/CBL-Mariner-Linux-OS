Vendor:         Microsoft Corporation
Distribution:   Mariner
Summary: Capture sosreports from multiple nodes simultaneously
Name: sos-collector
Version: 1.8
Release: 3%{?dist}
Source0: http://people.redhat.com/jhunsake/sos-collector/%{name}-%{version}.tar.gz
License: GPLv2
BuildArch: noarch
Url: https://github.com/sosreport/sos-collector
Requires: sos >= 3.0
Obsoletes: clustersos < 1.2.2-2
Provides: clustersos = %{version}-%{release}


%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: python-devel
BuildRequires: python-pexpect
Requires: python-futures
Requires: python-six
Requires: python-pexpect
%else
BuildRequires: python3-devel
BuildRequires: python3-pexpect
BuildRequires: python3-six
Requires: python3-six
Requires: python3-pexpect
%endif


%description
sos-collector is a utility designed to capture sosreports from multiple nodes
at once and collect them into a single archive. If the nodes are part of
a cluster, profiles can be used to configure how the sosreport command
is run on the nodes.

%prep
%setup -q

%build
%if 0%{?rhel} && 0%{?rhel} <= 7
%py2_build
%else
%py3_build
%endif

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m644 man/en/sos-collector.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
%if 0%{?rhel} && 0%{?rhel} <= 7
%py2_install
%else
%py3_install
%endif



%check
%if 0%{?rhel} && 0%{?rhel} <= 7
%{__python2} setup.py test
%else
%{__python3} setup.py test
%endif

%files
%{_bindir}/sos-collector
%if 0%{?rhel} && 0%{?rhel} <= 7
%{python2_sitelib}/*
%else
%{python3_sitelib}/*
%endif
%{_mandir}/man1/*

%license LICENSE

%changelog
* Fri Oct 15 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.8-3
- Initial CBL-Mariner import from Fedora 32 (license: MIT).

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.8-1
- New upstream release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-2
- Fix 'none' cluster type enablement

* Mon Apr 01 2019 Jake Hunsaker <jhunsake@redhat.com> - 1.7-1
- New upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.6-2
- Local execution to use pexpect as well

* Sat Dec 15 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.6-1
- New upstream release
- Drop paramiko dependency, now use OpenSSH ControlPersist 

* Tue Oct 16 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-3
- Pull in fixes for non-root local execution and bytes conversion

* Thu Oct 11 2018 Jake Hunsaker <jhunsake@redhat.com> - 1.5-1
- New upstream release
- Resolves CVE-2018-14650

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Jake Hunsaker <jhunsake@redhat.com> 1.4-2
- New Upstream release

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.7

* Thu May 24 2018 Jake Hunsaker <jhunsake@redhat.com> 1.3-3
- Fix sos-collector archive organization
- Fix cluster option validation

* Mon May 07 2018 Jake Hunsaker <jhunsake@redhat.com> 1.3-2
- Fix collection of sosreport tarballs

* Fri Apr 27 2018 Jake Hunsaker <jhunsake@redhat.com> 1.3-1
- Reset versioning to continue from clustersos

* Thu Apr 26 2018 Jake Hunsaker <jhunsake@redhat.com> 1.0-1
- Renamed project to sos-collector
- Moved github repo to sosreport org
