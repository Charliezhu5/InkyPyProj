Introduction:
	Inky pHAT red version attached to Raspberry Pi Zero WH(shortened as rpi0) running in Raspbian OS.
	Inky pHAT(shortened as Ip) is a great low consumption high resolution e ink display, powered by rpi0 thus make it a very versatile display. Since it's controlled by python3 library Inky(provided by manufacture), it is extremely easy to control what is displayed on the screen. You can literally run your imagination wild to utilize this small gizmo.
	The fun is unlimited at your disposal, just make sure you don't destroy it by putting it in water or microwave, otherwise this is a pretty sturdy gadget that should live throughout the future of Milky Way! Of course, there is no warranty associated with this DIY-for-fun product. You will be using it at your own risk, if you try to modify it into a killing machine or sort.

How does it work?
	This small gadget has two hardware components. The Ip and rpi0, both are physically connected by serial pins called GPIO, it is a universal connection for Pi family, which is also capable of transferring data used to control whatever is connected. The Ip itself is manufactured by Pimoroni, more information can be found on their website https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat you don't need to thank me for putting the work of copying the URL.
	As for rpi0, it's famous for its small dimension and super low cost at only 5 USD each. It is powered by micro USB cable at 5V and recommended 1.2A, usually it's fine to power it with your laptop. This rpi0 is connected to Bluetooth and/or 2.4GHz Wifi, so you can control it with your phone, tablet and computer.
	The gadget is pre-installed with necessary softwares, including Raspbian OS, python and packages. Basically setup and go. Since it's running on rpi0, a not so powerful computer, please be easy on her. That is to say, she is NOT CAPABLE OF running your machine learning code! But however you would like to play with her.

TL;DR
	rpi0 eats usb power, rpi0 spit image to GPIO. Ip take spits from GPIO and shows funny picture. Python tells rpi0 how when what to spit.

Quick Setup:
	Although ideally, the assembly will be plug-n-play, but you still need to set it up to function properly. Please follow these steps:
	1. Plug SD card into your computer, in the boot drive, there is a wpa_supplicant.conf file, open it with any text editor.
	2. Find ssid and password, change them to your home netword setting, the rpi0 only connects to 2.4GHz wifi.
	3. Plug SD card back to rpi0, power it on by pluging in usb cable.
	4. After a while, check your router's page, and look for a device named RaspberryPi, note its ip address, like 192.168.x.x(remember this address, it is important)
	5. Open up PowerShell(windows) or Terminal(Mac) then ssh into the rpi0, username and password below. & ssh pi@192.168.x.x
	6. Once logged into rpi0 as user pi, run this command $ InkyPyProj/startServer.sh
	7. Now your rpi0 will be configurable by http request, please see usage instruction for details.

Updates:
	1. The software and python files are from this Git repo, https://github.com/Charliezhu5/InkyPyProj. All changes will be updated on the repo.
	2. In the rpi0, I put a shell command to update from the repo, you can run $ sudo /home/pi/InkyPyProj/update.sh
	3. DO NOT make changes to local files, it will cause git conflict to prevent you from future updates. I haven't setup it in a proper way yet.
	4. If you want to make changes to the files and controll the Ip in your own way, you can fork or create your own repo.

Usage Instruction:
	At this point after you finished Quick Setup, the http server will be running, you can use any browser to send requests to the assembly by entering in address bar.
	a. enter address 192.168.x.x:5000/logo will tell the Ip to show a deault image. It takes about 10 s to finish.


Full Setting Up(Optional):
	The assembly is already setup and go, all files are stored in the attached SD card. Should you need to setup everything ground up again, please follow these steps:
	1. Get a SD card, download Raspberry Pi Imager from Raspberry website.
	2. Use the Imager, select Raspbian OS Lite version, and prepare the SD card.
	3. Setup headless start following these steps:
		a.
		b.
		c.
	4. SSH into the rpi0, take control.
	5. Install important Inky library, you can run the bash file from their website by running this command & curl https://get.pimoroni.com/inky | bash
	6. After selecting yes and few minutes, the hardware part setup is done, and you should be able to follow the tutorial from Pimoroni https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
	7. Install python Flask, $ sudo pip3 install Flask
	8. Git clone from this repo for latest files.
	9. ??? it's yours now.

Important installed packages:
	1. Inky, the python library for pi zero to control inky display.
	2. Flask, a python library to handle Http requests for configuration on the go.

Linux user:
	1. Username(super user): pi
	   paswd: SuperStrongPassword

File path:
	1. All python codes are here: /home/pi/Pimoroni

Routes:
	1. "/" main route, return Hello world message.
	2. "/clean" start a clean screen cycle to clear Ip of ghost image. Takes 30s. Return success message.
	3. "/logo" set Ip to display default logo image. Takes 20s. Return success message.
	4. "/namebadge/{Name}" change {Name} to whatever you like, and the Ip will display that name as a name badge. Takes 10s, and return success message.
