import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'DenverTemps2020.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
# Get high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[3])
        low = int(row[4])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
# Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.5)
# Format plot.
    ax.set_title("Daily high and Low Temperatures for Denver - 2020", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
