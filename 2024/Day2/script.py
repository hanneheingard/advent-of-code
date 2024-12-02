print("Day2 challenge 1/2: start")

antalSafeReports = 0

#Read from file
with open("input.txt", "r") as file:
    for line in file:
        report = []
        for num in line.split():
            report.append(int(num))

#Check if safe or unsafe
        safe = False
#check if increase or decrease
        decreasing = report[0] - report[1] > 0
        if not decreasing:
            report.reverse()
            #Check diff between indexes
        for index, value in enumerate(report[:-1]):
            diff = report[index] - report[index + 1]
            safe = 0 < diff < 4
            if not safe:
                break

        if safe:
            antalSafeReports += 1

    print(antalSafeReports)
