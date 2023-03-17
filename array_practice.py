from array import *

# 1. Create an array and traverse:
print("Step 1")
my_array = array("i", [1,2,3,4,5,6,7]) # Time Complexity: O(1) and Space Complexity: O(N)
 
for num in my_array:   # Time Complexity: O(1) Space Complexity: O(N)
    print(num)

# 2. Access individual elements through indexes
print("Step 2")
def individualElements(arr, index):
    if index > len(arr)-1:
        print("Error - no such index")
    else:
        print(arr[index])

individualElements(my_array, 3)
individualElements(my_array, 133)

# 3. Append any value to the end of the array
print("Step 3")
my_array.append(543)
print(my_array)

# 4. Insert value using the insert() method
print("Step 4")
my_array.insert(4,12)
my_array.insert(0,45)
my_array.insert(7,23)
print(my_array)

# 5. Extend array by a list of items
print("Step 5")
my_array.extend([9,8,10])
print(my_array)

# 6. Add items from list into array using fromlist() method
print("Step 6")
thisList = [26,27,34,56]
my_array.fromlist(thisList)
print(my_array)

# 7. Remove any array element using remove() method
print("Step 7")
my_array.remove(12)
my_array.remove(543)
print(my_array)

# 8. Remove last array element
print("Step 8")
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using the index() method
print("Step 9")
print(my_array.index(3))

# 10. Reverse an array
print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information using buffer_info()
print("Step 11")
print(my_array.buffer_info())

# 12. Check for number of occurrences of an element using count()
print("Step 12")
print(my_array.count(133))
print(my_array.count(3))
print(my_array.count(543))


# 13. Convert array to one string
print("Step 13")
print("".join(map(str, my_array)))


# 14. Convert array to a python list with same elements 
print("Step 14")
intList = my_array.tolist()
print(intList)


# 15. Slice elements from an array
print("Step 15")
print(my_array[1:4])
print(my_array[:])
print(my_array[4:])
