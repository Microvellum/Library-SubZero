"""
Microvellum 
Appliances 
Stores all of the Logic, Product, and Insert Class definitions for appliances
"""

import os
from mv import fd_types, unit
from . import appliance_classes

REFRIGERATORS_PATH = os.path.join(os.path.dirname(__file__),"Refrigerators")
REFRIGERATED_BEVERAGE_PATH = os.path.join(os.path.dirname(__file__),"Refrigerated Beverage Center")
REFRIGERATOR_DRAWERS_PATH = os.path.join(os.path.dirname(__file__),"Refrigerator Drawers")
FREEZER_PATH = os.path.join(os.path.dirname(__file__),"Freezers")
WINE_PATH = os.path.join(os.path.dirname(__file__),"Wine Storage")
ICE_PATH = os.path.join(os.path.dirname(__file__),"Ice Maker")

#---------PRODUCT: REFRIGERATORS
        
class PRODUCT_SubZero_648PROG(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "648PROG"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero_648PROG.blend")
 
class PRODUCT_SubZero_BI_36RG_O(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "BI-36RG-O"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero_BI-36RG_O.blend")
 
class PRODUCT_SubZero_BI_36UID_O(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "BI-36UID-O"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero_BI-36UID_O.blend")
 
class PRODUCT_SubZero_BI_42UFD_O(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "SBI-42UFD-O"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero_BI-42UFD_O.blend")
 
class PRODUCT_SubZero_IC_36R(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "IC-36R"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero_IC-36R.blend")
        
class PRODUCT_SubZero_BI_36UFD(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "BI-36UFD"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero BI-36UFD.blend")
        
class PRODUCT_SubZero_ID_24R(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerator Drawers"
        self.assembly_name = "ID-24R"
        self.appliance_path = os.path.join(REFRIGERATOR_DRAWERS_PATH,"SubZero ID-24R.blend") 
        
class PRODUCT_SubZero_IT_30CI(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "IT-30CI"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero IT-30CI.blend")
        
class PRODUCT_SubZero_IT_36CI(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerators"
        self.assembly_name = "IT-36CI"
        self.appliance_path = os.path.join(REFRIGERATORS_PATH,"SubZero IT-36CI.blend")
        
class PRODUCT_SubZero_UC_24BG(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Refrigerated Beverage Center"
        self.assembly_name = "UC-24BG"
        self.appliance_path = os.path.join(REFRIGERATED_BEVERAGE_PATH,"SubZero UC-24BG.blend")                                       
        
#---------PRODUCT: FREEZERS

class PRODUCT_SubeZero_IC_18FI(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Freezers"
        self.assembly_name = "IC-18FI"
        self.appliance_path = os.path.join(FREEZER_PATH,"SubZero IC-18FI.blend") 
        
class PRODUCT_SubeZero_IC_24FI(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Freezers"
        self.assembly_name = "IC-24FI"
        self.appliance_path = os.path.join(FREEZER_PATH,"SubZero IC-24FI.blend")
        
class PRODUCT_SubeZero_IC_30R(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Freezers"
        self.assembly_name = "IC-30R"
        self.appliance_path = os.path.join(FREEZER_PATH,"SubZero IC-30R.blend") 
        
class PRODUCT_SubeZero_ID_30F(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Freezers"
        self.assembly_name = "ID-30F"
        self.appliance_path = os.path.join(FREEZER_PATH,"SubeZero_ID-30F.blend")                              
         
#---------PRODUCT: WINE STORAGE 
 
class PRODUCT_SUB_ZERO_UW_24FS(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Wine Storage"
        self.assembly_name = "UW-24FS"
        self.appliance_path = os.path.join(WINE_PATH,"SUB-ZERO_UW-24FS.blend") 
        
class PRODUCT_SUB_ZERO_IW_18(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Wine Storage"
        self.assembly_name = "IW-18"
        self.appliance_path = os.path.join(WINE_PATH,"SubZero IW-18.blend")
        
class PRODUCT_SUB_ZERO_IW_24(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Wine Storage"
        self.assembly_name = "IW-24"
        self.appliance_path = os.path.join(WINE_PATH,"SubZero IW-24.blend")                
 
#---------PRODUCT: ICE MAKER 
 
class PRODUCT_SubZero_UC_15I(appliance_classes.Static_Wall_Appliance):
    
    def __init__(self):
        self.category_name = "Ice Maker"
        self.assembly_name = "UC-15I"
        self.appliance_path = os.path.join(ICE_PATH,"SubZero UC-15I.blend") 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        