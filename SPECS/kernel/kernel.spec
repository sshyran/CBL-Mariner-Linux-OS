%global security_hardening none
%global sha512hmac bash %{_sourcedir}/sha512hmac-openssl.sh
%define uname_r %{version}-%{release}
Summary:        Linux Kernel
Name:           kernel
Version:        5.10.146.1
Release:        1%{?dist}
License:        GPLv2
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/Kernel
URL:            https://github.com/microsoft/CBL-Mariner-Linux-Kernel
#Source0:        https://github.com/microsoft/CBL-Mariner-Linux-Kernel/archive/rolling-lts/mariner/%{version}.tar.gz
Source0:        kernel-%{version}.tar.gz
Source1:        config
Source2:        config_aarch64
Source3:        sha512hmac-openssl.sh
Source4:        cbl-mariner-ca-20211013.pem
Patch0:         0001-clocksource-drivers-hyper-v-Re-enable-VDSO_CLOCKMODE.patch
# Kernel CVEs are addressed by moving to a newer version of the stable kernel.
# Since kernel CVEs are filed against the upstream kernel version and not the
# stable kernel version, our automated tooling will still flag the CVE as not
# fixed.
# To indicate a kernel CVE is fixed to our automated tooling, add nopatch files
# but do not apply them as a real patch. Each nopatch file should contain
# information on why the CVE nopatch was applied.
Patch1000:      CVE-2020-8992.nopatch
Patch1001:      CVE-2020-12770.nopatch
Patch1002:      CVE-2020-13143.nopatch
Patch1003:      CVE-2020-11884.nopatch
Patch1004:      CVE-2020-11494.nopatch
Patch1005:      CVE-2020-11565.nopatch
Patch1006:      CVE-2020-12655.nopatch
Patch1007:      CVE-2020-12771.nopatch
Patch1008:      CVE-2020-13974.nopatch
Patch1009:      CVE-2020-15393.nopatch
Patch1010:      CVE-2020-8647.nopatch
Patch1011:      CVE-2020-8648.nopatch
Patch1012:      CVE-2020-8649.nopatch
Patch1013:      CVE-2020-9383.nopatch
Patch1014:      CVE-2020-11725.nopatch
Patch1015:      CVE-2020-10757.nopatch
Patch1016:      CVE-2020-12653.nopatch
Patch1017:      CVE-2020-12657.nopatch
Patch1018:      CVE-2010-3865.nopatch
Patch1019:      CVE-2020-11668.nopatch
Patch1020:      CVE-2020-12654.nopatch
Patch1021:      CVE-2020-24394.nopatch
Patch1022:      CVE-2020-8428.nopatch
Patch1023:      CVE-2018-1000026.nopatch
Patch1024:      CVE-2018-16880.nopatch
Patch1025:      CVE-2020-12464.nopatch
Patch1026:      CVE-2020-12465.nopatch
Patch1027:      CVE-2020-12659.nopatch
Patch1028:      CVE-2020-15780.nopatch
Patch1029:      CVE-2020-14356.nopatch
Patch1030:      CVE-2020-14386.nopatch
Patch1031:      CVE-2020-25645.nopatch
Patch1032:      CVE-2020-25643.nopatch
Patch1033:      CVE-2020-25211.nopatch
Patch1034:      CVE-2020-25212.nopatch
Patch1035:      CVE-2008-4609.nopatch
Patch1036:      CVE-2020-14331.nopatch
Patch1037:      CVE-2010-0298.nopatch
Patch1038:      CVE-2020-10690.nopatch
Patch1039:      CVE-2020-25285.nopatch
Patch1040:      CVE-2020-10711.nopatch
Patch1041:      CVE-2019-3887.nopatch
Patch1042:      CVE-2020-14390.nopatch
Patch1043:      CVE-2019-19338.nopatch
Patch1044:      CVE-2019-20810.nopatch
Patch1045:      CVE-2020-10766.nopatch
Patch1046:      CVE-2020-10767.nopatch
Patch1047:      CVE-2020-10768.nopatch
Patch1048:      CVE-2020-10781.nopatch
Patch1049:      CVE-2020-12768.nopatch
Patch1050:      CVE-2020-14314.nopatch
Patch1051:      CVE-2020-14385.nopatch
Patch1052:      CVE-2020-25641.nopatch
Patch1053:      CVE-2020-26088.nopatch
Patch1054:      CVE-2020-10942.nopatch
Patch1055:      CVE-2020-12826.nopatch
Patch1056:      CVE-2019-3016.nopatch
Patch1057:      CVE-2019-3819.nopatch
Patch1058:      CVE-2020-16166.nopatch
Patch1059:      CVE-2020-11608.nopatch
Patch1060:      CVE-2020-11609.nopatch
Patch1061:      CVE-2020-25284.nopatch
Patch1062:      CVE-2020-12888.nopatch
Patch1063:      CVE-2017-8244.nopatch
Patch1064:      CVE-2017-8245.nopatch
Patch1065:      CVE-2017-8246.nopatch
Patch1066:      CVE-2009-4484.nopatch
Patch1067:      CVE-2015-5738.nopatch
Patch1068:      CVE-2007-4998.nopatch
Patch1069:      CVE-2010-0309.nopatch
Patch1070:      CVE-2011-0640.nopatch
Patch1071:      CVE-2020-12656.nopatch
Patch1072:      CVE-2011-2519.nopatch
Patch1073:      CVE-1999-0656.nopatch
Patch1074:      CVE-2010-4563.nopatch
Patch1075:      CVE-2019-20794.nopatch
Patch1076:      CVE-1999-0524.nopatch
Patch1077:      CVE-2020-25705.nopatch
Patch1078:      CVE-2020-15436.nopatch
Patch1079:      CVE-2020-28974.nopatch
Patch1080:      CVE-2020-29368.nopatch
Patch1081:      CVE-2020-29369.nopatch
Patch1082:      CVE-2020-29370.nopatch
Patch1083:      CVE-2020-29374.nopatch
Patch1084:      CVE-2020-29373.nopatch
Patch1085:      CVE-2020-28915.nopatch
Patch1086:      CVE-2020-28941.nopatch
Patch1087:      CVE-2020-27675.nopatch
Patch1088:      CVE-2020-15437.nopatch
Patch1089:      CVE-2020-29371.nopatch
# CVE-2020-29372 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1090:      CVE-2020-29372.nopatch
# CVE-2020-27194 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1091:      CVE-2020-27194.nopatch
# CVE-2020-27152 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1092:      CVE-2020-27152.nopatch
Patch1093:      CVE-2020-14351.nopatch
Patch1094:      CVE-2020-14381.nopatch
Patch1095:      CVE-2020-25656.nopatch
Patch1096:      CVE-2020-25704.nopatch
Patch1097:      CVE-2020-29534.nopatch
Patch1098:      CVE-2020-29660.nopatch
Patch1099:      CVE-2020-29661.nopatch
Patch1100:      CVE-2020-27777.nopatch
Patch1101:      CVE-2020-29569.nopatch
Patch1102:      CVE-2020-28374.nopatch
Patch1103:      CVE-2020-36158.nopatch
Patch1104:      CVE-2021-26930.nopatch
Patch1105:      CVE-2020-35499.nopatch
Patch1106:      CVE-2021-26931.nopatch
Patch1107:      CVE-2021-26932.nopatch
Patch1108:      CVE-2021-27365.nopatch
Patch1109:      CVE-2021-27364.nopatch
Patch1110:      CVE-2021-27363.nopatch
Patch1111:      CVE-2020-27170.nopatch
Patch1112:      CVE-2020-27171.nopatch
Patch1113:      CVE-2021-28375.nopatch
Patch1114:      CVE-2021-28660.nopatch
Patch1115:      CVE-2021-28950.nopatch
Patch1116:      CVE-2021-28951.nopatch
Patch1117:      CVE-2021-28952.nopatch
Patch1118:      CVE-2021-28971.nopatch
Patch1119:      CVE-2021-28972.nopatch
Patch1120:      CVE-2021-29266.nopatch
Patch1121:      CVE-2021-28964.nopatch
Patch1122:      CVE-2020-35508.nopatch
Patch1123:      CVE-2020-16120.nopatch
Patch1124:      CVE-2021-29264.nopatch
Patch1125:      CVE-2021-29265.nopatch
Patch1126:      CVE-2021-29646.nopatch
Patch1127:      CVE-2021-29647.nopatch
Patch1128:      CVE-2021-29649.nopatch
Patch1129:      CVE-2021-29650.nopatch
Patch1130:      CVE-2021-30002.nopatch
# CVE-2021-29648 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1131:      CVE-2021-29648.nopatch
Patch1132:      CVE-2021-23133.nopatch
Patch1133:      CVE-2021-29154.nopatch
# CVE-2021-30178 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1134:      CVE-2021-30178.nopatch
Patch1135:      CVE-2021-23134.nopatch
Patch1136:      CVE-2021-29155.nopatch
Patch1137:      CVE-2021-31829.nopatch
Patch1138:      CVE-2021-31916.nopatch
Patch1139:      CVE-2021-32399.nopatch
Patch1140:      CVE-2021-33033.nopatch
Patch1141:      CVE-2021-33034.nopatch
Patch1142:      CVE-2021-3483.nopatch
Patch1143:      CVE-2021-3501.nopatch
Patch1144:      CVE-2021-3506.nopatch
Patch1145:      CVE-2020-25672.nopatch
Patch1146:      CVE-2021-33200.nopatch
Patch1147:      CVE-2021-34693.nopatch
Patch1148:      CVE-2021-33624.nopatch
Patch1149:      CVE-2021-35039.nopatch
Patch1150:      CVE-2021-33909.nopatch
Patch1151:      CVE-2021-37576.nopatch
Patch1152:      CVE-2021-34556.nopatch
Patch1153:      CVE-2021-35477.nopatch
Patch1154:      CVE-2021-28691.nopatch
Patch1155:      CVE-2021-3564.nopatch
Patch1156:      CVE-2020-25639.nopatch
Patch1157:      CVE-2021-29657.nopatch
Patch1158:      CVE-2021-38199.nopatch
# CVE-2021-38201 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1159:      CVE-2021-38201.nopatch
# CVE-2021-38202  - Introducing commit not in stable tree. No fix necessary at this time.
Patch1160:      CVE-2021-38202.nopatch
Patch1161:      CVE-2021-38207.nopatch
Patch1162:      CVE-2021-38204.nopatch
Patch1163:      CVE-2021-38206.nopatch
Patch1164:      CVE-2021-38208.nopatch
# CVE-2021-38200 - Introducing commit not in stable tree / powerpc not supported.
Patch1165:      CVE-2021-38200.nopatch
# CVE-2021-38203 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1166:      CVE-2021-38203.nopatch
Patch1167:      CVE-2021-38160.nopatch
Patch1168:      CVE-2021-3679.nopatch
Patch1169:      CVE-2021-38198.nopatch
Patch1170:      CVE-2021-38209.nopatch
Patch1171:      CVE-2021-3655.nopatch
Patch1172:      CVE-2021-38166.nopatch
Patch1173:      CVE-2021-38205.nopatch
Patch1174:      CVE-2021-3573.nopatch
Patch1175:      CVE-2021-40490.nopatch
# CVE-2021-38300 - MIPS not supported.
Patch1176:      CVE-2021-38300.nopatch
Patch1177:      CVE-2021-41073.nopatch
Patch1178:      CVE-2021-3653.nopatch
Patch1179:      CVE-2021-42008.nopatch
Patch1180:      CVE-2021-41864.nopatch
Patch1181:      CVE-2021-42252.nopatch
Patch1182:      CVE-2021-43267.nopatch
Patch1183:      CVE-2021-42739.nopatch
Patch1184:      CVE-2021-42327.nopatch
Patch1185:      CVE-2021-43389.nopatch
Patch1186:      CVE-2021-43975.nopatch
Patch1187:      CVE-2021-45480.nopatch
Patch1188:      CVE-2021-45486.nopatch
Patch1189:      CVE-2021-45485.nopatch
Patch1190:      CVE-2021-44733.nopatch
Patch1191:      CVE-2021-45469.nopatch
Patch1192:      CVE-2021-28714.nopatch
Patch1193:      CVE-2021-28715.nopatch
Patch1194:      CVE-2021-46283.nopatch
Patch1195:      CVE-2021-45095.nopatch
Patch1196:      CVE-2022-0185.nopatch
Patch1197:      CVE-2022-23222.nopatch
Patch1198:      CVE-2021-4083.nopatch
Patch1199:      CVE-2021-4154.nopatch
Patch1200:      CVE-2021-4001.nopatch
Patch1201:      CVE-2022-0487.nopatch
Patch1202:      CVE-2021-3753.nopatch
# CVE-2021-4032 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1203:      CVE-2021-4032.nopatch
Patch1204:      CVE-2022-24448.nopatch
Patch1205:      CVE-2022-24959.nopatch
Patch1206:      CVE-2022-25258.nopatch
Patch1207:      CVE-2022-25375.nopatch
# CVE-2022-0264 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1208:      CVE-2022-0264.nopatch
Patch1209:      CVE-2021-45402.nopatch
Patch1210:      CVE-2021-3752.nopatch
Patch1211:      CVE-2021-20322.nopatch
Patch1212:      CVE-2021-43976.nopatch
# CVE-2021-4090 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1213:      CVE-2021-4090.nopatch
# CVE-2021-4093 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1214:      CVE-2021-4093.nopatch
# CVE-2022-25265 - gcc versions < 7.X.X not supported.
Patch1215:      CVE-2022-25265.nopatch
# CVE-2021-20320 - s390 not supported.
Patch1216:      CVE-2021-20320.nopatch
Patch1217:      CVE-2021-20321.nopatch
# CVE-2022-0382 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1218:      CVE-2022-0382.nopatch
Patch1219:      CVE-2022-0617.nopatch
Patch1220:      CVE-2022-0847.nopatch
Patch1221:      CVE-2021-3656.nopatch
Patch1222:      CVE-2021-3609.nopatch
Patch1223:      CVE-2021-3744.nopatch
Patch1224:      CVE-2021-3640.nopatch
Patch1225:      CVE-2021-3739.nopatch
Patch1226:      CVE-2022-0492.nopatch
Patch1227:      CVE-2022-0516.nopatch
Patch1228:      CVE-2021-3732.nopatch
# CVE-2022-0433 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1229:      CVE-2022-0433.nopatch
# CVE-2021-4095 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1230:      CVE-2021-4095.nopatch
Patch1231:      CVE-2022-24958.nopatch
Patch1232:      CVE-2021-3772.nopatch
Patch1233:      CVE-2021-4002.nopatch
Patch1234:      CVE-2021-45868.nopatch
Patch1235:      CVE-2022-26490.nopatch
# CVE-2022-26878 - Introducing commit not in stable tree. No fix necessary at this time.
Patch1236:      CVE-2022-26878.nopatch
Patch1237:      CVE-2022-26966.nopatch
Patch1238:      CVE-2022-27223.nopatch
BuildRequires:  audit-devel
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  diffutils
BuildRequires:  glib-devel
BuildRequires:  kbd
BuildRequires:  kmod-devel
BuildRequires:  libdnet-devel
BuildRequires:  libmspack-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  procps-ng-devel
BuildRequires:  python3
BuildRequires:  sed
BuildRequires:  xerces-c-devel
Requires:       filesystem
Requires:       kmod
Requires(post): coreutils
Requires(postun): coreutils
# When updating the config files it is important to sanitize them.
# Steps for updating a config file:
#  1. Extract the linux sources into a folder
#  2. Add the current config file to the folder
#  3. Run `make menuconfig` to edit the file (Manually editing is not recommended)
#  4. Save the config file
#  5. Copy the config file back into the kernel spec folder
#  6. Revert any undesired changes (GCC related changes, etc)
#  8. Build the kernel package
#  9. Apply the changes listed in the log file (if any) to the config file
#  10. Verify the rest of the config file looks ok
# If there are significant changes to the config file, disable the config check and build the
# kernel rpm. The final config file is included in /boot in the rpm.

