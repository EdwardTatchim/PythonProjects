
lst_ex = open("list.txt","w")

a = str(51)
b = str(-113)
c= str(10)
d = str(56)
e = str(-125)
f = str(2)
abc = []

ap = abc.append(a)
ap = abc.append(b)
ap = abc.append(c)
print(ap)
lst_ex.write(ap)

ap = abc.append(d)
ap = abc.append(e)
ap = abc.append(f)
print(ap)
lst_ex.write(ap)

print(lst_ex)

lst_ex.close()
