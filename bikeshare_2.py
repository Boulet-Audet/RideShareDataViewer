import time
import pandas as pd
import numpy as np
import os as os

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def list_available_files():
    ## Lists and return all available CSV files in the current directory.
    csvfiles = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
    if not csvfiles:
        raise FileNotFoundError("No CSV files found in the current directory.")
    print("Available CSV files:")
    for file in csvfiles:
        print(file)
    print("Please select a file from the list of CSV above in the current working directory.")
    return csvfiles


def get_filters(csvfiles):
    # Asks user to specify a city, month, and day to analyze.
    #Returns:
    #   (str) city - name of the city to analyze
    #   (str) month - name of the month to filter by, or "all" to apply no month filter
    #   (str) day - name of the day of week to filter by, or "all" to apply no day filter

    print('Explore some US bikeshare data from the CSV files listed above.')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityFile = input("Please enter the city csv file you want to analyze ").lower()
    #Adds the .csv extension if it dones't exists
    if not cityFile.endswith('.csv'):
        cityFile = cityFile + ".csv"
    
    #Check if the city file exists in the current directory
    if cityFile not in csvfiles:
        raise ValueError(f"The file {cityFile} is not available in the current directory. Please select from the available files: {csvfiles}")

    #Replace the spaces with underscores
    cityFile = cityFile.replace(" ", "_")

    # get user input for month (all, january, february, ... , december)
    month = input("Please enter the month you want to analyze (all, january, february, ... , december): ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day of the week you want to analyze (all, monday, tuesday, ... sunday): ").lower()

    return cityFile, month, day


def load_data(cityFile, month, day):
    # Loads data for the specified city and filters by month and day if applicable.
    #   (str) cityFile - name of the city to analyze
    #   (str) month - name of the month to filter by, or "all" to apply no month filter
    #   (str) day - name of the day of week to filter by, or "all" to apply no day filter
    # Returns:
    #    df - Pandas DataFrame containing city data filtered by month and day
    df = pd.read_csv(cityFile)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Filter out the month if specified except 'all'
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        # Convert month name to index from 1 to 12
        if month not in months:
            raise ValueError(f"Invalid month: {month}. Please choose from {months}.")
        # Get the month index (1-12) and filter the DataFrame
        month_index = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month_index]
    #Filter out the day if specified except 'all'
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in days:
            raise ValueError(f"Invalid day: {day}. Please choose from {days}.")
        # Get the day index (0-6) and filter the DataFrame
        day_index = days.index(day)
        # Convert day name to index from 0 to 6
        df = df[df['Start Time'].dt.dayofweek]
        # Filter the DataFrame based on the day index
        df = df[df['Start Time'] == day_index]
    #Returns the dataframe after filtering
    if df.empty:
        raise ValueError("No data available for the specified filters. Please try different filters.")
    print(f"Data loaded successfully from {cityFile}.")
    print(f"DataFrame shape: {df.shape}")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        csvfiles = list_available_files()
        cityFile, month, day = get_filters(csvfiles)
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#Find and list the available CSV files in the current directory
list_available_files()

if __name__ == "__main__":
	main()
