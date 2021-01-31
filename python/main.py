import csv
import math
import json

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
recentTrend = []
marketTrendAverages = [0, 0, 0, 0, 0, 0] #Bull days, %, count, Bear days, count, %
stabilityCoefficientsHigh = []
stabilityCoefficientsClose = []
stabilityHigh = float(0)
stabilityClose = float(0)
varianceHigh = float(0)
varianceClose = float(0)
stocks = ["BTC-USD", "ETH-USD", "LTC", "DOGE-USD"]
#["SCHM", "EES", "IYH", "VWO", "SPY", "ARKK"]
#["ALL", "HIG", "LNC", "MET", "PFG", "PGR"]
#["ETSY", "OSTK", "AMZN", "CHWY", "W", "EBAY", "APRN"]
#["M", "KSS", "DDS", "CPPRQ", "TGT", "MSLH.L"]
#["SPOT", "AAPL", "SIRI", "TCEHY", "AMZN", "AMC", "RICK", "GNUS"]
#["TTWO", "TCEHY", "ATVI", "EA", "NTDOY"]
#["AMZN", "WMT", "TGT", "COST", "BJ", "KR"]
#["F", "TM", "GM", "HMC", "TSLA", "NIO", "RACE", "VWAGY"]
#["AXP", "COF", "C", "V", "DFS", "WFC", "PYPL"]
#["JNJ", "KO", "PG", "CLX", "CPB", "GIS", "CL"]

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
    # print("Standard Deviation (highs):", end=" ")
    # print(stabilityHigh)
    # print("Standard Deviation (closes):", end=" ")
    # print(stabilityClose)
    # print("Variance (highs):", end=" ")
    # print(varianceHigh)
    # print("Variance (closes):", end=" ")
    # print(varianceClose)
    stabilityCoefficientsClose.append(stabilityClose)
    stabilityCoefficientsHigh.append(stabilityHigh)

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
    print("Printing Findings...")


    #Appends the stability and variance for a stock to the output file
    with open('./csvData/output.csv', mode='a') as output:
        output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        output.writerow([input, coefficients[0][0], coefficients[0][1], coefficients[0][2], coefficients[0][3]])


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

