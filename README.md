Project status: currently updating

<h1 align="center"> <strong>3D House Project</strong> </h1>

| ![](Results/3D-house-example-1.png) |
|:-:|
| Result example |

- Repository: 3D-House-Project
- Type of Challenge: Learning & Consolidation
- Duration: 2 weeks
- Deadline: 25/02/21 5:00 PM
- Deployment strategy : Github page | Powerpoint | Jupyter Notebook | Webpage | App
- Team challenge : solo

---

## **Table of Contents**
Your section headers will be used to reference the location of the destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [Repo Artitecture](#repo-artitecture)
- [Next Step](#next-step)
- [License](#license)
- [Author Info](#author-info)

## **Description**

### *Mission Objectives*
3D plot a user-given address (located within Belgium) and plot the house/building that is associated with this address.

### *Learning Objectives*

to be able to search and implement new librairies
to be able to read and use shapefiles
to be able to read and use geoTIFFs
to be able to render a 3D plot
to be able to present a final product

### *The Setting*

We are LIDAR PLANES , active in the Geospatial industry. We would like to use our data to launch a new branch in the insurrance business. So, we need you to build a solution with our data to model a house in 3D with only a home address.

<br/>

### **Technologies**
<br/>

| Library          | Used to                                        |
| ---------------- | :----------------------------------------------|
| Numpy            | To handle Numpy arrays                         |
| Pandas           | To store and access info in a DataFrame        |
| Matplotlib       | To plot the data                               |
| request          | To make request to an API                      |
| jupyter          | To open Jupyter Notebook                       |
| plotly           | To plot in (interactive) 3D                    |
| rasterio         | To open and handle LIDAR files                 |
| rioxarray        | To convert LIDAR files into arrays             |

[**↥ Back To The Top**](#table-of-contents)


### Must-have features

3D lookup of houses.

### Nice-to-have features

Optimize your solution to have the result as fast as possible.
Features like the living area of the house in m², how many floors, if there is a pool, the vegetation in the neighborhood, etc...
Better visualization.

### Miscellaneous information

What is LIDAR ?
LIDAR is a method to measure distance using light. The device will illuminate a target with a laser light and a sensor will measure the reflection. Differences in wavelength and return times will be used to get 3D representations of an area.


### Lidar Segmentation

With those points clouds we can easily identify houses, vegetation, roads, etc...
The results we're insterested in are DSM (Digital Surface Map) and DTM (Digital Terrain Map).
Which are already computed and available here :DSM, DTM

## Before using this code

1.Create a virtual environment with python 3.7 (with its own kernel) and download the following libraries:

- requests
- json
- rasterio
- rioxarray
- plotly

2.Create a directory to work in.

note: the following data to download is quite extensive. DO NOT CHANGE THE NAMES OF THE FILES.

3.Download the DSM .zip files from this website: http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m
and unpack ONLY the .tif file inside the GEOTiff folder to a created folder called DSM.

4.Download the DTM .zip files from this website: http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m
and unpack ONLY the .tif file inside the GEOTiff folder to a created folder called DTM.

5.Download and open the 3D-House-Project_Code.ipynb in the created virtual environment.

6.Within the dsm_search function within class LidarData, change your directory to the directory where your DSM and DTM folder are stored.

7.Run all in 3D-House-Project_Code.ipynb

## How does it work

This will be added.

| ![](Images/CHM_example.png) |
|:-:|
| CHM = DSM - DTM |

## Results

These are examples of results of adresses in Belgium (the precise location will not be shared out of privacy).

| ![](Results/3D-house-example-1.png)  | ![](Results/3D-house-example-2.png)  |
|:-:|:-:|
| Result example 1 | Result example 2 | 

## Pending things to do

- Add raised errors
- Make the project work without downloading the DSM and DTM (f.e.: with an online server)
- Make the project more general and user friendly
- Add the "Nice-to-have features"
- Add a small boarder around the x-axis and y-axis so all walls are included (sometimes walls are excluded at the boundary points of the polygon)
- Add 'How does it work' to create more clarity to users
