# OSMC Snapcast for Raspberry Pi

This OSMC Snapcast addons bringing now the possibility to let run both, Snapserver and Snapclient, independent or together on Raspberry Pi.

For now Snapserver is limited to serve only Kodi audio through ALSA loopback device.
For now Snapclient is only available for people with no need for pulseaudio support.

I know that Kodi v.19 is available now and OSMC is going to change soon to it but as long this is not the case i'm using this on my official OSMC Release with Kodi v.18.
Maybe one sunny day i will change my systems to LibreELEC for example or go further with OSMC. But for now i'm stuck on my nice running old OSMC. :-D

Base Snapcast binaries are of course from the main developer Johannes Pohl [(badaix)](https://github.com/badaix).
Mainly the ideas to create this addons including code fragments comes from Anton Voyl [(awiouy)](https://github.com/awiouy) for Team LibreELEC (https://libreelec.tv)

[![Platform](https://img.shields.io/badge/platform-OSMC-informational)](https://osmc.tv/) [![Platform](https://img.shields.io/badge/platform-Kodi-informational)](https://kodi.tv/)

## ToDo

A lot of improvements needed. Addons are still in development status. Feel free to report me back issues or improvements. Or if you familiar with coding and Git adjust the code and make a pull request.

## Update

#### 2021-06-20
- Initial commit with corrected addon structure
- Snapclient and Snapserver v0.25.0

#### Before 2021-06-20
- Adjusted Snapclient locally to hear mopidy snapserver multiroom audio on Kodi
- No Git commits since established

## Installation

Currently there is no Kodi package installation routine. Therefore, some adjustments have to be made directly.

All required system packages should already be installed by default (please correct me if i'm wrong).
No further customization should be necessary. Except in case of special sound card configuration.

Copy the addons individually or together into your Raspberry Pi OSMC Kodi addon folder using your preferred method.

You can also clone the Git repository to Kodi, but make sure you also have Git installed or already present in the system.
Afterwards check addons on filesystem level if user, group and permissions are correctly set.

Log into your OSMC commandline.

Make script and binary executable:
````sh
cd ~/.kodi/addons/script.service.snapclient/resources/bin/
chmod +x ./snapclient*
````
Same for Snapserver if you want to use it. Just replace all occurences of `snapclient` to `snapserver` from code above.
````sh
cd ~/.kodi/addons/script.service.snapserver/resources/bin/
chmod +x ./snapserver*
````

### System service

You should create a system service for Snapserver and Snapclient.
Example files are in system.d folder `service.snapserver.service` and `service.snapclient.service`

Add a Snapclient system service started at boot:

````sh
cd ~/.kodi/addons/script.service.snapclient/system.d/

sudo cp service.snapclient.service /usr/lib/systemd/system/snapclient.service

cd /usr/lib/systemd/system

sudo systemctl enable snapclient
sudo systemctl status snapclient
sudo systemctl start snapclient
````

Add a Snapserver system service too:

````sh
cd ~/.kodi/addons/script.service.snapserver/system.d/

sudo cp service.snapserver.service /usr/lib/systemd/system/snapserver.service

cd /usr/lib/systemd/system

sudo systemctl enable snapserver
sudo systemctl status snapserver
sudo systemctl start snapserver
````

## Usage

Make adjustments inside Kodi addon settings (TV screen or whatever you use for Kodi addon management).

Snapclient should play stream from remote server:
- Setup Snapclient server host IP address to your remote Snapserver
- Give your client a unique host ID


Snapclient should play stream from local Snapserver e.g. for Kodi:
- Enable Snapserver in addon settings
- Setup Snapclient server host IP address to 127.0.0.1
- Give your Snapclient a unique host ID
- Set switch for stopping Snapclient if Kodi is playing to disabled
- In Kodi system settings set audio output to Loopback device
- Everything else should work now out of the box
- Play with latency time of Snapclient in case you have asynchronized video/audio

## Credits
- Many thx to [(badaix)](https://github.com/badaix) for the great [Snapcast](https://github.com/badaix/snapcast) system to inspire me to make a old-fashioned OSMC addon from it.
- Special thx to Anton Voyl [(awiouy)](https://github.com/awiouy) for his great work to support Snapcast on LibreELEC Kodi. I reused ;-) a lot of code from him.
- For LibreELEC reference look at [Snapserver](https://github.com/LibreELEC/LibreELEC.tv/tree/master/packages/addons/service/snapserver) and [Snapclient](https://github.com/LibreELEC/LibreELEC.tv/tree/master/packages/addons/service/snapclient)
