import urllib.request
import urllib.error
import gzip
import os
import pandas as pd
from datetime import datetime, date, time, timedelta
from argparse import ArgumentParser
from io import StringIO





class Command():
    def execute(self, file_output, date_arg):
        start_date = date(2018, 8, 29)

        counter = start_date
        final_date = datetime.strptime(date_arg, '%Y-%m-%d').date()

        while counter < final_date:
            try:
                request = urllib.request.Request("https://lykkedwhpublic.blob.core.windows.net/lykke-dwh-tradelog/tradelog_"+counter.strftime("%Y-%m-%d")+".gz",
                                                    headers={
                                                        "Accept-Encoding": "gzip",
                                                        "User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11", 
                                                    })
                response = urllib.request.urlopen(request)
            except urllib.error.URLError:
                print("File for {} does not exist".format(counter.strftime("%Y-%m-%d")))
                counter = counter + timedelta(1)
                continue

            
            archive = gzip.GzipFile(fileobj=response)
            
            byte_content = archive.read()

            string_content = str(byte_content, 'utf-8')
            data = StringIO(string_content)
            try:
                dataframe_content = pd.read_csv(data)
            except pd.errors.EmptyDataError:
                print("File for {} is empty".format(counter.strftime("%Y-%m-%d")))

            if not os.path.isfile(file_output):
                dataframe_content.to_csv(file_output, index=False)
            else:
                dataframe_content.to_csv(file_output, mode='a', header=False, index=False)
            counter = counter + timedelta(1)

def createParser():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', default='combined.csv')
    parser.add_argument('-d', '--date', default=date.today())

    return parser

def main():
    parser = createParser()
    namespace = parser.parse_args()
    
    command = Command()
    command.execute(namespace.file, namespace.date)



if __name__ == '__main__':
    main()      