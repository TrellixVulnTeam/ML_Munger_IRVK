import ScrapeLinks as sl

core_link = "https://www.gutenberg.org/files/30580/30580-h/30580-h.htm#blue"

links = sl.scrape_links_from_page(core_link)


head = "http://www.gutenberg.org/files/"

cleaned_links = []
for link in links: 
    if head in link and ".zip" not in link:
        cleaned_links.append(link)

links = cleaned_links

print(links[0])

print(sl.scrape_site(links[0]))

# print(sl.scrape_site(links[6]))