#!/bin/sh

cat <<- EOF > /tmp/hostapd.conf
		# This is the name of the WiFi interface we configured above
		interface=wlan0
		# Use the nl80211 driver with the brcmfmac driver
		driver=nl80211
		# This is the name of the network
		ssid=SINGTEL-6969
		# Use the 2.4GHz band
		hw_mode=g
		# Use channel 6
		channel= 6
		# Enable 802.11n
		ieee80211n=1
		# Enable WMM
		wmm_enabled=1
		# Enable 40MHz channels with 20ns guard interval
		ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]
		# Accept all MAC addresses
		macaddr_acl=0

		# Use WPA authentication
		auth_algs=1
		# Use WPA2
		wpa=2
		# Use a pre-shared key
		wpa_key_mgmt=WPA-PSK
		# The network passphrase
		wpa_passphrase=P@ssw0rd
		# Use AES, instead of TKIP
		rsn_pairwise=CCMP
EOF

cat <<- EOF > /tmp/dnsmasq_wifi.conf
		interface=wlan0      # Use the require wireless interface - usually wlan0
        dhcp-range=192.168.0.2,192.168.0.20,255.255.255.0,24h
EOF

hostapd -d /tmp/hostapd.conf > /tmp/hostapd.log &
dnsmasq -C /tmp/dnsmasq_wifi.conf
ifconfig wlan0 192.168.0.1 netmask 255.255.255.0
