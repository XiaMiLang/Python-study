import sys


str = sys.argv[1:]

allpin = []
allstate = []
for i in range(int(len(str))):
    allpin.append(str[i].split(":")[0])
    allstate.append(str[i].split(":")[1])

print (allpin)
print (allstate)