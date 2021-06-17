import rasterio #Used for handling .tif files
from rasterio.plot import show #Used to plot a .tif file
import rioxarray #Used for handling rasters
import os

class LidarData:

    def __init__(self, coordinates, file_zip_name):
        self.coordinates = coordinates
        self.file_tif_name = file_zip_name.replace(".zip",".tif")
    
    def start_creating_chm(self):
        
        """
        Function that will start the creation of a canopy height model (CHM) of the house linked to the given adress
        :attrib DSM_tif will contain the dsm_search function
        :attrib DTM_tif will contain the dsm_search function
        :attrib clipped_DSM will contain the dsm_clipping function
        :attrib clipped_DTM will contain the dtm_clipping function
        :attrib clipped_CHM will contain the chm_calculating function
        This function will return the CHM of a house linked to the given adress
        """
        
        DSM_tif = LidarData.dsm_search(self.coordinates)
        DTM_tif = LidarData.dtm_search(DSM_tif)

        clipped_DSM, clip_boundaries = LidarData.dsm_clipping(DSM_tif)
        clipped_DTM = LidarData.dtm_clipping(DTM_tif, clip_boundaries)
        clipped_CHM = LidarData.chm_calculating(clipped_DSM, clipped_DTM)
        
        return clipped_CHM
    
    def dsm_search(self):
        
        """
        Function that will search in which of the DSM (digital surface model) .tif the given address is located
        !For this function to work, adjust your directory to your DSM folder!
        :attrib dataset will contain the rasterio.open function
        :attrib bbox will contain the rasterio.bounds function
        This function will return the name of the DSM .tif file in which the given address is located
        """
        
        file = (os.getcwd()+f"\\data\\DSM\\GeoTIFF\\{self.file_tif_name}")
        print("file:",file)
        DSM_tif = rasterio.open(file, masked=True)
          
        return (DSM_tif)
    
    
    def dtm_search(self, DSM_tif):
        
        """
        Function that will alter the name of the DSM .tif file name to the matching DTM .tif file name
        :attrib DTM_tif will contain the replace function
        This function will return the name of the DTM .tif file in which the given address is located
        """
        print (type(DSM_tif), DSM_tif)
        DTM_tif = DSM_tif.replace("DSM","DTM")
        
        return DTM_tif
    
    
    def dsm_clipping(DSM_tif, polygon):
        
        """
        Function that will clip the DSM .tif file based on the polygon of the house
        :attrib DSM will contain rioxarray.open_rasterio function
        :attrib clipped_DSM will contain rioxarray.rio.clip function
        This function will return the clipped DSM .tif file
        """

        DSM = rioxarray.open_rasterio(DSM_tif,
                                           masked=True)
        clip_boundaries = [ {'type': 'Polygon',
                        'coordinates': polygon}]
        clipped_DSM = DSM.rio.clip(clip_boundaries)
    
        return clipped_DSM, clip_boundaries
    
    
    def dtm_clipping(DTM_tif, clip_boundaries):
        
        """
        Function that will clip the DTM .tif file based on the polygon of the house
        :attrib DTM will contain rioxarray.open_rasterio function
        :attrib clipped_DTM will contain rioxarray.rio.clip function
        This function will return the clipped DSM .tif file
        """
        
        DTM = rioxarray.open_rasterio(DTM_tif,
                                           masked=True)
        clipped_DTM = DTM.rio.clip(clip_boundaries)
    
        return clipped_DTM
    
    def chm_calculation(clipped_DSM, clipped_DTM):
        
        """
        Function that will calculate the CHM (canopy height model) based on the clipped DSM .tif file and
        the clipped DTM .tif file
        :attrib clipped_CHM will contain the compute and fillna functions
        This function will return the CHM of the house
        """
        
        clipped_CHM = clipped_DSM - clipped_DTM 
        clipped_CHM.compute()
        clipped_CHM = clipped_CHM.fillna(0)
        
        return clipped_CHM