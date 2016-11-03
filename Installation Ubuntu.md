## Ubuntu MATE

Version of used system is 16.04 with kernel 4.4.8-v7+. For installation is needed minimum 8GB SD card. After installation file system can be resized to occupy the unallocated space of the microSD card.
There is no predefined user account. When you first boot it will run through a setup wizard and you will be able to create your own accout and set timezone, location

### Re-size file system

You can use Ubuntu MATE Welcome to resize automaticaly by clicking the **Resize** button.

Or you can do it manually 
```python
sudo fdisk /dev/mmcblk0
```
Delete the second partition (d, 2), then re-create it using the defaults (n, p, 2, enter, enter), then write and exit (w). Reboot the system, then:
```
sudo resize2fs /dev/mmcblk0p2
```
More on [MATE](https://ubuntu-mate.org/raspberry-pi/).

### Wi-Fi

You have to download correct driver, in my case (TL-WN725N). 

First find your kernel version:
`uname -a` and we get `Linux raspberrypi 4.4.8-v7+ #881 SMP Sat Apr 30 12:16:50 BST 2016 armv7l GNU/Linux

So now when we know kernel version we can download the driver.
```
 wget https://dl.dropboxusercontent.com/u/80256631/8188eu-4.4.8-v7-881.tar.gz 
 tar xzf 8188eu-4.4.8-v7-881.tar.gz  #(-x --extract –z –gzip –f --file)
 ./install.sh
```
After this the Wi-Fi should work.

And again you have to enable Pi Camera, but there is not `raspi-config` so just type:
```
sudo nano /boot/config.txt
```
And find line "Camera Settings" and change line from `##start_x=1` to this `start_x=1`

When you do this save file and reboot Raspberry.

Now you can use system and dont forget for install python library of picamera.

`sudo apt-get install python-picamera`
