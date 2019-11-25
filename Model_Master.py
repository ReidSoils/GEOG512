import arcpy

# Allow overwrite of outputs
arcpy.env.overwriteOutput = True

# Geoprocessing environments
arcpy.env.scratchWorkspace = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb"
arcpy.env.outputCoordinateSystem = "PROJCS['NAD_1983_2011_StatePlane_Tennessee_FIPS_4100',GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',600000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-86.0],PARAMETER['Standard_Parallel_1',35.25],PARAMETER['Standard_Parallel_2',36.41666666666666],PARAMETER['Latitude_Of_Origin',34.33333333333334],UNIT['Meter',1.0]],VERTCS['NAVD88_height_(ftUS)',VDATUM['North_American_Vertical_Datum_1988'],PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Foot_US',0.3048006096012192]]"
arcpy.env.extent = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\c2290557SW"
arcpy.env.cellSize = "1"
arcpy.env.workspace = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb"

# Script parameters
Trail = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\trailgps"
DEM = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\c2290557SW"
SoilData = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Soils_AOI"
# Local variables:
Fill_DEM = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Fill_DEM"
Output_drop_raster = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Drop_DEM"
Hillshade = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\DEM_HShade"
Slope_Percent = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\DEM_Slper"
DEM_Aspect = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\DEM_Asp"
DEM_Domain = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\DEM_Domain"
Trail_Clip = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_Clip"
Trail_Raster = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_Raster"
DEM_FlowDir = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\DEM_FlowDir"
FlowAcc_DEM = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\FlowAcc_DEM"
FlowAcc_1ha = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\FlowAcc_1ha"
FlowLines1ha = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\FlowLines1ha"
WShed_1ha = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\WShed_1ha"
WShed_1k = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\WShed_1k"
Trail_Seg = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_Seg"
Trail_WShed = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_WShed"
Trail_Area = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_Area"
Trail_Filt10 = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_Filt10"
Trail_Line = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_Poly"
Trail_FlMax = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Trail_FlMax"
Pour_Flow = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Pour_Flow"
T_FlowMax = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_FlowMax"
Soils = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Soils"
CN_P = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Precip_2x24"
Soil_CN = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Soil_Curve"
CN_S = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Curve_S"
CN_Q = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Curve_Q"
CN_RO_SI = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\RO_Meters"
RO_Acc_SI = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\ROAcc_CuMt"
Trail_RO = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\RO_Trail"
T_ROFlow = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\ROT_Flow"
WST_Slope = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Tshed_slope"
WST_Aspect = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Tshed_Aspect"
WSF_Slope = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Tflw_slope"
WSF_Aspect = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Tflw_Aspect"
RO_MaxFlow = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\ROAcc_PPFlow"
PP_MaxFlow = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\MaxFlow_Point"
Trail_Slope = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_SlopePer"
Trail_Aspect = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_AspectAvg"
Trail_Slope_Pt = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_Slope_Pt"
Trail_Aspect_Pt = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_Aspect_Pt"
Trail_RelSlo_Pt = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_SloRel_Pt"
Trail_TSA_Pt = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_TSA_Pt"
TrailTSA_Fall = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\T_FallLine"
TrailSeg_FallLine = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\TSeg_Fall"
TrailPT_OverSlope = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Tpt_SloWarn"
TrailSeg_OverSlope = r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\Tseg_SloWarn"

    # Process: Fill - works
fill = arcpy.sa.Fill(DEM)
fill.save(Fill_DEM)
print ("Fill complete.")

    # Process: Flow Direction - works
flow = arcpy.gp.FlowDirection_sa(Fill_DEM, DEM_FlowDir, "Normal", "D8")
print ("Flow Direction complete.")

    # Process: Hillshade - works
hshade = arcpy.HillShade_3d(Fill_DEM, Hillshade, "315", "45", "NO_SHADOWS", "1")
print ("Hillshade complete.")

     # Process: Slope Raster
slope = arcpy.Slope_3d(Fill_DEM, Slope_Percent, "PERCENT_RISE", 0.3048, "PLANAR", "")
print ("Slope Raster complete.")

     # Process: Aspect Raster
aspect = arcpy.sa.Aspect(Fill_DEM, "PLANAR", "")
aspect.save (DEM_Aspect)
print ("Aspect Raster complete.")

    # Process: Raster Domain - works
