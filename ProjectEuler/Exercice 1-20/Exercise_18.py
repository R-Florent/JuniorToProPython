triangle = ''' 
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# Split the string into lines
triangle = triangle.split("\n")
triangle_list_de_list = []

# Process each line
for element in triangle:
    numbers = list(map(int, element.strip().split()))
    triangle_list_de_list.append(numbers)

# Print the processed list of lists

local_max_sum = [[0] * len(ligne) for ligne in triangle_list_de_list]
max_sum = 0

#logique de code
for i in range(len(triangle_list_de_list)):
    for y in range(len(triangle_list_de_list[i])):
        if local_max_sum[i][y] < triangle_list_de_list[i][y] + (local_max_sum[i-1][y] if i > 0 and y < len(local_max_sum[i-1]) else 0):
            right_parent = (local_max_sum[i-1][y] if i > 0 and y < len(local_max_sum[i-1]) else 0)
            left_parent = local_max_sum[i-1][y-1] if y-1 >= 0 else 0
            local_max_sum[i][y] = triangle_list_de_list[i][y] + max(right_parent,left_parent)


print(local_max_sum[-1])

#local_max_sum = triangle_list_de_list[0][0]+triangle_list_de_list[1][0]+triangle_list_de_list[2][0]+triangle_list_de_list[3][0]
print(max_sum)