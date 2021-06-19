# OSMC Snapcast for Raspberry Pi

This OSMC Snapcast addons bringing now the possibility to let run both, Snapserver and Snapclient, independent or together on Raspberry Pi.

For now Snapserver is limited to serve only Kodi audio through ALSA loopback device.
For now Snapclient is only available for people with no need for pulseaudio support.

Base Snapcast binaries are of course from the main developer Johannes Pohl [(badaix)](https://github.com/badaix).
Mainly the ideas for this addons including code fragments comes from Team LibreELEC (https://libreelec.tv)

[![Platform](https://img.shields.io/badge/platform-OSMC-informational)](https://osmc.tv/) [![Platform](https://img.shields.io/badge/platform-Kodi-informational)](https://kodi.tv/)

## ToDo

A lot of improvements needed. Addons are still in development status.

## Installation

Currently there is no Kodi package installation routine. Therefore, some adjustments have to be made directly.

All required system packages should already be installed by default (please correct me if i'm wrong).
No further customization should be necessary. Except in case of special sound card configuration.

Copy the addons individually or together into your Raspberry Pi OSMC Kodi addon folder using your preferred method.

You can also clone the Git repository to Kodi, but make sure you also have Git installed or already present in the system.
Afterwards check if addon on filesystem level if user, group and permissions are correctly set.

Log into your OSMC commandline.

Make script and binary executable:
````sh
cd ~/.kodi/addons/script.service.snapclient/resources/bin/
chmod +x ./snapclient*
````
Same for Snapserver if you want to use it. Just replace all occurences of `snapclient` to `snapserver` from code above.

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
sudo systemctl status snapclient
sudo systemctl start snapclient
````

## Usage

Make adjustments inside Kodi addon settings (TV screen or whatever you use for Kodi addon management).

Snapclient should play stream from remote server:
- Setup Snapclient server host IP address to your remote Snapserver
- Give your client a unique host ID


Snapclient should play stream from local Snapserver:
- Enable Snapserver in addon settings
- Setup Snapclient server host IP address to 127.0.0.1
- Give your client a unique host ID
- Set switch for stopping Snapclient if Kodi is playing to disabled
- Everything else should work now out of the box
- Play with latency time of Snapclient in case you have asynchronized video/audio

## Credits
- Many thx to [(badaix)](https://github.com/badaix) for the great [Snapcast](https://github.com/badaix/snapcast) system to inspire me to make a old-fashioned OSMC addon from it.
- Special thx to Anton Voyl [awiouy](https://github.com/awiouy) for his great work to support Snapcast on LibreELEC Kodi. I stole a lot of code from him.
- For LibreELEC reference look at [Snapserver](https://github.com/LibreELEC/LibreELEC.tv/tree/master/packages/addons/service/snapserver) and [Snapclient](https://github.com/LibreELEC/LibreELEC.tv/tree/master/packages/addons/service/snapclient)