arcpy.RasterDomain_3d(Fill_DEM, DEM_Domain, "POLYGON")
print ("Raster Domain complete.")

    # Process: Clip - works
tempEnvironment0 = arcpy.env.extent
arcpy.Clip_analysis(Trail, DEM_Domain, Trail_Clip)
arcpy.env.extent = tempEnvironment0
print ("Trail Clip complete.")

    # Process: Feature to Raster - works
arcpy.FeatureToRaster_conversion(Trail_Clip, "OBJECTID", Trail_Raster, "1")
print ("Feature to Raster complete.")

    # Process: Flow Accumulation - works
flowacc = arcpy.sa.FlowAccumulation(DEM_FlowDir, "", "FLOAT", "D8")
flowacc.save(FlowAcc_DEM)
print ("Flow Accumulation complete.")

    # Process: Flow Threshold - works
outSetNull = arcpy.sa.SetNull(FlowAcc_DEM, FlowAcc_DEM, "Value < 10000")
outSetNull.save(FlowAcc_1ha)
print ("Flow Accumulation Threshold complete.")

    # Process: Stream Link- works
outStreamLink = arcpy.sa.StreamLink("FlowAcc_1ha", "DEM_FlowDir")
outStreamLink.save(FlowLines1ha)
print ("Stream Link complete.")

    # Process: Watershed - works
wShed = arcpy.sa.Watershed(DEM_FlowDir, FlowLines1ha, "VALUE")
wShed.save(WShed_1ha)
print ("Watershed_1ha complete.")

   # Process: TrailSeg_ID - works
Trail_ID = arcpy.sa.Raster(Trail_Raster) * arcpy.sa.Raster(WShed_1ha)
Trail_ID.save(Trail_Seg)
print ("Trail Segment ID complete.")

    # Process: Trail Watershed - works
Trail_Shed = arcpy.sa.Watershed(DEM_FlowDir, Trail_Seg, "VALUE")
Trail_Shed.save(Trail_WShed)
print ("Trail Watershed complete.")

    # Process: Zonal Sum - works
Trail_Sum = arcpy.sa.ZonalStatistics(in_zone_data=Trail_Seg, zone_field="Value", in_value_raster=Trail_Raster, statistics_type="SUM", ignore_nodata="DATA")
Trail_Sum.save(Trail_Area)
print ("Trail Area complete.")

    # Process: Raster Calculator
Trail_Con = arcpy.sa.Con(arcpy.sa.Raster("Trail_Area") >= 10, "Trail_Seg")
Trail_Con.save(Trail_Filt10)
print ("Trail Filter complete.")

    # Process: Zonal Flow Max
Trail_FlAx = arcpy.sa.ZonalStatistics(in_zone_data=Trail_Filt10, zone_field="Value", in_value_raster=FlowAcc_DEM, statistics_type="MAXIMUM", ignore_nodata="DATA")
Trail_FlAx.save(Trail_FlMax)
print ("Trail Flow Max complete.")

    # Process: TrailPour_Flow
Trail_Pour = arcpy.sa.Con(arcpy.sa.Raster("Trail_FlMax") == arcpy.sa.Raster("FlowAcc_DEM"), Trail_Seg)
Trail_Pour.save(Pour_Flow)
print ("Trail Pour Points complete.")

    # Process: Watershed FlMax
Trail_Shed = arcpy.sa.Watershed(DEM_FlowDir, Pour_Flow)
Trail_Shed.save(T_FlowMax)
print ("Trail Watershed complete.")

    # Clip Soil data to DEM
tempEnvironment0 = arcpy.env.extent
arcpy.Clip_analysis(SoilData, DEM_Domain, Soils)
arcpy.env.extent = tempEnvironment0
print ("Soil Clip complete.")

    # Add field
