import unittest
from day1 import read_data, calculate_distance, calculate_similarity_score

class TestAdventOfCodeDay1(unittest.TestCase):
    def test_calculate_total_distance(self):
        # Example input
        left_list, right_list = read_data(filename)
        
        # Calculate total distance
        total_distance = calculate_distance(left_list, right_list)
        self.assertEqual(total_distance, 11)
    
    def test_calculate_similarity_score(self):
        # Example input
        left_list, right_list = read_data(filename)
        
        # Calculate similarity score
        similarity_score = calculate_similarity_score(left_list, right_list)
        self.assertEqual(similarity_score, 31)

if __name__ == '__main__':
    filename = "testData_day1.txt"
    unittest.main()
