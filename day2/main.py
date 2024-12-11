with open("day2/input.txt") as file: 
    data = file.read().strip()
data = data.split('\n')

safe_reports =0

for report in data:
    
    report = report.split()

    ascending = (int(report[1])-int(report[0]))
    print(ascending)
    for idx in range(len(report)):
        
        report[idx]
    #if element: