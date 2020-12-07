#read from input
inp = open("input.txt", "r")
nums = inp.readlines()
inp.close()

#convert to int
for i in range(len(nums)):
    nums[i] = int(nums[i][:-1])

#solve part 1
def part1(inputNums):
    for n in inputNums:
        find = 2020 - n
        found = False
        
        for j in inputNums:
            if find == j:
                print(n, " ", find)
                print(n * find)
                break
#solve part 2
def part2(inputNums):
    for n in inputNums:
        find_1 = 2020 - n
        
        for j in inputNums:
            find_2 = find_1 - j
            
            for k in inputNums:
                if find_2 == k:
                    print(n, " ", j, " ", k)
                    print(n * j * k)
#execute
#357504 two entries that sum to 2020 - what do you get if you multiply them - 1824 196
part1(nums)
#12747392 the product for the three entries that sum to 2020 - 1312 14 694
part2(nums)
