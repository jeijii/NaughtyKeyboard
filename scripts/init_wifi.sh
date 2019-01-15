#!/bin/sh

systemctl stop hostapd
systemctl stop dnsmasq

cp /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.orig
cp /etc/dnsmasq.conf /etc/dnsmasq.conf.orig

cp /etc/default/hostapd /etc/default/hostapd.orig

cat <<- EOF > /etc/hostapd/hostapd.conf
	interface=uap0
ssid=SINGTEL-6969
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=P@ssw0rd
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOF

cat <<- EOF > /etc/dnsmasq.conf
        interface=lo,uap0
        no-dhcp-interface=lo,wlan0
        bind-interfaces
        server=8.8.8.8
        dhcp-range=172.24.0.2,172.24.0.100,12h
EOF

cat <<- EOF > /etc/network/interfaces.d/ap
        allow-hotplug uap0
        auto uap0
        iface uap0 inet static
        address 172.24.0.1
        netmask 255.255.255.0
EOF

cat <<- EOF > /etc/udev/rules.d/90-wireless.rules
        ACTION=="add", SUBSYSTEM=="ieee80211", KERNEL=="phy0", \
        RUN+="/sbin/iw phy %k interface add uap0 type __ap"
EOF

cat <<- EOF > /etc/default/hostapd
        DAEMON_CONF="/etc/hostapd/hostapd.conf"
EOF


echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -s 172.24.0.0/24 ! -d 172.24.0.0/24 -j MASQUERADE
iptables-save > /etc/iptables/rules.v4