arcpy.AddField_management(Soils, "CN", "SHORT")
print ("Fields added")
field1 = "hydgrpdcd"
field2 = "CN"
print ("Variables assigned")
cursor = arcpy.UpdateCursor(Soils)
row = cursor.next()
# Set row count to 0
rowC = 0
# Assign buffer values
while row:
    if row.getValue(field1) == "A":
        row.setValue(field2, 30)
    elif row.getValue(field1) == "B":
        row.setValue(field2, 55)
    elif row.getValue(field1) == "C":
        row.setValue(field2, 70)
    elif row.getValue(field1) == "D":
        row.setValue(field2, 77)
    else:
        row.setValue(field2, 0)
    cursor.updateRow(row)
    row = cursor.next()
    rowC += 1
    # print row count    
    print ("CN values assigned to row: " + str(rowC))
# CN field update complete
print("Operation complete")

    # Create Constant Raster
Precip = arcpy.sa.CreateConstantRaster(3.65, "FLOAT", 1, r"C:\Users\NReid\Documents\ArcGIS\Projects\TrailProjectModel\modelData.gdb\c2290557SW")
Precip.save (CN_P)
print("Design storm raster complete")

    # Process: Feature to Raster - works
arcpy.FeatureToRaster_conversion(Soils, "CN", Soil_CN, "1")
print ("Soil CN to Raster complete.")

     # Process: Create S Raster
S_Term = arcpy.sa.Raster((1000 / arcpy.sa.Raster(Soil_CN)) - 10)
S_Term.save(CN_S)
print ("CN S complete.")

    # Process: Create Q Raster
Q_Term = arcpy.sa.Raster((arcpy.sa.Power((arcpy.sa.Raster(CN_P)-(0.2*arcpy.sa.Raster(CN_S))),2) / (arcpy.sa.Raster(CN_P)+(0.8*arcpy.sa.Raster(CN_S)))))
Q_Term.save(CN_Q)
print ("CN Q complete.")

    # Process: Create Runoff Raster (convert Q to meters)
Cont_RO = arcpy.sa.Raster(arcpy.sa.Raster(CN_Q)/39.37)
Cont_RO.save(CN_RO_SI)
print ("Runoff raster complete")

    # Watershed RO - Trail
TRO = arcpy.sa.ZonalStatistics(in_zone_data=Trail_WShed, zone_field="Value", in_value_raster=CN_RO_SI, statistics_type="SUM", ignore_nodata="DATA")
TRO.save(Trail_RO)
print ("Trail Runoff Watershed complete.")

    # Slope_Trail Watershed
TWS_Slope = arcpy.sa.ZonalStatistics(in_zone_data=Trail_WShed, zone_field="Value", in_value_raster=Slope_Percent, statistics_type="MEAN", ignore_nodata="DATA")
TWS_Slope.save(WST_Slope)
print ("Trail Watershed slope complete.")

    # Aspect_MaxFlow Watershed
TWS_Aspect = arcpy.sa.ZonalStatistics(in_zone_data=Trail_WShed, zone_field="Value", in_value_raster=DEM_Aspect, statistics_type="MEAN", ignore_nodata="DATA")
TWS_Aspect.save(WST_Aspect)
print ("Trail Watershed aspect complete.")

    # Watershed RO - FlowMax
TRO_Flow = arcpy.sa.ZonalStatistics(in_zone_data=T_FlowMax, zone_field="Value", in_value_raster=CN_RO_SI, statistics_type="SUM", ignore_nodata="DATA")
TRO_Flow.save(T_ROFlow)
print ("Trail Max Flow watershed complete.")

    # Slope_MaxFlow Watershed
FWS_Slope = arcpy.sa.ZonalStatistics(in_zone_data=T_FlowMax, zone_field="Value", in_value_raster=Slope_Percent, statistics_type="MEAN", ignore_nodata="DATA")
FWS_Slope.save(WSF_Slope)
print ("Trail Max Flow slope complete.")

   # Aspect_MaxFlow Watershed
FWS_Aspect = arcpy.sa.ZonalStatistics(in_zone_data=T_FlowMax, zone_field="Value", in_value_raster=DEM_Aspect, statistics_type="MEAN", ignore_nodata="DATA")
FWS_Aspect.save(WSF_Aspect)
print ("Trail Max Flow aspect complete.")

    # Process: Runoff Accumulation (in cubic meters)
runoff = arcpy.sa.FlowAccumulation(DEM_FlowDir, CN_RO_SI, "FLOAT", "D8")
runoff.save(RO_Acc_SI)
print ("Runoff Accumulation complete.")

    # Process: Runoff Accumulation @ Pour Points-Max Flow
