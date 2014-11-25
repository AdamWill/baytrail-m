Name:       baytrail-firmware
Version:    1.2
Release:    1awb
Summary:    Not-yet-upstreamed firmwares for Baytrail devices

Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://github.com/qca/ath6kl-firmware
Source0:    ath6kl-firmware-2e02576c1da.tar.xz
# From 'Asus T100 Linux&Ubuntu' Google Drive, General Files / Patches & firmware
# / Wifi Firmware / Brainwreck / wifi test . Thanks to Brainwreck. This is
# intended for and tested on the Asus T100, it may not be appropriate for any
# other Baytrail devices that use the same wifi chipset. See
# http://comments.gmane.org/gmane.linux.kernel.wireless.general/119700
# and http://wireless.kernel.org/en/users/Drivers/brcm80211
# for background.
Source1:    brcmfmac43241b4-sdio.txt.brainwreck.20140822
BuildArch:  noarch

Requires: linux-firmware

%description
This package contains firmwares needed for Baytrail devices which are not
currently upstreamed. Currently contains API 5 firmwares for AR6004 (ath6kl)
wireless adapters and a Broadcom NVRAM map file for the Asus T100.

%prep
%setup -q -n ath6kl-firmware

%build

%install
mkdir -p %{buildroot}/usr/lib/firmware/ath6k/AR6004/hw1.3
cp -aR ath6k/AR6004/hw3.0 %{buildroot}/usr/lib/firmware/ath6k/AR6004
install -m 0644 ath6k/AR6004/hw1.3/fw-5.bin %{buildroot}/usr/lib/firmware/ath6k/AR6004/hw1.3
mkdir -p %{buildroot}/usr/lib/firmware/brcm
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/firmware/brcm/brcmfmac43241b4-sdio.txt


%files
%doc LICENSE.qca_firmware
/usr/lib/firmware/ath6k/AR6004/hw3.0
/usr/lib/firmware/ath6k/AR6004/hw1.3/fw-5.bin
/usr/lib/firmware/brcm/brcmfmac43241b4-sdio.txt

%changelog
* Sat Nov 22 2014 Adam Williamson <awilliam@redhat.com> - 1.2-1
- add a Broadcom NVRAM map appropriate for Asus T100

* Thu Sep 11 2014 Adam Williamson <awilliam@redhat.com> - 1.1-1
- drop audio firmware (upstreamed), instead package ath6kl wireless firmware

* Wed Feb 26 2014 Adam Williamson <awilliam@redhat.com> - 1.0-1
- initial package (sound firmware, for private use only)
