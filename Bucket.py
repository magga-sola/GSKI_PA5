class NotFoundException(BaseException):
    pass

class ItemExistsException(BaseException):
    pass

class Bucket:
    # 30%
    # must fully implement the Map ADT
    def __init__(self):
        self.error = True
    def __str__(self):
        pass
    def __setitem__(self, key, data):
        pass
    def __getitem__(self, key):
        if self.error:
            raise NotFoundException()
    def __len__(self):
        pass


    def insert(self, key, data):
        if self.error:
            raise ItemExistsException()

    def update(self, key, data):
        if self.error:
            raise NotFoundException()

    def find(self, key):
        if self.error:
            raise NotFoundException()

    def contains(self, key):
        pass

    def remove(self, key):
        if self.error:
            raise NotFoundException()

