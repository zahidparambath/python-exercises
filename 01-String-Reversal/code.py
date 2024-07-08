# Exercise Name:
# 	01-String-Reversal
# Description:
# 	Reverse each word of a string.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"nohtyP si emosewA"


sentence = "Python is Awesome"
result=sentence.split(' ')
for item in result :
    print(''.join(reversed(item)), end=' ')


