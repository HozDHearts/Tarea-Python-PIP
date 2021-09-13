import numpy as np
x = [2, 3, 4, 5, 6]
print(x)
print("These is the base data, you will chose a number to add to the existant data.")
print("But first selec if you want to use numpy or not.")

b= input("Write 1 if you want to use numpy, 2 if you don't want to use numpy: ")


if int(b) <= 1:
    val = input("Enter a numeric value to add to each data: ")
    y = [a + int(val) for a in x]
    print(x)
    print(y)


else: 
    val = input("Enter a numeric value to add to each: ")

    nums = np.array([2, 3, 4, 5, 6])
    nums2 = nums + int(val)
    print(nums)
    print(nums2)