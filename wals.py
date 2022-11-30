from pycldf import Dataset

wals2020 = Dataset.from_metadata('https://raw.githubusercontent.com/cldf-datasets/wals/v2020/cldf/StructureDataset-metadata.json')

for value in wals2020.objects('ValueTable'):
    print(value.parameter.__dict__.keys())
    print(value.language.name, value.data['Parameter_ID'],
            value.data['Value'])
    break

#import urllib.request
#import zipfile
#class WALSData:
#    def __init__(self):
#        pass
#
#    def get_file(self):
#        """Return the filename of the WALS zip file, download if needed"""
#        url = 'https://zenodo.org/record/6806407/files/cldf-datasets/' \
#              'wals-v2020.2.zip?download=1'
#        filename = 'wals.zip'
#        if not os.path.exists(filename):
#            urllib.request.urlretrieve(url, filename)
#        return filename
#
#    def load_data(self):
#        filename = self.get_file()
#        prefix = ['cldf-datasets-wals-ba04a3a', 'raw']
#    # TODO: create methods to load the data, and some to produce simplified
#    # versions. May want to create one class per output format, e.g. JSON,
#    # Python code, s-expressions, etc.