%description
The kernel package contains the Linux kernel.

%package devel
Summary:        Kernel Dev
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}
Requires:       gawk
Requires:       python3
Obsoletes:      linux-dev

%description devel
This package contains the Linux kernel dev files

%package drivers-accessibility
Summary:        Kernel accessibility modules
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}

%description drivers-accessibility
This package contains the Linux kernel accessibility support

%package drivers-sound
Summary:        Kernel Sound modules
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}

%description drivers-sound
This package contains the Linux kernel sound support

%package docs
Summary:        Kernel docs
Group:          System Environment/Kernel
Requires:       python3

%description docs
This package contains the Linux kernel doc files

%ifarch x86_64
%package oprofile
Summary:        Kernel driver for oprofile, a statistical profiler for Linux systems
Group:          System Environment/Kernel
Requires:       %{name} = %{version}-%{release}

%description oprofile
Kernel driver for oprofile, a statistical profiler for Linux systems
%endif

%package tools
Summary:        This package contains the 'perf' performance analysis tools for Linux kernel
Group:          System/Tools
Requires:       %{name} = %{version}-%{release}
Requires:       audit

%description tools
This package contains the 'perf' performance analysis tools for Linux kernel.

%package dtb
Summary:        This package contains common device tree blobs (dtb)
Group:          System Environment/Kernel

%description dtb
This package contains common device tree blobs (dtb)

%package -n bpftool
License: GPLv2
Summary:        Inspection and simple manipulation of eBPF programs and maps


