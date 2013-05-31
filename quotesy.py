import urllib as p
import re
from random import randrange
import subprocess

sock = p.urlopen("http://www.brainyquote.com/" +
                 "quotes/topics/topic_intelligence.html")
grabSource = sock.read()

sock.close()

#uncomment this line if you want to grab without link
#matches = re.findall('<span class="bqQuoteLink">
#<a title"view quote">(.*?)</a></span><br>')
##EndOfCommentedCode

matches = re.findall('<span class="bqQuoteLink"><a title=(.*?)</a></span><br>',
                     grabSource, re.S)

#holder = list()
#holder.append(matches)


#remove crap from match and print result!
n = randrange(20)
removeextra = matches[n].split()[3::]
result = ' '.join(removeextra)

#We now call open the call from subprocess and use cowsay with tux
#and put in the quote tada!
subprocess.call(['cowsay', '-f', '/usr/share/cows/tux.cow', result])
