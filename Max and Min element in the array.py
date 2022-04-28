# Finding the Maximum element in the array.
from array import *
arr = array('i',[2,6,43,5,33,8,54,23,69,78,3])
x = 0
for i in range(len(arr)):
    if arr[i] > x:
        x = arr[i]
print('The maximum element in the array is',x)


# Find the minimum element in the array.
arr = array('i',[5,35,54,87,4,8,75,2,35,78,])
x=arr[1]
for i in range(len(arr)):
    if arr[i] < x:
        x = arr[i]
print('The minimum element in the array is',x)


