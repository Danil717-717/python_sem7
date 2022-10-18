from os.path import exists
from CSV_create import creating
from Writing import writing_scv
from Writing import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()