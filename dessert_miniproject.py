from abc import abstractmethod


from abc import ABC  

class dessert_item():

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def get_cost(self):
        pass



