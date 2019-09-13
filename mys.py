import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "kumar09",
    database = "ram"
)

mycursor = mydb.cursor()
# show database
# mycursor.execute("show databases")
 
# for i in mycursor:
#     print(i) 

#create table 
# mycursor.execute("CREATE TABLE kumar (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),address VARCHAR(20))")
# for x in mycursor:
#     print(x)

# mycursor.execute("ALTER TABLE OM ADD COLUMN rollno INT")
# mycursor.execute("")
# print(mycursor)

sql = "INSERT INTO om(id,name,address) VALUES(%s,%s,%s)"
val =[ 
    ('1','praveen','abu'),
    ('3','raku','abuur'),
    ('2','pushu','abur')
]
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")