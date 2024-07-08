# Exercise Name:
# 	06-Pattern-Fun
# Description:
# 	Prompt for row count and print a number pattern using that value
# Given:
# 	row_count = 5
# Return:
# 	1 1 1 1 1 
# 	2 2 2 2 
# 	3 3 3 
# 	4 4 
# 	5

row_count = 5

for i in range(1, row_count+1):
    for j in range(1, row_count+2-i):
        print(i,end =" ")
    print()   
