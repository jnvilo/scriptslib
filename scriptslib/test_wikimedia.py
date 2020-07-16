from scriptslib.wikimedia import WikiMediaRequest

class TestWikiMediaRequest(object):

    def test_create_instance(self):
        instance = WikiMediaRequest("jason","testpass")
        assert isinstance(instance, WikiMediaRequest)
