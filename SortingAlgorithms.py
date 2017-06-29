# N.B. code is written in Python 2.7, superclass method calls might not work the
# same in 3.x, abstract class declaration is also different for 3.x too.
from abc import ABCMeta, abstractmethod 

class SortingAlgorithm(object):
        """Abstract class and simple sorting algorithm framework for concrete
        sorting classes.
        """
        
        __metaclass__ = ABCMeta

        def __init__(self, input_list):
            """Abstract class constructor ensures all concrete sorts have a
                valid input list before being instantiated.
                Checks for empty lists and that lists are of correct typing.
            """
            if len(input_list) < 1:
                    raise IndexError("Empty array given.")
            elif not(all(isinstance(item, (int, long)) for item in input_list)):
                    raise TypeError("Invalid array given.")
            else:
                    self.input = input_list
    
        @abstractmethod
        def sort(self):
            """Sorts the input list of integers into ascending order.

            Python's abc module allows for abstract methods to be defined but
            not implemented and raises a TypeError if object is instantiated
            without sort() implemented in a concrete class.
            """
            
class InsertionSort(SortingAlgorithm):
        """Concrete class for Insertion sort implementation.
        """
        
        def __init__(self, input_list):
            """Does a superclass method call to inherit input list error
                handling.
            """
            super(InsertionSort, self).__init__(input_list)
    
        def sort(self):
            for i in range(1, len(self.input)):
                val = self.input[i]
                j = i-1
                while (j >= 0) and (self.input[j] > val):
                    self.input[j+1] = self.input[j]
                    j = j-1
                self.input[j+1] = val
            return self.input

################################################################################
## Tests
################################################################################
##print InsertionSort([]).sort()                    # Empty input
##print InsertionSort([1]).sort()                   # One element
##print InsertionSort([0, 1]).sort()                # Two different elements
##print InsertionSort([1, 0]).sort()
##print InsertionSort([5, 4, 3, 2, 1, 0]).sort()    # Long input 
##print InsertionSort([0, 1, 2, 3, 4, 5]).sort()
##print InsertionSort([1000000, 4, 3, 2, 1]).sort() # Large integer
##print InsertionSort([1, 2, 3, 4, 1000000]).sort()
##print InsertionSort([1, 1]).sort()                # Duplicate elements
##print InsertionSort([0, 1, 1]).sort()             # Duplicate elements and one different
##print InsertionSort([1, 0, 1]).sort()
##print InsertionSort([1, 1, 0]).sort()
##print InsertionSort([5, 3, 2, -1, -9]).sort()     # Negative elements
##print InsertionSort([-9, -1, 2, 3, 5]).sort()
##print InsertionSort("a").sort()                   # Invalid inputs
##print InsertionSort([1, "a"]).sort()
##print InsertionSort(["a", 1]).sort()
##print InsertionSort([0.1]).sort()
##print InsertionSort([1, 0.1]).sort()
##print InsertionSort([0.1, 1]).sort()
