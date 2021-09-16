import csv
import math
import json

print("Welcome to the Trendi Algorithm! Below, csv values will be stored and processed.")

#print("__name__ value: ", __name__)
highVolumes = []
largeDrop = []
largeGain = []
sumCollection = [] #used to hold total values which will be divided by the number of entries to reach the average
avgCollection = [] #used to hold the afformentioned calculated averages, which are the next step toward the final data
orig_data = [] #holds a single stock's total raw data for processing, set in main for each during a for loop
headers = []
dates = []
opens = []
highs = []
lows = []
closes = []
adj_closes = []
volumes = []
recentTrend = []
marketTrendAverages = [0, 0, 0, 0, 0, 0] #Bull days, %, count, Bear days, %, count

#Stability coefficients are found by dividing the standard deviation by the stock values in two different metrics in attempt to normalize the scale of them and make them comparable independent of stock price
stabilityCoefficientsHigh = [] 
stabilityCoefficientsClose = []

stabilityHigh = float(0)
stabilityClose = float(0)
varianceHigh = float(0)
varianceClose = float(0)
stocks = [["F", "TM", "GM", "HMC", "TSLA", "NIO", "RACE", "VWAGY"],["BTC-USD", "ETH-USD", "LTC", "DOGE-USD"],
           ["M", "KSS", "DDS", "CPPRQ", "TGT", "MSLH.L"],["SPOT", "AAPL", "SIRI", "TCEHY", "AMZN", "AMC", "RICK", "GNUS"],
        ["SCHM", "EES", "IYH", "VWO", "SPY", "ARKK"], ["AXP", "COF", "C", "V", "DFS", "WFC", "PYPL"], ["JNJ", "KO", "PG", "CLX", "CPB", "GIS", "CL"],
        ["ALL", "HIG", "LNC", "MET", "PFG", "PGR"], ["ETSY", "OSTK", "AMZN", "CHWY", "W", "EBAY", "APRN"], ["TTWO", "TCEHY", "ATVI", "EA", "NTDOY"],
            ["AMZN", "WMT", "TGT", "COST", "BJ", "KR"]
           ]

#Function for processing data into stability coefficients
def findChanges():
    #print("\nFinding Changes...\n")

    for entry in orig_data: #orig_data is the data provided by the excel spreadsheets (raw from yahoo), each entry is a day which has each of the metrics listed below provided at the start
        dates.append(entry[0])
        opens.append(float(entry[1]))
        highs.append(float(entry[2]))
        lows.append(float(entry[3]))
        closes.append(float(entry[4]))
        adj_closes.append(float(entry[5]))
        volumes.append(float(entry[6]))

    for i in range(0, 6): #Start each value in (see variable descriptions above) as 0
        sumCollection.append(float(0))
        avgCollection.append(float(0))

    for i in range(0, len(dates)): #add the appropriate value to the appropriate index to make totals for each
        sumCollection[0] += float(opens[i])
        sumCollection[1] += float(highs[i])
        sumCollection[2] += float(lows[i])
        sumCollection[3] += float(closes[i])
        sumCollection[4] += float(adj_closes[i])
        sumCollection[5] += float(volumes[i])

    for i in range(0, 6): #rounding to make numbers neater and more manageable, then divigind by then number of entries (len(dates)) to get averages for each
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
    varianceHigh = stdDevHigh/(len(highs)-1) #Variance formula from statistics (source?)
    varianceClose = stdDevClose/(len(closes)-1)
    stdDevHigh = math.sqrt(stdDevHigh)
    stabilityHigh = stdDevHigh/avgCollection[1] #dividing by average highs
    stdDevClose = math.sqrt(stdDevClose)
    stabilityClose = stdDevClose / avgCollection[3] #dividing by the average closes

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

    #Finding Days of Interest....
    #SECTION OF CODE CURRENTLY UNUSED! :(
    for i in range(0, len(dates)):
        if volumes[i]/avgCollection[5] >= 1.40: #when large volumes have been traded (40% above average) or....
            highVolumes.append(dates[i])
        #Only accounts for a single day, should be dynamic and start watching interesting activity (follow through on potential past days)
        if closes[i]/opens[i] >= 1.05: #there is a gain of more than 5% in a day...
            largeGain.append(dates[i])
        elif highs[i]/lows[i] >= 1.05:
            largeGain.append(dates[i])
        if opens[i]/closes[i] >= 1.05: #there is a loss of more than 5% in a day
            largeDrop.append(dates[i])
        elif highs[i]/lows[i] <= 0.95: 
            largeDrop.append(dates[i])

    yield [stabilityHigh, varianceHigh, stabilityClose, varianceClose]


