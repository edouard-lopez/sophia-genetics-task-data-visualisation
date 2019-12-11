from app import feeder

class TestFeederClass:
    # feeder.Feeder()

    def test_init(self):
        assert feeder.Feeder()

    def test_get_user_usage(self):
        user_usage = feeder.Feeder().user_usage()
        
        assert len(user_usage) == 151

    def test_get_domainX(self):
        domainX = feeder.Feeder().domainX()
        
        assert len(domainX) == 2
        assert domainX == { "from": "04-2016", "to": "03-2017" }

    def test_get_domainY(self):
        domainY = feeder.Feeder().domainY()
        
        assert len(domainY) == 151

    def test_get_categoriesY(self):
        categoriesY = feeder.Feeder().categoriesY()
        
        assert categoriesY == 'Client'