%description -n bpftool
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%prep
%setup -q -n CBL-Mariner-Linux-Kernel-rolling-lts-mariner-%{version}
%patch0 -p1

%build
make mrproper

%ifarch x86_64
cp %{SOURCE1} .config
arch="x86_64"
archdir="x86"
%endif

%ifarch aarch64
cp %{SOURCE2} .config
arch="arm64"
archdir="arm64"
%endif

# Add CBL-Mariner cert into kernel's trusted keyring
cp %{SOURCE4} certs/mariner.pem
sed -i 's#CONFIG_SYSTEM_TRUSTED_KEYS=""#CONFIG_SYSTEM_TRUSTED_KEYS="certs/mariner.pem"#' .config

cp .config current_config
sed -i 's/CONFIG_LOCALVERSION=""/CONFIG_LOCALVERSION="-%{release}"/' .config
make LC_ALL=  ARCH=${arch} oldconfig

# Verify the config files match
cp .config new_config
sed -i 's/CONFIG_LOCALVERSION=".*"/CONFIG_LOCALVERSION=""/' new_config
diff --unified new_config current_config > config_diff || true
if [ -s config_diff ]; then
    printf "\n\n\n\n\n\n\n\n"
    cat config_diff
    printf "\n\n\n\n\n\n\n\n"
    echo "Config file has unexpected changes"
    echo "Update config file to set changed values explicitly"

#  (DISABLE THIS IF INTENTIONALLY UPDATING THE CONFIG FILE)
    exit 1
fi

make VERBOSE=1 KBUILD_BUILD_VERSION="1" KBUILD_BUILD_HOST="CBL-Mariner" ARCH=${arch} %{?_smp_mflags}
make -C tools perf

#Compile bpftool
make -C tools/bpf/bpftool

%define __modules_install_post \
for MODULE in `find %{buildroot}/lib/modules/%{uname_r} -name *.ko` ; do \
    ./scripts/sign-file sha512 certs/signing_key.pem certs/signing_key.x509 $MODULE \
    rm -f $MODULE.{sig,dig} \
    xz $MODULE \
    done \
%{nil}

# We want to compress modules after stripping. Extra step is added to
# the default __spec_install_post.
%define __spec_install_post\
    %{?__debug_package:%{__debug_install_post}}\
    %{__arch_install_post}\
    %__os_install_post\
    %{__modules_install_post}\
%{nil}

%install
install -vdm 755 %{buildroot}%{_sysconfdir}
install -vdm 700 %{buildroot}/boot
install -vdm 755 %{buildroot}%{_defaultdocdir}/linux-%{uname_r}
install -vdm 755 %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}
install -vdm 755 %{buildroot}%{_lib}/debug/lib/modules/%{uname_r}
make INSTALL_MOD_PATH=%{buildroot} modules_install

%ifarch x86_64
install -vm 600 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{uname_r}
%endif

%ifarch aarch64
install -vm 600 arch/arm64/boot/Image %{buildroot}/boot/vmlinuz-%{uname_r}
install -D -m 640 arch/arm64/boot/dts/freescale/imx8mq-evk.dtb %{buildroot}/boot/dtb/fsl-imx8mq-evk.dtb
%endif

