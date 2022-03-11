#Python program to print pascal triangle format


def pas_tri(n):
    new_lis = []
    for i in range(n):
        new_lis.append([])
        new_lis[i].append(1)
        if  i>0:
            for m in range(1,i):
                new_lis[i].append(new_lis[i-1][m-1] + new_lis[i-1][m])
            if(n!= 0):
                new_lis[i].append(1)
    
    print(new_lis)

pas_tri(3)
        
        
        
