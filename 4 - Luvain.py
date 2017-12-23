L = []                           
for i in range(100,1000):         
    for j in range(100,1000):     
        a = i * j            
        b = str(a)               
        c = b[::-1]              
        if cmp(b,c)==0:          
            L.append(a)          
print max(L)