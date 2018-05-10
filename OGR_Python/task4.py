##############
#BEGIN TASK 4#
##############

import ogr
import os
import gdalconst
import sys
import math

#this opens the PowerLine shp file using the ESRI driver
linesource = 'PowerLine\\PowerLine.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
linedatasource = driver.Open(linesource, gdalconst.GA_ReadOnly)

#if the shapefile doesn't exist, the program exits
if linedatasource is None:
   print 'Failed to open file'
   sys.exit(1)

#then it extracts the data we need, such as the only layer and its line feature
linelayer = linedatasource.GetLayer(0)
linefeat = linelayer.GetFeature(0)
line = linefeat.GetGeometryRef()

#this opens the Parcels shp file using the ESRI driver
parsource = 'Parcels\\Parcels.shp'
pardatasource = driver.Open(parsource, gdalconst.GA_ReadOnly)

#if the shapefile doesn't exist, the program exits
if pardatasource is None:
   print 'Failed to open file'
   sys.exit(1)

#then it extracts the data we need, such as the only layer and its polygon features
parlayer = pardatasource.GetLayer(0)
parfeat = parlayer.GetFeature(0)
par = parfeat.GetGeometryRef()
#we get a count of how many polygons are in the layer for a loop later on
parcount = parlayer.GetFeatureCount()

#begin to set up new shapefile by checking to make sure it doesn't already exist
#if it does, delete it
if os.path.exists('ParsWithin250.shp'):
   os.remove('ParsWithin250.shp')

#Create properites for new shp file
dsout = driver.CreateDataSource('ParsWithin250.shp')
#pull the SRS from the Parcels shapefile
SRS = parlayer.GetSpatialRef()
#create the actual layer using the SRS, geometry type, and name as arguments
layer = dsout.CreateLayer('ParcelsWithin',SRS,geom_type=ogr.wkbPolygon)
#we will need the layerdef when adding features to the layer
layerdef = layer.GetLayerDefn()

#create buffer feature and add it to the geometry
width = 250
buff = line.Buffer(width)

'''
THIS COMMENT SECTION IS FOR THE FOLLOWING FOR LOOP
first we set a count to 0 so we can se the ID number later on
then we want to loop through each polygon in the parcels layer
to see if it is fully within the 'buff' feature
if the parcel is within the buffer, then 'cross' is True and
the if statement may execute.
in there, we add 1 to the count, and then begin making the new feature
first it gets created based on the 'layerdef' which was defined
when creating the shapefile. then we actually add the parcel as the
new feature which is stored as 'tpoly' or test polygon.
then we give that feature an ID value of the count variable so they are
identified in order. and finally, we actually add the newfeature to the
layer with the CreateFeature method.
'''

count = 0
for i in range(0,parcount-1):
   tfeat = parlayer.GetFeature(i)
   tpoly = tfeat.GetGeometryRef()
   cross = buff.Contains(tpoly)
   if cross == True:
      count += 1
      newfeature = ogr.Feature(layerdef)
      newfeature.SetGeometry(tpoly)
      newfeature.SetFID(count)
      layer.CreateFeature(newfeature)

print 'The ParsWithin250.shp file has been created which displays\nthe %d parcels fully within 250 feet of the power line.' % count

#close all opened features and datasets to free up memory
tfeat.Destroy()
linefeat.Destroy()
parfeat.Destroy()
dsout.Destroy()
linedatasource.Destroy()
pardatasource.Destroy()
