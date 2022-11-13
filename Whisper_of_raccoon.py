import csv


def readData(address):
    data = list()
    with open(address) as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            data.append(row)
    return data


def cleanData(data):
    return list(filter(lambda thisList: False if ' ?' in thisList else True, data))


# Education     Status     Others      Skin Color     Sex
fileAddres = './adult.csv'
data = readData(fileAddres)
print(len(data))
data = cleanData(data)
print(len(data))

# learn percent = 70% and test = 30% --> lentgh * 0.3 and lentgh * 0.7 !!!
trainTestBorder = round(len(data)*0.7)
trainingData = data[1:trainTestBorder]
testingData = data[trainTestBorder:]
