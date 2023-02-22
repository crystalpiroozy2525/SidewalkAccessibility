# -*- coding: utf-8 -*-
"""
Created on Jul 2022
Calculate Function Python Script for Tyree's Sidewalk Project'

@author: Crystal Posey
"""
##Input for the object field type. It takes the Reclass Function and its parameters.
Reclass(!Cross_Slope_b!, !Cross_Slope_m!, !Cross_Slope_e!, !Roadway_Longitudinal_Slope_b!, !RoadwayLongslope__m!, !RoadwayLongslope__e!, !Sidewalk_Longitudinal_Slope_b!, !Sidewalkslope_m!, !Sidewalkslope_e!, !Widthofsidewakl_b!, !Narrowest!, !Widthofsidewalk_e!, !Ramp_Compliant_Accessible___Y_or_N_!, !Vertical_Clearance_Compliant_!, !Driveways_Compliant___Y_or_N_!, !Stairs_in_segment_!, !Any_Pedestrian_Barriers___stairs__trees__narrow_sidewalk__no_ram!)

##Code block input for the Reclass Function
def Reclass(cross_slope_b, cross_slope_m, cross_slope_e, roadway_long_b, roadway_long_m, roadway_long_e, sidewalk_long_b, sidewalk_long_m, sidewalk_long_e, sidewalk_width_b, sidewalk_narrow_m, sidewalk_width_e, ramp_compliant_b, vertical_compliant_m, driveway_comp, stairs_segment, ped_barrier):
    if cross_slope_b>3.5 or cross_slope_m>3.5 or cross_slope_e>3.5:
        return 'red'
    elif stairs_segment == 'Yes':
        return 'red'
    elif sidewalk_width_b<=3:
        return 'red'
    elif sidewalk_narrow_m<=3:
        return 'red'
    elif sidewalk_width_e<=3:
        return 'red'
    elif cross_slope_b<3.5 and cross_slope_b>2.5:
        return 'yellow'
    elif cross_slope_m<3.5 and cross_slope_m>2.5:
        return 'yellow'
    elif cross_slope_e<3.5 and cross_slope_e>2.5:
        return 'yellow'
    elif sidewalk_long_b>5 or sidewalk_long_m>5 or sidewalk_long_e>5:
        if roadway_long_b == (sidewalk_long_b+1.5) or roadway_long_b == (sidewalk_long_b-1.5):
            return 'yellow'
        elif roadway_long_m == (sidewalk_long_m+1.5) or roadway_long_m == (sidewalk_long_m-1.5):
            return 'yellow'
        elif roadway_long_e == (sidewalk_long_e+1.5) or roadway_long_e == (sidewalk_long_e-1.5):
            return 'yellow'
        else:
            return 'red'
    elif sidewalk_width_b>3 and sidewalk_width_b<=4:
        return 'yellow'
    elif sidewalk_narrow_m>3 and sidewalk_narrow_m<=4:
        return 'yellow'
    elif sidewalk_width_e>3 and sidewalk_width_e<=4:
        return 'yellow'
    elif ramp_compliant_b =='No':
        return 'yellow'
    elif vertical_compliant_m == 'No':
        return 'yellow'
    elif driveway_comp =='No':
        return 'yellow'
    elif ped_barrier =='Yes':
        return 'yellow'
    else:
        return 'green'
