# 202588618 ,  Career Professional/Continuing Education
# 202579587 ,  International Student Programs
# 202588608 ,  Open University
# 202579607 ,  General Student Information
# 360002248154 ,  Instructor Manual
# print sections and categories
import json

# Opening JSON File
f = open('categories.json')

# return JSON object as a dictionary
data = json.load(f)

#Iterate through the json list
for i in data['categories']:
    print(i['name'].strip(),",",str(i['id']).strip())

#close the file
f.close();