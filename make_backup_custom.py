import os
import datetime
import csv
import requests

credentials = '{username}', '{password}'
zendesk = 'https://ucsantabarbaraextension.zendesk.com/'
language = 'en-us'

now = datetime.datetime.now()
backup_path = os.path.join(str(now), language)
if not os.path.exists(backup_path):
    os.makedirs(backup_path)

log = []

endpoint = zendesk + '/api/v2/help_center/{locale}/articles.json'.format(locale=language.lower())
while endpoint:
    response = requests.get(endpoint, auth=credentials)
    if response.status_code != 200:
        print('Failed to retrieve articles with error {}'.format(response.status_code))
        exit()
    data = response.json()

    for article in data['articles']:
        # omit blank articles
        if article['body'] is None:
            continue
        # Export only Published articles
        if article['draft'] is True:
            continue
        title = '<h1>' + article['title'].strip() + '</h1>'
        filename = '{id}.html'.format(id=article['id'])
        with open(os.path.join(backup_path, filename), mode='w', encoding='utf-8') as f:
            f.write(title + '\n' + article['body'])
        print('{id} copied!'.format(id=article['id']))

        log.append((filename, article['title'].strip(), article['author_id'], article['draft'], article['promoted'], article['section_id']))

    endpoint = data['next_page']

with open(os.path.join(backup_path, f'_log_{now}.csv'), mode='wt', encoding='utf-16') as f:
    writer = csv.writer(f)
    writer.writerow( ('File', 'Title', 'Author ID', 'Draft', 'Promoted', 'Section ID') )
    for article in log:
        writer.writerow(article)