from random import shuffle

allDataName = "sensor_readings_24.data"
trainFileName = "training.in"
testFileName = "input.in"

f = open(allDataName, "r")
g = open(trainFileName, "w")
h = open(testFileName, "w")
lines = f.readlines()

shuffle(lines)

g.write("value0,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11,value12,value13,value14,value15,value16,value17,value18,value19,value20,value21,value22,value23,class")

for line in lines[:4000]:
    g.write(line)
for line in lines[4000:]:
    h.write(line)
    
f.close()
g.close()
h.close()
