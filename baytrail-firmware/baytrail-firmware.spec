Name:       baytrail-firmware
Version:    1.1
Release:    1awb
Summary:    Not-yet-upstreamed firmwares for Baytrail devices

Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://github.com/qca/ath6kl-firmware
Source0:    ath6kl-firmware-2e02576c1da.tar.xz
BuildArch:  noarch

Requires: linux-firmware

%description
This package contains firmwares needed for Baytrail devices which are not
currently upstreamed. Currently contains API 5 firmwares for AR6004 (ath6kl)
wireless adapters.

%prep
%setup -q -n ath6kl-firmware

%build

%install
mkdir -p %{buildroot}/usr/lib/firmware/ath6k/AR6004/hw1.3
cp -aR ath6k/AR6004/hw3.0 %{buildroot}/usr/lib/firmware/ath6k/AR6004
install -m 0644 ath6k/AR6004/hw1.3/fw-5.bin %{buildroot}/usr/lib/firmware/ath6k/AR6004/hw1.3


%files
%doc LICENSE.qca_firmware
/usr/lib/firmware/ath6k/AR6004/hw3.0
/usr/lib/firmware/ath6k/AR6004/hw1.3/fw-5.bin

%changelog
* Thu Sep 11 2014 Adam Williamson <awilliam@redhat.com> - 1.1-1
- drop audio firmware (upstreamed), instead package ath6kl wireless firmware

* Wed Feb 26 2014 Adam Williamson <awilliam@redhat.com> - 1.0-1
- initial package (sound firmware, for private use only)
