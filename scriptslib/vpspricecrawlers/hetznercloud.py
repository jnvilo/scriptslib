from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from urllib.parse import urljoin
import hashlib
from pathlib import Path
import os

from scriptslib.requestsutils import FileCache
from scriptslib.vpspricecrawlers.base import PriceResult
from scriptslib.vpspricecrawlers.base import VPSPriceCrawler

class HetznerCloudPricing(VPSPriceCrawler):
    
    def __init__(self, url):
        super().__init__(url)
        
    def parse_prices(self):
        content = self.get_price_page()
        
        soup = BeautifulSoup(content)
        
        #print(soup)
        
        price_cards = soup.select(".price-card")
        
        for price_card in price_cards:
            #Get the price-table
            print("=========================================================")
            price_tables = price_card.select(".price-table")
            
            price_main = price_card.select(".price-main")[0]
            price_second = price_card.select(".price-second")[0]
            
            print(price_main.getText())
            print(price_second.getText())
            
            for price_table in price_tables:
                
                tr_list = price_table.find_all("tr")
                
                for tr in tr_list:
                    td_list = tr.find_all("td")
                    
                    
                    name = td_list[1].find("span")
                    value = td_list[0].find("strong")                
                    
                    if not None in [name, value]:
                        name = name.getText()
                        value = value.getText()
                        print(f"name={name},value={value}")
                    
            
                #print(tr_list)   
            print("----------------------------")
            
if __name__ == '__main__':
    
    url = "https://www.hetzner.com/cloud"
    hc = HetznerCloudPricing(url)
    hc.parse_prices()

        
    