import time
import pandas as pd
import numpy as np
import matplotlib
#matplotlib.use('Agg')  # Use a non-GUI backend 
import matplotlib.pyplot as plt
import os as os
import tempfile

def is_directory_writable(directory='.'):
    #Check if the given directory is writablewith a test file.
    try:
        # Try to create a temporary file in the directory
        test_file = os.path.join(directory, '.test_write_permission')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        return True
    except (PermissionError, OSError):
        return False

def get_safe_save_path(filename):
    #Get a safe path to save files, using temp directory if current directory is not writable.
    if is_directory_writable():
        return filename
    else:
        # Use system temp directory as fallback
        temp_dir = tempfile.gettempdir()
        return os.path.join(temp_dir, filename)

def list_available_files():
    ## Lists and return all available CSV files in the current directory.
    csvfiles = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
    if not csvfiles:
        print("No CSV files found in the current directory. Add CSV files to the current directory and try again.")
        exit()
    else:
        print("Available CSV files:")
        for file in csvfiles:
            print(file)
        print(f"Total number of files: {len(csvfiles)}")
        return csvfiles

def get_filters(csvfiles):
    # Asks user to specify a city, month, and day to analyze.
    #(str) city - name of the city to analyze
    #(str) month - name of the month to filter by, or "all" to apply no month filter
    #(str) day - name of the day of week to filter by, or "all" to apply no day filter

    # print('Explore some US bikeshare data from the CSV files listed above.')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityFile = input("Please enter the city csv file you want to analyze from the list above:").lower()
    #Adds the .csv extension if it dones't exists
    if not cityFile.endswith('.csv'):
        cityFile = cityFile + ".csv"
    
    #Check if the city file exists in the current directory
    if cityFile not in csvfiles:
        print(f"The file {cityFile} is not available in the current directory. Please select from the available files: {csvfiles}")
        return None, None, None
    #Replace the spaces with underscores
    cityFile = cityFile.replace(" ", "_")

    # get user input for month (all, january, february, ... , december)
    month = input("Please enter the month you want to analyze (all, january, february, ... , december): ").lower()
    #Check if the month is valid and if not, set the filter to 'all' by default
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december','all']
    if month not in months:
        print(f"Invalid month: {month}. Month filter set to 'all' by default.")
        month = 'all'

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day of the week you want to analyze (all, monday, tuesday, ... sunday): ").lower()
    #Check that the day is valid and if not set the filter to 'all' by default
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    if day not in days:
        print(f"Invalid day: {day}. Day filter set to 'all' by default.")
        day = 'all'

    return cityFile, month, day # Returns the city file, month, and day filters


def load_data(cityFile, month, day):
    # Loads data for the specified city and filters by month and day if applicable.
    #   (str) cityFile - name of the city to analyze
    #   (str) month - name of the month to filter by, or "all" to apply no month filter
    #   (str) day - name of the day of week to filter by, or "all" to apply no day filter
    # Check that the file is valid and if not, return None
    if cityFile is None:
        print("No data available for the specified file.")
        return None # Returns None if the file is not valid instead of the dataframe

    df = pd.read_csv(cityFile)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Filter out the month if specified except 'all'
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        # Convert month name to index from 1 to 12
        if month not in months:
            #Set ravlue to all if the month is not valid
            month = 'all'
        else:# Get the month index (1-12) and filter the DataFrame
            month_index = months.index(month) + 1
            df = df[df['Start Time'].dt.month == month_index]
    #Filter out the day if specified except 'all'
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in days:
            day = 'all'
        else:
            # Get the day index (0-6) and filter the DataFrame
            day_index = days.index(day)
            # Convert day name to index from 0 to 6
            # df2 = df['Start Time'].dt.dayofweek #Uncomment this to see the day of the week in the dataframe
            # Filter the DataFrame based on the day index
            df = df[df['Start Time'].dt.dayofweek == day_index]
    #Returns the dataframe after filtering
    if df.empty:
        print("No data available for the specified file and filters. Please try different file or filter day/month filter.")
        #End the function
        return None
    else:
        print(f"Data loaded successfully from {cityFile}. of {df.shape[0]} rows and {df.shape[1]} columns.")


    #Set the head index to 0 to initialize the loop.
    idx = 0
    #Prompt the user to display the first 5 rows of the dataframe
    while True and idx < len(df):
        display_data = input("Would you like to display the next 5 rows of the dataframe? (yes/no): ").lower()
        if display_data in ['yes', 'y', 1]:
            print("Displaying the next 5 rows of the dataframe:")
            print(df.iloc[idx:idx+5])
            #Increment the index to show the next 5 rows
            idx += 5
        else:
            break
    return df # Returns the no empty dataframe after filtering

def time_stats(df):
    if df is None:
        print("No data available to calculate time statistics.")
        return None
    
    # Displays statistics on the most frequent times of travel.
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # display the most common month
        df['month'] = df['Start Time'].dt.month
        most_common_month = df['month'].mode()[0]
        print(f"The most common month is: {most_common_month}")
        #Creates the Figure
        fig1 = plt.figure(figsize=(10, 6))
        #Creates a new subplot for the months
        ax1 = fig1.add_subplot(221)
        #Plot the histogram of the most common months in the first subplot
        df['month'].hist(bins=12, edgecolor='black', ax=ax1)
        ax1.set_title('Months Histogram')
        ax1.set_ylabel('Frequency')
        ax1.set_xlabel('Month')
        #ax1.set_xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        plt.show(block=False) #Uncomment this to display the plot
    except KeyError:
        print("Error: 'Start Time' column is missing from the data.")
    except Exception as e:
        print(f"Warning: Could not save plot due to error: {e}")
    finally:
        if 'fig1' in locals() and fig1:
            plt.close(fig1)  # Close the figure to free memory
        print(f"\nThis took {((time.time() - start_time) * 1000):.1f} ms.")

