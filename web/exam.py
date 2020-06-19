from urllib.parse import urlsplit
url='https://www.hello.org/bye/'
domain="{0.scheme}://{0.netloc}/".format(urlsplit(url))
print (domain)