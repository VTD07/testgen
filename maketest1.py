import subprocess, os

test = input('Generate file (Empty if you don\'t need to generate input): ')
task = input('Task file (Empty if you don\'t need to generate output): ')

currpos = os.path.dirname(__file__)
test_cpp = f"{test}.cpp"
task_cpp = f"{task}.cpp"
test_exe = f"{test}.exe"
task_exe = f"{task}.exe"

def checkfile(name2, path): 
    for files in os.walk(path): 
        for check in files: 
            if name2 in check: 
                return True
    return False

def runfile(name1_cpp, name2_exe): 
    x = subprocess.getoutput(f'g++ {name1_cpp} -o {name2_exe}')
    if x != "":
        print(f"Error in {name1_cpp} file")
        print(x)
        quit()
    else: 
        print(f"File {name1_cpp} compiled")

# Check if test file exists
if test != "":
    if not checkfile(test_cpp, currpos):
        print("Put test file in the same place as maketest file")
        quit()

# Check if task file exists
if task != "":
    if not checkfile(task_cpp, currpos): 
        print("Put task file in the same place as maketest file")
        quit()

# Compile the test and task files if they exist
if test != "":
    runfile(test_cpp, test_exe)

if task != "":
    runfile(task_cpp, task_exe)

prefix = input('Problem name: ')
filename = input('File test name: ')
start = int(input('Start testcase index: '))
end = int(input('End testcase index: '))

# Validation of start and end indices
assert start >= 0, 'The starting index cannot be a negative integer'
assert start < end, 'The starting index must be less than the ending index'
assert end <= 1000, 'The ending index must be less than or equal to 1000'

# Create directory if it doesn't exist
if not os.path.exists("TESTALL"):
    os.mkdir("TESTALL")
path=os.path.join("TESTALL",prefix)
if not os.path.exists(path): 
    os.mkdir(path)
# Generate input/output files for each test case
for index in range(start, end+1):
    total=f'{filename}{index:02d}'
    fullpath=os.path.join(path,total)
    os.makedirs(fullpath,exist_ok=True)
    input_filename = os.path.join(fullpath, f'{prefix}.inp')
    output_filename = os.path.join(fullpath, f'{prefix}.out')
    if test:
        with open(input_filename, 'w', encoding='utf-8') as file:
            # Use the compiled .exe directly without './'
            subprocess.run([test_exe], stdout=file)
        print(f'Done generating input for test case {index}')

    if task:
        with open(input_filename, 'r', encoding='utf-8') as fin:
            with open(output_filename, 'w', encoding='utf-8') as fout:
                # Use the compiled .exe directly without './'
                subprocess.run([task_exe], stdin=fin, stdout=fout)
        print(f'Done generating output for test case {index}')
