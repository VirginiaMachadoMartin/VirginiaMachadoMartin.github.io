
# my_list_0 = list()
#my_list_1 = []
#my_list_2 = [0, 1, 3]

#print(my_list_0)
#print(my_list_1)
#print(my_list_2)


# Can you predict the outcome of the following? 

#adding 4 to the list
[0, 1, 2] + [4]
#repeating list 4 times
[0, 1, 2] * 4
#gives '1st' element of list, which is actually the 2nd element since we start counting with 0
[0, 1, 2][1]
#gives you last element of list
[0, 1, 2][-1]
#gives error because out of range element being requested
# [0, 1, 2][4]
#gives number of elements in list
#len([0, 1, 2])
#gives error since you can't get length from number not string
#len([0, 1, 2][-1])

#establish list 
my_list = [0, 1, 2]
my_list.append(3)
my_list.append("hello")
print(my_list)
qm = my_list.pop(0)
print(my_list)
print(qm)

import sys
def main():
  print(sys.argv)
  print("Hello " + sys.argv[1] + "!")
