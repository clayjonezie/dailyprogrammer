import sys
import os

words = []
for i in range(input()):
    words.append(raw_input())

longestL = 0
for i in range(len(words)):
    if (len(words[i]) > longestL):
        longestL = len(words[i])
        iLongest = i

os.system("clear")

for i in range(longestL):
    for word in words:
        if len(word) > i:
            sys.stdout.write(word[i])
        else:
            sys.stdout.write(" ")
    sys.stdout.write("\n")
