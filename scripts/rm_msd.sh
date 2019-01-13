#!/bin/sh

cd /sys/kernel/config/usb_gadget

rm -rf functions/mass_storage.usb0

#reset udc then connect
echo > UDC
ls /sys/class/udc > UDC