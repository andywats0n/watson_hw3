import csv

filepath = './Resources/budget_data.csv'


def getMonthlyDiff(curNum, numToSub):
    return curNum - numToSub


def getAvgDiff(monthDiffs):
    return round(sum(monthDiffs) / len(monthDiffs), 2)


def getMaxDiff(monthDiffs):
    return max(monthDiffs)


def getMinDiff(monthDiffs):
    return min(monthDiffs)


def formatCurrency(diff):
    if(str(diff).find("-") == -1):
        return "${:,.2f}".format(float(diff))

    splitDiff = str(diff).split("-", 2)
    formatted = "-${:,.2f}".format(float(splitDiff[1]))
    return formatted


with open(filepath) as data:
    reader = csv.reader(data)
    next(reader)

    row_count = 0
    netPL = 0
    monthlyDiffs = []

    for row in reader:
        if(row_count == 0):
            periodStart = row[0]
            monthToSub = row[0]
            numToSub = int(row[1])
        else:
            curMonth = row[0]
            curNum = int(row[1])

            curDiff = getMonthlyDiff(curNum, numToSub)

            if(row_count > 1):
                if(curDiff > getMaxDiff(monthlyDiffs)):
                    maxDiff = curDiff
                    maxMonthOfDiff = curMonth
                if(curDiff < getMinDiff(monthlyDiffs)):
                    minDiff = curDiff
                    minMonthOfDiff = curMonth

            monthlyDiffs.append(curDiff)

            monthToSub = curMonth
            numToSub = curNum

        row_count += 1
        netPL += int(row[1])
        periodEnd = row[0]

    print("")
    print(f"Financial Analysis: {periodStart} - {periodEnd} ({row_count} months)")
    print(f"---------------------------------------------------")
    print(f"Max Profit: {formatCurrency(maxDiff)}   {maxMonthOfDiff}")
    print(f"Max Loss:   {formatCurrency(minDiff)}  {minMonthOfDiff}")
    print(f"Net P/L:    {formatCurrency(netPL)}")
    print(f"Avg P/L:    {formatCurrency(getAvgDiff(monthlyDiffs))}")

with open("report.txt", "w") as report:
    print(f"Financial Analysis: {periodStart} - {periodEnd} ({row_count} months)", file=report)
    print(f"---------------------------------------------------", file=report)
    print(f"Max Profit: {formatCurrency(maxDiff)}   {maxMonthOfDiff}", file=report)
    print(f"Max Loss:   {formatCurrency(minDiff)}  {minMonthOfDiff}", file=report)
    print(f"Net P/L:    {formatCurrency(netPL)}", file=report)
    print(f"Avg P/L:    {formatCurrency(getAvgDiff(monthlyDiffs))}", file=report)
