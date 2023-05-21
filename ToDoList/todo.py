from datetime import datetime
import os
cwd = os.getcwd()
def check_todo():
    file_path = os.path.join(cwd, 'todo.txt')
    with open(file_path, "r") as file:
        # Rest of the code
        content = file.read()
        lines = content.splitlines()
        number = 1
        print("---//---")
        outputs = []
        for i in range(0, 9999):
            if i % 2 == 0:
                try:
                    line1 = lines[i]
                    outputs.append(f"{number}) {line1}")
                    number += 1
                except:
                    break

        # Sort and print the organized outputs
        sorted_outputs = organize_outputs_by_date(outputs)
        for output in sorted_outputs:
            print(output)

def write_todo():
    a = str(input("Title of the to do: "))
    b = int(input("Day: "))
    c = int(input("Month: "))
    d = (f"{b}/{c}")
    content = str(input("Write the content of it: "))
    file_path = os.path.join(cwd, 'todo.txt')
    with open(file_path, "a") as file:
        file.write(f"{a} / Expire Date = {d}\nContent: {content}\n")

def copytext():
    file_path = os.path.join(cwd, 'todo.txt')
    with open(file_path, "r") as file:
        content = file.read()
    with open(file_path, "w") as file:
        file.write(content)

def separatelines():
    global n
    n = int(input("Type the number of the \"to do\" to remove: "))
    file_path = os.path.join(cwd, 'temp.txt')
    with open(file_path, "r") as file:
        content = file.read()
        lines = content.splitlines()
    for i in range(1, 99):
        try:
            if i != n:
                file_path = os.path.join(cwd, 'todo.txt')
                with open(file_path, "a") as file:
                    file.write(f"{lines[(i*2)-2]}\n")
                    file.write(f"{lines[(i*2)-1]}\n")
            if i == n:
                file_path = os.path.join(cwd, 'todo.txt')
                with open(file_path, "w") as file:
                    file.write(f"{lines[(n*2)-2]}\n")
                    file.write(f"{lines[(n*2)-1]}\n")

        except:
            break

def resettext():
    file_path = os.path.join(cwd, 'todo.txt')
    with open(file_path, "w") as file:
        file.write(f"")

def delete_one():
    copytext()
    resettext()
    separatelines()
    pass

def check_finished():
    file_path = os.path.join(cwd, 'finished.txt')
    with open(file_path, "r") as file:
        content = file.read()
        lines = content.splitlines()
        b = 1
        print("---//---")
        outputs = []
        for i in range(0, 9999):
            if i % 2 == 0:
                try:
                    line1 = lines[i]
                    outputs.append(line1)
                    b += 1
                except:
                    break
        
        # Sort and print the organized outputs
        sorted_outputs = organize_outputs_by_date(outputs)
        for output in sorted_outputs:
            print(output)


def organize_outputs_by_date(outputs):
    # Define the current date
    current_date = datetime.now().date()

    # Define a helper function to extract the date from the output
    def extract_date(output):
        start = output.find('=') + 2  # Find the start index of the date
        date_str = output[start:]  # Extract the date string
        day, month = map(int, date_str.split('/'))  # Split and convert to integers
        return datetime(year=current_date.year, month=month, day=day).date()

    # Parse and calculate time differences
    parsed_outputs = []
    for output in outputs:
        date = extract_date(output)
        time_diff = abs(date - current_date)
        parsed_outputs.append((output, time_diff))

    # Sort the outputs based on time differences
    sorted_outputs = sorted(parsed_outputs, key=lambda x: x[1])

    # Return the organized outputs
    return [output for output, _ in sorted_outputs]
def get_more_info1():
    temp_input = int(input("1 to reset all to do's\n2 to delete a single to do\ninput: "))
    if temp_input == 1:
        resettext()
    elif temp_input == 2:
        delete_one()
    else:
        print("Incorrect input")
        get_more_info1()
def delete_one():
    n = int(input("Choose the \"to do\" you want to know more about: "))
    for i in range(1, 99):
        #sorry for nesting, still really a beginner
        try:
            if i == n:
                file_path = os.path.join(cwd, 'todo.txt')
                with open(file_path, "r") as file:
                    content = file.read()
                lines = content.splitlines()
                line1 = f"{lines[(i*2)-2]}"
                line2 = f"{lines[(i*2)-1]}\n"
                print("---//---\n")
                print(line1)
                print(line2)
            else:
                pass
        except:
            break