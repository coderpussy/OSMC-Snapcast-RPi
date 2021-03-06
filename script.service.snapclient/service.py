################################################################################
#      Original form LibreELEC - https://libreelec.tv
################################################################################

import subprocess
import xbmc
import xbmcaddon


def systemctl(command):
    subprocess.call(['systemctl', command, 'snapclient.service'])


class Monitor(xbmc.Monitor):

    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)
        self.player = Player()

    def onSettingsChanged(self):
        self.player.start('restart')


class Player(xbmc.Player):

    def __init__(self):
        super(Player, self).__init__(self)
        self.start('start')

    def onPlayBackEnded(self):
        if xbmcaddon.Addon().getSetting('sc_stop_if_kodi_play') == 'true':
            xbmc.sleep(500)
            if not self.isPlaying():
                systemctl('start')

    def onPlayBackStarted(self):
        if xbmcaddon.Addon().getSetting('sc_stop_if_kodi_play') == 'true':
            systemctl('stop')

    def onPlayBackStopped(self):
        if xbmcaddon.Addon().getSetting('sc_stop_if_kodi_play') == 'true':
            systemctl('start')

    #def onPlayBackPaused():
        #xbmc.log("Snapcast event onPlayBackPaused!", level=xbmc.LOGNOTICE)

    #def onPlayBackResumed():
        #xbmc.log("Snapcast event onPlayBackResumed!", level=xbmc.LOGNOTICE)

    def start(self, command):
        if xbmcaddon.Addon().getSetting('sc_stop_if_kodi_play') == 'true':
            if self.isPlaying():
                systemctl('stop')
            else:
                systemctl(command)
        else:
            systemctl(command)


if __name__ == '__main__':
    Monitor().waitForAbort()
