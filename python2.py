def inter(l1,l2):
    # s1 = set(l1)
    # s2 = set(l2)
    # s3 = s1 & s2
    # print(s3)
    new_l3 = []
    # t1 = tuple(l1)
    # t2 = tuple(l2)
    new_dict ={}
    for i, values in enumerate(l1):
        new_dict[values] = i
    print(new_dict)

    
    for i in l2:
        if i in new_dict:
            new_l3.append(i)
    print(new_l3) 


l1 = [10, 20, 30, 35, 50] 
l2 = [5, 10, 15, 16, 50]
inter(l1,l2)