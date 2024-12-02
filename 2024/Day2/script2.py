print("Day2 challenge 2/2: start")

antalSafeReports = 0

def isReportSafe(report):
    decreasing = report[0] - report[1] > 0
    if decreasing:
        for index, value in enumerate(report[:-1]):
            diff = report[index] - report[index + 1]
            safe = 0 < diff < 4
            if not safe:
                return index
    else:
        for index, value in enumerate(report[:-1]):
            diff = report[index + 1] - report[index]
            safe = 0 < diff < 4
            if not safe:
                return index

    return -1

#Read from file
with open("input.txt", "r") as file:
    for line in file:
        report = []
        for num in line.split():
            report.append(int(num))
        indexOfUnsafe = isReportSafe(report)
        if indexOfUnsafe == -1:
            antalSafeReports +=1
        else:
            #Remove one element at a time from the list, and thereafter check if it is now safe
            for index, value in enumerate(report):
                templist = report[:]
                del templist[index]
                if isReportSafe(templist) == -1:
                    antalSafeReports +=1
                    break

    print(antalSafeReports)