from pathlib import Path
import hashlib
import os

class FileCache():
    """
    This provides method to cache the content. 
    """
    
    def __init__(self, cache_dir=None):
        if cache_dir is None:
            self.cache_dir = "/tmp"
        else:
            self.cache_dir = cache_dir
    
    def _get_cache_filename(self, name):
        """
        Returns a sha1sum of the given path together 
        with the name of the script that uses this. 
        
        Ensures that the file is unique to the current 
        running script.
        """

        m = hashlib.sha256()
        fullpath = "{}-{}".format(Path(__file__).stem, name.encode())
        m.update(fullpath.encode('utf-8'))
        filename = m.hexdigest()
        
        cache_path = os.path.join(self.cache_dir, filename)
        return cache_path

    def save_to_cache(self,name, content):

        filename = self._get_cache_filename(name)
        with open(filename, "w") as f:
            f.write(content)

    def load_from_cache(self, name):


        filename = self._get_cache_filename(name)
        try:

            with open(filename, "r") as f:
                content =  f.read()
        except Exception as e:
            content = None

        return content    
    

