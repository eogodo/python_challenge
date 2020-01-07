import os
import csv

import_path = os.path.join('Resources','budget_data.csv')

with open(import_path, 'r', newline='') as csv_file:
    lines = csv.reader(csv_file, delimiter = ",")

    csv_header = next(lines)

    noMonths = 0
    net = 0
    old = 867884
    greatestInc = 0
    greatestIncDate = ''
    greatestDec = 0
    greatestDecDate = ''

    totalchange = 0

    for line in lines:
        noMonths += 1

        net += int(line[1])
        
        if (greatestInc < (int(line[1])-old)):
            greatestInc = (int(line[1]) - old)
            greatestIncDate = line[0]
        if (greatestDec > (int(line[1])-old)):
            greatestDec = (int(line[1]) - old)
            greatestDecDate = line[0]

        totalchange += (int(line[1])-old) 

        old = int(line[1])

    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months: {noMonths}')
    print(f'Total: ${net}')
    print(f'Average Change: ${round(totalchange/(noMonths-1),2)}')
    print(f'Greatest Increase in Profits: {greatestIncDate} (${greatestInc})')
    print(f'Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})')

output_file = open("output.txt",'w')
    
output_file.write("Financial Analysis")
output_file.write("---------------------------")
output_file.write(f'Total Months: {noMonths}\n')
output_file.write(f'Total: ${net}\n')
output_file.write(f'Average Change: ${round(totalchange/(noMonths-1),2)}\n')
output_file.write(f'Greatest Increase in Profits: {greatestIncDate} (${greatestInc})\n')
output_file.write(f'Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})\n')

output_file.close()
