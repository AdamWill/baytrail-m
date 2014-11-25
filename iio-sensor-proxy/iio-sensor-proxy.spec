%global commit 748176bceec7d9371ff8fa511cd2e9d9a3f709a6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           iio-sensor-proxy
Version:        0
Release:        0.3.git%{shortcommit}%{?dist}
Summary:        IIO accelerometer sensor to input device proxy
Source0:        https://github.com/hadess/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
# From Jan-Michael Brummer: fix compilation (tries to set wrong variable)
Patch0:         0001-main-Fix-compiling-issues-in-buffered-accelerometer.patch
# From Jan-Michael Brummer: fix skip of scan processing if no new data
Patch1:         0004-main-Skip-process_scan-in-case-we-are-receiving-EGAI.patch
URL:            https://github.com/hadess/iio-sensor-proxy
License:        GPLv2+
Group:          User Interface/X Hardware Support

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
# For RPM macros
BuildRequires:  systemd
# Build uses GNOME_COMPILE_WARNINGS
BuildRequires:  gnome-common

Requires:       systemd

%description
IIO accelerometer sensor to input device proxy. This allows accelerometer
data to be read as if from an X input device, allowing desktop enviroments
and possibly other things to use accelerometer data, for example, for
detecting rotation of tablet devices.

%prep
%setup -q -n %{name}-%{commit}
autoreconf -i
%patch0 -p1
%patch1 -p1
%configure

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_presetdir}
# Upstream hardcodes /lib/udev/rules.d , but this is really the right place...
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}/lib/udev/rules.d/* %{buildroot}%{_udevrulesdir}

%clean
rm -rf %{buildroot}

%post
%systemd_post iio-sensor-proxy.service

%preun
%systemd_preun iio-sensor-proxy.service

%postun
%systemd_postun_with_restart iio-sensor-proxy.service

%files
%doc README.md
%{_udevrulesdir}/40-iio-sensor-proxy.rules
%{_unitdir}/iio-sensor-proxy.service
%{_sbindir}/iio-sensor-proxy

%changelog
* Mon Nov 24 2014 Adam Williamson <awilliam@redhat.com> - 0-0.3.git748176b
- new upstream snapshot
- various fixes from Jan-Michael Brummer

* Sat Nov 22 2014 Adam Williamson <awilliam@redhat.com> - 0-0.2.git4a5fb99
- drop the preset (loading is done via udev)

* Sat Nov 22 2014 Adam Williamson <awilliam@redhat.com> - 0-0.1.git4a5fb99
- initial package
