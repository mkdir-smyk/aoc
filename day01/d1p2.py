left_list = []
right_list = []

with open('d1.input', 'r') as file:
    for line in file:

        values = line.split()
        left_list.append(int(values[0]))  
        right_list.append(int(values[1]))  


right_count = {}
for num in right_list:
    right_count[num] = right_count.get(num, 0) + 1

similarity_score = 0
for num in left_list:
    count_in_right = right_count.get(num, 0)
    similarity_score += num * count_in_right

print("Similarity Score:", similarity_score)
