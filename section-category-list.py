# print sections and categories
import json

# Opening JSON File
f = open('sections.json')

# return JSON object as a dictionary
data = json.load(f)

#Iterate through the json list
for i in data['sections']:
    # print(i['id'], "," , i['name'] , "," , i['category_id'])
    print( i['name'] , ",", str(i['id']), "," , str(i['category_id']))

#close the file
f.close();