import pandas as pd
import os as os
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    filename = CITY_DATA[city]
    cwd = os.getcwd()
    filename = os.path.join(cwd, filename)
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    df = pd.read_csv(filename)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        #Capitalize the day to match the format in the dataframe
        day = day.capitalize()
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df
    
df = load_data('chicago', 'march', 'Friday')
#df = load_data('chicago', 'march', 'all')

#Print the dataframe head
print(df.head())
#Print the dataframe shape
print(df.shape)