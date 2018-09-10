import csv

filepath = './election_data.csv'


def numFormat(num):
    return "{:,}".format(int(num))


def getCandidates(cand):
    if(cand not in candidates):
        candidates.append(cand)


def getCounts(cand, counts):
    if(cand == "Marsh"):
        counts[0] += 1
    if(cand == "Queen"):
        counts[1] += 1
    if(cand == "Bamoo"):
        counts[2] += 1
    if(cand == "Trandee"):
        counts[3] += 1
    if(cand == "Raffah"):
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

        cand = row[1]

        getCandidates(cand)
        getCounts(cand, counts)

        total += 1

        for i in range(len(counts)):
            ratios[i] = getRatios(counts[i], total)

    print(" ")
    print("Election Results")
    print("-------------------------")
    winner = ""
    ratio = 0
    maxRatio = ratios[0]
    for cand, count, ratio in zip(candidates, counts, ratios):
        print(f"{cand}:  {ratio}% ({numFormat(count)})")
        winner = getMaxRatio(cand, ratio, maxRatio, winner)
    print(" ")
    print(winner)

with open("results.txt", "w") as results:
    print("Election Results", file=results)
    print("-------------------------", file=results)
    winner = ""
    ratio = 0
    maxRatio = ratios[0]
    for cand, count, ratio in zip(candidates, counts, ratios):
        print(f"{cand}:  {ratio}% ({numFormat(count)})", file=results)
        winner = getMaxRatio(cand, ratio, maxRatio, winner)
    print(" ", file=results)
    print(winner, file=results)

