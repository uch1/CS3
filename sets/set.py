#!python
#from linkedlist import LinkedList
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        """Initialize a new empty set structure
           and add each elements if a sequence is given
        """
        self.set = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def contains(self, element):
        '''
            returns a boolean indicating whether element is in this set
        '''
        return self.contains(element)


    def add(self, element):
        '''
            adds an element to this set, if not present already
        '''
        if self.contains(element):
            raise ValueError("{} already exists in the set.").format(element)
        else:
            self.set.set(element, None)
            self.size += 1

    def remove(self, element):
        '''
            removes an element from this set, if present, or else raise KeyError
        '''
        if self.contains(element):
            self.set.delete(element)
            self.size -= 1
            return
        else:
            raise KeyError("{} doesn't exist in the set").format(element)

    def union(self, other_set):
        '''
            returns a new set that is the union of this set and other_set
        '''

        # for key, value in other_set.items():
        #     # check if the current set has
        #     # the same elements in the other set
        #     if not self.contains(key):
        #         self.add(key)
        #
        #     else:

    def intersection(self, other_set):
        '''
            returns a new set that is the intersection of this set and other_set
        '''
        new_set = Set()

        for key in other_set.keys():
            if self.contains(key):
                new_set.add(key)
        return new_set


    def difference(self, other_set):
        '''
            returns a new set that is the difference of this set and other_set
        '''
        new_set = Set()

        for key in other_set.keys():
            if not self.contains(keys):


    def is_subset(self, other_set):
        '''
            returns a boolean indicating whether other_set is a subset of this set
        '''



def main():
    set = Set()
    set.
