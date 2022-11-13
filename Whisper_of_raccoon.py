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


fileAddres = './adult.csv'
data = readData(fileAddres)
print(len(data))
data = cleanData(data)
print(len(data))
