f_maxValue = open("maxValue.txt", "r")
maxValue = f_maxValue.readline()
f_maxValue.close()

f_minValue = open("minValue.txt", "r")
minValue = f_minValue.readline()
f_minValue.close()

print maxValue
print minValue
