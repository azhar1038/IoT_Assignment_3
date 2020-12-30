def binary_search(values, element):
    values.sort()
    print("Sorted list: ", values)
    low = 0
    high = len(values)-1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == element:
            return mid
        if values[mid] < element:
            low = mid+1
        else:
            high = mid-1
    return -1
numbers = []
for i in range(20):
    numbers.append(int(input("Enter number_%d: "%(i+1))))
element = int(input("Enter element to search: "))
position = binary_search(numbers, element)
if position >= 0:
    print(element, "was found at position", position, "(zero based index) in the sorted list.")
else:
    print("Element not found")
