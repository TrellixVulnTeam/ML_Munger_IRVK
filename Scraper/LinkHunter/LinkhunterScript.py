from enum import Enum
import ScrapeLinks as sl

class Corrections(Enum):
    HEADER = 1

link_scrape_list = []

correction_types = []

def add_header(positions, text):
    for position in positions:
        link_scrape_list[position] = text + link_scrape_list[position]
    return lin

def correct_links(corr_positions, correction, text):
    if correction == Corrections.HEADER:
        add_header(corr_positions, text)
    
def print_link_scrape_list():
    for count, link in enumerate(links):
        print(count + 1, link)

root_link = input("Enter root link: ")

links = sl.scrape_links_from_page(root_link)

print_link_scrape_list()

print("Would you like to add a correction?")
print("Type A for header correction: ")

#Add other correction instructions. 
correction_selections = input("Enter root link: ")

if "A" in correction_selections:
    header = input("Enter Header: ")
    choice = input("Apply to all? (Y or N):")
    if choice == "Y":
        correct_links([i for i in range(0, len(link_scrape_list))], Corrections.Header, header)
    print_link_scrape_list()

    if choice != "Y":
        choice = input ("Apply to subset? (Y or N):")
        if choice == "Y":
            subset = input("Enter subset each number followed by a space (1,2,3): ")
            choices = subset.split(" ")