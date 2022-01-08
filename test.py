file1 = open('hello.cpp', 'r')
Lines = file1.readlines()

# for line in Lines:
#     print(line)
import json
import ast

mystring = "['#include<iostream>', 'using namespace std;', '']"
s = ast.literal_eval(mystring)
r = json.dumps(s)
print(r)

