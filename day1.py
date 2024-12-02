def main():
  file = open("day1_input.txt", "r")
  for line in file: 
    print(line)
list1 = sorted([])
list2 = sorted([])
distance = 0
for i in range(list1.length()):
  distance += abs(list1[i] - list2[i])
return distance


main()
