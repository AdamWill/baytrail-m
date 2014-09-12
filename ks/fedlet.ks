# the 'base' image we're modifying - your copy may be elsewhere, of course
%include spin-kickstarts/fedora-live-workstation.ks

# if you particularly need your rawhide repo to be bang up-to-date you may
# want to uncomment this, it forces use of the primary mirror; but that's
# kind of rude, of course, so don't do it unless you have a good reason
#repo --name=fedora --baseurl=http://dl.fedoraproject.org/pub/fedora/linux/development/$releasever/$basearch/os/

# this is the fedlet repo
repo --name=fedlet --baseurl=http://www.happyassassin.net/fedlet/repo/$basearch

# this contains the very very latest rawhide builds as they come out of the
# build system, it has limited capacity, please don't use it unless absolutely
# necessary
#repo --name=koji --baseurl=http://kojipkgs.fedoraproject.org/repos/rawhide/latest/$basearch

# when we're in freezes, this is the side repo where releng puts blocker /
# freeze exception fixes so they can be pulled 'through the freeze' into the
# composes
repo --name=bleed --baseurl=http://kojipkgs.fedoraproject.org/mash/bleed/$basearch

%post
cat >> /etc/rc.d/init.d/livesys << EOF
# make the rotater show up
sed -i -e "s/'libreoffice-writer.desktop'/'v8p-rotate.desktop', 'gnome-terminal.desktop'/g" /usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override
# rebuild schema cache with any overrides we installed
glib-compile-schemas /usr/share/glib-2.0/schemas

# drop the welcome screen as it's branded (and I don't really want to
# advertise installation)
rm -f /usr/share/applications/fedora-welcome.desktop
rm -f ~liveuser/.config/autostart/fedora-welcome.desktop
EOF
%end

%packages

# handy debugging / configuration tools
acpica-tools
dconf-editor
evtest
gnome-tweak-tool
intel-gpu-tools
monitor-edid
rfkill

# video playback acceleration (needs libva-driver-intel from Some Other Place to actually work)
libva
gstreamer1-vaapi
libva-utils

# firmwares for fedlet-y hardware
baytrail-firmware

# fedlet-specific config-y things and tools
v8p-rotate

# fedlet repo stuff
fedlet-repo

# i'm building this image and I like these things, damnit
nano
htop

# we don't really need this for tablets
-@libreoffice

# debranding
firewalld-config-standard
generic-logos
generic-release
generic-release-notes
-fedora-logos
-fedora-release*
-fedora-repos*
-firewalld-config-workstation

%end
