# Given a list [1, 2, 3, 2, 4, 1, 5, 3], remove duplicate elements while preserving the original order

numbers = [1, 2, 3, 2, 4, 1, 5, 3]
list = [] #create the empty set
for num in numbers: #using for loop to the numbers
    if num not in list: #checking the element is present or not
        list.append(num) #adding the element if it is not present
print(list)
