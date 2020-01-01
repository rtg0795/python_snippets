import zipfile
import os

# zf = zipfile.ZipFile('test/developer_survey_2019.zip', 'r')
# zf.extractall(path='test', members=None, pwd=None)

def extract_zip_without_pass(path_to_file, path_to_extract=None):
    if path_to_extract is None:
        head, tail = os.path.split(path_to_file)
        filename = os.path.splitext(tail)[0]
        path_to_extract = os.path.join(head, filename)
    zf = zipfile.ZipFile(path_to_file, 'r')
    zf.extractall(path=path_to_extract, members=None, pwd=None)


extract_zip_without_pass('/test/developer_survey_2019.zip')