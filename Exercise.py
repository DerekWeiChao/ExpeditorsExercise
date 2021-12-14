import csv
import string

#place to store data
storage = []

addressNumber = {}

#everything needs to have the same format for comparison
def sanitize():
    for item in storage:
        #makes it so all addresses have the same format
        tempAddress = item['address']
        tempAddress = tempAddress.replace(',','')
        tempAddress = tempAddress.replace('.','')
        #title capitalizes every first letter of each word while strip removes whitespace at the start and end
        item['address'] = string.capwords(tempAddress)

        #city and state are now properly capitalized, age is displayed as an int
        item['state'] = item['state'].upper()
        item['city'] = item['city'].title()
        item['age'] = int(item['age'])

        #adds full name by last name first to storage for ease of sorting
        item['fullName'] = item['lastName'] + ', ' + item['firstName']

        #adds a full address to better sort through the stuff
        item['fullAddress'] = item['address'] + ', ' + item['city'] + ', ' + item['state']

#where the sorting happens
def sortData():
    for item in storage:
        people = {}
        #initialize dict key if it doesn't already exist in addressNumber
        if item['fullAddress'] in addressNumber:
            addressNumber[item['fullAddress']]['count'] += 1
        else:
            addressNumber[item['fullAddress']] = {}
            addressNumber[item['fullAddress']]['count'] = 1
            addressNumber[item['fullAddress']]['people'] = []

        #add new entry at said key
        people['fullName'] = item['fullName']
        people['firstName'] = item['firstName']
        people['lastName'] = item['lastName']
        people['age'] = item['age']

        addressNumber[item['fullAddress']]['people'].append(people)
    for key in addressNumber:
        addressNumber[key]['people'] = sorted(addressNumber[key]['people'], key=lambda d: d['fullName'])
    return

#print results here
def printData():
    for key in addressNumber:
        print('Address: ' + key)
        print(' Count: ' + str(addressNumber[key]['count']))      
        print(' People Older Than 18: ')
        #print(addressNumber[key]['people'])

        for person in addressNumber[key]['people']:
            if person['age'] > 18:
                print('     Name: ' + person['firstName'] + ' ' + person['lastName'] + ' - Age: ' + str(person['age']))
        print()
    return

if __name__ == '__main__':
    with open('input.csv') as newFile:
        #since the formatting 
        reader = csv.DictReader(newFile, fieldnames=['firstName','lastName', 'address', 'city', 'state', 'age'])
        for row in reader:
            #adds each row in the input to an array
            storage.append(row)
        newFile.close()
    sanitize()
    sortData()
    printData()