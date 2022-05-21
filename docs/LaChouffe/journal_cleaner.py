import json 
import os
import argparse
def clean(path):
    data = None
    with open(path, 'r') as x:
        data = json.load(x)

    df = dict()

    for journal in data:

        if 'pissn' in journal['bibjson']:

            df[journal['bibjson']['pissn']]= {'code':'pissn', "country":journal['bibjson']['publisher']['country'], "subject":journal['bibjson']['subject'][0]}

        elif 'eissn' in journal['bibjson']:

            df[journal['bibjson']['eissn']]= {"country":journal['bibjson']['publisher']['country'], "subject":journal['bibjson']['subject'][0]}
        else:
            print('both missing')
            
    with open('cleanJournalsDump.json', 'w+') as out:
        json.dump(df,out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process files to populate with Crossref information about presence.')
    parser.add_argument('path', metavar='path',type=str, 
                    help='Path to the file or to the directory')
    
    args = parser.parse_args()
    if not os.path.isdir(f'.{sep}cleaned'):
        os.makedirs(f'.{sep}cleaned')
    clean(args.path)
    