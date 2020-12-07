"""
By Juan Peralta Web Scrapping Project: The followign script has the porpuse to learn a little bit more about each culture.

On first phase we are scrapping The World Cultures Encyclopedia to realize how many cultures and descritpions. 

"""
from app import db, Countries, CultureOfCountries, WorldCultures
from worldcultures import scrape

url = "https://www.everyculture.com/"
webscraper = scrape(url)

def dbloader():
    # webscraper = WorldCulturesScraper() #Class Name
    # webscraper.scrape()
    #scrape() # call a function
# this function should run after scraping the web data to load it into db 
# this script is ran.
    db.create_all()
    #self.scrape()
    for country,description in webscraper.items():
        new_row = Countries(CountryName=country, CountryDescription=description)
        print(new_row)
        db.session.add(new_row)
        db.session.commit()    
        
        #return rows

if __name__ == '__main__':
    dbloader()