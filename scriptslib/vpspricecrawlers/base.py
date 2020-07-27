from urllib.parse import urlparse
import requests
from scriptslib.requestsutils import FileCache

class PriceResult(object):
    
    def __init__(self):
        self.memory = None
        self.cpu = None
        self.storage = None
        self.transfer = None
        self.price_hourly = None
        self.price_monthly = None
        
    def __str__(self):
        
        template = "{},{},{},{},{},{}"
        return template.format(self.memory,
                               self.cpu,
                               self.storage,
                               self.transfer,
                               self.price_hourly,
                               self.price_monthly)
        
class VPSPriceCrawler(object):
    
    
    def __init__(self, url):
        
        self.url = url 
        self.file_cache = FileCache()
        self.price_list = []
        
        self.name = urlparse(url).path
    
    def download_price_page(self):
        
        try:
            
            r = requests.get(self.url)
            self.file_cache.save_to_cache(self.name, r.text)
        except Exception as e:
            t = "Failed to download. You can try to download and save it to: {}"
            print(t.format(self.file_cache._get_cache_filename(self.name)))
            import sys
            sys.exit(1)
    def get_price_page(self):
        
        content = self.file_cache.load_from_cache(self.name)
        if content is None:
            content = self.download_price_page()
        
        return content      

    def parse_prices(self):
        
        raise NotImplementedError("parse_prices is not implemented.")