#Writing to a CSV file
def printFindings(input, coefficients):
    #print("Printing Findings...")


    #Appends the stability and variance for a stock to the output file
    with open('./csvData/output.csv', mode='a') as output:
        output = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        output.writerow([input, coefficients[0][0], coefficients[0][1], coefficients[0][2], coefficients[0][3]])

#Necessary for appending data for running multiple files
def clearLists():
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

#Used to identify positive and negative market trends
def turnaround(fmtDataArr):
    #print("\nFinding average increasing and decreasing turnaround...\n")

    recentHigh = 0
    recentLow = highs[2*dates.index(fmtDataArr[0][0])] #Not sure what the x2 is for. Should return first entry in highs. 
    
    #Small Recent Trend Thing which needs to use the weeks Array
    for z in range(len(fmtDataArr)-3, len(fmtDataArr)): #len(fmtDataArray) is how many 5 day "weeks" have been separated out of the data. Using only the last few (3) weeks to try to estimate a recent trend
        for q in range(0, len(fmtDataArr[z])):
            if recentHigh < highs[q]:
                recentHigh = highs[q]
            if recentLow > lows[q]:
                print("teehee")
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
        saveLow = 2*weekInit #arbitrary "low" value compared to stock price which is actually very high (x2) so that it will be replaced regardless of stock price
        saveHigh = 0

        #might be able to modify line below and combine with following for loop so that incomplete weeks can be used as well
        if len(fmtDataArr[c]) < 5: #if the week is not complete, don't bother using it (wont affect average much in the long run)
            break

        for i in range(0, 5):
            if highs[startIndex+i] > saveHigh:
                saveHigh = highs[startIndex+i]
            if lows[startIndex+i] < saveLow:
                saveLow = lows[startIndex+i]

        counter = 0
        BullBear = 0 #used to hold one of 4 key values which correspond to different 
        if (saveHigh/weekInit >= 1.1) and (saveLow/weekInit <= .9): #if the week had performance which brought it outside the normal range (+- 10%)
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
            #while remaining data exists, look for a fall of 10 % (bull), counting until the streak ends
            for x in range(startIndex+i+1, len(lows)):
                if highs[x] > saveHigh:
                    saveHigh = highs[x] #checking if a new standard has been set for the high, and the percentages adjusted
                if (lows[x]/saveHigh <= 0.9):
                    BullBear = 1 #once it drops below the predetermined threshold, mark BullBear with the proper number and break out of the data loop
                    break
                counter += 1 #used to count how long this type of market lasted
            #After array is done
            if BullBear != 1:
                BullBear = 3 #as long as BullBear hasn't been marked to show the end of the trend, it is ongoing and has a different syntax in the final print
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
            #print("There were ", counter, " days of bull market starting on", fmtDataArr[c][0], "with a return of ", (saveHigh/weekInit)*100, "%!")
            marketTrendAverages[0] += counter
            marketTrendAverages[1] += (saveHigh/weekInit)*100
            marketTrendAverages[2] += 1
        elif BullBear == 2:
            #print("There were ", counter, " days of bear market starting on", fmtDataArr[c][0], "with a return of ", (saveLow/weekInit)*100, "%...")
            marketTrendAverages[3] += counter
            marketTrendAverages[4] += (saveLow / weekInit) * 100
            marketTrendAverages[5] += 1
        elif BullBear == 3:
            #print("There have been ", counter, " days of bull market starting on", fmtDataArr[c][0], "with a return of ", (saveHigh/weekInit)*100, "% and counting!")
            marketTrendAverages[0] += counter
            marketTrendAverages[1] += (saveHigh / weekInit) * 100
            marketTrendAverages[2] += 1
        elif BullBear == 4:
            #print("There have been ", counter, " days of bear market starting on", fmtDataArr[c][0], "with a return of ", (saveLow/weekInit)*100, "% and counting!")
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

        hdr.writerow( #Labels for columns in output.csv
            ['Stock', 'Stability Coefficient (high)', 'Variance (high)', 'Stability Coefficient (close)',
             'Variance (close)'])

    for category in range(0, 11): #This loop runs through each stock category, a category being a grouping of stocks based on market sector (see in sock list at top off file)
        # The csv filename is pulled from the list at the top of the script
        for i in range(0, len(stocks[category])): #THIS IS THE FOR LOOP WHICH RUNS THROUGH INDIVIDUAL STOCKS ~~~ 1 iteration of this equals one stock's data processed and added to the output
            f = open('./5yr/' + stocks[category][i] + ".csv")


            csv_f = csv.reader(f)

            # Saving the data, the program uses the 5 year data rn but can be adjusted to do different lengths or just take smaller lengths of data
            for row in csv_f:
                orig_data.append(row)

            for x in range(0, 7):
                headers.append(orig_data[0][x])
            orig_data.pop(0)

            coefficients = list(findChanges())

            fmtDates = list(divide_dates(dates)) #fmtDates is an ARRAY of ARRAYS of 5 consecutive dates in the data, starting at the beginning of the data set

            turnaround(fmtDates)

            printFindings(stocks[category][i], coefficients)

            highCoef = sum(stabilityCoefficientsHigh) / len(stabilityCoefficientsHigh)
            closeCoef = sum(stabilityCoefficientsClose) / len(stabilityCoefficientsClose)
            if highCoef > stabilityCoefficientsHigh[i] and closeCoef > stabilityCoefficientsClose[i]:
                if recentTrend[i] == "Negative Trajectory":
                    recentTrend[i] = "Indeterminate"
            if highCoef < stabilityCoefficientsHigh[i] and closeCoef < stabilityCoefficientsClose[i]:
                if recentTrend[i] == "Positive Trajectory":
                    recentTrend[i] = "Indeterminate"

            clearLists()

            f.close()

        sectors = ["Automobiles", "Cryptocurrencies", "Department Stores", "Music and Digital Entertainment",
                   "Exchange-Traded Funds (ETF)", "Banking and Finance", "Home and Food Products", "Insurance",
                   "Online Retail", "Video Games", "Grocery and Wolesale"]
        filenames = ["automobiles", "cryptocurrency", "departmentstores", "entertainment", "etf", "finance",
                     "homegoods", "insurance", "onlineretail", "videogames", "wholesale"]

        # End of for loop - sending JSON
        data = {}
        data['stocks'] = []
        data['stocks'].append({
            'Sector': sectors[category],
            'Stock Names': stocks[category],
            'Stability Coefficients (highs)': stabilityCoefficientsHigh,
            'Avg Stab. Coefficient (highs)': round(highCoef, 2),
            'Stability Coefficients (at close)': stabilityCoefficientsClose,
            'Avg Stab. Coefficient (at close)': round(closeCoef, 2),
            'Avg Up Market Length (days)': round(marketTrendAverages[0] / marketTrendAverages[2], 2), #calculating averages based on trend day length and number of instances
            'Avg Up Market Return (%)': round(marketTrendAverages[1] / marketTrendAverages[2], 2),  #calculating averages based on % gain or loss and number of instances
            'Avg Down Market Length (days)': round(marketTrendAverages[3] / marketTrendAverages[5], 2),
            'Avg Down Market Return (%)': round(marketTrendAverages[4] / marketTrendAverages[5], 2),
            'Recent Trajectories': recentTrend
        })

        with open('../src/rawJsons/'+filenames[category]+'.json', 'w') as outfile: #Written out to the respective json file by the stock's name within /rawJsons
            json.dump(data, outfile)

        print("Done!")




if __name__ == '__main__':
    main()
