from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite="http://laatmijmaargaan.nl/"

def addStreams():
    pBar = xbmcutil.createProgressBar('NL Sports', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 24, 'LMMG - Stream 1')
    addStream('stream1', 'LaatMijMaarGaan - Stream 1')
    
    xbmcutil.updateProgressBar(pBar, 48, 'LMMG - Stream 2')
    addStream('stream2', 'LaatMijMaarGaan - Stream 2')
    
    xbmcutil.updateProgressBar(pBar, 72, 'LMMG - Stream 3')
    addStream('stream3', 'LaatMijMaarGaan - Stream 3')
    
    xbmcutil.updateProgressBar(pBar, 96, 'LMMG - Stream 4')
    addStream('stream4', 'LaatMijMaarGaan - Stream 4')
    
    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()

def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        veetle.addChannel(display, streamUrl, 'lmmg')
    else :
        if bitly.getResponse(streamUrl) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'lmmg','lmmg')


def findStream(page) :
    ua = bitly.getUserAgent()
    page1 = resolveIframe(sourceSite + '/' + page +'.html')
    page2 = resolveIframe(page1)
    print page2
    pagecontent = bitly.getPage(page2, sourceSite, ua)
    b64coded = bitly.getBaseEncodedString(pagecontent)
    print(b64coded)
    streamUrl = bitly.getStreamUrl(b64coded)
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page
        userAgent = bitly.getUserAgent()
        pagecontent = bitly.getPage(page, sourceSite, userAgent)
        regIframe = re.compile('<iframe(.*?)src="(.*?)"(.*?)><\/iframe>', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(2)
        return iframesrc
    except :
        return page

