import csv
import math

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
stabilityHigh = float(0)
stabilityClose = float(0)
varianceHigh = float(0)
varianceClose = float(0)
stocks = ["JNJ.csv", "COST.csv", "CL.csv", "RSG.csv", "AMC.csv", "BTC-USD.csv", "DOGE-USD.csv", "GME.csv", "SIEB.csv"]

#Function for seeking trends and exceptions in the data
def findChanges():
    print("\nFinding Changes...\n")

    for entry in orig_data:
        dates.append(entry[0])
        opens.append(float(entry[1]))
        highs.append(float(entry[2]))
        lows.append(float(entry[3]))
        closes.append(float(entry[4]))
        adj_closes.append(float(entry[5]))
        volumes.append(float(entry[6]))

    for i in range(0, 6):
        sumCollection.append(float(0))
        avgCollection.append(float(0))

    for i in range(0, len(dates)):
        sumCollection[0] += float(opens[i])
        sumCollection[1] += float(highs[i])
        sumCollection[2] += float(lows[i])
        sumCollection[3] += float(closes[i])
        sumCollection[4] += float(adj_closes[i])
        sumCollection[5] += float(volumes[i])

    for i in range(0, 6):
        sumCollection[i] = round(sumCollection[i], 2)
        avgCollection[i] += round(sumCollection[i]/len(dates), 4)

    #Calculating DAILY Standard deviation of the set
    stdDevHighs = []
    stdDevCloses = []
    for i in range(0, len(dates)):
        #The standard deviation of the highs and closes found each day, squared to eliminate negatives
        highVal = (highs[i]-avgCollection[1])**2
        closeVal = (closes[i]-avgCollection[3])**2
        stdDevHighs.append(highVal)
        stdDevCloses.append(closeVal)

    #Summing and arithmetic to find the values for outputting
    stdDevHigh = float(0)
    stdDevClose = float(0)
    for i in range(0, len(dates)):
        stdDevHigh += stdDevHighs[i]
        stdDevClose += stdDevCloses[i]
    varianceHigh = stdDevHigh/(len(highs)-1)
    varianceClose = stdDevClose/(len(closes)-1)
    stdDevHigh = math.sqrt(stdDevHigh)
    stabilityHigh = stdDevHigh/avgCollection[1]
    stdDevClose = math.sqrt(stdDevClose)
    stabilityClose = stdDevClose / avgCollection[3]

    #Optional Printing for the generated values
    print("Standard Deviation (highs):", end=" ")
    print(stabilityHigh)
    print("Standard Deviation (closes):", end=" ")
    print(stabilityClose)
    print("Variance (highs):", end=" ")
    print(varianceHigh)
    print("Variance (closes):", end=" ")
    print(varianceClose)

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

    yield [stabilityHigh, varianceHigh, stabilityClose, varianceClose]


def printFindings(input, coefficients):
    print("\nPrinting Findings...\n")

    #Appends the stability and variance for a stock to the output file
    with open('./csvData/output.csv', mode='a') as output:
        output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        output.writerow([input, coefficients[0][0], coefficients[0][1], coefficients[0][2], coefficients[0][3]])

    # Code below could be used later for very general stats - Printing headers, the csv column headers as labels
    # for a in range(0, len(headers)):
    #     print(headers[a], end="           ")
    # print()

    # print("\nDates with drops 5% or more include...")
    # for b in range(0, len(largeDrop)):
    #     index = dates.index(largeDrop[b])
    #     print(dates[index], end="     ")
    #     print(opens[index], end="     ")
    #     print(highs[index], end="     ")
    #     print(lows[index], end="     ")
    #     print(closes[index], end="     ")
    #     print(adj_closes[index], end="     ")
    #     print(volumes[index], end="     \n")
    # print("\nDates with gains by 5% or more include...")
    # for c in range(0, len(largeGain)):
    #     index = dates.index(largeGain[c])
    #     print(dates[index], end="     ")
    #     print(opens[index], end="     ")
    #     print(highs[index], end="     ")
    #     print(lows[index], end="     ")
    #     print(closes[index], end="     ")
    #     print(adj_closes[index], end="     ")
    #     print(volumes[index], end="     \n")
    # print("\nDates with increased trading volume by 40% or more above average...")
    # for d in range(0, len(highVolumes)):
    #     index = dates.index(highVolumes[d])
    #     print(dates[index], end="     ")
    #     print(opens[index], end="     ")
    #     print(highs[index], end="     ")
    #     print(lows[index], end="     ")
    #     print(closes[index], end="     ")
    #     print(adj_closes[index], end="     ")
    #     print(volumes[index], end="     \n")


def clearLists():
    #Necessary for appending data for running multiple files
    highVolumes.clear()
    largeDrop.clear()
    largeGain.clear()
    sumCollection.clear()
    avgCollection.clear()
    orig_data.clear()
    headers.clear()
    dates.clear()
    opens.clear()
    highs.clear()
    lows.clear()
    closes.clear()
    adj_closes.clear()
    volumes.clear()

def main():
    #Print Headers for flagged data outputs
    with open('./csvData/output.csv', mode='w') as hdr:
        hdr = csv.writer(hdr, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        hdr.writerow(
            ['Stock', 'Stability Coefficient (high)', 'Variance (high)', 'Stability Coefficient (close)',
             'Variance (close)'])

    #The csv filename is pulled from the list at the top of the script
    for i in range(0, len(stocks)):
        f = open('./csvData/' + stocks[i])

        csv_f = csv.reader(f)

    #Saving the data
        for row in csv_f:
            orig_data.append(row)

        for x in range(0, 7):
            headers.append(orig_data[0][x])
        orig_data.pop(0)

        coefficients = list(findChanges())

        printFindings(stocks[i], coefficients)

        clearLists()

        f.close()

if __name__ == '__main__':
    main()
