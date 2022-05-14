import os
import json

directory = 'doaj_article_data_2022-04-19/chiara' 

for filename in os.listdir(directory):
    print(filename)
    if filename != '.DS_Store':
        file = open(directory+'/'+filename)
        data =  json.load(file)
        result = dict()
        x = 0
        for article in data:
            x+=1
            check = False #checker if the article has doi, if not it will be skipped as we cannot query Crossref without it 
            
            for item in article['bibjson']['identifier']:
                if 'doi' in item.values():
                    if 'id' in item:
                        doi = item['id']
                        check = True
                        Mydict = dict()

            if check: #doi is present
                
                if 'year' in article['bibjson']:
                    year = article['bibjson']['year']
                    Mydict['year'] = year
               
                else:
                    Mydict['year'] = 0
                
                if 'issns' in article['bibjson']['journal']:
                    issns = article['bibjson']['journal']['issns']
                    Mydict['issns'] = issns
                    
                else:
                    Mydict['issns'] = 0

                
                result[doi] = Mydict
           
            else: #doi is not present
                pass

        with open("doaj_article_data_2022-04-19/clean/clean_"+filename, "w+") as f:
            json.dump(result, f, indent=4)
            f.close()
      
        # output.write(result)
    