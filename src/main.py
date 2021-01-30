import csv

print("Welcome to the Trendi Algorithm! Below, csv values will be stored and processed.")

#print("__name__ value: ", __name__)

#This is where the algorithm happens. Starting with finding totals and averages, then looking at % changes
def find_changes(dates, opens, closes, highs, lows, adj_closes, volumes):
    sumCollection = []
    avgCollection = []
    for i in range(0, len(dates)-1):
        sumCollection[0] += float(opens[i])
        sumCollection[1] += float(highs[i])
        sumCollection[2] += float(lows[i])
        sumCollection[3] += float(closes[i])
        sumCollection[4] += float(adj_closes[i])
        sumCollection[5] += float(volumes[i])

    for i in range(0, 5):
        sumCollection[i] += round(sumCollection[0], 2)
        avgCollection[i] += round(sumCollection[i]/len(dates))

    print("Days which are found to have higher trading rate and most dramatic changes...\n")
    highVolumes = []
    largeDrop = []
    largeGain = []
    for i in range(0, len(dates)-1):
        if volumes[i]/avgCollection[5] >= 1.33:
            highVolumes.append(dates[i])
        if (opens[i]/closes[i] >= 1.20):
            largeDrop.append(dates[i])


def main():
    #The csv file must be included in the same directory to be referenced like this. Using this one as a test dummy rn
    f = open('JNJ.csv')

    orig_data = []
    headers = []
    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    adj_closes = []
    volumes = []
    #Object in python that allows us to pull out data from the csv
    csv_f = csv.reader(f)

    #Saving the data
    for row in csv_f:
        for x in range(0, 6):
            orig_data.append(row[x])

    for x in range(0, 6):
        headers.append(orig_data[0])
        orig_data.pop(0)

    for entry in orig_data:
        dates.append(row[0])
        opens.append(row[1])
        highs.append(row[2])
        lows.append(row[3])
        closes.append(row[4])
        adj_closes.append(row[5])
        volumes.append(row[6])
        for x in range(0, 6):
            orig_data.pop(0)

    #Printing the csv column headers as labels
    for j in range(0, len(headers)):
        print(headers[j], end = "        ")


    f.close()

if __name__ == '__main__':
    main()
