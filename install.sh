#!/bin/sh
# Credit to mame82/p4wnp1

# get dir of pwd
wdir=$( cd $(dirname $BASH_SOURCE[0]) && pwd)


#update rpi
echo "Updating Raspberry Pi..."
sudo apt-get -y update
sudo apt-get -y upgrade

echo "Installing necessary packages..."
sudo apt-get -y install python-pip python-dev screen

echo "create udev rule for hid devices..."
echo 'SUBSYSTEM=="hidg",KERNEL=="hidg[0-9]", MODE="0666"' > /tmp/udevrule
sudo bash -c 'cat /tmp/udevrule > /lib/udev/rules.d/99-usb-hid.rules'

#create mass storage device
mkdir -p $wdir/USB_STORAGE
dd if=/dev/zero of=$wdir/USB_STORAGE/image.bin bs=1M count=128
mkdosfs $wdir/USB_STORAGE/image.bin

# create folder to store loot found
mkdir -p $wdir/collected

#create service for startup
if [ ! -f /etc/systemd/system/NaughtyKeyboard.service ]; then
           echo "Injecting startup script..."
        cat <<- EOF | sudo tee /etc/systemd/system/NaughtyKeyboard.service > /dev/null
                [Unit]
                Description= Startup Service
                #After=systemd-modules-load.service
                After=local-fs.target
                DefaultDependencies=no
                Before=sysinit.target
                [Service]
                #Type=oneshot
                Type=forking
                RemainAfterExit=yes
                ExecStart=/bin/bash $wdir/boot/boot_script.sh
                StandardOutput=journal+console
                StandardError=journal+console
                [Install]
                WantedBy=multi-user.target
                #WantedBy=sysinit.target
EOF
fi

sudo systemctl enable NaughtyKeyboard.service

#remove fsck from fstab
echo "Disabling FSCK on boot.."
sudo sed -i -E 's/[12]$/0/g' /etc/fstab

#autologin for user pi
echo "Enable autologin for user pi..."
sudo ln -fs /etc/systemd/system/autologin@.service /etc/systemd/system/getty.target.wants/getty@tty1.service


# setup USB gadget capable overlay FS
echo "Enable overlay filesystem for USB gadgedt suport..."
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules


# add libcomposite to /etc/modules
echo "Enable kernel module for USB Composite Device emulation..."
if [ ! -f /tmp/modules ]; then sudo touch /etc/modules; fi
sudo echo "libcomposite" | sudo tee -a /etc/modules

# Raspbian stretch with Kernel >= 4.9.78+ (working bluetooth, nexmon module compiled for this version)
sudo rpi-update 23a007716a0c6a8677097be859cf7063ae093d27


echo "Completed!"