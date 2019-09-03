import os

DEBUG = True
DEBUG_PRINT = False

if DEBUG:
    BASE_DIR = os.path.join(os.getcwd(), '桌面/twAddr/twAddr')
    print('開發 :', BASE_DIR)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

countyCSV = os.path.join(BASE_DIR, 'county.csv')
roadStreetCSV = os.path.join(BASE_DIR, 'roadStreet.csv')
villageCSV = os.path.join(BASE_DIR, 'village.csv')


# # make a directory
# _dir = Directory(_db_path)
#
# # the API only exposed
# find = _dir.find
