# def solution(num1,num2):
#     eval(num1) + eval(num2)
#     return str(eval(num1) + eval(num2))

# def solution(num1, num2):
#     n1, n2 = 0, 0
#     m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

#     for i in num1:
#         n1 += (ord(i) - ord("0")) * m1 
#         m1 = m1//10        

#         # n1 = 10, m1 = 10
#         # n1 = 10, m1 = 1

#     for i in num2:
#         n2 += (ord(i) - ord("0")) * m2
#         m2 = m2//10

#     return str(n1 + n2)

# def my_range():
#     for i in range(5):
#         print(i)

# print(my_range())
# # print(solution("10","20"))

s = 'rakar'
def solution(s):
    if s == s[::-1]:
        print('in if')
        return True
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        print(t)        
        if t == t[::-1]: return True

    
  
print(solution(s))