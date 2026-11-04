# Write a program to find the student with the highest marks from a dictionary

dt = {"Ravi": 66 , "Ram": 333 ,"Kishore": 25}

Highest = max(dt , key = dt.get)
print("Highest Scorer:" , Highest)
