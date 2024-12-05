from collections import defaultdict, deque
import os
os.chdir(os.path.dirname(__file__))


def parse_input(input_data):
    # Split input into two parts: ordering rules and updates
    parts = input_data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in parts[0].splitlines()]
    updates = [list(map(int, update.split(','))) for update in parts[1].splitlines()]
    return rules, updates

def is_valid_update(update, rules):
    # Build a dependency map only for pages in the update
    dependency_map = defaultdict(set)
    for x, y in rules:
        if x in update and y in update:
            dependency_map[y].add(x)  # y depends on x (x must come before y)
    
    # Check if the order in the update satisfies all dependencies
    seen = set()
    for page in update:
        if dependency_map[page] - seen:
            return False
        seen.add(page)
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def topological_sort(update, rules):
    # Build a directed graph of dependencies for the current update
    in_degree = {page: 0 for page in update}
    graph = defaultdict(list)
    
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1

    # Perform topological sort using Kahn's algorithm
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def solve(input_data):
    rules, updates = parse_input(input_data)
    valid_updates = []
    invalid_updates = []

    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    
    # Part 1: Middle pages of valid updates
    middle_pages_valid = [find_middle_page(update) for update in valid_updates]
    part1_result = sum(middle_pages_valid)

    # Part 2: Fix invalid updates and find their middle pages
    fixed_updates = [topological_sort(update, rules) for update in invalid_updates]
    middle_pages_fixed = [find_middle_page(update) for update in fixed_updates]
    part2_result = sum(middle_pages_fixed)

    return part1_result, part2_result

def readFromFile(filename):
    """
    Reads the input data from a file and returns it as a string.
    
    :param filename: Path to the input file
    :return: String containing the contents of the file
    """
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    file_path = "input.txt"
    #file_path = "testData_day5.txt"

    input_data = readFromFile(file_path)

    part1_result, part2_result = solve(input_data)
    print("Sum of middle pages of valid updates (Part 1):", part1_result)
    print("Sum of middle pages of fixed updates (Part 2):", part2_result)