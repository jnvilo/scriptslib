from scriptslib.wikimedia import WikiMediaRequest

class TestWikiMediaRequest(object):

    def test_create_instance(self):
        instance = WikiMediaRequest("http://example.com/api", "jason","testpass")
        assert isinstance(instance, WikiMediaRequest)
