# Given a string "programming", create a dictionary that counts how many times each character appears.

st = "programming"
repeated = {}
for ch in st:
    if ch in repeated:
        repeated[ch] +=1
    else:
        repeated[ch] = 1
    print(repeated)
    
