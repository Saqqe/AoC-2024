import re
import os
os.chdir(os.path.dirname(__file__))


def read_data(filename):
    # Read and parse the data from the file
    with open(filename, 'r') as file:
        reports = [list(map(int, line.strip().split())) for line in file if line.strip()]
    
    return reports


def is_safe(report):
    # Check if the report is strictly increasing or strictly decreasing
    is_increasing = all(x < y for x, y in zip(report, report[1:]))
    is_decreasing = all(x > y for x, y in zip(report, report[1:]))
    
    # Check if all adjacent differences are within the range [1, 3]
    differences_valid = all(1 <= abs(x - y) <= 3 for x, y in zip(report, report[1:]))
    
    return (is_increasing or is_decreasing) and differences_valid


def count_safe_reports_p1(reports):
    # Count the number of safe reports
    safe_count = sum(1 for report in reports if is_safe(report))
    
    return safe_count


def validate_with_dampener(sequence):
    # Check if the sequence is directly safe
    if is_safe(sequence):
        return "Safe"
    
    # Check if removing a single level makes it safe
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i+1:]
        if is_safe(modified_sequence):
            return "Safe"
    
    return "Unsafe"


def count_safe_reports_p2(reports):
    return sum(1 for report in reports if validate_with_dampener(report) == "Safe")

# Main
if __name__ == "__main__":
    #print("Current Working Directory:", os.getcwd())
    filename = "testData_day2.txt"
    #filename = "input.txt"
    reports = read_data(filename)

    #Part 1
    print(f"PART 1: Number of safe reports:", count_safe_reports_p1(reports))

    #Part 2
    print(f"PART 2: Number of safe reports:", count_safe_reports_p2(reports))