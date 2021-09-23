import unittest
from challenge import tuple_added


class TestSums(unittest.TestCase):
    SAMPLE_LISTS = [[2, 7, 11, 15],
                    [-1, -2, 6, 3],
                    [0, 0, 0, 0],
                    [5, 3, 0, 1],
                    ["a", "b", "c"],
                    [4.3, 10.2, 9.9, 5.7]]

    def test_result(self):
        self.assertEqual(tuple_added(nums=self.SAMPLE_LISTS[0], target=26), second=(2, 3))
        self.assertEqual(tuple_added(nums=self.SAMPLE_LISTS[1], target=1), second=(1, 3))
        self.assertEqual(tuple_added(nums=self.SAMPLE_LISTS[2], target=0), second=(0, 1))
        self.assertEqual(tuple_added(nums=self.SAMPLE_LISTS[3], target=0), second=None)
        self.assertEqual(tuple_added(nums=self.SAMPLE_LISTS[4], target="ab"), second=(0, 1))
        self.assertEqual(tuple_added(nums=self.SAMPLE_LISTS[5], target=10), second=(0, 3))


    def test_types(self):
        self.assertRaises(TypeError, tuple_added, "daniel", 90)
        self.assertRaises(TypeError, tuple_added, 389, 40)

    if __name__ == "__main__":
        unittest.main()
