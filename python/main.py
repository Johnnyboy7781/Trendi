import csv

print("Welcome to the Trendi Algorithm! Below, csv values will be stored and processed.")

#print("__name__ value: ", __name__)
highVolumes = []
largeDrop = []
largeGain = []
sumCollection = []
avgCollection = []
orig_data = []
headers = []
dates = []
opens = []
highs = []
lows = []
closes = []
adj_closes = []
volumes = []
stdDev = []

#Change this so things are passed by reference, arrays are defined in main, and printFindings() can be called from main
#Make orig_data into 2D array?
#This is where the algorithm happens. Starting with finding totals and averages, then looking at % changes
def findChanges():
    print("\nFinding Changes...\n")

    for i in range(0, 6):
        sumCollection.append(float(0))
        avgCollection.append(float(0))
        #print("sumCollection", end = " ")
        #print(j, end = "")
        #print(": ", sumCollection[j])
    for i in range(0, len(dates)):
        sumCollection[0] += float(opens[i])
        sumCollection[1] += float(highs[i])
        sumCollection[2] += float(lows[i])
        sumCollection[3] += float(closes[i])
        sumCollection[4] += float(adj_closes[i])
        sumCollection[5] += float(volumes[i])

    # for j in range(0, 6):
    #     print("sumCollection", end = " ")
    #     print(j, end = "")
    #     print(": ", sumCollection[j])

    for i in range(0, 6):
        sumCollection[i] = round(sumCollection[i], 2)
        avgCollection[i] += round(sumCollection[i]/len(dates), 4)

    #Calculating DAILY Standard deviation of the set
    for i in range(0, len(dates)):
        value = ((highs[i]-lows[i])-(opens[i]-closes[i]))^2 #Need to figure out which values I'm going to use
        stdDev.append(value)

    total = float(0)
    for i in range(0, len(dates)):
        total += stdDev[i]
    stdDevWholeData = total/len(dates)
    print("Standard Deviation:", end=" ")
    print(stdDevWholeData)

    #Finding days of interest
    for i in range(0, len(dates)):
        if volumes[i]/avgCollection[5] >= 1.40:
            highVolumes.append(dates[i])
        #Only accounts for a single day, should be dynamic and start watching interesting activity (follow through on potential past days)
        if closes[i]/opens[i] >= 1.05:
            largeGain.append(dates[i])
        elif highs[i]/lows[i] >= 1.05:
            largeGain.append(dates[i])
        if opens[i]/closes[i] >= 1.05:
            largeDrop.append(dates[i])
        elif highs[i]/lows[i] <= 0.95:
            largeDrop.append(dates[i])


def printFindings():
    print("\nPrinting Findings...\n")

    # Printing headers, the csv column headers as labels
    for a in range(0, len(headers)):
        print(headers[a], end="           ")
    print()

    print("\nDates with drops 5% or more include...")
    for b in range(0, len(largeDrop)):
        index = dates.index(largeDrop[b])
        print(dates[index], end="     ")
        print(opens[index], end="     ")
        print(highs[index], end="     ")
        print(lows[index], end="     ")
        print(closes[index], end="     ")
        print(adj_closes[index], end="     ")
        print(volumes[index], end="     \n")
    print("\nDates with gains by 5% or more include...")
    for c in range(0, len(largeGain)):
        index = dates.index(largeGain[c])
        print(dates[index], end="     ")
        print(opens[index], end="     ")
        print(highs[index], end="     ")
        print(lows[index], end="     ")
        print(closes[index], end="     ")
        print(adj_closes[index], end="     ")
        print(volumes[index], end="     \n")
    print("\nDates with increased trading volume by 40% or more above average...")
    for d in range(0, len(highVolumes)):
        index = dates.index(highVolumes[d])
        print(dates[index], end="     ")
        print(opens[index], end="     ")
        print(highs[index], end="     ")
        print(lows[index], end="     ")
        print(closes[index], end="     ")
        print(adj_closes[index], end="     ")
        print(volumes[index], end="     \n")


def main():
    #The csv file must be included in the same directory to be referenced like this. Using this one as a test dummy rn
    f = open('JNJ.csv')

    #Object in python that allows us to pull out data from the csv
    csv_f = csv.reader(f)

    #Saving the data
    for row in csv_f:
        orig_data.append(row)

    for x in range(0, 7):
        headers.append(orig_data[0][x])
    orig_data.pop(0)

    for entry in orig_data:
        dates.append(entry[0])
        opens.append(float(entry[1]))
        highs.append(float(entry[2]))
        lows.append(float(entry[3]))
        closes.append(float(entry[4]))
        adj_closes.append(float(entry[5]))
        volumes.append(float(entry[6]))


    findChanges()

    printFindings()

    f.close()

if __name__ == '__main__':
    main()