def station_stats(df):
    if df is None:
        print("No data available to calculate station statistics.")
        return None
    #Displays statistics on the most popular stations and trip.
    print('\nCalculating The Most Popular Stations and Trip...\n')
    #Start the timer
    start_time = time.time()

    try:
        # display most commonly used start station
        start_station_mode0 = df['Start Station'].mode()[0]
        print(f"The most commonly used start station is: {start_station_mode0}")

        # display most commonly used end station
        end_station_mode0 = df['End Station'].mode()[0]
        print(f"The most commonly used end station is: {end_station_mode0}")

        #Create a new series in the data frame that combines the start and end stations
        df['Start to End Station'] = df['Start Station'] + " to " + df['End Station']

        # display most frequent combination of start station and end station trip
        Start_to_end_station_mode0 = df['Start to End Station'].mode()[0]
        #Print the mode common combination of start to end station
        print(f"The most common start to end station is: {Start_to_end_station_mode0}")
    except KeyError:
        print("Error: 'Start Station' column is missing from the data.")
    except Exception as e:
        print(f"Warning: Could not save plot due to error: {e}")
    finally:
        if 'fig1' in locals() and fig1:
            plt.close(fig1)  # Close the figure to free memory
    print(f"\nThis took {((time.time() - start_time) * 1000):.1f} ms.")


def trip_duration_stats(df):
    if df is None:
        print("No data available to calculate trip duration statistics.")
        return None
    
    if 'Trip Duration' not in df.columns:
        print("No duration data available to calculate trip duration statistics.")
        return None
    
    #Displays statistics on the total and average trip duration.
    print('\nCalculating Trip Duration...\n')
    #Start the timer
    start_time = time.time()

    # Sums the total travel time in days and prints it
    total_travel_time = df['Trip Duration'].sum() / (3600 * 24)  # Convert seconds to days
    print(f"Total travel time: {total_travel_time:.2f} days")

    # Calculates and prints the mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60  # Convert seconds to minutes
    print(f"Mean travel time: {mean_travel_time:.2f} minutes")

    #Calculate and prints the travel time standard deviation in minutes
    travel_time_std = df['Trip Duration'].std() / 60
    print(f"Standard deviation of travel time: {travel_time_std:.2f} minutes")

    #Creates a new figure for the trip duration
    fig2 = plt.figure(figsize=(10, 6))
    ax4 = fig2.add_subplot(111)
    #Plot the histogram of the trip duration wit 30 bins from 0 to the max trip duration
    max_duration = df['Trip Duration'].max()
    #Calculate the bin range from zero to triple the mean in to 30bins
    bin_range = np.linspace(0, (mean_travel_time + (3*travel_time_std)) * 60, 30)
    df['Trip Duration'].hist(bins=bin_range, edgecolor='black', ax=ax4)
    ax4.set_title('Trip Duration Histogram')
    ax4.set_xlabel('Trip Duration (seconds)')
    ax4.set_ylabel('Frequency')
    plt.show() #Uncomment this to display the plot
    save_path = get_safe_save_path('trip_duration_stats.png')
    try:
        plt.savefig(save_path)
        print(f"Trip duration plot saved as '{save_path}'")
    except PermissionError:
        print(f"Warning: Could not save to '{save_path}' - permission denied")
    except Exception as e:
        print(f"Warning: Could not save plot due to error: {e}")
    finally:
        plt.close(fig2)  # Close the figure to free memory

    #End the timer and print the time taken
    print(f"\nThis took {((time.time() - start_time) * 1000):.1f} ms.")


def user_stats(df):
    if df is None:
        print("No data available to calculate user statistics.")
        return None
    if 'User Type' not in df.columns:
        print("No user type data available to calculate user statistics.")
        return None
    
    #Displays statistics on bikeshare users.
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_value_counts = df['User Type'].value_counts()
    print(f"Counts of user types: {user_types_value_counts}")

    # Display counts of gender if available
    if 'Gender' in df.columns:
        gender_value_counts = df['Gender'].value_counts()
        print(f"Counts of gender: {gender_value_counts}")
    else:
        print("Counts of gender: Not available")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {most_recent_year}")
        print(f"Most common year of birth: {most_common_year}")
    else:
        print("No Birth Year data available.")

    print(f"\nThis took {((time.time() - start_time) * 1000):.1f} ms.")

def main():
    while True:
        #Find and list the available CSV files in the current directory
        csvfiles = list_available_files()
        #Get the city, month, and day filters from the user
        cityFile, month, day = get_filters(csvfiles)
        #Load the data based on the user's input
        df = load_data(cityFile, month, day)
        #Calculate and display the time statistics
        time_stats(df)
        #Calculate and display the station statistics
        station_stats(df)
        #Calculate and display the trip duration statistics
        trip_duration_stats(df)
        #Calculate and display the user statistics
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' and restart.lower() != 'y':
            break
if __name__ == "__main__":
    #Loads the main function to start the program
	main()
