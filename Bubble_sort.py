import random
import math
# Program for bubble sort
numList = []

for i in range(5):
    numList.append(random.randrange(1, 51))

print("List of random numbers: ")
for i in numList:
    print(i, end=" ")

print("")


def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1]:
                print("{} > {} swap".format(num_list[j], num_list[j+1]))
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                for k in num_list:
                    print(k, end=" ")

                print("\n")

            else:
                print("{} < {} don't swap".format(num_list[j], num_list[j + 1]))
                for k in num_list:
                    print(k, end=" ")

                print("\n")


print("")
bubble_sort(numList)
print("")
print("List of sorted numbers: ")
for i in numList:
    print(i, end=" ")
