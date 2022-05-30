"""l={1:5,
2:"naa",
3:"mzd",
"vamsi":"madhuri"
}
print(l["vamsi"],l.get(3),l.get(7,"madhu"),l.get(1,"vghbjn"),"\n\n")
l["k"]="pyaar"

del l["vamsi"]
print(l)
m={5:0,"m":"madhuti"}
f={1,2,3}
g={"bnm","esdrftgh","gvbh","sdfghjk"}
z=dict(zip(f,g))

print(z) """
#we have to use array method to use array in python
#we have to import array to use array
import array as a
b=a.array("i",[1,2,3,4,5,6])
print(b.buffer_info(),b.typecode)

b.pop(2)
b.append(8)
b.remove(2)
b.insert(1,7)
b.extend([0,0])
print(b)
b.reverse()
print(b)
b.append(7)
print(b.index(8),b.count(7))
print(b[::-1])

for i in range(len(b)):
    print(b[i])
for i in b:
    print(i,end=" ")  
print("\n")    

#new array with  same array(array comprehension)
newarr=a.array(b.typecode,[i*i for i in b])     
print("newarray",newarr)


#values from user
y=a.array("i",[])  #empty array
print(y,len(y))
n=int(input("enter length of array"))
for i in range(n):
    z=int(input("enter number"))
    y.append(z)
print(y)   

#search for an element

k=int(input("enter ele to search"))
for i in y:  #using index method
    if i==k:
        print(y.index(i))
for i in range(len(y)):   #manually
    if y[i]==k:
        print(i)

