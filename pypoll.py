import csv

filepath = './Resources/election_data.csv'


def numFormat(num):
    return "{:,}".format(int(num))


def getCounts(cand, counts):
    if(cand not in candidates):
        candidates.append(cand)
    if(cand == candidates[0]):
        counts[0] += 1
    if(len(candidates) > 1 and cand == candidates[1]):
        counts[1] += 1
    if(len(candidates) > 2 and cand == candidates[2]):
        counts[2] += 1
    if(len(candidates) > 3 and cand == candidates[3]):
        counts[3] += 1
    if(len(candidates) > 4 and cand == candidates[4]):
        counts[4] += 1


def getRatios(count, total):
    return round((count / total)*100, 2)


def getMaxRatio(cand, ratio, maxRatio, winner):
    if(ratio > maxRatio):
        maxRatio = ratio
        winner = f"Winner: {cand}"
    elif(ratio == maxRatio):
        winner = f"Winner: {cand}"
    return winner


with open(filepath, newline="") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader)

    total = 0

    candidates = []
    counts = [0, 0, 0, 0, 0]
    ratios = [0, 0, 0, 0, 0]

    for row in reader:

        cand = row[2]

        getCounts(cand, counts)

        total += 1

        for i in range(len(counts)):
            ratios[i] = getRatios(counts[i], total)

    winner = ""
    ratio = 0
    maxRatio = ratios[0]

    print(" ")
    print("Election Results")
    print("--------------------------------")

    for cand, count, ratio in zip(candidates, counts, ratios):
        if(len(cand) >= len('o-tooley')):        
            print(f"{cand}: {ratio}% ({numFormat(count)})")
        else:
            print(f"{cand}:\t{ratio}% ({numFormat(count)})")
        winner = getMaxRatio(cand, ratio, maxRatio, winner)

    print("--------------------------------")
    print(winner)

with open("results.txt", "w") as results:
    winner = ""
    ratio = 0
    maxRatio = ratios[0]

    print(" ", file=results)
    print("Election Results", file=results)
    print("--------------------------------", file=results)

    for cand, count, ratio in zip(candidates, counts, ratios):
        if(len(cand) >= len('o-tooley')):
            print(f"{cand}: {ratio}% ({numFormat(count)})", file=results)
        else:
            print(f"{cand}:\t{ratio}% ({numFormat(count)})", file=results)
        winner = getMaxRatio(cand, ratio, maxRatio, winner)

    print("--------------------------------", file=results)
    print(winner, file=results)
