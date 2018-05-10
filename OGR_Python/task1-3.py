#Per the instructions, this script contains tasks 1-3

##############
#BEGIN TASK 1#
##############

import ogr
import gdalconst
import sys
import math

print 'TASK 1 INFORMATION\n'

#open the PowerLine shp file with the ESRI driver to read its information
source = 'PowerLine\\PowerLine.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
datasource = driver.Open(source, gdalconst.GA_ReadOnly)

#if the file DNE, the program will close
if datasource is None:
   print 'Failed to open file'
   sys.exit(1)

layer = datasource.GetLayer(0) #extract the lone layer from the data source
feat = layer.GetFeature(0) #extract the first/only feature from that layer
line = feat.GetGeometryRef() #find out what kind of feature it is
np = line.GetPointCount() #count how many points are in that line which we need for the length calculation

pl = [] #create an empty list to store the points

'''
the following bit loops through all points on the line
and appends their coordinates to the point list
each unique straight segment of the line's distance is then calculated
with the distance function using each successive point. since there are
the 3 straight segements are then added together and divided by 5280 to
get the final value in miles.
'''

for i in range(0, np):
    pt = line.GetPoint(i)
    pl.append(pt)

d1 = math.sqrt( (pl[0][0] - pl[1][0])**2 + (pl[0][1] - pl[1][1])**2)
d2 = math.sqrt( (pl[1][0] - pl[2][0])**2 + (pl[1][1] - pl[2][1])**2)
d3 = math.sqrt( (pl[2][0] - pl[3][0])**2 + (pl[2][1] - pl[3][1])**2)

distance = (d1 + d2 + d3)/5280
print 'The length of the power line via point by point calculation is',distance

val = line.Length()
vmiles = val/5280 #you can also simply take the length of the line through the Length method
print 'The length of the power line via the length method is',vmiles

#close the feature and dataset accordingly
feat.Destroy()
datasource.Destroy()

if distance == vmiles:
   print '\nThe two methods of calcuation are identical.'
else:
   print'\nThe two methods are NOT identical.'

##############
#BEGIN TASK 2#
##############

print '\nTASK 2 INFORMATION'

#open the Parcel shp file with the ESRI driver to read its information
source = 'Parcels\\Parcels.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
datasource = driver.Open(source, gdalconst.GA_ReadOnly)

if datasource is None:
   print 'Failed to open file'
   sys.exit(1) #if the file DNE, the program will close

layer = datasource.GetLayer(0) #extract the lone layer from the data source
featureDefn = layer.GetLayerDefn() #get the feature definition, or the information of its attributes
fieldCount = featureDefn.GetFieldCount() #count how many fields of attributes there are
featureCount = layer.GetFeatureCount() #count how many features are in the layer

print '\nThe attribute names and their data types are as follows:\n'

'''
the following will loop through each field of the features and extract
that field's name (which is turned into a string) and type
then each field's string name and type are printed out
'''

for i in range(0,fieldCount):
   fieldDef = featureDefn.GetFieldDefn(i)
   name = fieldDef.GetNameRef()
   fldtype = fieldDef.GetType()
   fieldstring = fieldDef.GetFieldTypeName(fldtype)
   print 'Name: %10s Type: %s' % (name,fieldstring)

'''I did not Destroy the data or feat because they are used in task 3
I read task 3 before completing task two so I knew not to do this
HOWEVER I did not read task 3 before completing task 1 so the beginning
of task 3 is actually me reopening the Powerline.shp to be read and setting
those variouables as x2 because source and layer were already being used by
the parcel information.'''
   
##############
#BEGIN TASK 3#
##############

print '\nTASK 3 INFORMATION'

source2 = 'PowerLine\\PowerLine.shp'
datasource2 = driver.Open(source2, gdalconst.GA_ReadOnly)

if datasource2 is None:
   print 'Failed to open file'
   sys.exit(1)

layer2 = datasource2.GetLayer(0)
feat2 = layer2.GetFeature(0)
line = feat2.GetGeometryRef()

print '\nThe following parcels with their corresponding sizes are crossed by the power line.\n'

'''
now that the powerline.shp has been opened and its data organized again, we can begin to use that
to complete the 'cross' task.
this for loop loops through each polygon in the parcel layer and then uses the Crosses method to
see if it crosses the powerline (line). if it does, cross = True and the if statement will
execute. that polygon's address and area will be extracted accordingly and printed out. Once
all of the polygons have been checked the program will destroy the open features and datasets
and print a statement saying exactly how many polygons are crossed by the polygon, just for
a reference.
'''

count = 0
for i in range(0,featureCount-1):
   feat = layer.GetFeature(i)
   poly = feat.GetGeometryRef()
   cross = poly.Crosses(line)
   if cross == True:
      count += 1
      address = feat.GetField('SITUSADDR')
      area = feat.GetField('AREA')
      print 'Address: %17s Size: %.2f' % (address,area)

feat.Destroy()
feat2.Destroy()
datasource.Destroy()
datasource2.Destroy()

print '\nIn total',count,'parcels are crossed by the power line.'
