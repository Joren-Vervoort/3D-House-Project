from utils.download import DownloadFiles
from utils.address import AddressData
from utils.chm import LidarData
from utils.plotting import Plotting

#ADDRESSDATA

address = AddressData()
coordinates, data_address = address.coordinates()
polygon = address.polygon(data_address)

#DOWNLOAD CORRECT DTM AND DSM FILES

files = DownloadFiles()
files.create_directory()
num = files.bbox_check(coordinates)
print(num)
file_zip_name = files.download()
files.unzip()

#LIDARDATA

LidarData = LidarData(coordinates, file_zip_name)

DSM_tif = LidarData.dsm_search()
DTM_tif = LidarData.dtm_search(DSM_tif)

clipped_DSM, clip_boundaries = LidarData.dsm_clipping(DSM_tif, polygon)
clipped_DTM = LidarData.dtm_clipping(DTM_tif, clip_boundaries)
clipped_CHM = LidarData.chm_calculation(clipped_DSM, clipped_DTM)

#PLOTTING
Plotting = Plotting(clipped_CHM)
Plotting.surface_plot_3d()