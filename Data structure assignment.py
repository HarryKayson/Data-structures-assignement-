#Assignment:
#Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list.

#Creating an empty list called my_list
my_list=[]

#Appending 10, 20, 30, 40 into my_list list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting the value 15 at the second position [1]
my_list.insert(1, 15)

#Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

#Removing the last element from my_list.
del my_list[-1]

#Sorting my_list in ascending order.
my_list.sort()

#Finding and printing the index of the value 30 in my_list.
index_of_30= my_list.index(30)

#Printing the final list and the index of 30
print("Final list is ",my_list)
print("The index of the value 30 is ", index_of_30)