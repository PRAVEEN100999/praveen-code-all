import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("F:\om\Train.csv")
# print(data)
# print(data.head())
# print(data.describe())
data_ = data.loc[:,['humidity','temperature']]
# # print(data_.head(5))

data_.plot(x='humidity',y='temperature',style='o')
plt.xlabel('humidity')
plt.ylabel('temperature')
# plt.show()

x = pd.DataFrame(data_['humidity'])
y = pd.DataFrame(data_['temperature'])
# print(x.size , y.size)


from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y , test_size=0.2 , random_state=1)
# print(x_train.shape)
# print(y_train.shape)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
print(regressor.intercept_)
print(regressor.coef_)

y_pred = regressor.predict(x_test)
y_pred =pd.DataFrame(y_pred,columns = ['Predicted'])
print(y_pred)
