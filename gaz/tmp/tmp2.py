import sys
sys.path.append('/home/aidan/IE/Elie2/')
import tagging

f = open(sys.argv[1])
words = {}
for line in f:
    if line:
        word = line.split()[0]
        word = word.strip().lower()
        words[word]=1

d = tagging.stopGaz()
for k in words.keys():
    if d.search(k):
        print k
