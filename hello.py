from Bucket import NotFoundException
from Bucket import ItemExistsException
# READ THIS!!
# DO NOT USE THE BUILT-IN HASH
# FUNCTIONS FOR INTEGERS AND STRINGS!
# MAKE SURE YOUR IMPLEMENTATION OF
# __hash__ RETURNS A POSITIVE INTEGER!


class MyHashableKey:
    def __init__(self, int_value, string_value):
        self.int_value = 1
        self.string_value = "string_value"
    def __eq__(self, other):
        if self.int_value == other.int_value:
            return True
        return False
    def __hash__(self):
        return self.int_value