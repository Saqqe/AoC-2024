import re
import os
os.chdir(os.path.dirname(__file__))


def read_data(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            # Split the line into two numbers based on whitespace
            numbers = line.strip().split()
            if len(numbers) == 2:
                left_list.append(int(numbers[0]))
                right_list.append(int(numbers[1]))

    return left_list, right_list


def sort_lists(left_list, right_list):
    left_list.sort()
    right_list.sort()


# Puzzle 1
def calculate_distance(left_list, right_list):
    sort_lists(left_list, right_list)
    return sum(abs(left - right) for left, right in zip(left_list, right_list))


# Puzzle 2
def calculate_similarity_score(left_list, right_list):
    from collections import Counter

    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)

    # Initialize similarity score
    similarity_score = 0

    # Calculate the similarity score
    for num in left_list:
        if num in right_counts:
            similarity_score += num * right_counts[num]

    return similarity_score

# Main
if __name__ == "__main__":
    #print("Current Working Directory:", os.getcwd())
    #filename = "testData.txt"
    filename = "input.txt"

    left_list, right_list = read_data(filename)

    #Puzzle 1
    print("Puzzle 1 - Distance:", calculate_distance(left_list.copy(), right_list.copy()))

    #Puzzle 2
    print("Puzzle 2 - Similarity score:", calculate_similarity_score(left_list.copy(), right_list.copy()))
