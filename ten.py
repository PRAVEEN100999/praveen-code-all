a =[]# simple method 
for i in range(1,11):
    a.append(i**2)
print(a)    
a1 = [i**2 for i in range(1,11)]# list comprehesion 
print (a1)
def rev(l):# normal
    name=[]
    for i in l:
        name.append(i[::-1])
    return(name) 
print(rev(['abc','asd','pra']))   
def rev1(l):# comprehension
    name2 =[i[::-1] for i in l]
    return(name2)
print(rev1(['abc','asd','pra']))  
squre = {n:n**2 for n  in range(1,11)} 
print(squre) 
string = "praveen"# dict comprehension
countt ={char:string.count(char) for char in string}
print(countt)
s = {k**2  for k in range (1,11)}
print(s)
