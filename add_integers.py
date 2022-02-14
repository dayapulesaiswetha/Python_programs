# add 2 number given as string arguments without using
#  inbuilt function

# def addStrings(string1,string2):
#     string1 = string1.strip()
#     string2 = string2.strip()
#     if not string1:
#         return string2
#     if not string2:
#         return string1
#     return str(str2num(string1) + str2num(string2))


# def str2num(numstr):
#     nums_map = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
#     '9':9}
#     num,count = 0,len(numstr)-1
#     for i in numstr:                        
#         num += (nums_map[i] * (10 ** count))        
#         count = count-1
#     return num


# print(addStrings("123","011"))


#Add 1 to the list of the array [1,2,3] so it would be 123 + 1 =124
# which would give us output [1,2,4]

def solution(digits):
    last_index = len(digits) -1 
    d = update_prev(digits,last_index)
    return d

def update_prev(lis,current_index):
    if lis[current_index] == 9:
        if current_index != 0:
            update_prev(lis,current_index-1)
            lis[current_index] = 0
        else:
            lis[current_index] = 1
            lis.append[0]
    else:
        lis[current_index] = lis[current_index] + 1
    return lis
    
digits = [9,9,9]
print(solution(digits))
