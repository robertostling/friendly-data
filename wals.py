import urllib.request
import zipfile

class WALSData:
    def __init__(self):
        pass

    def get_filename(self):
        url = 'https://zenodo.org/record/6806407/files/cldf-datasets/' \
              'wals-v2020.2.zip?download=1'
        filename = 'wals.zip'
        if not os.path.exists(filename):
            urllib.request.urlretrieve(url, filename)
        return filename

    # TODO: create methods to load the data, and some to produce simplified
    # versions. May want to create one class per output format, e.g. JSON,
    # Python code, s-expressions, etc.

