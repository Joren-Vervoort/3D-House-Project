from urllib.request import urlopen
import urllib.request
from zipfile import ZipFile
import os, zipfile
import pandas as pd

class DownloadFiles:

    """
    Class that contains functions to download, unzip the DTM and DSM files
    in a generated directory, after which the zip files will be deleted
    :attrib files(optional)

    f.e.: DownloadFiles() to use the class functions for DTM and DSM files
    
    """

    def __init__(self, files=["DTM","DSM"]):
        self.files = files
        self.number = ''

    def create_directory(self):

        """
        Function used to generate a directory to save the downloaded DSM and DTM files if
        this directory is not present yet
        """

        # create dirs if not present
        for dir in self.files:
            print("Checking directories...")
            dir = f"/data/{dir}"
            if os.path.exists(dir):
                print("Directory is already satisfied")
            if not os.path.exists(dir):
                os.makedirs(dir)
                print("Directory created")

    def bbox_check(self,coordinates):
        """
        
        """
        bbox = pd.read_csv('./data/bounding-box.csv')
        for i in range(bbox.shape[0]):
            if bbox['Left (X)'][i] <= coordinates[0]:
                if bbox['Right (X)'][i] >= coordinates[0]:
                    if bbox['Bottom (Y)'][i] <= coordinates[1]:
                        if bbox['Top (Y)'][i] >= coordinates[1]:
                            i = i
                            break

        if i < 9:
            self.number = f'k0{i+1}'
        else:
            self.number = f'k{i+1}'
        return self.number


    def download(self):

        """
        Function used to download the needed DTM and DSM files while checking to prevent
        re-downloading
        """

        for i in range(len(self.files)):
            
            folder_name = self.files[i]
            
            if folder_name == "DSM":
                url = f"https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dsm-raster-1m/DHMVIIDSMRAS1m_{self.number}.zip"
            else:
                url = f"https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dtm-raster-1m/DHMVIIDTMRAS1m_{self.number}.zip"
                    
            file_zip_name = url.split('/')[-1]
            for folder in self.files:
                dir_name = (os.getcwd()+f"\\data\\{folder}")
                number_of_files = len(os.listdir(dir_name))
                if number_of_files == 0:
                    # Downloading the files
                    print(f"downloading {folder}.zip file... This may take a while")
                    urllib.request.urlretrieve(url, f'./data/{folder_name}/{file_zip_name}')
                else:
                    i = 0
                    for item in os.listdir(dir_name): # loop through items in dir
                        if item == file_zip_name: # check if file is already downloaded
                            print("file is already downloaded")
                            break
                        elif i != number_of_files:
                            i += 1
                            continue
                        else:
                            # Downloading the files
                            print(f"downloading {folder}.zip file... This may take a while")
                            urllib.request.urlretrieve(url, f'./data/{folder_name}/{file_zip_name}')
        print("All files have been downloaded")
        
        return file_zip_name
            
    
    def unzip(self):

        """
        Function that unzips the downloaded files and deletes the .zip files afterwards
        """

        for folder in self.files:
            dir_name = (os.getcwd()+f"\\data\\{folder}")
            extension = ".zip"

            for item in os.listdir(dir_name): # loop through items in dir
                if item.endswith(extension): # check for ".zip" extension
                    file_name = (dir_name + f"\\{item}")
                    zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                    zip_ref.extractall(dir_name) # extract file to dir
                    zip_ref.close() # close file

