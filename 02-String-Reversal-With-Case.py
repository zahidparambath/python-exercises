# Exercise Name:
# 	02-String-Reversal-With-Case
# Description:
# 	Reverse each word of a string without changing upper-case positions.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"Nohtyp si Emosewa"

sentence = "Python is Awesome"
resultList = sentence.split(' ')
for item in resultList:
    result = ''.join(reversed(item))
    if(result[-1].isupper()):
        print(result[0].upper(), end='')
        print(result[1:-1], end='')
        print(result[-1].lower(), end =' ')
    else :
        print(result, end=' ')
