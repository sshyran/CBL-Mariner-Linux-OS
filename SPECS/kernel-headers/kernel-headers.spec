Summary:        Linux API header files
Name:           kernel-headers
Version:        5.10.146.1
Release:        1%{?dist}
License:        GPLv2
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/Kernel
URL:            https://github.com/microsoft/CBL-Mariner-Linux-Kernel
#Source0:       https://github.com/microsoft/CBL-Mariner-Linux-Kernel/archive/rolling-lts/mariner/%%{version}.tar.gz
Source0:        kernel-%{version}.tar.gz
Patch0:         0001-clocksource-drivers-hyper-v-Re-enable-VDSO_CLOCKMODE.patch
BuildArch:      noarch

%description
The Linux API Headers expose the kernel's API for use by Glibc.

%prep
%setup -q -n CBL-Mariner-Linux-Kernel-rolling-lts-mariner-%{version}
%patch0 -p1

%build
make mrproper

%install
cd %{_builddir}/CBL-Mariner-Linux-Kernel-rolling-lts-mariner-%{version}
make headers
find usr/include -name '.*' -delete
rm usr/include/Makefile
mkdir -p /%{buildroot}%{_includedir}
cp -rv usr/include/* /%{buildroot}%{_includedir}

%files
%defattr(-,root,root)
%license COPYING
%{_includedir}/*

%changelog
* Thu Oct 06 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.10.146.1-1
- Upgrade to 5.10.146.1

* Tue Sep 27 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.10.145.1-1
- Upgrade to 5.10.145.1

* Thu Sep 22 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.10.144.1-1
- Upgrade to 5.10.144.1

* Wed Sep 14 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.10.142.1-1
- Upgrade to 5.10.142.1

* Thu Sep 08 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.10.139.1-1
- Upgrade to 5.10.139.1

* Thu Sep 01 2022 Chris Co <chrco@microsoft.com> - 5.10.134.1-2
- Bump release number to match kernel release

* Tue Aug 23 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.10.134.1-1
- Upgrade to 5.10.134.1

* Wed Aug 17 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.133.1-1
- Update source to 5.10.133.1

* Sun Jul 24 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.131.1-1
- Update source to 5.10.131.1

* Wed Jul 06 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.10.128.1-1
- Update source to 5.10.128.1

* Mon Jun 20 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.123.1-1
- Update source to 5.10.123.1
- Remove make headers_check

* Wed Jun 01 2022 Minghe Ren <mingheren@microsoft.com> - 5.10.117.1-2
- Bump release number to match kernel release

* Tue May 24 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.10.117.1-1
- Update source to 5.10.117.1

* Tue May 17 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.116.1-1
- Update source to 5.10.116.1

* Tue Apr 19 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.111.1-1
- Update source to 5.10.111.1

* Fri Apr 01 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.109.1-2
- Bump release number to match kernel release

* Tue Mar 29 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.10.109.1-1
- Update source to 5.10.109.1
- Remove CVE-2022-24958.patch and CVE-2022-1016.patch

* Fri Mar 25 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.102.1-3
- Apply CVE-2022-1016.patch

* Fri Mar 18 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.102.1-2
- Bump release number to match kernel release

* Mon Feb 28 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.102.1-1
- Update source to 5.10.102.1
- Apply CVE-2022-24958.patch
- Remove CVE-2021-43976.patch and CVE-2022-0435.patch

* Fri Feb 11 2022 Vince Perri <viperri@microsoft.com> - 5.10.93.1-4
- Bump release number to match kernel release

* Wed Feb 09 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.93.1-3
- Address CVE-2022-0435 with patch
  
* Thu Jan 27 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.93.1-2
- Bump release number to match kernel release

* Mon Jan 24 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.93.1-1
- Update source to 5.10.93.1

* Thu Jan 20 2022 Chris Co <chrco@microsoft.com> - 5.10.89.1-2
- Bump release number to match kernel release

* Sun Jan 16 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.89.1-1
- Update source to 5.10.89.1
- Remove patch add-linux-syscall-license-info.patch

* Fri Jan 14 2022 Henry Li <lihl@microsoft.com> - 5.10.88.1-3
- Bump release number to match kernel release

* Wed Jan 12 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.10.88.1-2
- Bump release number to match kernel release

* Mon Jan 03 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.10.88.1-1
- Update Kernel source to 5.10.88.1
- Apply patch to address CVE-2021-43976

* Mon Nov 29 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.78.1-2
- Update to kernel release 5.10.78.1-2

* Mon Nov 08 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.78.1-1
- Update source to 5.10.78.1
- Add patch to fix SPDX-License-Identifier in headers

* Tue Oct 26 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.74.1-2
- Bump release number to match kernel release

* Tue Oct 19 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.74.1-1
- Update source to 5.10.74.1
- License verified

* Thu Oct 07 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.69.1-1
- Update source to 5.10.69.1

* Wed Sep 22 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-3
- Bump release number to match kernel release

* Tue Sep 21 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-2
- Bump release number to match kernel release

* Mon Sep 20 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-1
- Update source to 5.10.64.1

* Mon Sep 13 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.60.1-2
- Bump release number to match kernel release

* Mon Aug 23 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.60.1-1
- Update source to 5.10.60.1
- Remove patch for CDROM eject errors

* Thu Aug 12 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.57.1-1
- Update source to 5.10.57.1

* Tue Aug 03 2021 Chris Co <chrco@microsoft.com> - 5.10.52.1-3
- Add patch to fix VDSO in HyperV

* Fri Jul 30 2021 Chris Co <chrco@microsoft.com> - 5.10.52.1-2
- Add patch to fix CDROM eject errors

* Tue Jul 20 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.52.1-1
- Update source to 5.10.52.1

* Mon Jul 19 2021 Chris Co <chrco@microsoft.com> - 5.10.47.1-2
- Bump release number to match kernel release

* Tue Jul 06 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.47.1-1
- Update source to 5.10.47.1

* Wed Jun 30 2021 Chris Co <chrco@microsoft.com> - 5.10.42.1-4
- Bump release number to match kernel release

* Tue Jun 22 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.42.1-3
- Bump release number to match kernel release

* Wed Jun 16 2021 Chris Co <chrco@microsoft.com> - 5.10.42.1-2
- Bump release number to match kernel release

* Tue Jun 08 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.42.1-1
- Update source to 5.10.42.1

* Thu Jun 03 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.37.1-2
- Bump release number to match kernel release

* Fri May 28 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.37.1-1
- Update source to 5.10.37.1

* Thu May 27 2021 Chris Co <chrco@microsoft.com> - 5.10.32.1-7
- Bump release number to match kernel release

* Wed May 26 2021 Chris Co <chrco@microsoft.com> - 5.10.32.1-6
- Bump release number to match kernel release

* Tue May 25 2021 Daniel Mihai <dmihai@microsoft.com> - 5.10.32.1-5
- Bump release number to match kernel release

* Thu May 20 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.10.32.1-4
- Bump release number to match kernel-signed update

* Tue May 18 2021 Andrew Phelps <anphel@microsoft.com> - 5.10.32.1-3
- Bump release number to match kernel release

* Thu May 13 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.32.1-2
- Bump release number to match kernel release

* Mon May 03 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.32.1-1
- Update source to 5.10.32.1

* Thu Apr 22 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-4
- Bump release number to match kernel release

* Mon Apr 19 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-3
- Bump release number to match kernel-signed update

* Thu Apr 15 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.28.1-2
- Update to kernel release 5.10.28.1-2

* Thu Apr 08 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-1
- Update source to 5.10.28.1

* Fri Mar 26 2021 Daniel Mihai <dmihai@microsoft.com> - 5.10.21.1-4
- Update to kernel release 5.10.21.1-4

* Thu Mar 18 2021 Chris Co <chrco@microsoft.com> - 5.10.21.1-3
- Update to kernel release 5.10.21.1-3

* Wed Mar 17 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.10.21.1-2
- Update to kernel release 5.10.21.1-2

* Thu Mar 11 2021 Chris Co <chrco@microsoft.com> - 5.10.21.1-1
- Update source to 5.10.21.1

* Fri Mar 05 2021 Chris Co <chrco@microsoft.com> - 5.10.13.1-4
- Update to kernel release 5.10.13.1-4

* Thu Mar 04 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.13.1-3
- Update to kernel release 5.10.13.1-3

* Mon Feb 22 2021 Thomas Crain <thcrain@microsoft.com> - 5.10.13.1-2
- Update to kernel release 5.10.13.1-2

* Thu Feb 18 2021 Chris Co <chrco@microsoft.com> - 5.10.13.1-1
- Update source to 5.10.13.1

* Tue Feb 16 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-5
- Update to kernel release 5.4.91-5

* Tue Feb 09 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-4
- Update to kernel release 5.4.91-4

* Thu Jan 28 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-3
- Update to kernel release 5.4.91-3

* Thu Jan 28 2021 Daniel McIlvaney <damcilva@microsoft.com> - 5.4.91-2
- Update release number to match kernel spec

* Wed Jan 20 2021 Chris Co <chrco@microsoft.com> - 5.4.91-1
- Update source to 5.4.91

* Tue Jan 12 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.4.83-4
- Update release number to match kernel spec

* Sat Jan 09 2021 Andrew Phelps <anphel@microsoft.com> - 5.4.83-3
- Update to kernel release 5.4.83-3

* Mon Dec 28 2020 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.83-2
- Update to kernel release 5.4.83-2

* Tue Dec 15 2020 Henry Beberman <henry.beberman@microsoft.com> - 5.4.83-1
- Update source to 5.4.83

* Fri Dec 04 2020 Chris Co <chrco@microsoft.com> - 5.4.81-1
- Update source to 5.4.81

* Mon Oct 26 2020 Chris Co <chrco@microsoft.com> - 5.4.72-1
- Update source to 5.4.72
- Add license file
- Lint spec

* Tue Sep 01 2020 Chris Co <chrco@microsoft.com> - 5.4.51-2
- Update source hash

* Wed Aug 19 2020 Chris Co <chrco@microsoft.com> - 5.4.51-1
- Update source to 5.4.51

* Fri Jun 12 2020 Chris Co <chrco@microsoft.com> - 5.4.42-1
- Update source to 5.4.42

* Thu Apr 30 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-2
- Renaming linux-api-headers to kernel-headers

* Tue Dec 10 2019 Chris Co <chrco@microsoft.com> - 5.4.23-1
- Update to Microsoft Linux Kernel 5.4.23.
- Use make headers since with 5.4, headers_install now requires rsync.

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> - 4.19.52-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Mon Jun 17 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.52-1
- Update to version 4.19.52

* Tue May 07 2019 Ajay Kaher <akaher@vmware.com> - 4.19.40-1
- Update to version 4.19.40

* Wed Mar 27 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.32-1
- Update to version 4.19.32

* Thu Mar 14 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.29-1
- Update to version 4.19.29

* Tue Mar 05 2019 Ajay Kaher <akaher@vmware.com> - 4.19.26-1
- Update to version 4.19.26

* Tue Jan 15 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.15-1
- Update to version 4.19.15

* Mon Dec 10 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.6-1
- Update to version 4.19.6

* Mon Nov 05 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.1-1
- Update to version 4.19.1

* Thu Sep 20 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.18.9-1
- Update to version 4.18.9

* Wed Sep 19 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.67-1
- Update to version 4.14.67

* Mon Jul 09 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> - 4.14.54-1
- Update to version 4.14.54

* Fri Dec 22 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.14.8-1
- Version update

* Mon Dec 04 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.66-1
- Version update

* Tue Nov 21 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.64-1
- Version update

* Mon Nov 06 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.60-1
- Version update

* Thu Oct 05 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.53-1
- Version update

* Mon Oct 02 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.52-1
- Version update

* Mon Sep 04 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.47-1
- Version update

* Mon Aug 14 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.43-1
- Version update

* Wed Jun 28 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.34-1
- Version update

* Fri May 26 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.30-1
- Version update

* Tue May 16 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.28-1
- Version update

* Wed May 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.27-1
- Update to linux-4.9.27

* Sun May 7 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.26-1
- Update to linux-4.9.26

* Tue Apr 25 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.24-1
- Update to linux-4.9.24

* Tue Feb 28 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.13-1
- Update to linux-4.9.13

* Thu Feb 09 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.9-1
- Update to linux-4.9.9

* Tue Jan 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.2-1
- Update to linux-4.9.2

* Mon Dec 12 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.9.0-1
- Update to linux-4.9.0

* Mon Nov 28 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.35-1
- Update to linux-4.4.35

* Thu Nov 10 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-1
- Update to linux-4.4.31

* Wed Sep  7 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-1
- Update kernel version to 4.4.20

* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> - 4.4.8-2
- GA - Bump release of all rpms

* Thu Apr 28 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-1
- Update to linux-4.4.8

* Wed Dec 16 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-1
- Upgrading kernel version to 4.2.0.

* Wed Aug 12 2015 Sharath George <sharathg@vmware.com> - 4.0.9-1
- Upgrading kernel version.

* Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> - 3.13.3-1
- Initial build. First version
