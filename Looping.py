import unittest

def find_smallest_cycle(arr):
    n = len(arr)  # Length of the array
    # Iterate over all divisors of n
    for cycle_length in range(1, n + 1):
        if n % cycle_length == 0:  # Only consider divisors of n
            # Try to find a cycle of the current cycle_length
            cycle_pattern = arr[:cycle_length]  # Extract the potential repeating pattern
            match = True
            for i in range(cycle_length, n):
                if arr[i] != cycle_pattern[i % cycle_length]:
                    match = False
                    break
            if match:
                return cycle_length
    return n  # If no cycle is found, return the full length

# Test cases to verify the implementation
class TestFindSmallestCycle(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        expected = 3
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_2(self):
        arr = [4, 5, 6, 4, 5, 6, 4]
        expected = 7
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_3(self):
        arr = [1, 2, 1, 2, 1, 2, 1]
        expected = 7
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_4(self):
        arr = [7, 8, 9, 10, 11]
        expected = 5
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_5(self):
        arr = [1, 1, 1, 1, 1]
        expected = 1
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

    def test_case_6(self):
        arr = [5, 10, 5, 10, 5]
        expected = 5
        result = find_smallest_cycle(arr)
        self.assertEqual(result, expected)

# Run the tests
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
