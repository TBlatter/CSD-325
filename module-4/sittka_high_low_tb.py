#Tyson Blatter 4/5/2025 4.2
import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


# code to plot the highs and lows
def plot_temperatures(dates, temps, color, title):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


# code to load data from CSV
def load_data():
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high and low temperatures from the file
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))

    return dates, highs, lows


# Main menu function
def main_menu():
    print("Welcome to Tyson's weather program.")
    print("\nPlease select an option:")
    print("1 - View High Temperatures")
    print("2 - View Low Temperatures")
    print("3 - Exit")


# the code that is shown based on what user's picked.
#Also a loop
def main():
    dates, highs, lows = load_data()  # Load the weather data
    while True:
        main_menu()  # Display the menu
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            plot_temperatures(dates, highs, 'red', 'Daily High Temperatures - 2018')

        elif choice == '2':
            plot_temperatures(dates, lows, 'blue', 'Daily Low Temperatures - 2018')

        elif choice == '3':
            print("Thank you for using Tyson's weather program. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
