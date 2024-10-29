list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Determine the maximum number of elements in the sublists
max_length = max(len(sublist) for sublist in list_of_lists)

# Loop through each index up to the maximum length
for i in range(max_length):
    for sublist in list_of_lists:
        if i < len(sublist):  # Check if the index exists in the sublist
            print(sublist[i])