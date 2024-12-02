print("Day2 challenge 1/2: start")

antalSafeReports = 0

def isReportSafe(report):
    decreasing = report[0] - report[1] > 0
    if not decreasing:
        report.reverse()

    for index, value in enumerate(report[:-1]):
        diff = report[index] - report[index + 1]
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
            del report[indexOfUnsafe]
            if isReportSafe(report) == -1:
                antalSafeReports +=1


    print(antalSafeReports)
