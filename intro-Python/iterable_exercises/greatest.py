
# Example list
numbers = [10, 6, 8, 2, 4, 15, 3]

# Initialize with the first element
largest = numbers[0]

# Loop through the rest of the list
for num in (numbers):  #[1:]:
    if num > largest:
        largest = num

print("Greatest value:", largest)
