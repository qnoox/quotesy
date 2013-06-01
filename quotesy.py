#!/usr/bin/python2
#from random import randrange
import random
import subprocess
import urllib
import re


def sockethandler():
    sock = urllib.urlopen("http://www.brainyquote.com/" +
                          "quotes/topics/topic_intelligence.html")
    grabSource = sock.read()
    sock.close()

    matches = re.findall(
        '<span class="bqQuoteLink"><a title=(.*?)</a></span><br>',
        grabSource, re.S)
    #n = randrange(20)
    n = random.choice(
        [1, 2, 3, 5, 9, 12, 20, 14, 25, 22, 4, 6, 13, 23, 24, 19, 21])
    removeextra = matches[n].split()[3::]
    result = ' '.join(removeextra)
    #return result
    subprocess.call(['cowsay', '-f', '/usr/share/cows/tux.cow', result])
    return

sockethandler()
