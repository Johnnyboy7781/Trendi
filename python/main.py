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
decreWeeks = []
increWeeks = []
decreLargeWeeks = []
increLargeWeeks = []
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
    
def trends(fmtDataArr):
    print("\nFinding weekly trends...")

    actualChangePercent = 0
    weekOpen = 0
    avgSum = 0
    weeklyChange = 0

    for i in range(0,len(fmtDataArr)):
        for x in range(0, len(fmtDataArr[i])):
            index = dates.index(fmtDataArr[i][x])
            if len(fmtDataArr[i]) != 5:
                print("\n***Finished***\n")
                break
            elif x == 0:
                index = dates.index(fmtDataArr[i][x])
                avgSum = (opens[index] + closes[index] + highs[index] + lows[index]) / 4
                weekOpen = opens[index]
            elif x == 4:
                index = dates.index(fmtDataArr[i][x])
                weeklyChange = ((opens[index] + closes[index] + highs[index] + lows[index]) / 4) - avgSum
                actualChangePercent = weeklyChange / weekOpen
                if actualChangePercent < -0.07:
                    decreLargeWeeks.append(dates[index - 4])
                elif actualChangePercent > 0.07:
                    increLargeWeeks.append(dates[index - 4])
                elif actualChangePercent < -0.025:
                    decreWeeks.append(dates[index - 4])
                elif actualChangePercent > 0.025:
                    increWeeks.append(dates[index - 4])

    print("Between the dates of " + dates[0] + " - " + dates[len(dates) - 1] + ", the following trends have been parsed ")
    print(" * * * * * * * * * * * * \nThis stock decreased by 7.0% in these weeks")
    for i in range(0, len(decreLargeWeeks)): 
        print(" - " + decreLargeWeeks[i])
    print(" * * * * * * * * * * * * \nThis stock increased by 7.0% in these weeks")
    for i in range(0, len(increLargeWeeks)):
        print(" - " + increLargeWeeks[i])
    print(" * * * * * * * * * * * * \nThis stock decreased by 2.5% in these weeks")
    for i in range(0, len(decreWeeks)): 
        print(" - " + decreWeeks[i])
    print(" * * * * * * * * * * * * \nThis stock increased by 2.5% in these weeks")
    for i in range(0, len(increWeeks)):
        print(" - " + increWeeks[i])

def turnaround(decreArr, increArr, fmtDataArr):
    print("\nFinding average increasing and decreasing turnaround...\n")

    decreWeeks = 0
    decreTimes = 0
    increWeeks = 0
    increTimes = 0
    dIndex = 0
    iIndex = 0

    for i in range(0, len(fmtDataArr)):
        if 0 <= dIndex < len(decreArr) and decreArr[dIndex] == fmtDataArr[i][0]:
            if increWeeks > 0 and increTimes > 1:
                print("This stock has increased without substantialy decresing for " + str(increWeeks) + " weeks")
                startIndex = dates.index(increArr[iIndex - increTimes])
                endIndex = dates.index(increArr[iIndex - 1])
                percentChange = ((closes[endIndex] - closes[startIndex]) / closes[startIndex]) * 100
                print("start: " + dates[startIndex] + ", end: " + dates[end])
                print("It has increased by " + str(round(percentChange, 2)) + "% in that time")
                increWeeks = 0
                increTimes = 0
            decreTimes += 1
            decreWeeks += 1
            dIndex += 1
        elif 0 <= iIndex < len(increArr) and increArr[iIndex] == fmtDataArr[i][0]:
            if decreWeeks > 0 and decreTimes > 1:
                print("This stock has decreased without substantially increasing for " + str(decreWeeks) + " weeks")
                index = decreArr.index(decreArr[iIndex - 1])
                percentChange = ((closes[index] - closes[index - decreWeeks]) / closes[index - decreWeeks]) * 100
                print("It has decreased by " + str(round(percentChange, 2)) + "% in that time")
                decreWeeks = 0
                decreTimes = 0
            increTimes += 1
            increWeeks += 1
            iIndex += 1
        else :
            if decreWeeks > 0 :
                decreWeeks += 1
            elif increWeeks > 0 :
                increWeeks += 1



def divide_dates(l):
    for i in range(0, len(l), 5):
        yield l[i:i +5]

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
        
        fmtDates = list(divide_dates(dates))

        trends(fmtDates)

        turnaround(decreWeeks, increWeeks, fmtDates)

        f.close()

        clearLists()

        f.close()

if __name__ == '__main__':
    main()
