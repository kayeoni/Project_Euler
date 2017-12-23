def spe_pytha_tri(n):
    for i in range(1,int(n/3)+1):
        for k in range(int(n/3)-1,n-2):
            for j in range(i+1,k):
                if pow(i,2) + pow(j,2) == pow(k,2) and i + j + k == n:
                    return (i,j,k,i*j*k)

print(spe_pytha_tri(12)) #return 3,4,5 // 12
print(spe_pytha_tri(30)) #return 5,12,13 // 780
print(spe_pytha_tri(24)) #return 6,8,10 // 480
print(spe_pytha_tri(1000)) #return 200,375,425 // 31875000