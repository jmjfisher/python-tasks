'''
REFERENCES
    https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python
https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Create-your-first-GUI-application
http://effbot.org/tkinterbook/canvas.htm
http://effbot.org/tkinterbook/pack.htm
'''

print "Importing libraries...\n"

import PIL.Image
import PIL.ImageTk
import os
import arcpy
from arcpy import env
from arcpy.sa import *
from tkinter import *
from tkinter.ttk import Progressbar

print "Libraries imported...\n"

window = Tk()
window.title("Spatial Analysis: Linear Regression of Cancer and Nitrate")
window.geometry('900x680')

global bar
global runk

intro = Label(window, text="An application that runs linear regression analysis to determine if cancer rates "+
              "are impacted by nitrate levels in water in Wisconsin through IDW and GWR.")
intro.pack(padx=10, pady= 10, side= TOP, anchor=W)

mainframe = Frame(window, relief=SUNKEN, borderwidth=5)
mainframe.pack(fill=BOTH, expand=True)

#scrollbar = Scrollbar(mainframe)
#scrollbar.pack(side=RIGHT, fill=Y)

baseheight = 580
new_img = PIL.ImageTk.PhotoImage(PIL.Image.open("splash.png"))
canvas = Canvas(mainframe, bg='white', width=652, height=580)
canvas.pack()
item = canvas.create_image(0, 0, anchor=NW, image=new_img)

#scrollbar.config(command=canvas.yview)

buttonframe = Frame(window, padx=5, pady=5, height=40)
buttonframe.pack(fill=X, side=BOTTOM)

arcpy.env.workspace = "C:/UWGIS/777_Capstone/proj_1"

arcpy.CheckOutExtension("Spatial")

def idw_create(kval):

    print "\nCreating IDW raster..."

    IDWfile = "idwout.tif"
    if arcpy.Exists(IDWfile):
        arcpy.Delete_management(IDWfile)

    outIDW = Idw("well_4326.shp", "nitr_ran","",kval)
    outIDW.save(IDWfile)

    print "IDW created!\n"

    bar['value'] = 20
    bar.update()

    zone_stat(IDWfile)

def zone_stat (IDWfile):
    
    print "Creating the Zonal Statistics raster..."

    ZSfile = "ZonalStats.tif"
    if arcpy.Exists(ZSfile):
        arcpy.Delete_management(ZSfile)

    outZonalStats = ZonalStatistics ("tract_4326.shp", "GEOID10", IDWfile, "MEAN")
    outZonalStats.save(ZSfile)

    print "Zonal Statistics raster created!\n"

    bar['value'] = 40
    bar.update()

    raster_to_point(ZSfile)

def raster_to_point (ZSfile):

    print "Converting zonal statistics raster to points..."

    ZSpoints = "zs_points.shp"
    if arcpy.Exists(ZSpoints):
        arcpy.Delete_management(ZSpoints)
    
    arcpy.RasterToPoint_conversion(ZSfile, ZSpoints, "Value")

    print "Finished raster to points!\n"

    bar['value'] = 60
    bar.update()

    spatial_join(ZSpoints)

def spatial_join (ZSpoints):

    print "Creating spatial join layer..."

    SJfile = "spatial_join.shp"
    if arcpy.Exists(SJfile):
        arcpy.Delete_management(SJfile)
    
    arcpy.SpatialJoin_analysis("tract_4326.shp", ZSpoints, SJfile, "", "", "", "CLOSEST")

    print "Finished spatial join!\n"

    bar['value'] = 80
    bar.update()

    gwr_shape(SJfile)

def gwr_shape(SJfile):

    print "Creating GWR layer..."

    GWRfile = "gwr_final.shp"
    GWRdbf = "gwr_final_supp.dbf"
    if os.path.isfile(GWRdbf) == True:
        os.remove(GWRdbf)
    if arcpy.Exists(GWRfile):
        arcpy.Delete_management(GWRfile)
        
    arcpy.GeographicallyWeightedRegression_stats(SJfile, "canrate", "grid_code", GWRfile, "FIXED", "AICc")

    print "Finished GWR!\n"

    bar['value'] = 100
    bar.update()

    idwbtn.config(state=NORMAL)
    tractsbtn.config(state=NORMAL)

def raster(mxd_idw):

    if os.path.isfile("work_idw.mxd") == True:
        os.remove("work_idw.mxd")

    mxd_idw.saveACopy("work_idw.mxd")

    mxd = arcpy.mapping.MapDocument("work_idw.mxd")
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "Legend")[0]
    legend.autoAdd = True

    IDWwork = "idw_working.lyr"
    if arcpy.Exists(IDWwork):
        arcpy.Delete_management(IDWwork)

    arcpy.MakeRasterLayer_management("idwout.tif",IDWwork)

    IDWlyr = arcpy.mapping.Layer(IDWwork)

    arcpy.mapping.AddLayer(df, IDWlyr, "TOP")

    updateLayer = arcpy.mapping.ListLayers(mxd, "*", df)[0]
    sourceLayer = arcpy.mapping.Layer("IDW3.lyr")
    arcpy.mapping.UpdateLayer(df, updateLayer, sourceLayer, True)

    legend.autoAdd = False
    WIoutline = arcpy.mapping.Layer("wi_outline.lyr")
    arcpy.mapping.AddLayer(df, WIoutline, "TOP")

    df.extent = WIoutline.getSelectedExtent()

    outPNG = "idw_pic"+str(runk)+".png"
    resizePNG = "resized_idw"+str(runk)+".png"
    if os.path.isfile(outPNG) == True:
        os.remove(outPNG)
        
    arcpy.mapping.ExportToPNG(mxd, outPNG)

    print "idw png exported\n"
    del IDWwork
    del mxd
    os.remove("work_idw.mxd")

    global img
    img = PIL.Image.open(outPNG)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(resizePNG)

    global new_img
    new_img = PIL.ImageTk.PhotoImage(PIL.Image.open(resizePNG))
    canvas.itemconfigure(item, image=new_img)

    idwbtn.config(state=DISABLED)
    tractsbtn.config(state=NORMAL)

    bar['value'] = 0
    bar.update()
    
    return;

def linear(mxd_linear):

    if os.path.isfile("work_linear.mxd") == True:
        os.remove("work_linear.mxd")

    mxd_linear.saveACopy("work_linear.mxd")

    mxd = arcpy.mapping.MapDocument("work_linear.mxd")
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT", "Legend")[0]
    legend.autoAdd = True

    GWRwork = "gwr_working.lyr"
    if arcpy.Exists(GWRwork):
        arcpy.Delete_management(GWRwork)

    arcpy.MakeFeatureLayer_management("gwr_final.shp", GWRwork)

    GWRlyr = arcpy.mapping.Layer(GWRwork)

    arcpy.mapping.AddLayer(df, GWRlyr, "TOP")

    updateLayer = arcpy.mapping.ListLayers(mxd, "*", df)[0]
    sourceLayer = arcpy.mapping.Layer("GWR_ARC.lyr")
    arcpy.mapping.UpdateLayer(df, updateLayer, sourceLayer, True)

    legend.autoAdd = False
    WIoutline = arcpy.mapping.Layer("wi_outline.lyr")
    arcpy.mapping.AddLayer(df, WIoutline, "TOP")

    df.extent = WIoutline.getSelectedExtent()
    
    outPNG = "gwr_pic"+str(runk)+".png"
    resizePNG = "resized_gwr"+str(runk)+".png"
    if os.path.isfile(outPNG) == True:
        os.remove(outPNG)
        
    arcpy.mapping.ExportToPNG(mxd, outPNG)
    
    print "gwr png exported"
    del GWRwork
    del mxd
    os.remove("work_linear.mxd")

    global img
    img = PIL.Image.open(outPNG)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(resizePNG)

    global new_img
    new_img = PIL.ImageTk.PhotoImage(PIL.Image.open(resizePNG))
    canvas.itemconfigure(item, image=new_img)

    tractsbtn.config(state=DISABLED)
    idwbtn.config(state=NORMAL)

    bar['value'] = 0
    bar.update()
    
    return;

mxd_idw = arcpy.mapping.MapDocument("temp_idw.mxd")
mxd_linear = arcpy.mapping.MapDocument("temp_linear.mxd")

instruction = Label(buttonframe, text="Enter a k value (>1) for the IDW analysis: ")
instruction.pack(side=LEFT)

kval = Entry(buttonframe, width=10)
kval.pack(side=LEFT, padx=5)

def clickedStart():

    global runk
    runk = kval.get()
    print "q value: " + str(runk)

    idw_create(runk)

def clickedRaster():
    raster(mxd_idw)

def clickedTracts():
    linear(mxd_linear)

runbtn = Button(buttonframe,text="Run Analysis", command=clickedStart)
runbtn.pack(side=LEFT)

bar = Progressbar(buttonframe, length=200, mode='determinate')
bar.pack(side=LEFT, padx=10)
bar['value'] = 0

tractsbtn = Button(buttonframe,text="View Regression Results", state=DISABLED, command=clickedTracts)
tractsbtn.pack(side=RIGHT)

idwbtn = Button(buttonframe,text="View IDW Results", state=DISABLED, command=clickedRaster)
idwbtn.pack(side=RIGHT, padx=5)

window.mainloop()
