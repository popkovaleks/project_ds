from lykke_files import Command
from db_creating import create_db
from db_creating_table import create_everything

from argparse import ArgumentParser
from datetime import datetime, date

def createParser():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', default='combined.csv')
    parser.add_argument('-d', '--date', default=date.today())
    parser.add_argument('-db', '--dbname', default='lykke')

    return parser


def main():
    parser = createParser()
    namespace = parser.parse_args()

    command = Command()
    command.execute(namespace.file, namespace.date)

    create_db(namespace.dbname)
    create_everything(namespace.dbname, namespace.file)
    
    print("Database is created")

if __name__ == '__main__':
    main()
