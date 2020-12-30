from collections import Counter
def remove_repeat(values):
    counter = Counter(values)
    repeat_count = 0
    for i in range(len(values)-1, -1, -1):
        if counter[values[i]] > 1:
            counter[values[i]] -= 1
            values.pop(i)
            repeat_count += 1
    return repeat_count

numbers = []
for i in range(20):
    numbers.append(int(input("Enter number_%d: "%(i+1))))
print("Original List:", numbers)
repeated = remove_repeat(values=numbers)
print("There were %d repeated numbers"%(repeated))
print("List after removal of repeated numbers:", numbers)