%include spin-kickstarts/fedora-livecd-desktop.ks

#repo --name=fedora --baseurl=http://dl.fedoraproject.org/pub/fedora/linux/development/$releasever/$basearch/os/
repo --name=fedlet --baseurl=http://www.happyassassin.net/fedlet/repo/$basearch
#repo --name=koji --baseurl=http://kojipkgs.fedoraproject.org/repos/rawhide/latest/$basearch
repo --name=fusionfree --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
#repo --name=bleed --baseurl=http://kojipkgs.fedoraproject.org/mash/bleed/$basearch

bootloader --append="intel_pstate=disable video=800x1280@75"

%post
cat >> /etc/rc.d/init.d/livesys << EOF
# make the rotater show up
sed -i -e 's,libreoffice-writer.desktop,v8p-rotate.desktop,g' /usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override
# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas

rm -f /usr/share/applications/fedora-welcome.desktop
rm -f ~liveuser/.config/autostart/fedora-welcome.desktop
EOF
%end

%packages
monitor-edid
libva
libva-intel-driver
gstreamer1-vaapi
xorg-config-baytrail-800x1280
acpica-tools
libva-utils
intel-gpu-tools
dconf-editor
nano
generic-release
generic-release-rawhide
generic-logos
generic-release-notes
v8p-rotate
-gstreamer-plugins-ugly
-gstreamer1-plugins-ugly
-fedora-release
-fedora-release-rawhide
-fedora-logos
-fedora-release-notes
%end
