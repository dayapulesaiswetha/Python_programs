import json

def read_file():

    #with open('sample2.json') as f:
    f = open('sample2.json')
    line = json.load(f)
    
    print(line['name'])

read_file()

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)