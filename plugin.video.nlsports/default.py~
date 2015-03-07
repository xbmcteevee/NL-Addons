import sys, urllib2, urllib
import xbmcgui
import xbmcplugin, xbmcaddon
import urlparse
import paths

import socket, sys

from lib.streams import *
from lib.utils import *

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

pDialog = xbmcgui.DialogProgress()
_PERCENT_ = 0
progIncrease = 19

xbmcplugin.setContent(addon_handle, 'movies')

addon = xbmcaddon.Addon('plugin.video.nlsports')
newFeatures = addon.getSetting('newFeatures')

def addSubMenu(internal, readable):
    print 'adding ' + internal
    url = build_url({'site': internal})
    icon = xbmcutil.getIcon(internal)
    li = xbmcgui.ListItem(label=readable, iconImage=icon, thumbnailImage=icon)
    fanart = xbmcutil.getFanart(internal)
    li.setProperty('fanart_image',fanart)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

def mainMenu():
    addSubMenu('janlul', 'JanLul Streams')
    addSubMenu('daz','DazSports Streams')
    addSubMenu('stv','STV Streams')
    addSubMenu('13stream', '13th Stream')
    addSubMenu('bvls','BVLS Streams')
    #addSubMenu('lmmg','LMMG Streams')
    #addSubMenu('mdhzk','MDHZK Streams')
    addSubMenu('spst','Sports-streams')
    #if newFeatures == "true":
        #addSubMenu('hdstreams','HD Streams - [COLOR red]Unsupported[/COLOR]')
    addDummyItem('')
    addDummyItem('[COLOR yellow]Bedank de streamers, SMS: \'DONATE STREAM\' naar 7733 (E 3,00 p/b)[/COLOR]')
    addDummyItem('[COLOR green]Stream online[/COLOR]')
    addDummyItem('[COLOR red]Stream offline[/COLOR]')
    xbmcplugin.endOfDirectory(addon_handle)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)
    
def addDummyItem(labelString, icon=False, iconName = '', fanart=False, fanartName=''):
    if icon:
        iconimg = xbmcutil.getIcon(iconName)
        li = xbmcgui.ListItem(label=labelString, iconImage=iconimg, thumbnailImage=iconimg)
    else:
        li = xbmcgui.ListItem(label=labelString)

    li.setProperty('IsPlayable','false')
    if fanart:
        fanartimg = xbmcutil.getFanart(fanartName)
        li.setProperty('fanart_image',fanartimg)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url='plugin://plugin.video.nlsports/none', listitem=li)

argSite = args.get('site', None)
playUrl = args.get('play', None)
p2pMode = args.get('mode', None)
streamName = args.get('streamName', None)

if argSite is None:
    if playUrl is None :
        mainMenu()
    else :
        if p2pMode is not None :
            playUrl[0] = str(playUrl[0]) + "&mode=" + str(p2pMode[0])
        while xbmc.Player().isPlaying():
            xbmc.Player().stop()
            xbmc.sleep(5)
        pl=xbmc.PlayList(1)
        pl.clear()
        #credits = os.path.join(paths.videoDir, 'credits.mp4')
        #li = xbmcgui.ListItem('Credits')
        #li.setProperty('IsPlayable','true')
        #xbmc.PlayList(1).add(credits, li)
        li = xbmcgui.ListItem(str(streamName[0]))
        li.setProperty('IsPlayable', 'true')
        xbmc.PlayList(1).add(str(playUrl[0]), li)
        xbmc.Player().play(pl)
else:
    site = argSite[0]
    pDialog.create('NL Sports', 'Laden van streams...')
    if site == 'janlul': #Janlul.com
        janlul.addStreams()
    elif site == 'daz': #DazSports.org
        dazsports.addStreams()
    elif site == 'dsc': #DSCPlus.ord
        dscplus.addStreams()
    elif site == 'ads': #AchterdijnSports
        ads.addStreams()
    elif site == 'stv': #STV-Streams.com
        stv.addStreams()
    elif site == 'ctv':
        ctv.addStreams()
    elif site == 'lmmg': #LaatMijMaarGaan.nl
        lmmg.addStreams()
    elif site == 'mdhzk': #MooiDatHetZoKan.nl
        mdhzk.addStreams()
    elif site == 'spst': #sports-streams.com
        spst.addStreams()
    elif site == 'bvls': #bvls2013.com
        bvls.addStreams()
    elif site == '13stream':
        sopcast.add13Stream()
    elif site == 'hdstreams':
        sopcast.addStreams()
    else:
        mainMenu()

    xbmcplugin.endOfDirectory(addon_handle)
