from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_links_from_page(url):
    links = urlopen(url).read()
    soup = BeautifulSoup(links, "html.parser")
    links = []

    for link in soup.findAll('a'):
        href = link.get('href')
        if href is not None:
            links.append(str(href))
    

    return links

def scrape_site(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = "\n".join(chunk for chunk in chunks if chunk)
    return text

def scrape_site_list(urls):
    data = []
    for url in urls:
        try:
            text = scrape_site(url)
            data.append(text)
        except:
            print("url: ", url, " failed")
    return data


# sites = ["https://www.churchofjesuschrist.org/?lang=eng","https://en.wikipedia.org/wiki/Berry"]

# text = scrape_site("https://www.churchofjesuschrist.org/?lang=eng")

# data = scrape_site_list(sites)
# for d in data:
#     print(d)

# links = scrape_links_from_page("https://sites.ualberta.ca/~urban/Projects/English/Content/ATU_Tales.htm#ATU0750")
# print(links)