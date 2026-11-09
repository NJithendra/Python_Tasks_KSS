#Given two lists, find: Common elements., Elements present only in the first list., All unique elements from both lists.

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
set1 = set(list1)
set2 = set(list2)
common = set1.intersection(set2)
first = set1.difference(set2)
unique = set1.union(set2)
print("Common Element" , common)
print("First Element" , first)
print("Unique Element" , unique)
