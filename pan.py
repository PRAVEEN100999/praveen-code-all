import pandas as pd
data = [1,2,3,4]
# series1 =pd.Series(data)
# print(series1)
# print(type(series1))
# #changing the index
# series1 =pd.Series(data,index = ['a','b','c','d'])

# print(series1)
# #creating a dataframe
# df = pd.DataFrame(data)
# print(df)
# #data frame using dict
# dict = {'fruits':['apple','banana','mangoes'],'count':[12,32,15]}
# di = pd.DataFrame(dict)
# print(di)
# # creating a data frame using a numpy array
# import numpy as np
# numpyary = np.array([[200000,3000000],['om','ram']])
# dff = pd.DataFrame({'name':numpyary[1],'salary':numpyary[0]})
# print(dff)


# merge opretion
# player = ['p1','p2','p3']
# point = [8,9,6]
# title = ['gm1','gm2','gm3']
# df1 = pd.DataFrame({'player':player,'points':point,'tite':title})
# print(df1)

# player = ['p1','p5','p6']
# power = ['punch','kick','defence']
# title = ['gm1','gm5','gm6']
# df2 = pd.DataFrame({'player':player,'power':power,'tite':title})
# print(df2)

# print(df1.merge(df2, on='tite', how='inner'))

# print(df1.merge(df2, on='tite', how='left'))



# # join operation 
# player = ['p1','p2','p3']
# point = [8,9,6]
# title = ['gm1','gm2','gm3']
# df3 = pd.DataFrame({'player':player,'points':point,'tite':title},index = ['L1','L2','L3'])
# print(df3)


# player = ['p1','p5','p6']
# power = ['punch','kick','defence']
# title = ['gm1','gm5','gm6']
# df4 = pd.DataFrame({'players':player,'power':power,'tites':title},index = ['L2','L3','L4'])
# print(df4)


# print(df3.join(df4, how = 'inner'))


# # concatination

# print(pd.concat([df3,df4]))


# csv file read

cars = pd.read_csv("sale.csv")
# print(cars)
# print(cars.head())
# print(cars.tail())
# print(cars.info(null_counts=True))
# print(cars.mean())
# print(cars.median())
# print(cars.std())
# print(cars.max())
# print(cars.min())
# print(cars.count())
# print(cars.describe())


cars = cars.rename(columns = {'Product':'Productss'})
# print(cars.head())
cars.Latitude = cars.Latitude.fillna(cars.Latitude.mean())


cars = cars.drop(columns =['State'])
# print(cars.info(null_counts=True))
f = cars[['Latitude','Longitude','City','Price','Account_Created']].corr()
# print(f)
cars.Latitude = cars.Latitude.astype(int)
# print(cars.info(null_counts= True))

#manipulating
# print(cars.iloc[:,4])
# print(cars.iloc[0:5,4])
# print(cars.loc[:,"Price"])

cars['praveen'] = 1

f = lambda x:x*2
cars['praveen'] = cars['praveen'].apply(f)
# print(cars)
# print(cars.sort_values(by = 'Latitude'))

# print(cars['Latitude']>25)

# fit = cars['Latitude'] > 45
# fit1 = cars[fit]
# print(fit1)

fit2 = (cars['Latitude'] > 45)&(cars['Longitude']>35)
fit3 = cars[fit2]
print(fit3)