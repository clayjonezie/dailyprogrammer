words = []
for i in range(input()):
    words.append(raw_input())

longestL = 0
for i in range(len(words)):
    if (len(words[i]) > longestL):
        longestL = len(words[i])
        iLongest = i

for i in range(longestL):
    #do stuff
