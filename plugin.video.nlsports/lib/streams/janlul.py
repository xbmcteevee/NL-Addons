from ..utils import bitly, xbmcutil
from . import veetle
import re

sourceSite = 'http://www.janlul.com'

def addStreams() :
    pBar = xbmcutil.createProgressBar('NL Sports', 'Laden van Streams...')

    xbmcutil.updateProgressBar(pBar, 12, 'JanLul.com - stream 1')
    addStream('stream1', 'JanLul.com - Stream 1')

    xbmcutil.updateProgressBar(pBar, 24, 'JanLul.com - stream 2')
    addStream('stream2', 'JanLul.com - Stream 2')

    xbmcutil.updateProgressBar(pBar, 36, 'JanLul.com - stream 3')
    addStream('stream3', 'JanLul.com - Stream 3')

    xbmcutil.updateProgressBar(pBar, 48, 'JanLul.com - stream 4')
    addStream('stream4', 'JanLul.com - Stream 4')

    xbmcutil.updateProgressBar(pBar, 60, 'JanLul.com - stream 5')
    addStream('stream5', 'JanLul.com - Stream 5')

    xbmcutil.updateProgressBar(pBar, 72, 'JanLul.com - stream 6')
    addStream('stream6', 'JanLul.com - Stream 6')

    xbmcutil.updateProgressBar(pBar, 84, 'JanLul.com - stream 7')
    addStream('stream7', 'JanLul.com - Stream 7')

    xbmcutil.updateProgressBar(pBar, 96, 'JanLul.com - stream 8')
    addStream('stream8', 'JanLul.com - Stream 8')

    xbmcutil.endOfList()


def addStream(stream, display) :
    streamUrl = findStream(stream) 
    if streamUrl[-4:] == '.flv' :
        print('Veetle')
        veetle.addChannel(display, streamUrl, 'janlul')
    else :
        print('M3U')
        if bitly.getResponse(streamUrl) :
            color = 'green'
        else :
            streamUrl = ''
            color = 'red'
        xbmcutil.addMenuItem('[COLOR '+color+']'+display+'[/COLOR]', streamUrl, 'true', 'janlul','janlul')


def findStream(page) :
    ua = bitly.getUserAgent()
    page1 = resolveIframe(sourceSite + '/' + page +'.html')
    page2 = resolveIframe(page1)
    page2content = bitly.getPage(page2, sourceSite, ua)
    b64coded = bitly.getBaseEncodedString(page2content)
    streamUrl = bitly.getStreamUrl(b64coded)
    return streamUrl
    
def resolveIframe(page) :
    try :
        if(page[:4] != 'http') :
            page = sourceSite + '/' + page
        userAgent = bitly.getUserAgent()
        pagecontent = bitly.getPage(page, sourceSite, userAgent)
        regIframe = re.compile('iframe\ src\=\"(.*?)\"\ name\=\"iframe_name\"', re.DOTALL)
        iframesrc = regIframe.search(pagecontent).group(1)
        return iframesrc
    except :
        return page

def addStreams2():
    pBar = xbmcutil.createProgressBar('NL Sports', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 16, 'JanLul 1')
    jl_stream1 = bitly.getLink('janlul1', sourceSite)
    veetle.addChannel('JanLul.com - Stream 1', jl_stream1, 'janlul')
    #janlul1 = 'http://cctv-lh.akamaihd.net/i/janlul1_live@125119/master.m3u8'
    #if bitly.getResponse(janlul1) :
    #    color = 'green'
    #else :
    #    color = 'red'
    #xbmcutil.addMenuItem('[COLOR '+color+']JanLul.com - Stream 1[/COLOR]', janlul1, 'true', 'janlul', 'janlul')
	
    xbmcutil.updateProgressBar(pBar, 32, 'JanLul 2')
    jl_stream2 = bitly.getLink('janlul2', sourceSite)
    veetle.addChannel('JanLul.com - Stream 2', jl_stream2, 'janlul')
    #janlul2 = 'http://cctv-lh.akamaihd.net/i/janlul2_live@125116/master.m3u8'
    #if bitly.getResponse(janlul2):
    #    color = 'green'
    #else :
    #    color = 'red'
    #xbmcutil.addMenuItem('[COLOR '+color+']JanLul.com - Stream 2[/COLOR]', janlul2, 'true', 'janlul', 'janlul')

    xbmcutil.updateProgressBar(pBar, 48, 'JanLul 3')
    jl_stream3 = bitly.getLink('janlul3', sourceSite)
    veetle.addChannel('JanLul.com - Stream 3', jl_stream3, 'janlul')

    xbmcutil.updateProgressBar(pBar, 64, 'JanLul 4')
    jl_stream4 = bitly.getLink('janlul4', sourceSite)
    veetle.addChannel('JanLul.com - Stream 4', jl_stream4, 'janlul')

    xbmcutil.updateProgressBar(pBar, 80, 'JanLul 5')
    jl_stream5 = bitly.getLink('janlul5', sourceSite)
    veetle.addChannel('JanLul.com - Stream 5', jl_stream5, 'janlul')

    xbmcutil.updateProgressBar(pBar, 96, 'JanLul 6')
    if bitly.getResponse('http://stream.ssh101.com/hls/janlul6.m3u8') :
        jl6color = 'green'
    else :
        jl6color = 'red'
    xbmcutil.addMenuItem('[COLOR '+jl6color+']JanLul.com - Stream 6[/COLOR]', 'http://stream.ssh101.com/hls/janlul6.m3u8', 'true', 'janlul', 'janlul')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
