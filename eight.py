user = {'name':'ram','age':24}
print(user)
print(type(user))
user1 = dict(name = 'ram',age = 24)
print(user1)
print(type(user1))
print(user['name'])
user_info ={}
user_info['name']= 'ram'

user_info['age'] = 189
print(user_info)
if 'nam' in user_info:
    print('present')
else:
    print('not present') 
if 'ram' in user_info.values():
    print('present')
else:
    print('not present') 
if 189 in user_info.values():
    print('present')
else:
    print('not present')  
a = [1,2,3,4,5]      
user_info['lis']  = a
print(user_info)
a = user_info.values()#value method for print values 
print(a)
a = user_info.keys()#key method for print values 
print(a)
for i,j in user_info.items():# item method
    
    print(f"key is {i} and value is {j}")