RO_PPFlow = arcpy.sa.Raster(Pour_Flow) * arcpy.sa.Raster(RO_Acc_SI)
RO_PPFlow.save(RO_MaxFlow)
print ("Runoff Accumulation @ Pour Points-Max Flow complete.")

    # Process: Raster to Point - Pour Points-Max Flow
arcpy.RasterToPoint_conversion(RO_MaxFlow, PP_MaxFlow)
print ("Max Flow Pour Points complete")

    # Trail_Slope
T_Slope = arcpy.sa.ZonalStatistics(in_zone_data=Trail_Seg, zone_field="Value", in_value_raster=Slope_Percent, statistics_type="MEAN", ignore_nodata="DATA")
T_Slope.save(Trail_Slope)
print ("Trail Segment slope complete.")

    # Trail_Aspect
T_Aspect = arcpy.sa.ZonalStatistics(in_zone_data=Trail_Seg, zone_field="Value", in_value_raster=DEM_Aspect, statistics_type="MEAN", ignore_nodata="DATA")
T_Aspect.save(Trail_Aspect)
print ("Trail Segment Aspect complete.")

    # Process: TrailPour_Flow - Slope
Trail_Pour = arcpy.sa.Con(arcpy.sa.Raster("Trail_FlMax") == arcpy.sa.Raster("FlowAcc_DEM"), Trail_Slope)
Trail_Pour.save(Trail_Slope_Pt)
print ("Trail Pour Points complete.")

    # Process: TrailPour_Flow - Aspect
Trail_Pour = arcpy.sa.Con(arcpy.sa.Raster("Trail_FlMax") == arcpy.sa.Raster("FlowAcc_DEM"), Trail_Aspect)
Trail_Pour.save(Trail_Aspect_Pt)
print ("Trail Pour Points complete.")

    # Trail_Relative Slope_Point
fiftyPer = arcpy.Raster(Trail_Slope_Pt)/arcpy.Raster(WSF_Slope)
fiftyPer.save(Trail_RelSlo_Pt)
print ("Trail relative slope complete.")

    # Process: Trail Polyline - works
arcpy.RasterToPolyline_conversion(in_raster=Trail_Seg, out_polyline_features=Trail_Line, background_value="ZERO", minimum_dangle_length="0", simplify="SIMPLIFY", raster_field="Value")
print("Trail Segment Polyline complete.")

    # Process: Trail Bearing
arcpy.AddGeometryAttributes_management(Trail_Line, "LINE_BEARING")

    # Trail_Slope_Alignment_Point
TSA_raw = arcpy.Raster(Trail_Aspect_Pt)-arcpy.Raster(WSF_Aspect)
TSA_diff = (TSA_raw + 180) % 360 - 180
TSA = arcpy.sa.Abs(TSA_diff)
TSA.save(Trail_TSA_Pt)
print ("Trail slope alignment complete.")

     # Trail_TSA _ Fall Line Points
TSAover45 = arcpy.sa.Con(arcpy.sa.Raster(Trail_TSA_Pt) < 45, Trail_TSA_Pt)
TSAover45.save(TrailTSA_Fall)
print ("Trail fall line points.")

    # Trail_Segment - Fall Line Violations
Fallseg = arcpy.sa.ZonalStatistics(in_zone_data=Trail_Seg, zone_field="Value", in_value_raster=TrailTSA_Fall, statistics_type="MAXIMUM", ignore_nodata="DATA")
Fallseg.save(TrailSeg_FallLine)
print ("Trail fall line segments complete.")

    # Trail_Pt - 50% Rule Violations
Over50pt = arcpy.sa.Con(arcpy.sa.Raster(Trail_RelSlo_Pt) > 0.50, Trail_RelSlo_Pt)
Over50pt.save(TrailPT_OverSlope)
print ("Trail 50% violation points complete.")

    # Trail_Segment - 50% Rule Violations
Over50seg = arcpy.sa.ZonalStatistics(in_zone_data=Trail_Seg, zone_field="Value", in_value_raster=TrailPT_OverSlope, statistics_type="MAXIMUM", ignore_nodata="DATA")
Over50seg.save(TrailSeg_OverSlope)
print ("Trail 50% violation segments complete.")

print ("arcpy code run complete.")