def main():
  file = open("day1_input.txt", "r")
  list1 = []
  list2 = []
  for line in file: 
    list1.append(line[0])
    list2.append(line[1])
list1.sort()
list2.sort()
distance = 0
for i in range(list1.length()):
  distance += abs(list1[i] - list2[i])
return distance


main()
