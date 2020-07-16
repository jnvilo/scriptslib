"""
Helper classes and methods to make it easier to deal 
with wikimedia api.
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from urllib.parse import urljoin
import hashlib
from pathlib import Path
import os


class WikiMediaRequest(object):
    
    def __init__(self, api_url, username,password):
        self.password = password
        self.username = username
        self.api_url = api_url
        
        url_parts = urlparse(api_url)
        self.wiki_uri = f"{url_parts.scheme}://{url_parts.netloc}"
        self.session = requests.Session()
        
        self.cache_dir = "/tmp"
        self.logged_in = False 
        
    def login(self):
        # Retrieve login token first
        PARAMS_0 = {
            'action':"query",
            'meta':"tokens",
            'type':"login",
            'format':"json"
        }
        
        URL = self.api_url
        R = self.session.get(url=URL, params=PARAMS_0)
        DATA = R.json()
        
        LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
        
        # Send a post request to login. Using the main account for login is not
        # supported. Obtain credentials via Special:BotPasswords
        # (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
        
        PARAMS_1 = {
            'action':"login",
            'lgname':self.username,
            'lgpassword':self.password,
            'lgtoken':LOGIN_TOKEN,
            'format':"json"
        }
        
        R = self.session.post(URL, data=PARAMS_1)
          
    def _get_cache_filename(self, path):
        
        m = hashlib.sha256()
        m.update(path.encode())
        filename = m.hexdigest()
        cache_path = os.path.join(self.cache_dir, filename)
            
        return cache_path
          
    def _save_to_cache(self,path, content):
        
        filename = self._get_cache_filename(path)
        with open(filename, "w") as f:
            f.write(content)
            
    def _load_from_cache(self, path):
        
        filename = self._get_cache_filename(path)
        try:
            
            with open(filename, "r") as f:
                content =  f.read()
        except Exception as e:
            content = None
        
        return content
        
          
    def get(self, path):
        #cache the file
        content = self._load_from_cache(path)
        if content:
             return content
        else:
            url = urljoin(self.wiki_uri, path)
            r = self.session.get(url)
            content = r.text
            self._save_to_cache(path,content)
            return content
