def palin(a):
    real = a
    b = real[::-1]
    if a==b:
        return "palindrome " 
    return "not palin"    

name = input("enter your name :")
print(f"your name is{palin(name)} ")    