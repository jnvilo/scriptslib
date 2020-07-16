import unittest
from scriptslib import wikimedia

class TestWikiMediaRequest(unittest.TestCase):

    def test_can_instantiate(self):
        wm = wikimedia.WikiMediaRequest("jnvilo","testpass")
        self.assertTrue(isinstance(wm, wikimedia.WikiMediaRequest))



