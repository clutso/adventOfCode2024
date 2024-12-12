with open("day2/input.txt") as file: 
    data = file.read().strip()


data = data.split('\n')


safe_reports =0
idx = 0
size = len (data)
report = data[idx]


while idx< size: 
    safe = True
    ascending = False
    r_idx = 1

    report = data[idx].split()
    r_size = len(report)

    delta = int(report[r_idx]) - int(report[r_idx-1])
    


    idx+=1


"""
while data:    
    safe = True
    ascending = False
    idx = 1

    report = report.split()
    size = len(report)
    delta = int(report[idx])-int(report[idx-1])
    
    if delta == 0: 
        continue

    if abs(delta) > 3:
        continue


    if ( delta > 0 ):
        ascending = True
    
    for idx in range(idx+1, size):    
        delta = int(report[idx])- int(report[idx-1])
        if ((ascending) and delta < 0): 
            safe = False
            break

        if ((not ascending) and delta > 0):
            safe = False
            break
        if abs(delta) > 3:
            safe = False
            break
        if delta == 0:
            safe = False
            break
    
    if safe: safe_reports+=1

"""
print (safe_reports)
    #if element:
