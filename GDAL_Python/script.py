import gdal
import os
import gdalconst
import numpy as N

'''
COMMENTS FOR THE ENTIRE SCRIPT
Based on the directions, it very simply asked us to write the sript that will create
a NDVI image from the data. I took that to mean that we did not need to check for input
errors or finding the correct files and such. I did this because I thought of it as if
an employer asked for this file and they would want the most efficient way of doing it
which is housing the script in the same folder as the files and therefore when
we call gdal.open it doesn't need a path since I know excactly where the files are housed.

first we need to import gdal, gdalconstr and numpy for the tasks to perform correctly.
then we will open the Red and NearIR files through gdal and "save" those datasets
those will then be read as arrays in gdal but we need to make sure that it is
in the float format, so we call numpy astype (found info on this online). we need them to be in float because
if they were not in float format they would round when dividing later on.
after that we have to set up our output dataset's details, such as its driver,
which is recognized by gdal automatically, then the image's rows, columns, bands,
and data type. since we are using two "bands" from the same tiff and the output is
basically a "new band" we can copy the transfer, projection, and size as they will
all be the same.

finally, the computation may begin once the new tiff is organized and set.
since there is a possibility of dividing by zero, I spent a lot of time on google
and in python threads on how to make sure this doesn't crash the program. the best
way I found is using the numpy.seterr method. what this does is ignores any division
errors and defaults to the value of 0 which is what we want (based on my basic understanding
of how it works). from there, I separate the top and bottom values of the NDVI equation
to prevent human errors, and then divide the two and set that to the ndvi variable. again,
all of these arrays utilize floats and not integers because the final output has values
between -1 and 1 so every fraction is extremely important. the image would not be nearly as
useful if they were all -1, 0 , or 1.
finally, we define the single band in the output dataset and then use that band to write the
array with the values within ndvi. this is where the NewRaster.tif is "filled" with data.
lastly, we "close" the datasets to save memory, which according to our module is done by
setting them all equal to "None"
'''

try:
    dsinred = gdal.Open('L71026029_02920000609_B30_CLIP.TIF')
    red = dsinred.ReadAsArray().astype(N.float)
except:
    print 'The Red file does not exist in this directory.'
    os._exit(1)
try:
    dsinnir = gdal.Open('L71026029_02920000609_B40_CLIP.TIF')
    nir = dsinnir.ReadAsArray().astype(N.float)
except:
    print 'The NearIR file does not exist in this directory.'
    os._exit(1)

outDriver = dsinred.GetDriver()
rows = dsinred.RasterYSize
cols = dsinred.RasterXSize
nBands = 1
dataType = gdal.GDT_Float32
dsOut = outDriver.Create('NDVI.tif',cols, rows, nBands, dataType)
dsOut.SetProjection(dsinred.GetProjection())
dsOut.SetGeoTransform(dsinred.GetGeoTransform())

N.seterr(divide = 'ignore')

top = N.subtract(nir,red)
bottom = N.add(nir,red)
ndvi = N.divide(top,bottom)

band = dsOut.GetRasterBand(1)
band.WriteArray(ndvi)

dsinred = dsinnir = dsOut = None
print "The file was successfully created and the datasets have been closed."
