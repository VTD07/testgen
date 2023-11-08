import subprocess, os

test = input('Generate file (Empty if you don\'t need to generate input): ')
task = input('Task file (Empty if you don\'t need to generate output): ')

currpos=os.path.dirname(__file__)
test_cpp="%s.cpp" %(test)
task_cpp='%s.cpp' %(task)
test_exe='%s.exe' %(test)
task_exe='%s.exe' %(task)
check1=False

def checkfile(name2,path): 
    for files in os.walk(path): 
        for check in files: 
            if name2 in check: 
                return True
    return False

def runfile(name1_cpp,name2_cpp): 
    x=subprocess.getoutput('g++ ' + name1_cpp + ' -o' + name2_cpp)
    if x!="":
        print("error in %s.file"%(name1_cpp))
        print(x)
        quit()
    else: print("file %s complied"%(name1_cpp))

if test!="":
    if(checkfile(test_cpp,currpos))==False:
        print("Put test file in the sameplace as maketest file")
        quit()

if task!="":
    if(checkfile(task_cpp,currpos))==False: 
        print("Put task file in the sameplace as maketest file")
        quit()

runfile(test_cpp,test_exe)

runfile(task_cpp,task_exe)

prefix = input('Prefix test case: ')
start = int(input('Start testcase index: '))
end = int(input('End testcase index: '))
assert start >= 0, 'The starting index cannot be a negative integer'
assert start < end, 'The starting index must be less than the ending index'
assert end <= 100, 'The ending index must be less than or equal to 100'


if not os.path.exists(prefix):
    os.mkdir(prefix)

for index in range(start, end):
    input_filename = os.path.join(prefix, '{filename}_{index}.inp'.format(filename=prefix, index=index))
    output_filename = os.path.join(prefix, '{filename}_{index}.out'.format(filename=prefix, index=index))

    if test:
        with open(input_filename, 'w', encoding='utf-8') as file:
            subprocess.run(['./' + test], stdout=file)
        print('Done generating input for test case', index)

    if task:
        with open(input_filename, 'r', encoding='utf-8') as fout:
            with open(output_filename, 'w', encoding='utf-8') as file:
                subprocess.run(['./' + task], stdin=fout, stdout=file)
        print('Done generating output for test case', index)
