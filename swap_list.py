# def swap(c,i):
#     c[i] , c[i+1] = c[i+1] , c[i]
#     print(c)

def cons(c):
    new_lis = c
    for i in range(len(c)-1):
        #new_lis= swap(lis,i)
        temp = i
        c[temp] , c[temp+1] = c[temp+1] , c[temp]
        print(c)       
        c[temp] , c[temp+1] = c[temp+1] , c[temp]
        
cons([2,3,2,3,2])
