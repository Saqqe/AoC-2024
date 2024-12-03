import re
import os
os.chdir(os.path.dirname(__file__))

def process_mul_instructions_from_file(file_path):
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            corrupted_memory = file.read()
        
        # Find all matches in the corrupted memory
        matches = re.findall(pattern, corrupted_memory)
        
        # Calculate the result of each multiplication
        results = [int(x) * int(y) for x, y in matches]
        
        # Return the sum of results
        return sum(results)
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"


def process_conditional_mul_instructions_inline(file_path):
    # Regular expressions to find valid mul(X,Y) and do()/don't() instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    condition_pattern = r"do\(\)|don't\(\)"

    # Initial condition: mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            corrupted_memory = file.read()

                # Split the memory into tokens based on conditions and instructions
            tokens = re.split(f"({condition_pattern})", corrupted_memory)

            for token in tokens:
                token = token.strip()

                # Check for condition instructions
                if token == "do()":
                    mul_enabled = True
                elif token == "don't()":
                    mul_enabled = False
                
                # Find all valid mul(X,Y) instructions in the current token
                matches = re.findall(mul_pattern, token)

                # Calculate results of valid mul(X,Y) instructions if enabled
                if mul_enabled:
                    for x, y in matches:
                        total_sum += int(x) * int(y)
            
            return total_sum

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    file_path = "input.txt"
    #file_path = "testData_day3.txt"

    print(f'puzzle 1: ', process_mul_instructions_from_file(file_path))


    print(f'puzzle 2: ', process_conditional_mul_instructions_inline(file_path))