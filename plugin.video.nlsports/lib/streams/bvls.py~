from ..utils import bitly, xbmcutil
from . import veetle

sourceSite='http://www.bvls2013.com/'

def addStreams():
    pBar = xbmcutil.createProgressBar('NL Sports', 'Laden van streams...')


    xbmcutil.updateProgressBar(pBar, 9, 'Sport 1 - Select HD (Stream 1)')
    tmp = bitly.getLink('bvls-1', sourceSite)
    veetle.addChannel('Sport 1 - Select HD (Stream 1)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 18, 'Sport 1 - Voetbal (Stream 2)')
    tmp = bitly.getLink('bvls-2', sourceSite)
    veetle.addChannel('Sport 1 - Voetbal (Stream 2)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 27, 'Jupile Pro League (Stream 3)')
    tmp = bitly.getLink('bvls-3', sourceSite)
    veetle.addChannel('Jupile Pro League (Stream 3)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 36, 'Jupiler Pro League (Stream 4)')
    tmp = bitly.getLink('bvls-4', sourceSite)
    veetle.addChannel('Jupiler Pro League (Stream 4)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 45, 'Fox Sports 1 (Stream 5)')
    tmp = bitly.getLink('bvls-5', sourceSite)
    veetle.addChannel('Fox Sports 1 (Stream 5)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 54, 'Fox Sports 2 (Stream 6)')
    tmp = bitly.getLink('bvls-6', sourceSite)
    veetle.addChannel('Fox Sports 2 (Stream 6)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 63, 'Fox Sports 3 (Stream 7)')
    tmp = bitly.getLink('bvls-7', sourceSite)
    veetle.addChannel('Fox Sports 3 (Stream 7)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 72, 'Fox Sports 4 (Stream 8)')
    tmp = bitly.getLink('bvls-8', sourceSite)
    veetle.addChannel('Fox Sports 4 (Stream 8)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 81, 'Fox Sports 5 (Stream 9)')
    tmp = bitly.getLink('bvls-9', sourceSite)
    veetle.addChannel('Fox Sports 5 (Stream 9)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 90, 'Premier League (Stream 10)')
    tmp = bitly.getLink('bvls-10', sourceSite)
    veetle.addChannel('Premier League (Stream 10)', tmp, 'bvls')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
