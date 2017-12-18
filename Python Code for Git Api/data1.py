import requests
import json
import csv

response = requests.get('https://api.github.com/repos/Blankj/awesome-java-leetcode/commits')

data = response.json()
file_changes = []
for obj in data:
    print(obj['url'])
    temp = requests.get(obj['url']).json()
    for fil in temp['files']:
        if (fil['filename'][-4:]=='java'):
            file_changes.append(fil['filename'])

# open a csv file with append, so old data will not be erased
with open('java1.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 # The for loop
 for value in file_changes:
    writer.writerow([value])
