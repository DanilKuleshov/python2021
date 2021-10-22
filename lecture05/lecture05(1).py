cnt = 0
a = 0
st = ''
m = []
f = open("numbers.txt")
n = sum(1 for _ in f) #считаем кол-во строк в нашем файле
f.close()
f = open(".txt")
for i in range(n):
    cnt+=1
    st = f.readline()
    m.append(int(st))
f.close()
print(m)

for i in range(0, n-2):
    for j in range(1,n-1):
        for k in range(2,n):
            if m[i]+m[j]+m[k] == 2020:
                print(m[i],m[j],m[k])
                print(m[i]*m[j]*m[k])