# Restrict the permission on System.map-X file
install -vm 400 System.map %{buildroot}/boot/System.map-%{uname_r}
install -vm 600 .config %{buildroot}/boot/config-%{uname_r}
cp -r Documentation/*        %{buildroot}%{_defaultdocdir}/linux-%{uname_r}
install -vm 644 vmlinux %{buildroot}%{_lib}/debug/lib/modules/%{uname_r}/vmlinux-%{uname_r}
# `perf test vmlinux` needs it
ln -s vmlinux-%{uname_r} %{buildroot}%{_lib}/debug/lib/modules/%{uname_r}/vmlinux

cat > %{buildroot}/boot/linux-%{uname_r}.cfg << "EOF"
# GRUB Environment Block
mariner_cmdline=init=/lib/systemd/systemd ro loglevel=3 quiet no-vmw-sta crashkernel=128M lockdown=integrity
mariner_linux=vmlinuz-%{uname_r}
mariner_initrd=initrd.img-%{uname_r}
EOF
chmod 600 %{buildroot}/boot/linux-%{uname_r}.cfg

# hmac sign the kernel for FIPS
%{sha512hmac} %{buildroot}/boot/vmlinuz-%{uname_r} | sed -e "s,$RPM_BUILD_ROOT,," > %{buildroot}/boot/.vmlinuz-%{uname_r}.hmac
cp %{buildroot}/boot/.vmlinuz-%{uname_r}.hmac %{buildroot}/lib/modules/%{uname_r}/.vmlinuz.hmac

# Register myself to initramfs
mkdir -p %{buildroot}/%{_localstatedir}/lib/initramfs/kernel
cat > %{buildroot}/%{_localstatedir}/lib/initramfs/kernel/%{uname_r} << "EOF"
--add-drivers "xen-scsifront xen-blkfront xen-acpi-processor xen-evtchn xen-gntalloc xen-gntdev xen-privcmd xen-pciback xenfs hv_utils hv_vmbus hv_storvsc hv_netvsc hv_sock hv_balloon virtio_blk virtio-rng virtio_console virtio_crypto virtio_mem vmw_vsock_virtio_transport vmw_vsock_virtio_transport_common 9pnet_virtio vrf"
EOF

#    Cleanup dangling symlinks
rm -rf %{buildroot}/lib/modules/%{uname_r}/source
rm -rf %{buildroot}/lib/modules/%{uname_r}/build

find . -name Makefile* -o -name Kconfig* -o -name *.pl | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
find arch/${archdir}/include include scripts -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
find $(find arch/${archdir} -name include -o -name scripts -type d) -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
find arch/${archdir}/include Module.symvers include scripts -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}' copy
%ifarch x86_64
# CONFIG_STACK_VALIDATION=y requires objtool to build external modules
install -vsm 755 tools/objtool/objtool %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}/tools/objtool/
install -vsm 755 tools/objtool/fixdep %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}/tools/objtool/
%endif

cp .config %{buildroot}%{_prefix}/src/linux-headers-%{uname_r} # copy .config manually to be where it's expected to be
ln -sf "%{_prefix}/src/linux-headers-%{uname_r}" "%{buildroot}/lib/modules/%{uname_r}/build"
find %{buildroot}/lib/modules -name '*.ko' -print0 | xargs -0 chmod u+x

%ifarch aarch64
cp scripts/module.lds %{buildroot}%{_prefix}/src/linux-headers-%{uname_r}/scripts/module.lds
%endif

# disable (JOBS=1) parallel build to fix this issue:
# fixdep: error opening depfile: ./.plugin_cfg80211.o.d: No such file or directory
# Linux version that was affected is 4.4.26
make -C tools JOBS=1 DESTDIR=%{buildroot} prefix=%{_prefix} perf_install

# Install bpftool
make -C tools/bpf/bpftool DESTDIR=%{buildroot} prefix=%{_prefix} bash_compdir=%{_sysconfdir}/bash_completion.d/ mandir=%{_mandir} install

%triggerin -- initramfs
mkdir -p %{_localstatedir}/lib/rpm-state/initramfs/pending
touch %{_localstatedir}/lib/rpm-state/initramfs/pending/%{uname_r}
echo "initrd generation of kernel %{uname_r} will be triggered later" >&2

%triggerun -- initramfs
rm -rf %{_localstatedir}/lib/rpm-state/initramfs/pending/%{uname_r}
rm -rf /boot/initrd.img-%{uname_r}
echo "initrd of kernel %{uname_r} removed" >&2

%postun
if [ ! -e /boot/mariner.cfg ]
then
     ls /boot/linux-*.cfg 1> /dev/null 2>&1
     if [ $? -eq 0 ]
     then
          list=`ls -tu /boot/linux-*.cfg | head -n1`
          test -n "$list" && ln -sf "$list" /boot/mariner.cfg
     fi
fi

%post
/sbin/depmod -a %{uname_r}
ln -sf linux-%{uname_r}.cfg /boot/mariner.cfg

%post drivers-accessibility
/sbin/depmod -a %{uname_r}

%post drivers-sound
/sbin/depmod -a %{uname_r}

%ifarch x86_64
%post oprofile
/sbin/depmod -a %{uname_r}
%endif

%files
%defattr(-,root,root)
%license COPYING
/boot/System.map-%{uname_r}
/boot/config-%{uname_r}
/boot/vmlinuz-%{uname_r}
/boot/.vmlinuz-%{uname_r}.hmac
%config(noreplace) /boot/linux-%{uname_r}.cfg
%config %{_localstatedir}/lib/initramfs/kernel/%{uname_r}
%defattr(0644,root,root)
/lib/modules/%{uname_r}/*
/lib/modules/%{uname_r}/.vmlinuz.hmac
%exclude /lib/modules/%{uname_r}/build
%exclude /lib/modules/%{uname_r}/kernel/drivers/gpu
%exclude /lib/modules/%{uname_r}/kernel/sound
%ifarch x86_64
%exclude /lib/modules/%{uname_r}/kernel/arch/x86/oprofile/
%endif

%files docs
%defattr(-,root,root)
%{_defaultdocdir}/linux-%{uname_r}/*

%files devel
%defattr(-,root,root)
/lib/modules/%{uname_r}/build
%{_prefix}/src/linux-headers-%{uname_r}

%files drivers-accessibility
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/drivers/accessibility

%files drivers-sound
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/sound

%ifarch x86_64
%files oprofile
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/arch/x86/oprofile/
%endif

%files tools
%defattr(-,root,root)
%{_libexecdir}
%exclude %{_libdir}/debug
%ifarch x86_64
%{_lib64}/traceevent
%endif
%ifarch aarch64
%{_lib}/traceevent
%endif
%{_bindir}
%{_sysconfdir}/bash_completion.d/*
%{_datadir}/perf-core/strace/groups/file
%{_datadir}/perf-core/strace/groups/string
%{_docdir}/*
%{_libdir}/perf/examples/bpf/*
%{_libdir}/perf/include/bpf/*

%ifarch aarch64
%files dtb
/boot/dtb/fsl-imx8mq-evk.dtb
%endif

%files -n bpftool
%{_sbindir}/bpftool
%{_sysconfdir}/bash_completion.d/bpftool

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
- Enable 32-bit time syscall support

* Tue Aug 23 2022 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 5.10.134.1-1
- Upgrade to 5.10.134.1

* Wed Aug 17 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.133.1-1
- Update source to 5.10.133.1

* Sun Jul 24 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.131.1-1
- Update source to 5.10.131.1

* Wed Jul 06 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.10.128.1-1
- Update source to 5.10.128.1
- Address CVE-2022-32296, CVE-2022-1652, CVE-2022-1786, CVE-2022-0854,
  CVE-2021-20194, CVE-2021-32078, CVE-2021-37159

* Mon Jun 20 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.123.1-1
- Update source to 5.10.123.1

* Wed Jun 01 2022 Minghe Ren <mingheren@microsoft.com> - 5.10.117.1-2
- Disable SMACK kernel configuration

* Tue May 24 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.10.117.1-1
- Update source to 5.10.117.1
- Address CVE-2022-28893 

* Tue May 17 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.116.1-1
- Update source to 5.10.116.1
- Address CVE-2022-1048, CVE-2022-1353, CVE-2022-29582, CVE-2022-1195
  CVE-2022-0494, CVE-2022-1015, CVE-2022-29968

* Tue Apr 19 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.111.1-1
- Update source to 5.10.111.1
- Enable CONFIG_BPF_UNPRIV_DEFAULT_OFF
- Address CVE-2021-4023, CVE-2021-4157, CVE-2022-0435, CVE-2022-0998
  CVE-2022-28356, CVE-2022-28388, CVE-2022-28389, CVE-2022-28390, 
  CVE-2021-4203, CVE-2022-0322, CVE-2022-27950, CVE-2021-4148, 
  CVE-2021-4149, CVE-2022-28796, CVE-2022-29156, CVE-2021-4202,
  CVE-2022-0500, CVE-2022-0330, CVE-2020-26558, CVE-2021-4197,
  CVE-2021-4150, CVE-2020-35501

* Fri Apr 01 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.109.1-2
- Remove hardcoded mariner.pem from configs and instead insert during
  the build phase
- Address CVE-2022-1055, CVE-2022-27666, CVE-2022-0995, CVE-2021-44879

* Tue Mar 29 2022 Max Brodeur-Urbas <maxbr@microsoft.com> - 5.10.109.1-1
- Update source to 5.10.109.1
- Remove CVE-2022-24958.patch and CVE-2022-1016.patch
- Enable CONFIG_MITIGATE_SPECTRE_BRANCH_HISTORY
- Address CVE-2021-3772, CVE-2021-4002, CVE-2021-45868, CVE-2022-26490,
  CVE-2022-26878, CVE-2022-26966, CVE-2022-27223

* Fri Mar 25 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.102.1-3
- Apply CVE-2022-1016.patch

* Fri Mar 18 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.102.1-2
- Disable CONFIG_FW_LOADER_USER_HELPER_FALLBACK

* Mon Feb 28 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.102.1-1
- Update source to 5.10.102.1
- Apply CVE-2022-24958.patch
- Remove CVE-2021-43976.patch and CVE-2022-0435.patch
- Address CVE-2021-3753, CVE-2021-4032, CVE-2022-24448, CVE-2022-24959,
  CVE-2022-25258, CVE-2022-25375, CVE-2022-0264, CVE-2021-45402,
  CVE-2021-3752, CVE-2021-20322, CVE-2021-4090, CVE-2021-4093,
  CVE-2022-25265, CVE-2021-20320, CVE-2021-20321, CVE-2022-0382,
  CVE-2022-0617, CVE-2022-0847, CVE-2021-3656, CVE-2021-3609,
  CVE-2021-3744, CVE-2021-3640, CVE-2021-3739, CVE-2022-0492,
  CVE-2022-0516, CVE-2021-3732, CVE-2022-0433, CVE-2021-4095

* Fri Feb 11 2022 Vince Perri <viperri@microsoft.com> - 5.10.93.1-4
- Add compressed firmware support

* Wed Feb 09 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.93.1-3
- Address CVE-2022-0435 with patch

* Thu Jan 27 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.93.1-2
- Address CVE-2021-4083

* Mon Jan 24 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.93.1-1
- Update source to 5.10.93.1
- Address CVE-2021-46283, CVE-2021-45095, CVE-2022-0185, CVE-2022-23222

* Thu Jan 20 2022 Chris Co <chrco@microsoft.com> - 5.10.89.1-2
- Rotate Mariner cert 

* Sun Jan 16 2022 Rachel Menge <rachelmenge@microsoft.com> - 5.10.89.1-1
- Update source to 5.10.89.1
- Address CVE-2021-44733, CVE-2021-45469, CVE-2021-28714, CVE-2021-28715
- Remove patch add-linux-syscall-license-info.patch

* Fri Jan 14 2022 Henry Li <lihl@microsoft.com> - 5.10.88.1-3
- Add patch to export mmput_async

* Wed Jan 12 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.10.88.1-2
- Addressed CVE-2021-45485

* Mon Jan 03 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.10.88.1-1
- Update Kernel source to 5.10.88.1
- Addressed CVE-2021-43975, CVE-2021-45480, CVE-2021-45486
- Patch for CVE-2021-43976

* Mon Nov 29 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.78.1-2
- Enable CONFIG_COMPAT kernel configs

* Mon Nov 08 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.78.1-1
- Update source to 5.10.78.1
- Address CVE-2021-43267, CVE-2021-42739, CVE-2021-42327, CVE-2021-43389
- Add patch to fix SPDX-License-Identifier in headers
- Revert ebpf configs due to increased boot times

* Tue Oct 26 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.74.1-2
- Update configs for eBPF support
- Add dwarves Build-requires

* Tue Oct 19 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.74.1-1
- Update source to 5.10.74.1
- Address CVE-2021-41864, CVE-2021-42252
- License verified

* Thu Oct 07 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.69.1-1
- Update source to 5.10.69.1
- Address CVE-2021-38300, CVE-2021-41073, CVE-2021-3653, CVE-2021-42008

* Wed Sep 22 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-3
- Enable CONFIG_NET_VRF
- Add vrf to drivers for dracut

* Tue Sep 21 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-2
- Export `bpftool` subpackage

* Mon Sep 20 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.64.1-1
- Update source to 5.10.64.1
- Address CVE-2021-40490

* Mon Sep 13 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.60.1-2
- Remove cn from dracut drivers argument

* Mon Aug 23 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.60.1-1
- Update source to 5.10.60.1
- Remove patch for CDROM eject errors
- Address CVE-2021-38166, CVE-2021-38205, CVE-2021-3573

* Thu Aug 12 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.57.1-1
- Update source to 5.10.57.1
- Address CVE-2021-37576, CVE-2021-34556, CVE-2021-35477, CVE-2021-28691,
  CVE-2021-3564, CVE-2020-25639, CVE-2021-29657, CVE-2021-38199,
  CVE-2021-38201, CVE-2021-38202, CVE-2021-38207, CVE-2021-38204,
  CVE-2021-38206, CVE-2021-38208, CVE-2021-38200, CVE-2021-38203,
  CVE-2021-38160, CVE-2021-3679, CVE-2021-38198, CVE-2021-38209,
  CVE-2021-3655

* Tue Aug 03 2021 Chris Co <chrco@microsoft.com> - 5.10.52.1-3
- Add patch to fix VDSO in HyperV

* Fri Jul 30 2021 Chris Co <chrco@microsoft.com> - 5.10.52.1-2
- Add patch to fix CDROM eject errors

* Tue Jul 20 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.52.1-1
- Update source to 5.10.52.1
- Address CVE-2021-35039, CVE-2021-33909

* Mon Jul 19 2021 Chris Co <chrco@microsoft.com> - 5.10.47.1-2
- Enable CONFIG_CONNECTOR and CONFIG_PROC_EVENTS

* Tue Jul 06 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.47.1-1
- Update source to 5.10.47.1
- Address CVE-2021-34693, CVE-2021-33624

* Wed Jun 30 2021 Chris Co <chrco@microsoft.com> - 5.10.42.1-4
- Enable legacy mcelog config

* Tue Jun 22 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.42.1-3
- Enable CONFIG_IOSCHED_BFQ and CONFIG_BFQ_GROUP_IOSCHED configs

* Wed Jun 16 2021 Chris Co <chrco@microsoft.com> - 5.10.42.1-2
- Enable CONFIG_CROSS_MEMORY_ATTACH

* Tue Jun 08 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.42.1-1
- Update source to 5.10.42.1
- Address CVE-2021-33200

* Thu Jun 03 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.37.1-2
- Address CVE-2020-25672

* Fri May 28 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.37.1-1
- Update source to 5.10.37.1
- Address CVE-2021-23134, CVE-2021-29155, CVE-2021-31829, CVE-2021-31916,
  CVE-2021-32399, CVE-2021-33033, CVE-2021-33034, CVE-2021-3483
  CVE-2021-3501, CVE-2021-3506

* Thu May 27 2021 Chris Co <chrco@microsoft.com> - 5.10.32.1-7
- Set lockdown=integrity by default

* Wed May 26 2021 Chris Co <chrco@microsoft.com> - 5.10.32.1-6
- Add Mariner cert into the trusted kernel keyring

* Tue May 25 2021 Daniel Mihai <dmihai@microsoft.com> - 5.10.32.1-5
- Enable kernel debugger

* Thu May 20 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.10.32.1-4
- Bump release number to match kernel-signed update

* Tue May 17 2021 Andrew Phelps <anphel@microsoft.com> - 5.10.32.1-3
- Update CONFIG_LD_VERSION for binutils 2.36.1
- Remove build-id match check

* Thu May 13 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.32.1-2
- Add CONFIG_AS_HAS_LSE_ATOMICS=y

* Mon May 03 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.32.1-1
- Update source to 5.10.32.1
- Address CVE-2021-23133, CVE-2021-29154, CVE-2021-30178

* Thu Apr 22 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-4
- Disable CONFIG_EFI_DISABLE_PCI_DMA. It can cause boot issues on some hardware.

* Mon Apr 19 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-3
- Bump release number to match kernel-signed update

* Thu Apr 15 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.10.28.1-2
- Address CVE-2021-29648

* Thu Apr 08 2021 Chris Co <chrco@microsoft.com> - 5.10.28.1-1
- Update source to 5.10.28.1
- Update uname_r define to match the new value derived from the source
- Address CVE-2020-27170, CVE-2020-27171, CVE-2021-28375, CVE-2021-28660,
  CVE-2021-28950, CVE-2021-28951, CVE-2021-28952, CVE-2021-28971,
  CVE-2021-28972, CVE-2021-29266, CVE-2021-28964, CVE-2020-35508,
  CVE-2020-16120, CVE-2021-29264, CVE-2021-29265, CVE-2021-29646,
  CVE-2021-29647, CVE-2021-29649, CVE-2021-29650, CVE-2021-30002

* Fri Mar 26 2021 Daniel Mihai <dmihai@microsoft.com> - 5.10.21.1-4
- Enable CONFIG_CRYPTO_DRBG_HASH, CONFIG_CRYPTO_DRBG_CTR

* Thu Mar 18 2021 Chris Co <chrco@microsoft.com> - 5.10.21.1-3
- Address CVE-2021-27365, CVE-2021-27364, CVE-2021-27363
- Enable CONFIG_FANOTIFY_ACCESS_PERMISSIONS

* Wed Mar 17 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.10.21.1-2
- Disable QAT kernel configs

* Thu Mar 11 2021 Chris Co <chrco@microsoft.com> - 5.10.21.1-1
- Update source to 5.10.21.1
- Add virtio drivers to be installed into initrd
- Address CVE-2021-26930, CVE-2020-35499, CVE-2021-26931, CVE-2021-26932

* Fri Mar 05 2021 Chris Co <chrco@microsoft.com> - 5.10.13.1-4
- Enable kernel lockdown config

* Thu Mar 04 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.10.13.1-3
- Add configs for CONFIG_BNXT bnxt_en and MSR drivers

* Mon Feb 22 2021 Thomas Crain <thcrain@microsoft.com> - 5.10.13.1-2
- Add configs for speakup and uinput drivers
- Add kernel-drivers-accessibility subpackage

* Thu Feb 18 2021 Chris Co <chrco@microsoft.com> - 5.10.13.1-1
- Update source to 5.10.13.1
- Remove patch to publish efi tpm event log on ARM. Present in updated source.
- Remove patch for arm64 hyperv support. Present in updated source.
- Account for new module.lds location on aarch64
- Remove CONFIG_GCC_PLUGIN_RANDSTRUCT
- Add CONFIG_SCSI_SMARTPQI=y

* Thu Feb 11 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-5
- Add configs to enable tcrypt in FIPS mode

* Tue Feb 09 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-4
- Use OpenSSL to perform HMAC calc

* Thu Jan 28 2021 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.91-3
- Add configs for userspace crypto support
- HMAC calc the kernel for FIPS

* Wed Jan 27 2021 Daniel McIlvaney <damcilva@microsoft.com> - 5.4.91-2
- Enable dm-verity boot support with FEC

* Wed Jan 20 2021 Chris Co <chrco@microsoft.com> - 5.4.91-1
- Update source to 5.4.91
- Address CVE-2020-29569, CVE-2020-28374, CVE-2020-36158
- Remove patch to fix GUI installer crash. Fixed in updated source.

* Tue Jan 12 2021 Rachel Menge <rachelmenge@microsoft.com> - 5.4.83-4
- Add imx8mq support

* Sat Jan 09 2021 Andrew Phelps <anphel@microsoft.com> - 5.4.83-3
- Add patch to fix GUI installer crash

* Mon Dec 28 2020 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.83-2
- Address CVE-2020-27777

* Tue Dec 15 2020 Henry Beberman <henry.beberman@microsoft.com> - 5.4.83-1
- Update source to 5.4.83
- Address CVE-2020-14351, CVE-2020-14381, CVE-2020-25656, CVE-2020-25704,
  CVE-2020-29534, CVE-2020-29660, CVE-2020-29661

* Fri Dec 04 2020 Chris Co <chrco@microsoft.com> - 5.4.81-1
- Update source to 5.4.81
- Remove patch for kexec in HyperV. Integrated in 5.4.81.
- Address CVE-2020-25705, CVE-2020-15436, CVE-2020-28974, CVE-2020-29368,
  CVE-2020-29369, CVE-2020-29370, CVE-2020-29374, CVE-2020-29373, CVE-2020-28915,
  CVE-2020-28941, CVE-2020-27675, CVE-2020-15437, CVE-2020-29371, CVE-2020-29372,
  CVE-2020-27194, CVE-2020-27152

* Wed Nov 25 2020 Chris Co <chrco@microsoft.com> - 5.4.72-5
- Add patch to publish efi tpm event log on ARM

* Mon Nov 23 2020 Chris Co <chrco@microsoft.com> - 5.4.72-4
- Apply patch to fix kexec in HyperV

* Mon Nov 16 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.72-3
- Disable kernel config SLUB_DEBUG_ON due to tcp throughput perf impact

* Tue Nov 10 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.72-2
- Enable kernel configs for Arm64 HyperV, Ampere and Cavium SoCs support

* Mon Oct 26 2020 Chris Co <chrco@microsoft.com> - 5.4.72-1
- Update source to 5.4.72
- Remove patch to support CometLake e1000e ethernet. Integrated in 5.4.72.
- Add license file
- Lint spec
- Address CVE-2018-1000026, CVE-2018-16880, CVE-2020-12464, CVE-2020-12465,
  CVE-2020-12659, CVE-2020-15780, CVE-2020-14356, CVE-2020-14386, CVE-2020-25645,
  CVE-2020-25643, CVE-2020-25211, CVE-2020-25212, CVE-2008-4609, CVE-2020-14331,
  CVE-2010-0298, CVE-2020-10690, CVE-2020-25285, CVE-2020-10711, CVE-2019-3887,
  CVE-2020-14390, CVE-2019-19338, CVE-2019-20810, CVE-2020-10766, CVE-2020-10767,
  CVE-2020-10768, CVE-2020-10781, CVE-2020-12768, CVE-2020-14314, CVE-2020-14385,
  CVE-2020-25641, CVE-2020-26088, CVE-2020-10942, CVE-2020-12826, CVE-2019-3016,
  CVE-2019-3819, CVE-2020-16166, CVE-2020-11608, CVE-2020-11609, CVE-2020-25284,
  CVE-2020-12888, CVE-2017-8244, CVE-2017-8245, CVE-2017-8246, CVE-2009-4484,
  CVE-2015-5738, CVE-2007-4998, CVE-2010-0309, CVE-2011-0640, CVE-2020-12656,
  CVE-2011-2519, CVE-1999-0656, CVE-2010-4563, CVE-2019-20794, CVE-1999-0524

* Fri Oct 16 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.51-11
- Enable QAT kernel configs

* Fri Oct 02 2020 Chris Co <chrco@microsoft.com> - 5.4.51-10
- Address CVE-2020-10757, CVE-2020-12653, CVE-2020-12657, CVE-2010-3865,
  CVE-2020-11668, CVE-2020-12654, CVE-2020-24394, CVE-2020-8428

* Fri Oct 02 2020 Chris Co <chrco@microsoft.com> - 5.4.51-9
- Fix aarch64 build error

* Wed Sep 30 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.51-8
- Update postun script to deal with removal in case of another installed kernel.

* Fri Sep 25 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.51-7
- Enable Mellanox kernel configs

* Wed Sep 23 2020 Daniel McIlvaney <damcilva@microsoft.com> - 5.4.51-6
- Enable CONFIG_IMA (measurement only) and associated configs

* Thu Sep 03 2020 Daniel McIlvaney <damcilva@microsoft.com> - 5.4.51-5
- Add code to check for missing config flags in the checked in configs

* Thu Sep 03 2020 Chris Co <chrco@microsoft.com> - 5.4.51-4
- Apply additional kernel hardening configs

* Thu Sep 03 2020 Chris Co <chrco@microsoft.com> - 5.4.51-3
- Bump release number due to kernel-signed-<arch> package update
- Minor aarch64 config and changelog cleanup

* Tue Sep 01 2020 Chris Co <chrco@microsoft.com> - 5.4.51-2
- Update source hash

* Wed Aug 19 2020 Chris Co <chrco@microsoft.com> - 5.4.51-1
- Update source to 5.4.51
- Enable DXGKRNL config
- Address CVE-2020-11494, CVE-2020-11565, CVE-2020-12655, CVE-2020-12771,
  CVE-2020-13974, CVE-2020-15393, CVE-2020-8647, CVE-2020-8648, CVE-2020-8649,
  CVE-2020-9383, CVE-2020-11725

* Wed Aug 19 2020 Chris Co <chrco@microsoft.com> - 5.4.42-12
- Remove the signed package depends

* Tue Aug 18 2020 Chris Co <chrco@microsoft.com> - 5.4.42-11
- Remove signed subpackage

* Mon Aug 17 2020 Chris Co <chrco@microsoft.com> - 5.4.42-10
- Enable BPF, PC104, userfaultfd, SLUB sysfs, SMC, XDP sockets monitoring configs

* Fri Aug 07 2020 Mateusz Malisz <mamalisz@microsoft.com> - 5.4.42-9
- Add crashkernel=128M to the kernel cmdline
- Update config to support kexec and kexec_file_load

* Tue Aug 04 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 5.4.42-8
- Updating "KBUILD_BUILD_VERSION" and "KBUILD_BUILD_HOST" with correct
  distribution name.

* Wed Jul 22 2020 Chris Co <chrco@microsoft.com> - 5.4.42-7
- Address CVE-2020-8992, CVE-2020-12770, CVE-2020-13143, CVE-2020-11884

* Fri Jul 17 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.42-6
- Enable CONFIG_MLX5_CORE_IPOIB and CONFIG_INFINIBAND_IPOIB config flags

* Fri Jul 17 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.42-5
- Adding XDP config flag

* Thu Jul 09 2020 Anand Muthurajan <anandm@microsoft.com> - 5.4.42-4
- Enable CONFIG_QED, CONFIG_QEDE, CONFIG_QED_SRIOV and CONFIG_QEDE_VXLAN flags

* Wed Jun 24 2020 Chris Co <chrco@microsoft.com> - 5.4.42-3
- Regenerate input config files

* Fri Jun 19 2020 Chris Co <chrco@microsoft.com> - 5.4.42-2
- Add kernel-secure subpackage and macros for adding offline signed kernels

* Fri Jun 12 2020 Chris Co <chrco@microsoft.com> - 5.4.42-1
- Update source to 5.4.42

* Thu Jun 11 2020 Chris Co <chrco@microsoft.com> - 5.4.23-17
- Enable PAGE_POISONING configs
- Disable PROC_KCORE config
- Enable RANDOM_TRUST_CPU config for x86_64

* Fri Jun 05 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.23-16
- Adding BPF config flags

* Thu Jun 04 2020 Chris Co <chrco@microsoft.com> - 5.4.23-15
- Add config support for USB video class devices

* Wed Jun 03 2020 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.23-14
- Add CONFIG_CRYPTO_XTS=y to config.

* Wed Jun 03 2020 Chris Co <chrco@microsoft.com> - 5.4.23-13
- Add patch to support CometLake e1000e ethernet
- Remove drivers-gpu subpackage
- Inline the initramfs trigger and postun source files
- Remove rpi3 dtb and ls1012 dtb subpackages

* Wed May 27 2020 Chris Co <chrco@microsoft.com> - 5.4.23-12
- Update arm64 security configs
- Disable devmem in x86_64 config

* Tue May 26 2020 Daniel Mihai <dmihai@microsoft.com> - 5.4.23-11
- Disabled Reliable Datagram Sockets protocol (CONFIG_RDS).

* Fri May 22 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-10
- Change /boot directory permissions to 600.

* Thu May 21 2020 Chris Co <chrco@microsoft.com> - 5.4.23-9
- Update x86_64 security configs

* Wed May 20 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 5.4.23-8
- Adding InfiniBand config flags

* Mon May 11 2020 Anand Muthurajan <anandm@microsoft.com> - 5.4.23-7
- Adding PPP config flags

* Tue Apr 28 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-6
- Renaming Linux-PAM to pam

* Tue Apr 28 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-5
- Renaming linux to kernel

* Tue Apr 14 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-4
- Remove linux-aws and linux-esx references.
- Remove kat_build usage.
- Remove ENA module.

* Fri Apr 10 2020 Emre Girgin <mrgirgin@microsoft.com> - 5.4.23-3
- Remove xml-security-c dependency.

* Wed Apr 08 2020 Nicolas Ontiveros <niontive@microsoft.com> - 5.4.23-2
- Remove toybox and only use coreutils for requires.

* Tue Dec 10 2019 Chris Co <chrco@microsoft.com> - 5.4.23-1
- Update to Microsoft Linux Kernel 5.4.23
- Remove patches
- Update ENA module to 2.1.2 to work with Linux 5.4.23
- Remove xr module
- Remove Xen tmem module from dracut module list to fix initramfs creation
- Add patch to fix missing trans_pgd header in aarch64 build

* Fri Oct 11 2019 Henry Beberman <hebeberm@microsoft.com> - 4.19.52-8
- Enable Hyper-V TPM in config

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> - 4.19.52-7
- Initial CBL-Mariner import from Photon (license: Apache2).

* Thu Jul 25 2019 Keerthana K <keerthanak@vmware.com> - 4.19.52-6
- Fix postun scriplet.

* Thu Jul 11 2019 Keerthana K <keerthanak@vmware.com> - 4.19.52-5
- Enable kernel configs necessary for BPF Compiler Collection (BCC).

* Wed Jul 10 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.52-4
- Deprecate linux-aws-tools in favor of linux-tools.

* Tue Jul 02 2019 Alexey Makhalov <amakhalov@vmware.com> - 4.19.52-3
- Fix 9p vsock 16bit port issue.

* Thu Jun 20 2019 Tapas Kundu <tkundu@vmware.com> - 4.19.52-2
- Enabled CONFIG_I2C_CHARDEV to support lm-sensors

* Mon Jun 17 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.52-1
- Update to version 4.19.52
- Fix CVE-2019-12456, CVE-2019-12379, CVE-2019-12380, CVE-2019-12381,
- CVE-2019-12382, CVE-2019-12378, CVE-2019-12455

* Tue May 28 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.40-3
- Change default I/O scheduler to 'deadline' to fix performance issue.

* Tue May 14 2019 Keerthana K <keerthanak@vmware.com> - 4.19.40-2
- Fix to parse through /boot folder and update symlink (/boot/photon.cfg) if
- mulitple kernels are installed and current linux kernel is removed.

* Tue May 07 2019 Ajay Kaher <akaher@vmware.com> - 4.19.40-1
- Update to version 4.19.40

* Thu Apr 11 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.32-3
- Update config_aarch64 to fix ARM64 build.

* Fri Mar 29 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.32-2
- Fix CVE-2019-10125

* Wed Mar 27 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.32-1
- Update to version 4.19.32

* Thu Mar 14 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.29-1
- Update to version 4.19.29

* Tue Mar 05 2019 Ajay Kaher <akaher@vmware.com> - 4.19.26-1
- Update to version 4.19.26

* Thu Feb 21 2019 Him Kalyan Bordoloi <bordoloih@vmware.com> - 4.19.15-3
- Fix CVE-2019-8912

* Thu Jan 24 2019 Alexey Makhalov <amakhalov@vmware.com> - 4.19.15-2
- Add WiFi (ath10k), sensors (i2c,spi), usb support for NXP LS1012A board.

* Tue Jan 15 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.15-1
- Update to version 4.19.15

* Fri Jan 11 2019 Srinidhi Rao <srinidhir@vmware.com> - 4.19.6-7
- Add Network support for NXP LS1012A board.

* Wed Jan 09 2019 Ankit Jain <ankitja@vmware.com> - 4.19.6-6
- Enable following for x86_64 and aarch64:
-  Enable Kernel Address Space Layout Randomization.
-  Enable CONFIG_SECURITY_NETWORK_XFRM

* Fri Jan 04 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.6-5
- Enable AppArmor by default.

* Wed Jan 02 2019 Alexey Makhalov <amakhalov@vmware.com> - 4.19.6-4
- .config: added Compulab fitlet2 device drivers
- .config_aarch64: added gpio sysfs support
- renamed -sound to -drivers-sound

* Tue Jan 01 2019 Ajay Kaher <akaher@vmware.com> - 4.19.6-3
- .config: Enable CONFIG_PCI_HYPERV driver

* Wed Dec 19 2018 Srinidhi Rao <srinidhir@vmware.com> - 4.19.6-2
- Add NXP LS1012A support.

* Mon Dec 10 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.6-1
- Update to version 4.19.6

* Fri Dec 07 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.19.1-3
- .config: added qmi wwan module

* Mon Nov 12 2018 Ajay Kaher <akaher@vmware.com> - 4.19.1-2
- Fix config_aarch64 for 4.19.1

* Mon Nov 05 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.19.1-1
- Update to version 4.19.1

* Tue Oct 16 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> - 4.18.9-5
- Change in config to enable drivers for zigbee and GPS

* Fri Oct 12 2018 Ajay Kaher <akaher@vmware.com> - 4.18.9-4
- Enable LAN78xx for aarch64 rpi3

* Fri Oct 5 2018 Ajay Kaher <akaher@vmware.com> - 4.18.9-3
- Fix config_aarch64 for 4.18.9
- Add module.lds for aarch64

* Wed Oct 03 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.18.9-2
- Use updated steal time accounting patch.
- .config: Enable CONFIG_CPU_ISOLATION and a few networking options
- that got accidentally dropped in the last update.

* Mon Oct 1 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.18.9-1
- Update to version 4.18.9

* Tue Sep 25 2018 Ajay Kaher <akaher@vmware.com> - 4.14.67-2
- Build hang (at make oldconfig) fix in config_aarch64

* Wed Sep 19 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.67-1
- Update to version 4.14.67

* Tue Sep 18 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.54-7
- Add rdrand-based RNG driver to enhance kernel entropy.

* Sun Sep 02 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.54-6
- Add full retpoline support by building with retpoline-enabled gcc.

* Thu Aug 30 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.14.54-5
- Apply out-of-tree patches needed for AppArmor.

* Wed Aug 22 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.14.54-4
- Fix overflow kernel panic in rsi driver.
- .config: enable BT stack, enable GPIO sysfs.
- Add Exar USB serial driver.

* Fri Aug 17 2018 Ajay Kaher <akaher@vmware.com> - 4.14.54-3
- Enabled USB PCI in config_aarch64
- Build hang (at make oldconfig) fix in config_aarch64

* Thu Jul 19 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.14.54-2
- .config: usb_serial_pl2303=m,wlan=y,can=m,gpio=y,pinctrl=y,iio=m

* Mon Jul 09 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> - 4.14.54-1
- Update to version 4.14.54

* Fri Jan 26 2018 Alexey Makhalov <amakhalov@vmware.com> - 4.14.8-2
- Added vchiq entry to rpi3 dts
- Added dtb-rpi3 subpackage

* Fri Dec 22 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.14.8-1
- Version update

* Wed Dec 13 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.66-4
- KAT build support

* Thu Dec 07 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.66-3
- Aarch64 support

* Tue Dec 05 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.66-2
- Sign and compress modules after stripping. fips=1 requires signed modules

* Mon Dec 04 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.66-1
- Version update

* Tue Nov 21 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.64-1
- Version update

* Mon Nov 06 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.60-1
- Version update

* Wed Oct 11 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.53-3
- Add patch "KVM: Don't accept obviously wrong gsi values via
    KVM_IRQFD" to fix CVE-2017-1000252.

* Tue Oct 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.53-2
- Build hang (at make oldconfig) fix.

* Thu Oct 05 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.53-1
- Version update

* Mon Oct 02 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.52-3
- Allow privileged CLONE_NEWUSER from nested user namespaces.

* Mon Oct 02 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.52-2
- Fix CVE-2017-11472 (ACPICA: Namespace: fix operand cache leak)

* Mon Oct 02 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.9.52-1
- Version update

* Mon Sep 18 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.47-2
- Requires coreutils or toybox

* Mon Sep 04 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.47-1
- Fix CVE-2017-11600

* Tue Aug 22 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.43-2
- Add missing xen block drivers

* Mon Aug 14 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.43-1
- Version update
- [feature] new sysctl option unprivileged_userns_clone

* Wed Aug 09 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.41-2
- Fix CVE-2017-7542
- [bugfix] Added ccm,gcm,ghash,lzo crypto modules to avoid
    panic on modprobe tcrypt

* Mon Aug 07 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.41-1
- Version update

* Fri Aug 04 2017 Bo Gan <ganb@vmware.com> - 4.9.38-6
- Fix initramfs triggers

* Tue Aug 01 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.38-5
- Allow some algorithms in FIPS mode
- Reverts 284a0f6e87b0721e1be8bca419893902d9cf577a and backports
- bcf741cb779283081db47853264cc94854e7ad83 in the kernel tree
- Enable additional NF features

* Fri Jul 21 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.38-4
- Add patches in Hyperv codebase

* Fri Jul 21 2017 Anish Swaminathan <anishs@vmware.com> - 4.9.38-3
- Add missing hyperv drivers

* Thu Jul 20 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.38-2
- Disable scheduler beef up patch

* Tue Jul 18 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.38-1
- Fix CVE-2017-11176 and CVE-2017-10911

* Mon Jul 03 2017 Xiaolin Li <xiaolinl@vmware.com> - 4.9.34-3
- Add libdnet-devel, kmod-devel and libmspack-devel to BuildRequires

* Thu Jun 29 2017 Divya Thaluru <dthaluru@vmware.com> - 4.9.34-2
- Added obsolete for deprecated linux-dev package

* Wed Jun 28 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.34-1
- [feature] 9P FS security support
- [feature] DM Delay target support
- Fix CVE-2017-1000364 ("stack clash") and CVE-2017-9605

* Thu Jun 8 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.31-1
- Fix CVE-2017-8890, CVE-2017-9074, CVE-2017-9075, CVE-2017-9076
    CVE-2017-9077 and CVE-2017-9242
- [feature] IPV6 netfilter NAT table support

* Fri May 26 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.30-1
- Added ENA driver for AMI
- Fix CVE-2017-7487 and CVE-2017-9059

* Wed May 17 2017 Vinay Kulkarni <kulkarniv@vmware.com> - 4.9.28-2
- Enable IPVLAN module.

* Tue May 16 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.28-1
- Version update

* Wed May 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.27-1
- Version update

* Sun May 7 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.26-1
- Version update
- Removed version suffix from config file name

* Thu Apr 27 2017 Bo Gan <ganb@vmware.com> - 4.9.24-2
- Support dynamic initrd generation

* Tue Apr 25 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.24-1
- Fix CVE-2017-6874 and CVE-2017-7618.
- Fix audit-devel BuildRequires.
- .config: build nvme and nvme-core in kernel.

* Mon Mar 6 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.13-2
- .config: NSX requirements for crypto and netfilter

* Tue Feb 28 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.13-1
- Update to linux-4.9.13 to fix CVE-2017-5986 and CVE-2017-6074

* Thu Feb 09 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.9-1
- Update to linux-4.9.9 to fix CVE-2016-10153, CVE-2017-5546,
    CVE-2017-5547, CVE-2017-5548 and CVE-2017-5576.
- .config: added CRYPTO_FIPS support.

* Tue Jan 10 2017 Alexey Makhalov <amakhalov@vmware.com> - 4.9.2-1
- Update to linux-4.9.2 to fix CVE-2016-10088
- Move linux-tools.spec to linux.spec as -tools subpackage

* Mon Dec 19 2016 Xiaolin Li <xiaolinl@vmware.com> - 4.9.0-2
- BuildRequires Linux-PAM-devel

* Mon Dec 12 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.9.0-1
- Update to linux-4.9.0
- Add paravirt stolen time accounting feature (from linux-esx),
    but disable it by default (no-vmw-sta cmdline parameter)

* Thu Dec  8 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.35-3
- net-packet-fix-race-condition-in-packet_set_ring.patch
    to fix CVE-2016-8655

* Wed Nov 30 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.35-2
- Expand `uname -r` with release number
- Check for build-id matching
- Added syscalls tracing support
- Compress modules

* Mon Nov 28 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.35-1
- Update to linux-4.4.35
- vfio-pci-fix-integer-overflows-bitmask-check.patch
    to fix CVE-2016-9083

* Tue Nov 22 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-4
- net-9p-vsock.patch

* Thu Nov 17 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-3
- tty-prevent-ldisc-drivers-from-re-using-stale-tty-fields.patch
    to fix CVE-2015-8964

* Tue Nov 15 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-2
- .config: add cgrup_hugetlb support
- .config: add netfilter_xt_{set,target_ct} support
- .config: add netfilter_xt_match_{cgroup,ipvs} support

* Thu Nov 10 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.31-1
- Update to linux-4.4.31

* Fri Oct 21 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.26-1
- Update to linux-4.4.26

* Wed Oct 19 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-6
- net-add-recursion-limit-to-GRO.patch
- scsi-arcmsr-buffer-overflow-in-arcmsr_iop_message_xfer.patch

* Tue Oct 18 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-5
- ipip-properly-mark-ipip-GRO-packets-as-encapsulated.patch
- tunnels-dont-apply-GRO-to-multiple-layers-of-encapsulation.patch

* Mon Oct  3 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-4
- Package vmlinux with PROGBITS sections in -debuginfo subpackage

* Tue Sep 27 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-3
- .config: CONFIG_IP_SET_HASH_{IPMARK,MAC}=m

* Tue Sep 20 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-2
- Add -release number for /boot/* files
- Use initrd.img with version and release number
- Rename -dev subpackage to -devel

* Wed Sep  7 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.20-1
- Update to linux-4.4.20
- apparmor-fix-oops-validate-buffer-size-in-apparmor_setprocattr.patch
- keys-fix-asn.1-indefinite-length-object-parsing.patch

* Thu Aug 25 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-11
- vmxnet3 patches to bumpup a version to 1.4.8.0

* Wed Aug 10 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-10
- Added VSOCK-Detach-QP-check-should-filter-out-non-matching-QPs.patch
- .config: pmem hotplug + ACPI NFIT support
- .config: enable EXPERT mode, disable UID16 syscalls

* Thu Jul 07 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-9
- .config: pmem + fs_dax support

* Fri Jun 17 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-8
- patch: e1000e-prevent-div-by-zero-if-TIMINCA-is-zero.patch
- .config: disable rt group scheduling - not supported by systemd

* Wed Jun 15 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.4.8-7
- fixed the capitalization for - System.map

* Thu May 26 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-6
- patch: REVERT-sched-fair-Beef-up-wake_wide.patch

* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> - 4.4.8-5
- GA - Bump release of all rpms

* Mon May 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.4.8-4
- Fixed generation of debug symbols for kernel modules & vmlinux.

* Mon May 23 2016 Divya Thaluru <dthaluru@vmware.com> - 4.4.8-3
- Added patches to fix CVE-2016-3134, CVE-2016-3135

* Wed May 18 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.4.8-2
- Enabled CONFIG_UPROBES in config as needed by ktap

* Wed May 04 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.4.8-1
- Update to linux-4.4.8
- Added net-Drivers-Vmxnet3-set-... patch

* Tue May 03 2016 Vinay Kulkarni <kulkarniv@vmware.com> - 4.2.0-27
- Compile Intel GigE and VMXNET3 as part of kernel.

* Thu Apr 28 2016 Nick Shi <nshi@vmware.com> - 4.2.0-26
- Compile cramfs.ko to allow mounting cramfs image

* Tue Apr 12 2016 Vinay Kulkarni <kulkarniv@vmware.com> - 4.2.0-25
- Revert network interface renaming disable in kernel.

* Tue Mar 29 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-24
- Support kmsg dumping to vmware.log on panic
- sunrpc: xs_bind uses ip_local_reserved_ports

* Mon Mar 28 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-23
- Enabled Regular stack protection in Linux kernel in config

* Thu Mar 17 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-22
- Restrict the permissions of the /boot/System.map-X file

* Fri Mar 04 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-21
- Patch: SUNRPC: Do not reuse srcport for TIME_WAIT socket.

* Wed Mar 02 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-20
- Patch: SUNRPC: Ensure that we wait for connections to complete
    before retrying

* Fri Feb 26 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-19
- Disable watchdog under VMware hypervisor.

* Thu Feb 25 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-18
- Added rpcsec_gss_krb5 and nfs_fscache

* Mon Feb 22 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-17
- Added sysctl param to control weighted_cpuload() behavior

* Thu Feb 18 2016 Divya Thaluru <dthaluru@vmware.com> - 4.2.0-16
- Disabling network renaming

* Sun Feb 14 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-15
- veth patch: don’t modify ip_summed

* Thu Feb 11 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-14
- Full tickless -> idle tickless + simple CPU time accounting
- SLUB -> SLAB
- Disable NUMA balancing
- Disable stack protector
- No build_forced no-CBs CPUs
- Disable Expert configuration mode
- Disable most of debug features from 'Kernel hacking'

* Mon Feb 08 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-13
- Double tcp_mem limits, patch is added.

* Wed Feb 03 2016 Anish Swaminathan <anishs@vmware.com> -  4.2.0-12
- Fixes for CVE-2015-7990/6937 and CVE-2015-8660.

* Tue Jan 26 2016 Anish Swaminathan <anishs@vmware.com> - 4.2.0-11
- Revert CONFIG_HZ=250

* Fri Jan 22 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-10
- Fix for CVE-2016-0728

* Wed Jan 13 2016 Alexey Makhalov <amakhalov@vmware.com> - 4.2.0-9
- CONFIG_HZ=250

* Tue Jan 12 2016 Mahmoud Bassiouny <mbassiouny@vmware.com> - 4.2.0-8
- Remove rootfstype from the kernel parameter.

* Mon Jan 04 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-7
- Disabled all the tracing options in kernel config.
- Disabled preempt.
- Disabled sched autogroup.

* Thu Dec 17 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-6
- Enabled kprobe for systemtap & disabled dynamic function tracing in config

* Fri Dec 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-5
- Added oprofile kernel driver sub-package.

* Fri Nov 13 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> - 4.2.0-4
- Change the linux image directory.

* Wed Nov 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-3
- Added the build essential files in the dev sub-package.

* Mon Nov 09 2015 Vinay Kulkarni <kulkarniv@vmware.com> - 4.2.0-2
- Enable Geneve module support for generic kernel.

* Fri Oct 23 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.2.0-1
- Upgraded the generic linux kernel to version 4.2.0 & and updated timer handling to full tickless mode.

* Tue Sep 22 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 4.0.9-5
- Added driver support for frame buffer devices and ACPI

* Wed Sep 2 2015 Alexey Makhalov <amakhalov@vmware.com> - 4.0.9-4
- Added mouse ps/2 module.

* Fri Aug 14 2015 Alexey Makhalov <amakhalov@vmware.com> - 4.0.9-3
- Use photon.cfg as a symlink.

* Thu Aug 13 2015 Alexey Makhalov <amakhalov@vmware.com> - 4.0.9-2
- Added environment file(photon.cfg) for grub.

* Wed Aug 12 2015 Sharath George <sharathg@vmware.com> - 4.0.9-1
- Upgrading kernel version.

* Wed Aug 12 2015 Alexey Makhalov <amakhalov@vmware.com> - 3.19.2-5
- Updated OVT to version 10.0.0.
- Rename -gpu-drivers to -drivers-gpu in accordance to directory structure.
- Added -sound package/

* Tue Aug 11 2015 Anish Swaminathan<anishs@vmware.com> - 3.19.2-4
- Removed Requires dependencies.

* Fri Jul 24 2015 Harish Udaiya Kumar <hudaiyakumar@gmail.com> - 3.19.2-3
- Updated the config file to include graphics drivers.

* Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> - 3.13.3-2
- Update according to UsrMove.

* Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> - 3.13.3-1
- Initial build. First version
