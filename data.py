import csv
from collections import Counter

with open("C:/WHITEHAT/Datascience/assignmentc104/SOCR-HeightWeight.csv",newline ='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
newData = []

for i in range(len(data)):
    n = data[i][2] 
    newData.append(float(n))

n_values = len(newData)
total = 0

for i in newData:
    total = total+i

print("Mean(Average) is  "+ str(total/n_values))
newData.sort()

if(n_values % 2 == 0):
    mode1 = newData[n_values//2]
    mode2 = newData[n_values//2 - 1]
    print("Median is " + str(mode1+mode2/2))
else:
    print*("Median is " + str(newData[n_values//2]))

mode = Counter(newData)
modeRange = {
    '75-95':0,'95-115':0,'115-135':0,'135-155':0,'155-175':0
}
for weight, frequency in mode.items():
    if(75<float(weight)<95):
        modeRange['75-95']= modeRange['75-95']+frequency
    elif(95<float(weight)<115):
        modeRange['95-115']= modeRange['95-115']+frequency
    elif(115<float(weight)<135):
        modeRange['115-135']= modeRange['115-135']+frequency
    elif(135<float(weight)<155):
        modeRange['135-155']= modeRange['135-155']+frequency
    elif(155<float(weight)<175):
        modeRange['155-175']= modeRange['155-175']+frequency

r1,f1 = 0,0

for range, frequency in modeRange.items():
    if(frequency> f1):
        r1,f1 = [int(range.split('-')[0]),int(range.split('-')[1])], frequency

finalMode = float((r1[0]+r1[1])/2)
print("Mode is " + str(finalMode))
