# OSMC-Snapcast

This OSMC Snapcast RPi addons bring now the possibility to let run both, Snapserver and Snapclient, independent or together serving audio from Kodi Source.
For now the Snapserver is limited to serve only Kodi audio trough ALSA loopback device.
Mainly the ideas for this addons including code fragments comes from Team LibreELEC (https://libreelec.tv)

[![Platform](https://img.shields.io/badge/platform-OSMC-informational)](https://osmc.tv/) [![Platform](https://img.shields.io/badge/platform-Kodi-informational)](https://kodi.tv/)

## Example

Will come soon

## ToDo

A lot of improvements needed

## Installation

Copy addon folder to your Raspberry Pi OSMC Kodi addon folder. Make adjustments to addon settings.
You should create a system service for Snapserver and Snapclient.
Example files are in system.d folder `service.snapserver.service` and `service.snapclient.service`