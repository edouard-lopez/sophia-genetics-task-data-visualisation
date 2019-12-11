from app.json_parser import JsonParser


class TestJsonParserClass:
    def test_init(self):
        assert JsonParser()

    def test_get_user_usage(self):
        user_usage = JsonParser().user_usage()

        assert len(user_usage) == 151

    def test_get_domainX(self):
        domainX = JsonParser().domainX()

        assert len(domainX) == 2
        assert domainX == {"from": "04-2016", "to": "03-2017"}

    def test_get_domainY(self):
        domainY = JsonParser().domainY()

        assert len(domainY) == 151

    def test_get_categoriesY(self):
        categoriesY = JsonParser().categoriesY()
        assert categoriesY == "Client"

