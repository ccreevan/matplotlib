import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'

# reads header rows in CSV file
with open(filename) as f:
    weather = csv.reader(f)
    header_row = next(weather)
    station = next(weather)[1]

    # outputs data into lists
    highs, lows, dates = [], [], []
    for row in weather:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        tmax = int(row[5])
        tmin = int(row[6])

        highs.append(tmax)
        lows.append(int(tmin))
        dates.append(date)

with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)

    # outputs data into lists
    highs2, lows2, dates2 = [], [], []
    for row in reader2:
        try:
            highs2.append(int(row[5]))
        except ValueError:
            pass
        else:
            lows2.append(int(row[6]))
            dates2.append(datetime.strptime(row[2], '%Y-%m-%d'))

fig, ax = plt.subplots()
plt.style.use('seaborn')
ax.plot(dates, highs, c='blue', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

#ax.plot(dates2, highs2, c='red', alpha=0.5)
#ax.plot(dates2, lows2, c='red', alpha=0.5)
fig.autofmt_xdate()

plt.title(f'Temperature, {station}, 2018', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temp. Fahr.', fontsize=16)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
#plt.fill_between(dates2, highs2, lows2, facecolor='red', alpha=0.2)
plt.tick_params(axis='both', which='major')

plt.show()
