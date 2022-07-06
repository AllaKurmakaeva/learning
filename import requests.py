from urllib.request import Request, urlopen
import random


url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
l=random.randint(1,2000)
r=random.randint(100,500)
first500 = webpage[l::r].split("\n")
random.shuffle(first500)
print(first500)
h=len(first500)
new_words = []
for i in first500:
    if i != '':
        new_words.append(i)
print(new_words)