#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/14

first_line  = input()
second_line = input()
third_line  = input()

max_width = int(first_line)
number_of_blocks = int(second_line)
width_blocks_of_indevidual = list(map(int, third_line.split(' ')))

width_blocks_ordered_by_asc = sorted(width_blocks_of_indevidual)

sum_width = 0
for block_index in range(number_of_blocks):
    sum_width += width_blocks_ordered_by_asc[block_index]
    if sum_width > max_width:
        print(block_index)
        break
if sum(width_blocks_ordered_by_asc) == max_width:
    print(len(width_blocks_ordered_by_asc))

# print(width_blocks_of_indevidual)
# print(width_blocks_ordered_by_asc)
