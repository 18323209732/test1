from api.address import Address
from api.wework import WeWork


class TestAddress:

    def setup(self):
        self.address = Address()

    def test_create(self):
        print(self.address.create("zhangsan3333","wangwu","13855552555"))

    def test_update(self):
        print(self.address.update("zhangsan3333","wangermazi","18300000000"))

    def test_get(self):
        print(self.address.get("zhangsan3333"))

    def test_delete(self):
        print(self.address.delete("zhangsan3333"))
