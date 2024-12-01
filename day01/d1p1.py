# Initialize the two lists
left_list = []
right_list = []

# Open the file and read its content
with open('d1.input', 'r') as file:
    for line in file:
        # Split the line by space and get the left and right values
        values = line.split()
        left_list.append(int(values[0]))  # Store the left value
        right_list.append(int(values[1]))  # Store the right value

left_list.sort()
right_list.sort()

total_distance = 0

for left, right in zip(left_list, right_list):
    distance = abs(left - right)
    total_distance += distance

# Output the total distance
print("Total distance:", total_distance)

