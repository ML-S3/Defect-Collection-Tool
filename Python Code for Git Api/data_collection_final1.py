import requests
import json
import csv

user = raw_input('Enter Owner-Name: ')
repo_name = raw_input('Enter Repository Name: ')
access_token = raw_input('Enter Access Token: ')

response = requests.get('https://api.github.com/repos/'+user+"/"+repo_name+'/commits?access_token='+access_token)

data = response.json()
file_changes = []
for commit in data:
    print(commit['url'])
    temp = requests.get(commit['url']+'?access_token='+access_token).json()
    for fil in temp['files']:
        if (fil['filename'][-4:]=='java'):
            file_changes.append(fil['filename'])


directory = {}
for _file in file_changes:
    if _file in directory:
        directory[_file] = directory[_file] + 1
    else :
        directory[_file] = 1

with open('dataml.csv', 'w') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(["Class Name","Defect Count"])
 for key in directory:
    writer.writerow([key,directory[key]])
