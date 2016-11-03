## Raspbian

I used Raspbian version 7 type Wheezy with kernel xxxx. The system was pre installed on card so i didnt have to download it from Raspbian website.
You will need keyboard, hdmi cabel, monitor. 

### First boot
After first boot the installation guide will be started, you have to set your Location, Timezone. Use TAB and arrows keys for navigation and the Space key for select or deselect. in terminal type **startx** at command prompt to start the graphical desktop.

There is predefined user **pi** with password **raspberry**.

Commands are same like in Debian or Ubuntu. 

Basic command for update, upgrade is 
**sudo apt-get update; sudo apt-get upgrade** 

Other important commands for my thesis are:

```python
sudo apt-get install python-picamera
sudo raspi-config
```
First is needed for python library picamera.
Second is for enabling Pi Camera in Raspberry config.
