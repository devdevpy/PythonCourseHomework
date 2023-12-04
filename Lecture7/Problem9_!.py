for row in range(1, 5):
    for col in range(row, row + 13, 4):
        print(col, end=" ")
    print()

# m = []
# for row in range(1, 5):
#     m.append([])
#     for col in range(row, row + 13, 4):
#         m[row - 1].append(col)
# print("---------------")
# for row in m:
#     for col in row:
#         print(col, end=" ")
#     print()
