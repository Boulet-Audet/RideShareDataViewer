import pandas as pd

filename = 'chicago.csv'

## load data file into a dataframe
df = pd.read_csv(filename)

## convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

## extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

## find the most popular hour
popular_hour = df['hour'].mode()[0]
#Calculates the median value of the hour
median_hour = df['hour'].median()

# print value counts for each user type
user_types = df['User Type'].value_counts()

print('Most Popular Start Hour:', popular_hour)
print('The median Start Hour:', median_hour)
print(user_types)
