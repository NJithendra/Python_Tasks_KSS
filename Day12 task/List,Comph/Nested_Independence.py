#Nested Data Independence

import copy
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
new_classes = copy.deepcopy(classes)
classes[0][1][0] = 50
print("Original:", classes)
print("Copied:", new_classes)
