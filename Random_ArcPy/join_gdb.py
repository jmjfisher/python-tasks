import arcpy
print ("Imported...")

arcpy.env.workspace = "O:/RO_GEOGRAPHY/FLD_GSB/CollectionGEO/Shapefiles/PDB_2018"

#counties = [] - list of every county in country

for co in counties:
    
    inFeatures = "/tract73_2018/tract73_2018_"+co+"_tract_v73.shp"
    inLayer = "tract73_2018_"+co+"_tract"
    in_field = "TRACTCE"
    joinTable = "/pdb2018/"+co+"_pdb.csv"
    join_field = "Tract"

    arcpy.MakeFeatureLayer_management(inFeatures, inLayer)
    print ("Layer ",co)
    joinLayer = arcpy.AddJoin_management(inLayer, in_field, joinTable, join_field)
    print ("Joined")
    arcpy.FeatureClassToGeodatabase_conversion(joinLayer,'testing.gdb')
    #arcpy.CopyFeatures_management(joinLayer,"justatest")
    arcpy.Delete_management(inLayer)
    arcpy.Delete_management(joinLayer)
    print ("Finished ",co)