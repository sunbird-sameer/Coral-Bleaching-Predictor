#pip installs

#pip install pandas
#pip install scikit-learn

# Imports
import pandas
from sklearn.linear_model import LinearRegression
from time import strftime

# Current year + month
year = int(strftime("%Y"))


month = int(strftime("%m"))
month = int(month/12*100)

# Current year + this month + 7 weeks
month2 = int(strftime("%m"))
month2 = int(month + float(0.61096)/12*100)

# both the current month and the next 7 weeks added to this month
year2 = float(str(year) + '.' + str(month2))
year = float(str(year) + '.' + str(month))


# Reading the data
data = pandas.read_csv('Mean_Sea_Temperature-Nasa_1997-2021.csv')

# Defining the model
model = LinearRegression()

# Training the model
model.fit(data[['Year']], data[['No_Smoothing']])

# Print Blank Seperater Line
print("\n")


# Current year prediction as a variable
prediction = model.predict([[year]])
print(prediction)

prediction2 = model.predict([[year2]])
print(prediction2)

# Print Blank Seperater Line
print("\n")

#warning

if prediction and prediction2 >= 0.8:
    print("There is going to be a coral bleaching in the next 6-8 (avg= 7 weeks) weeks")


else:
    print("There isn't going to be a coral bleaching in the next 6-8 (avg= 7 weeks) weeks")

# Print Blank Seperater Line
print("\n")

