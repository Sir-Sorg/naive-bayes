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


def findFeature(data: list):
    features = dict()
    for column in range(4):
        feature = dict()
        for sample in data:
            feature[sample[column]] = feature.get(sample[column], 0)+1
        features[column] = feature
    return features


def percentageFeature(features: dict):
    for column in features:
        feature = features[column]
        totalCount = sum(feature.values())
        for Key in feature:
            feature[Key] /= totalCount
    return features


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

# divide data into male and female list
male = list(
    filter(lambda thisList: True if thisList[4] == ' Male' else False, trainingData))
female = list(
    filter(lambda thisList: True if thisList[4] == ' Female' else False, trainingData))

maleFeature = findFeature(male)
femaleFeature = findFeature(female)
maleFeature = percentageFeature(maleFeature)
femaleFeature = percentageFeature(femaleFeature)
