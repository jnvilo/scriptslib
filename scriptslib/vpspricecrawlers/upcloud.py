
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

class UpCloudPricing(VPSPriceCrawler):
    
    def __init__(self, url):
        
        super().__init__(url)
        
    def parse_content(self):
        
        content = self.get_price_page()
        soup = BeautifulSoup(content)
    
        price_blocks = soup.select(".price-block")
    
        for price_block in price_blocks:
            blocks = price_block.select(".block")
            
            block_result = PriceResult()
            for block in blocks:
                name = block.select("p")[0].getText().lower()
                value = block.select("h3")[0].getText().lower()
                
                if name in ["memory","storage","transfer"]:
                    value = value[:value.find(" ")]
                    setattr(block_result, name, value)
            
                if (name.startswith("$") and name.endswith("h")):
                    price_hourly = name.lstrip("$").rstrip("/h")
                    price_monthly = value.lstrip("$").rstrip("/mo")
                    
                    block_result.price_hourly = price_hourly
                    block_result.price_monthly = price_monthly
                    
                if name == "cpu":
                    block_result.cpu = value
            self.price_list.append(block_result)
            
        
if __name__ == "__main__":
    
    print("starting...")
    url="https://upcloud.com/pricing/"
    upcloud = UpCloudPricing(url)
    upcloud.get_price_page()
    upcloud.parse_content()    
    
    for price in upcloud.price_list:
        
        print(price)
        