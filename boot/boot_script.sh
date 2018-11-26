#!/bin/sh

# find working dir of script
wdir=$( cd $(dirname $BASH_SOURCE[0]) && cd .. && pwd)

GADGETS_DIR=keyboard_gadget"

cd /sys/kernel/config/usb_gadget
	mkdir -p $GADGETS_DIR
	cd $GADGETS_DIR

# configure gadget details
# =========================
# set Vendor ID
echo 0x1d6b > idVendor
#echo $USB_VID > idVendor
echo 0x0104 > idProduct
#echo $USB_PID > idProduct
# set device version 1.0.0
echo 0x0100 > bcdDevice
# set USB mode to USB 2.0
echo 0x0200 > bcdUSB

#composite class / subclass / proto (needs single configuration)
echo 0xEF > bDeviceClass
echo 0x02 > bDeviceSubClass
echo 0x01 > bDeviceProtocol

# set device descriptions
mkdir -p strings/0x409 # English language strings
# set serial
echo "696969" > strings/0x409/serialnumber
# set manufacturer
echo "HP" > strings/0x409/manufacturer
# set product
echo "JZ's Keyboard" > strings/0x409/product

mkdir -p functions/hid.g1
		PATH_HID_KEYBOARD="/sys/kernel/config/usb_gadget/$GADGETS_DIR/functions/hid.g1/dev"
		echo 1 > functions/hid.g1/protocol
		echo 1 > functions/hid.g1/subclass
		echo 8 > functions/hid.g1/report_length
cat $wdir/conf/report_desc > functions/hid.g1/report_desc
ln -s functions/hid.g1 configs/c.1/