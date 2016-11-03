## Fedberry

Some information about Fedberry are [here](https://github.com/fedberry/fedberry#important-information).

I used Fedberry 23, now is avaliable version 24. When i tested 23 the Fedberry 24 was in Beta so i decided for stable version.

After the initial OS boot, please set the timezone, root password and create users when prompted at initial setup.

The Fedberry was a little complicated system for me, because i have never work with this kind of system before.
Package system is different from Raspbian and Ubuntu. For installing packages, tools etc. is used **dnf**.

When you succesfully boot in system run terminal and enter these commands:
```
sudo dnf install binutills
sudo dnf install update
``` 
After update the Fedberry should have python packages so you can install picamera and pushetta:
```
pip install picamera
pip install pushetta
``` 
Pushetta is program for sending notifications on your smartphone in real-time, for free. I used this program in Raspbian too, but in Ubuntu it's not possible. Pushetta is not supported in Ubuntu Mate.

Enable Pi Camera: type `nano /boot/config.txt` and change line at "Cammera Settings" from `##start_x=1` to `start_x=1`, then you should be able to use camera module.

If commands like `iwconfig, iwlist, ifconfig` are not found, than their packages are not installed.

Fixed it by type these commands
```
sudo dnf install net-tools
sudo dnf install wireless tools
```

## Wi-Fi

For install driver find type of your adapter by `lsusb`

`Bus 001 Device 004: ID 0bda:8179 Realtek Semiconductor Corp. RTL8188EUS 802.11n Wireless Network Adapter`

Then download it from github, extract it and install it
```
 wget https://github.com/lwfinger/rtl8188eu/archive/master.zip
 unzip master.zip
 make all
 sudo make install
```
Now reboot your machine and Wi-Fi should works fine.

If you want static IP address (its better because you dont have spend some time for looking what address RPi gets)
configurate wireless interface:

Open **ifcfg** (Interface configuration file) by `sudo nano /etc/sysconfig/network-skripts/ifcfg-wlan0`
then add this at the end of file:
```
 PREFIX=24
 IPADDR=192.168.0.108
 GATEWAY=192.168.0.1
 BOOTPROTO= none
```
After next reboot, boot system you should get your address.

### Known issues

When you install Wi-Fi driver you can get error about that **make didnt work**. It can be that you compiled different version of kernel then your system has (example: I compiled version of kernel 4.0.10 and my system kernel version is 4.2.10)

You can fix this:
```
 uname -r
 yum install kernel-devel-3.9.5-301.fc23.x86_64
 yum install kernel-headers-3.9.5-301.fc23.x86_64
 yum install gcc
```
First find your kernel version, then install kernel devel with that kernel version and then do it same with kernel headers. And last install gcc, that can be missing.
After this it should works.

Second problem can be that you cant download anything and you get **unable to resolve host address**. This happens when you dont have nameserver in file **resolv.conf**

So just add some nameservers to this file:
```
sudo nano /etc/resolv.conf
nameserver 8.8.8.8
nameserver 192.168.0.1
```
Thats all.
