import time
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Input a city")
    while city not in CITY_DATA.keys():
        print("Invalid input, Please try again..")
        city = input("Please input a city")
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Thanks, input a month..(all, january, february...,june")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Input day of week, (all, monday, tuesday..sunday)")
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city], header=0)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month.lower() != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f" Popular month is {popular_month}")
    # TO DO: display the most common day of week
    popular_day_of_wk = df['day_of_week'].mode()[0]
    print(f"Popular day of week is {popular_day_of_wk}")
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"Popular Hour is {popular_hour}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    print(f"Popular station is {popular_station}")
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Popular end station is {popular_end_station}")
    # TO DO: display most frequent combination of start station and end station trip
    start_station = df['Start Station'].mode()[0]
    end_station = df['End Station'].mode()[0]
    s = pd.Series([start_station, end_station])
    concatenated = s.str.cat(sep=",")
    print(f"Most popular start and end station {concatenated}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    start_time_df = pd.to_datetime(df['Start Time'])
    end_time_df = pd.to_datetime(df['End Time'])
    df['total_travel_time'] = end_time_df - start_time_df
    print(df['total_travel_time'].sum())
    # TO DO: display mean travel time
    print(df['total_travel_time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    df.drop(['total_travel_time'], axis=1, inplace=True)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    s = df['User Type']
    print(s.value_counts())
    # TO DO: Display counts of gender
    gender_cts = df['Gender']
    print(gender_cts.value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = str(df['Birth Year'].min())
    most_recent_year = str(df['Birth Year'].max())
    common_year = str(df['Birth Year'].mode()[0])
    series = pd.Series([earliest_year, most_recent_year, common_year])
    concatenated = series.str.cat(sep=",")
    print("Displaying earliest, most recent and most common yr of birth..")
    print(concatenated)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
