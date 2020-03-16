class MyHashableKey:
    #20% of the grade
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value
    def __eq__(self, other):
        pass
    def __hash__(self):
        pass