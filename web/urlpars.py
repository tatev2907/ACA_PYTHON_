import re
import urllib.request

request_url = urllib.request.urlopen('https://aca.am/en/index.html')
s = request_url.read()
paragraphs = re.findall(r'<!--(.*?)-->', str(s))
l = paragraphs[1]
h = l[4:-4].split(' ')
d = [chr(int(x, 2)) for x in h]
print(''.join(d))
