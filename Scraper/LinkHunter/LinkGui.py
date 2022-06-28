from tkinter import *
import ScrapeLinks as sl


test_link = "https://www.churchofjesuschrist.org/?lang=eng"

class LinkSearch:

    def __init__(self):
        
        self.Lb = None
        self.save_btn = None
        self.scrape_btn = None
        self.window = Tk()
        self.window.geometry('900x700')
        self.frame = Frame(self.window)
        # self.reset()
        self.frame.pack(side="top", expand=True, fill="both")
        self.window.mainloop()

    def reset(self, url = test_link):
        self.clear()
        print("test link: ", test_link)
        self.pick_links(url)
        self.create_buttons()
        
    
    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
    #     self.Lb.

    def create_buttons(self):
        self.frame.save_btn = Button(self.window, text = "Save Links", command = self.save_links)
        self.frame.save_btn.pack(side=RIGHT)
        self.frame.scrape_btn = Button(self.window, text = "Scrape", command = self.scan_link)
        self.frame.scrape_btn.pack(side=LEFT)
        
        # self.save_btn.pack()
        # self.scrape_btn.pack()

    def scan_link(self):
        selection = self.frame.Lb.get(0)
        print("selection: ", selection)
        self.reset(selection)
        

    
    def save_links(self):
        selections = [self.frame.Lb.get(i) for i in self.frame.Lb.curselection()]
        print("Links to save: ", selections)
        print("initiating save")


    def pick_links(self, source_url):
        
        yscrollbar = Scrollbar(self.frame, self.window)
        yscrollbar.pack(side= RIGHT, fill = Y)

        self.frame.Lb = Listbox(
            self.window, 
            selectmode = "multiple"
        )

        self.frame.Lb = Listbox(
            self.window, 
            selectmode = "multiple", 
            yscrollcommand = yscrollbar.set
        )

        self.frame.Lb.pack(expand = YES, fill = "both")
    

        # Get and pack the links.
        links = sl.scrape_links_from_page(source_url)

        count = 0
        for link in links:
            self.frame.Lb.insert(END, link)
            self.frame.Lb.itemconfig(count, bg = "yellow" if count % 2 == 0 else "cyan")
            count += 1
        
        yscrollbar.config(command=self.frame.Lb.yview)





if __name__ == "__main__":
    gui = LinkSearch()