def turnaround(fmtDataArr):
    print("\nFinding average increasing and decreasing turnaround...\n")

    recentHigh = 0
    recentLow = highs[2*dates.index(fmtDataArr[0][0])]
    #Small Recent Trend Thing which needs to use the weeks Array
    for z in range(len(fmtDataArr)-3, len(fmtDataArr)):
        for q in range(0, len(fmtDataArr[z])):
            if recentHigh < highs[q]:
                recentHigh = highs[q]
            if recentLow > lows[q]:
                recentLow = lows[q]

    if highs[dates.index(fmtDataArr[z][q])] < recentHigh:# and lows[dates.index(fmtDataArr[z][q])] > recentLow:
        recentTrend.append("Negative Trajectory")
    elif highs[dates.index(fmtDataArr[z][q])] > recentHigh:# and lows[dates.index(fmtDataArr[z][q])] < recentLow:
        recentTrend.append("Positive Trajectory")
    else:
        recentTrend.append("Indeterminate")



    for c in range(0, len(fmtDataArr)):
        #Check every close and high of the week against the first open and see if there was a 20% inc or 10% dec
        startIndex = dates.index(fmtDataArr[c][0])
        weekInit = opens[startIndex]
        saveLow = 2*weekInit
        saveHigh = 0

        if len(fmtDataArr[c]) < 5:
            break

        for i in range(0, 5):
            #Might have an issue trying to access non existant spaces here?
            if highs[startIndex+i] > saveHigh:
                saveHigh = highs[startIndex+i]
            if lows[startIndex+i] < saveLow:
                saveLow = lows[startIndex+i]

        counter = 0
        BullBear = 0
        if (saveHigh/weekInit >= 1.1) and (saveLow/weekInit <= .9):
            #Quick math to determine whether the trajectory of the week was positive or negative
            avgWkHighs = 0
            avdWkLows = 0
            for i in range(0, 5):
                avgWkHighs += highs[startIndex+i]
            for j in range(0, 5):
                avgWkHighs += highs[startIndex+j]
            performanceAvg = (avdWkLows+avgWkHighs)/2
            if performanceAvg - weekInit >= 0: #bull
                saveLow = 2 * weekInit
            elif performanceAvg - weekInit <= 0: #bear
                saveHigh = 0
            else:
                break
        if (saveHigh/weekInit >= 1.1):
            #while remaining data exists, look for a fall of 10 % (bull)
            for x in range(startIndex+i+1, len(lows)):
                if highs[x] > saveHigh:
                    saveHigh = highs[x]
                if (lows[x]/saveHigh <= 0.9):
                    BullBear = 1
                    break
                counter += 1
            #After array is done
            if BullBear != 1:
                BullBear = 3
        elif (saveLow/weekInit <= .9):
            # while remaining data exists, look for a gain of 10 % (bear)
            for x in range(startIndex+i+1, len(highs)):
                if lows[x] < saveHigh:
                    saveLow = lows[x]
                if (highs[x]/saveLow >= 1.1):
                    BullBear = 2
                    break
                counter += 1
            # After array is done
            if BullBear != 2:
                BullBear = 4

        #Print the news and save the counters for data processing later
        if BullBear == 1:
            print("There were ", counter, " days of bull market starting on", fmtDataArr[c][0], "with a return of ", (saveHigh/weekInit)*100, "%!")
            marketTrendAverages[0] += counter
            marketTrendAverages[1] += (saveHigh/weekInit)*100
            marketTrendAverages[2] += 1
        elif BullBear == 2:
            print("There were ", counter, " days of bear market starting on", fmtDataArr[c][0], "with a return of ", (saveLow/weekInit)*100, "%...")
            marketTrendAverages[3] += counter
            marketTrendAverages[4] += (saveLow / weekInit) * 100
            marketTrendAverages[5] += 1
        elif BullBear == 3:
            print("There have been ", counter, " days of bull market starting on", fmtDataArr[c][0], "with a return of ", (saveHigh/weekInit)*100, "% and counting!")
            marketTrendAverages[0] += counter
            marketTrendAverages[1] += (saveHigh / weekInit) * 100
            marketTrendAverages[2] += 1
        elif BullBear == 4:
            print("There have been ", counter, " days of bear market starting on", fmtDataArr[c][0], "with a return of ", (saveLow/weekInit)*100, "% and counting!")
            marketTrendAverages[3] += counter
            marketTrendAverages[4] += (saveLow / weekInit) * 100
            marketTrendAverages[5] += 1


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
        f = open('./5yr/' + stocks[i] + ".csv")

        csv_f = csv.reader(f)

    #Saving the data, the program uses the 5 year data rn but can be adjusted to do different lengths or just take smaller lengths of data
        for row in csv_f:
            orig_data.append(row)

        for x in range(0, 7):
            headers.append(orig_data[0][x])
        orig_data.pop(0)

        coefficients = list(findChanges())

        fmtDates = list(divide_dates(dates))

        turnaround(fmtDates)

        printFindings(stocks[i], coefficients)

        highCoef = sum(stabilityCoefficientsHigh) / len(stabilityCoefficientsHigh)
        closeCoef = sum(stabilityCoefficientsClose) / len(stabilityCoefficientsClose)
        if highCoef > stabilityCoefficientsHigh[i] and closeCoef > stabilityCoefficientsClose[i] :
            if recentTrend[i] == "Negative Trajectory":
                recentTrend[i] = "Indeterminate"
        if highCoef < stabilityCoefficientsHigh[i] and closeCoef < stabilityCoefficientsClose[i] :
            if recentTrend[i] == "Positive Trajectory":
                recentTrend[i] = "Indeterminate"

        clearLists()

        f.close()

    #End of for loop - sending JSON
    data = {}
    data['stocks'] = []
    data['stocks'].append({
        'Sector': 'Cryptocurrencies',
        'Stock Names': stocks,
        'Stability Coefficients (highs)': stabilityCoefficientsHigh,
        'Avg Stab. Coefficient (highs)': round(highCoef, 2),
        'Stability Coefficients (at close)': stabilityCoefficientsClose,
        'Avg Stab. Coefficient (at close)': round(closeCoef, 2),
        'Avg Up Market Length (days)' : round(marketTrendAverages[0]/marketTrendAverages[2], 2),
        'Avg Up Market Return (%)': round(marketTrendAverages[1] / marketTrendAverages[2], 2),
        'Avg Down Market Length (days)': round(marketTrendAverages[3] / marketTrendAverages[5], 2),
        'Avg Down Market Return (%)': round(marketTrendAverages[4] / marketTrendAverages[5], 2),
        'Recent Trajectories': recentTrend
    })

    with open('./jsons/cryptocurrency.txt', 'w') as outfile:
        json.dump(data, outfile)




if __name__ == '__main__':
    main()
