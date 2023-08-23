# #reverse the integer both positive and negative number
# def do_rev(inp):
#     string1 = str(inp)
#     if string1[0] == '-':
#         print(int('-'+ string1[:0:-1]))
#     else:    
#         print(int(string1[::-1]))

#
# #  l - 0   a -- 1  x --- 2  m    ---- 3    i ---- 4

# do_rev('-123')

#find the average length of the words in the sentence
# def length_words(str):
#     for p in "!?',:;.":
#         str = str.replace(p,' ')
#     words = str.split()
#     l1 = sum(len(word) for word in words)/len(words)
#     print(l1)

# #"I can do it"
# length_words('I can do it')

#find the non repeating character in the string and return its index

# def nonrepeat_char(str):
#     freq = {}
#     for i in str:
#         if i not in  freq:
#             freq[i] = 1
#         else:
#             freq[i] +=1
    
#     for i in range(len(str)):
#         if freq[str[i]] == 1:
#             return i
#     return -1

# print(nonrepeat_char('alphabet'))

#import collections

# def nonrepeat_char(str):
#     freq = collections.Counter(str) # it will assign number to each character 
#                                     # as per the number of repeatition
#     for i,ch in enumerate(str):
#         if freq[ch] == 1:
#             return i
#     return -1

# print(nonrepeat_char('numbernum'))

# find monolithic array
# def mono(ar1):
#     return(all(ar1[i]<=ar1[i+1] for i in range(len(ar1)-1)) or
#         all(ar1[i] >= ar1[i+1]  for i in range(len(ar1)-1))
#     )

# A=[1,2,3,4,1]

# print(mono(A))

# move all 0 to the end of the array

# def move_zero(A):
#     for i in A:
#         if 0 in A:
#             A.remove(0)
#             A.append(0)
#     print(A)

# A=[0,1,2,0,3,5,0]
# move_zero(A)

#find the none value and update it with the latest value

# def up_none(B):
#     i = 0
#     res = []
#     for j in B:
#         if j is not None:
#            res.append(i)
#            i = j
#         else:
#             res.append(i)
#     print(res)

# B = [None,None,2,None,None,3,None]
# up_none(B)

#Given two sentences, return an array that has the words that 
# appear in one sentence and not the other and an array 
# with the words in common. 

# sentence1 = 'We are really pleased to meet! you in our city'
# sentence2 = 'The city was hit, by a really heavy storm'

# def sol(sen1,sen2):
#     for i in "!,:;.":
#         sen1=sen1.replace(i,' ')
#         sen2=sen2.replace(i,' ')
#     s1=set(sen1.split())
#     s2=set(sen2.split())
#     return sorted(list(s1^s2)),sorted(list(s1&s2))

# print(sol(sentence1,sentence2))

# find the number of primenumbers between 1 and given number

# def prime_num(n):
#     l = []
#     for i in range(n):
#         if i > 1:
#             for j in range(2,i):
#                 if i%j == 0:
#                     break
#             else:
#                 l.append(i)
#     print(l)

# prime_num(10)


# Remove on alphabet and check for the palindrome or not
# def palin(str):
#     new_str = ""
#     for i in range(len(str)):
#         new_str = str[:i] + str[i+1:]
#         if new_str == new_str[::-1]:
#             return new_str
#         else:
#             continue
#     return "not palindrome"

# print(palin("radkar"))
    


#remove the consecutive duplicate characters in each string of 
#array of strings

# def rem_dup(ar):    
#     prev = ""
#     new_ar = []
#     for s in ar:
#         new_str = ""
#         for ch in s:
#             if len(new_str) == 0:
#                 new_str += ch
#                 prev = ch
#             elif ch == prev:
#                 continue
#             else:
#                 new_str += ch
#                 prev = ch
#         new_ar.append(new_str)        
#     return new_ar

    
# print(rem_dup(['unsuccessfully','happy']))


# str = "balnloon"
# dic = {'key1':'value1','key2':'value2'}
# print(str.count('n'))
# print(str.join(dic.values()))


