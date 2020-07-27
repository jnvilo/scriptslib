import unittest
from scriptslib.requestsutils import FileCache

class TestFileCache(unittest.TestCase):
    
    
    def test_default_behaviour(self):
        
        fc = FileCache()
        content = "this is a test content"
        
        fc.save_to_cache("mycontent", content)
    
        new_fc = FileCache()
        
        cached_content = new_fc.load_from_cache("mycontent")
        self.assertEqual(content, cached_content)
        
    