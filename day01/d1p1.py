
left_list = []
right_list = []

with open('d1.input', 'r') as file:
    for line in file:
        values = line.split()
        left_list.append(int(values[0])) 
        right_list.append(int(values[1]))  

left_list.sort()
right_list.sort()

total_distance = 0

for left, right in zip(left_list, right_list):
    distance = abs(left - right)
    total_distance += distance


print("Total distance:", total_distance)

