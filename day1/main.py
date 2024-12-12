def main():
    list1 = []
    list2 = []

    #if does not work check the pathfile...
    with open("day1/input.txt") as file: 
        data = file.read().split()

    for idx, num in enumerate(data):
        if idx%2 != 0 :
            list2.append(int(num))
        else:
            list1.append(int(num))

    list1.sort()
    list2.sort()
    #  part 1
    print(sum([abs(list2[n]- list1[n]) for n in range(len(list1))]))


    freq ={}
    for n in list2:
        freq[n] = freq.get(n,0)+1
    #part 2 

    print(sum([freq.get(n,0)*n for n in list1]))
        
if __name__ == "__main__":
    main()