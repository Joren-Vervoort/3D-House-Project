from utils.download import DownloadFiles
from utils.address import AddressData

#files = DownloadFiles()
#files.create_directory()
#files.download()
#files.unzip_and_delete()

#ADDRESSDATA

test = AddressData()
coordinates, data_address = test.coordinates()
polygon = test.polygon()
print(coordinates,data_address, polygon)

#DOWNLOAD CORRECT DTM AND DSM FILES

files = DownloadFiles()
#files.create_directory()
num = files.bbox_check(coordinates)
print(num)
files.download()
#files.unzip_and_delete()

