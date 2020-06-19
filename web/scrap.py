from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

class my_spider:
    def __init__(self, url):
        self.start = url
        self.base="{0.scheme}://{0.netloc}/".format(urlsplit(url))
        self.lst=[]
    def getTitle(self, link):
        title = ''
        if link.title.string is not None:
            title = link.title.string
        elif link.find("h1") is not None:
            title = link.find("h1")
        return title

    def url_not_exist_in_lst(self, searchFor):
        if not any(x == searchFor for x in self.lst):
            return True
        return False

    def append_urls_in_list_of_dict(self, link, start, previews) -> list:
        url= link.get('href')
        if url[0]=='/'and url[1] != '/' and len(url) != 1:
            if self.url_not_exist_in_lst(url):
                absolute_url=start+url
                link_html = urlopen(absolute_url).read()
                embedded_link = BeautifulSoup(link_html, 'html.parser')
                preview_dict = {
                    'title': self.getTitle(embedded_link),
                    'url': url,
                    'links': []
                }
                self.lst.append(url)
                previews.append(preview_dict)
        return previews

    def soup_htmls_get_links(self, start):
        r = urlopen(start)
        raw_html = r.read()
        soup = BeautifulSoup(raw_html, 'html.parser')
        links = soup.find_all('a', href=True)
        return links

    def scrape(self, depth):
        start = self.base
        previews = []
        links = self.soup_htmls_get_links(start)
        #all links in home page
        i=0
        for link in links:
            previews = self.append_urls_in_list_of_dict(link, start, previews)
            if previews!=[] and len(previews)==i+1:
                k=previews[i]
                print('start', k)
                print()
                for m in range(depth):
                    p = k['url']
                    new_start = start + p
                    if new_start[-1] == '/':
                        new_start = new_start[:-1]
                    lin = self.soup_htmls_get_links(new_start)
                    k['links'] = []
                    for l in lin:
                        k['links'] = self.append_urls_in_list_of_dict(l, start, k['links'])
                        n = '\t\t' * (m + 1)
                        if k['links'] != []:
                            print(n, k['links'])
                            break
                    k = k['links'][0]
                i+=1

        return previews


d = my_spider('https://en.wikipedia.org/wiki/Machine_learning')
k = d.scrape(2)

