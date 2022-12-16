# Read the Data
with open('day8.in') as file:
    forest = file.read().strip()
# Parse the data into a grid
trees = [list(x) for x in forest.split('\n')]

#Part 1 --------------------------------

# Since the input is 99x99, just multiply the length - 1 times 4, so you don't recount each corner
# visible = (len(trees) - 1) * 4

# # Loop through to correctly iterate the grid
# for i in range(1, len(trees) - 1):
#     for j in range(1, len(trees[i]) - 1):
#         # start booleans as false, as we check them, we mill mark them as true if they are visible from one end,
#         # so we don't count a tree visible from 2 or more ways as separate trees
#         top, left, right, bottom = False, False, False, False

#         #Check first if the tree to the left is smaller than the tree we are at. If it is,
#         #Continue checking the next tree to the left, once we find a tree bigger than our current tree, we will
#         #Just break the loop, but if the index gets all the way to 0 we know we are at the leftmost side,
#         #So we add to visible, and mark left as True for when we check the other trees.

#         if trees[i][j] > trees[i][j - 1]:
#             for k in range(j - 1, -1, -1):
#                 if trees[i][k] >= trees[i][j]:
#                     break
#                 if k == 0 and trees[i][k] < trees[i][j]:
#                     visible += 1
#                     left = True

#         #We do the same with each other side, just iterating slightly different for directional purposes.
#         #Right
#         if trees[i][j] > trees[i][j + 1]:
#             for k in range(j + 1, len(trees[i])):
#                 if trees[i][k] >= trees[i][j]:
#                     break
#                 if k == len(trees[i]) - 1 and trees[i][k] < trees[i][j] and left == False:
#                     visible += 1
#                     right = True
#         #Up
#         if trees[i][j] > trees[i - 1][j]:
#             for k in range(i - 1, -1, -1):
#                 if trees[k][j] >= trees[i][j]:
#                     break
#                 if k == 0 and trees[k][j] < trees[i][j] and left == False and right == False:
#                     visible += 1
#                     top = True
#         #Down
#         if trees[i][j] > trees[i + 1][j]:
#             for k in range(i + 1, len(trees)):
#                 if trees[k][j] >= trees[i][j]:
#                     break
#                 if k == len(trees) - 1 and trees[k][j] < trees[i][j] and left == False and right == False and top == False:
#                     visible += 1
#                     bottom = True

# #Finally, print the visible trees
# print(visible)

# Part 2 ----------------------------

visible = (len(trees) - 1) * 4
cur_top, cur_bottom, cur_right, cur_left = 0, 0, 0, 0
total = 0

for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[i]) - 1):

        if trees[i][j] > trees[i][j - 1]:
            for k in range(j - 1, -1, -1):
                cur_left += 1
                if trees[i][k] >= trees[i][j]:
                    break
                if k == 0 and trees[i][k] < trees[i][j]:
                    break

        if trees[i][j] > trees[i][j + 1]:
            for k in range(j + 1, len(trees[i])):
                cur_right += 1
                if trees[i][k] >= trees[i][j]:
                    break
                if k == len(trees[i]) - 1 and trees[i][k] < trees[i][j]:
                    break

        if trees[i][j] > trees[i - 1][j]:
            for k in range(i - 1, -1, -1):
                cur_top += 1
                if trees[k][j] >= trees[i][j]:
                    break
                if k == 0 and trees[k][j] < trees[i][j]:
                    break

        if trees[i][j] > trees[i + 1][j]:
            for k in range(i + 1, len(trees)):
                cur_bottom += 1
                if trees[k][j] >= trees[i][j]:
                    break
                if k == len(trees) - 1 and trees[k][j] < trees[i][j]:
                    break
        total = max(total, cur_top * cur_left * cur_bottom * cur_right)
        cur_top, cur_right, cur_bottom, cur_left = 0, 0, 0, 0

print(total)
