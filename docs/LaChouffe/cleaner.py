import json 

with open('journalsDump.json', 'r') as x:
    data = json.load(x)

df = dict()

for journal in data:

    if 'pissn' in journal['bibjson']:

        df[journal['bibjson']['pissn']]= {'code':'pissn', "country":journal['bibjson']['publisher']['country'], "subject":journal['bibjson']['subject'][0]['term']}

    elif 'eissn' in journal['bibjson']:

        df[journal['bibjson']['eissn']]= {"country":journal['bibjson']['publisher']['country'], "subject":journal['bibjson']['subject'][0]['term']}
    else:
        print('both missing')
        
with open('cleanJournalsDump.json', 'w+') as out:
    json.dump(df,out)