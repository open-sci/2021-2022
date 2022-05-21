'''
MIT License (MIT)
Copyright © 2022 Silvio Peroni, Alessandro Bertozzi, Davide Brembilla, Chiara Catizone, Constance Dami, Umut Kuçuk, Chiara Manca, Giulia Venditti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import json 
import os
from os import sep
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
    