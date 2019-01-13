#!/bin/sh

# find working dir of script
wdir=$( cd $(dirname $BASH_SOURCE[0]) && cd .. && pwd)

GADGETS_DIR="keyboard_gadget"

cd /sys/kernel/config/usb_gadget

#thumbdrive
mkdir -p functions/mass_storage.usb0
echo 1 > functions/mass_storage.usb0/stall # allow bulk EPs
echo 0 > functions/mass_storage.usb0/lun.0/cdrom # don't emulate CD-ROm
echo 0 > functions/mass_storage.usb0/lun.0/ro # write access
echo 0 > functions/mass_storage.usbcd0/lun.0/nofua
echo $wdir/USB_STORAGE/image.bin > functions/mass_storage.usb0/lun.0/file
ln -s functions/mass_storage.usb0 configs/c.1/

#reset udc then connect
echo > UDC
ls /sys/class/udc > UDC