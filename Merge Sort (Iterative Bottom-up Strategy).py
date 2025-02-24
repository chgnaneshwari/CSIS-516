def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    Steps:
    1. Compare elements from both lists.
    2. Append the smaller element to the result list.
    3. If one list is exhausted, append the remaining elements from the other list.
    :param left: Sorted left list
    :param right: Sorted right list
    :return: Merged sorted list
    """
    result = []
    i, j = 0, 0
    
    # Merge the two lists while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # If there are remaining elements in the left list
    if i < len(left):
        result.extend(left[i:])
    
    # If there are remaining elements in the right list
    if j < len(right):
        result.extend(right[j:])
    
    return result

def merge_sort(arr):
    """
    Iteratively sort an array using merge sort.
    Steps:
    1. Break the list into sublists of size 1.
    2. Iteratively merge sublists until the whole list is sorted.
    :param arr: List of elements to sort
    :return: Sorted list
    """
    # Step 1: Create sublists of size 1
    sublists = [[x] for x in arr]
    
    # Step 2: Merge sublists iteratively until there's only one sorted list
    while len(sublists) > 1:
        merged_sublists = []
        
        # Merge sublists in pairs
        for i in range(0, len(sublists), 2):
            left = sublists[i]
            right = sublists[i+1] if i+1 < len(sublists) else []
            merged_sublists.append(merge(left, right))
        
        sublists = merged_sublists
    
    return sublists[0] if sublists else []

# Unit Tests
import unittest

class TestMergeSort(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])
        
    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])
        
    def test_already_sorted(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        
    def test_reverse_sorted(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
    def test_unsorted_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])
        
    def test_merge_function(self):
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([], [2, 4, 6]), [2, 4, 6])
        self.assertEqual(merge([1, 3, 5], []), [1, 3, 5])
        self.assertEqual(merge([], []), [])

if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
