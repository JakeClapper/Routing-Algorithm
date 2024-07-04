from enum import Enum
import argparse
#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#raw data
#---------------------------------------------------------------
verbose = False
unitTests = False
inTownDuckData = [
    "1172-1160 EVEN Duck Rd",
    "Beachcomber Ct",
    "Turnbuckle Ct",
    "Hatch Cover Ct",
    "Ships Wheel Ct",
    "Duck Hunt Club Ln",
    "Halyard Ct",
    "Lala Ct",
    "172-0 Four Seasons Ln",
    "0-1000 Scarborough Ln",
    "186-0 Ocean Way Ct",
    "Ocean Front Dr",
    "Lone Way",
    "158-146 Christopher Dr",
    "Teresa Ct",
    "144-138 Christopher Dr",
    "Victoria Ct",
    "136-128 Christopher Dr",
    "Betsy Ct",
    "126-120 Christopher Dr",
    "Dunes Crest",
    "118-112 Christopher Dr",
    "Pamela Ct",
    "110-0 Christopher Dr",
    "1183 Duck Rd",
    "Mantoac Ct",
    "157-153 Poteskeet Dr",
    "Cherokee Ct",
    "151-147 Poteskeet Dr",
    "Rakiock Ct",
    "Arrowhead Ct",
    "134-130 Poteskeet Dr",
    "Wiroans Ct",
    "128-122 Poteskeet Dr",
    "Algonkian Ct",
    "120-116 Poteskeet Dr",
    "Uppowoc Ct",
    "114-104 Poteskeet Dr",
    "Winauk Ct",
    "Duck Landing Ln",
    "Schooner Ridge",
    "Schooner Ridge Dr",
    "Chip Ct",
    "Duck Ridge Village Court",
    "Wampum Dr",
    "Marlin Dr",
    "Marlin Ct",
    "Cook Dr",
    "117-135 Speckle Trout Dr",
    "117-135 Speckled Trout Dr",
    "117-135 SpeckledTrout Dr",
    "1000-0 BayBerry Dr",
    "Gifford Cir",
    "RockFish Ln",
    "115-0 Speckle Trout Dr",
    "115-0 SpeckleTrout Dr",
    "115-0 SpeckledTrout Dr",
    "153-148 Speckle Trout Dr",
    "153-148 SpeckleTrout Dr",
    "153-148 Speckledtrout Dr",
    "1000-0 Dune Rd",
    "Sea Colony Dr",
    "Olde Duck Rd",
    "Barrier Island Station",
    "1245 Duck Rd", 
    "Spinnaker Ct",
    "137-122 Ships Watch Dr",
    "ForeSail Ct",
    "121-117 Ships Watch Dr",
    "Mainsail Ct",
    "115-108 Ships Watch Dr",
    "Topsail Ct",
    "107-0 Ships Watch Dr",
    "Sandy Ridge Rd",
    
]
northDuckData = [
   "100-113 Nor'Banks Dr",
   "100-113 Nor Banks Dr",
   "Sunfish Ct",
   "Snipe Ct",
   "122 Nor'Banks Dr",
   "122 Nor Banks Dr"
   "Puffer Ct",
   "WindSurfer Ct",
   "137-0 Spindrift Ln",
   "129-112 Spyglass Rd",
   "Sandcastle Ct",
   "111-0 Spyglass Rd",
   "S Snow Geese Dr",
   "South Snow Geese Dr",
   "N Snow Geese Dr",
   "North Snow Geese Dr",
   "1309 Duck Rd",
   "1311 Duck Rd",
   "0-105 Widgeon Dr",
   "Bald Pate Dr",
   "106-137 Widgeon Dr",
   "153-169 Bufflehead Rd",
   "153-169 Buffell Rd",
   "Whistling Swan Dr",
   "151-143 Bufflehead Rd",
   "151-143 Buffell Rd",
   "130 Bufflehead Dr",
   "130 Buffell Dr",
   "1317 Duck Rd",
   "Pintail Dr",
   "141-133 Bufflehead Rd",
   "141-133 Buffell Rd",
   "126 Bufflehead Rd",
   "126 Buffell Rd",
   "Wood Duck Rd",
   "1331 Duck Rd",
   "Canvasback Dr", 
   "Canvas back Dr",
   "131-114 Bufflehead Rd",
   "131-114 Buffell Rd",
   "Sprigtail Dr",
   "1345-1351 ODD Duck Rd",
   "Old Squaw Dr",
   "113-100 Bufflehead Rd",
   "113-100 Buffell Rd",
   "1353-1355 ODD Duck Rd",
   "Dianne St",
   "Rene Ct",
   "Frazier Ct",
   "Mallard Dr",
   "Mallard Dr.",
   "Wild Duck Dunes Rd",
   "Trinitie Dr",
   "Quarterdeck Dr",
   "Skipjack Ct",
   "1365-1371 ODD Duck Rd",
   "Sea Tern Dr E",
   "1377-1379 ODD Duck Rd",
   "Carroll Dr",
   "Carrol Dr",
   "Hillside Ct",
   "Dock's Ct",
   "1385 Duck Rd",
   "100-104 Sound Sea Ave",
   "Cedar Ct",
   "105-110 Sound Sea Ave",
   "Cypress Dr",
   "112-1000 Sound Sea Ave",
   "Elm Dr",
   "Maple Dr",
   "Willow Ct",
   "1391 Duck Rd",
   "Acorn Oak Ave",
   "Ocean Bay Blvd",
   "Flight Dr"
   "1401 Duck Rd",
   "Ocean Pines Dr",
   "Sandpiper Cove",
   "Oyster Catcher Ln",
   "1000-111 Skimmer Way",
   "Bunting Way",
   "Bunting Ln",
   "Shearwater Way",
   "110-0 Skimmer Way",
   "Pelican Way",
   "Blue Heron Ln",
   "Waxwing Ln",
   "Waxwing Ct",
   "Vireo Way",
   "Martin Ln",
   "Station Bay Dr",
   "1475 Duck Rd",
   "S Baum Trail",
   "N Baum Trail",
   "North Baum Trail",
   "1574-1532 EVEN Duck Rd",
   "Quail Way",
   "Gannet Cove",
   "Gannet Ln",
   "Ruddy Duck Ln",
   "Royal Tern Ln",
   "1474-1308 EVEN Duck Rd"
]

pineIslandData= [
   "Cadwall Rd",
   "Salt House Rd",
   "Cottage Cove Rd",
   "Hicks Bay Ln",
   "240-255 Longfellow Cove",
   "Ballast Point",
   "269-271 Longfellow Cove",
   "Whites Point",
   "White Whale Way",
   "285-300 Longfellow Cove",
   "Pine Island Limited Wy",
   "Audubon Dr",
   "Lindsey Ln",
   "Deep Neck Rd",
   "Great Gap Point",
   "408-430 Myrtle Pond Rd",
   "Sprig Point",
   "SprigPoint Rd",
   "432-434 Myrtle Pond Rd",
   "Kitsy's Point",
   "435-1000 Myrtle Pond Rd",
   "Black Pine Rd",
   "N Cove Rd",
   "Pipsis Point Rd",
   "island Lead Rd",
   "Clarion Lp"






   
]

southernShoresData = [
   "1158-1154 EVEN Duck Rd",
   "Amy Ln",
   "1150 Duck Rd",
   "Nash Rd",
   "Settlers Ln",
   "Osprey Ridge Rd",
   "Sea Hawk Dr W",
   "1128 Duck Rd",
   "100-1000 Tuckahoe Dr W",
   "Mallard Ct",
   "Fawn Ct",
   "Choctaw Ct",
   "Sheldrake Ct",
   "Jasmine Ct",
   "W Bias Dr",
   "Abron Ct",
   "Cofield Ct",
   "Charles Jenkins Ln W",
   "1106 Duck Rd",
   "Jaycrest Rd",
   "1100 Duck Rd",
   "393-371 Sea Oats Trail",
   "Sea Oats Ct",
   "370-357 Sea Oats Trail",
   "18-12 Soundview Trail",
   "19-58 N Dune Loop",
   "30-41 12th Ave",
   "30-47 11th Ave",
   "356-337 Sea Oats Trail",
   "Kingfisher Trail",
   "Kingfisher Loop",
   "Kingfisher Ct",
   "30-42 10th Ave",
   "30-40 9th Ave",
   "339-265 Hillcrest Dr",
   "264-328 Sea Oats Trail",
   "334-262 Wax Myrtle Trail",
   "329-263 ODD Duck Rd",
   "29-72 Hickory Trail",
   "Redbay Ln",
   "N Dogwood Trail",
   "S Dogwood Trail",
   "Landing Trail",
   "Foxwood Cir",
   "PinTail Ct",
   "PinTail Trail",
   "Ginguite Trail",
   "Widgeon Ct",
   "Wood Duck Ct",
   "Blue Pete Ct",
   "Mallard Cove",
   "Wild Swan Ln",
   "Osprey Ln",
   "Fairway Dr",
   "Tall Pine Ln",
   "Yaupon Ln",
   "Sassafras Ln",
   "77-72 E Dogwood Trail",
   "Woodland Dr",
   "N Woodland Dr",
   "Holly Trail",
   "E Holly Trail",
   "W Holly Trail",
   "Live Oak Ln",
   "Birch Ln",
   "Loblolly Dr",
   "71-60 E Dogwood Trail",
   "Beech Tree Trail",
   "57-48 E Dogwood Trail",
   "Bayberry Trail",
   "Scuppernong Ln",
   "Mistletoe Ln",
   "Honeysuckle Ln",
   "Fox Grape Ln",
   "N Fox Grape Ln",
   "Dewberry Ln",
   "46-44 E Dogwood Trail",
   "214-261 Hillcrest Dr",
   "262-213 Sea Oats Trail",
   "212-259 Wax Myrtle Trail",
   "251-159 ODD Duck Rd",
   "30-1000 Porpoise",
   "155-207 Wax Myrtle Trail",
   "Sea Oats Ln",
   "Mizzen Mast Ln",
   "Bright Lantern Ln",
   "41-31 Dolphin Run",
   "149-139 ODD Duck Rd",
   "137-99 ODD Duck Rd",
   "137-99 ODD Ocean Blvd",
   "Chicahauk Trail",
   "Grey Squirrel",
   "Poteskeet Loop",
   "Poteskeet Trail",
   "Trinitie Trail",
   "Juniper Trail",
   "Palmetto Ln",
   "Fern Ln",
   "Cypress Ln",
   "Yucca Ln",
   "Sweet Gum Ln",
   "Deer Path Ln",
   "Eagles Nest Ln",
   "Gravey Pond Ln",
   "Old Passage Ln",
   "Hollow Beach Ct",
   "Turtle Pond Ct",
   "Twisted Tree Ct",
   "Bent Oak Ct",
   "Clam Shell Trail",
   "ClamShell Trail",
   "Otter Slide Ln",
   "Oyster Bed Ln",
   "Goose Feather Ln",
   "Crooked Back Loop",
   "Pudding Pan Ln",
   "Tea Plant Ct",
   "Sprindrift Trail",
   "Wildpony Ln",
   "Happy Indian Ln",
   "Happy Indian Ct",
   "High Dune Loop",
   "Tall Clf Ct",
   "Last Hunt Ln",
   "Landfall Loop",
   "95-39 ODD Ocean Blvd",
   "Skyline Rd",
   "37-27 ODD Ocean Blvd",
   "Ocean View Loop",
   "25-11 ODD Ocean Blvd",
   "2-8 EVEN Ocean Blvd",
   "Pelican Way Watch",
   "12 Ocean Blvd",
   "12 Ocean Blvd.",
   "Sea Bass Cir",
   "18-142 EVEN Ocean Blvd",
   "150-152 EVEN Duck Rd",
   "26-20 Purpoise Run",
   "157-147 ODD Ocean Blvd",
   "148A Ocean Blvd",
   "146-148 Ocean Blvd",
   "Bluefin Ln",
   "148-158 EVEN Ocean Blvd",
   "158-162 EVEN Duck Rd",
   "Trout Run",
   "169-159 ODD Ocean Blvd",
   "Yellowfin Ln",
   "160-180 EVEN Ocean Blvd",
   "181-171 ODD Ocean Blvd",
   "170-174 EVEN Duck Rd",
   "27-20 Dolphin Rd",
   "182-189 Ocean Blvd",
   "Mullet Cir",
   "190-208 EVEN Ocean Blvd",
   "207-195 ODD Ocean Blvd",
   "Pompano Ct",
   "193-191 ODD Ocean Blvd",
   "180-198 EVEN Duck Rd",
   "29-0 E Dogwood Trail",
   "210-234 EVEN Ocean Blvd",
   "231-209 ODD Ocean Blvd",
   "Sandfiddler Ct",
   "Perriwinkle Pl",
   "Mockingbird Ln"
   "235-239 Ocean Blvd",
   "Sandpiper Ln",
   "241-247 Ocean Blvd",
   "Purple Martin Ln",
   "248-253 Ocean Blvd",
   "0-28 Hickory Trail",
   "Circle Dr",
   "232 Duck Rd",
   "1-3 ODD Duck Wds Dr",
   "27-0 1st Ave",
   "270-272 EVEN Duck Rd",
   "24-0 2nd Ave",
   "282 Duck Rd",
   "24-0 3rd Ave",
   "24-0 4th Ave",
   "298 Duck Rd",
   "20-0 5th Ave",
   "304-306 EVEN Duck Rd",
   "22-0 6th Ave",
   "310-312 EVEN Duck Rd",
   "20-0 7th Ave",
   "316-318 EVEN Duck Rd",
   "0-26 8th Ave",
   "29-0 9th Ave",
   "334 Duck Rd",
   "27-0 10th Ave",
   "340 Duck Rd",
   "28-0 11th Ave",
   "346-348 EVEN Duck Rd",
   "26-0 12th Ave",
   "352 Duck Rd",
   "28-0 13th Ave",
   "358-360 EVEN Duck Rd",
   "Charles Jenkins Ln E",
   "Ocean Crest Way",
   "Vivian Ct",
   "Yolanda Terrace",
   "Bias Ln E",
   "Tides Dr",
   "Tuckahoe Drive E",
   "Sea Eider Ct",
   "Thrush Ct",
   "Sunflower Ct",
   "Azalea Ct",
   "Magnolia Ct",
   "Sea Hawk Dr E",
   "1135 Duck Rd",
   "Seabreeze Dr",
   "Georgetown Sands Rd",
   "Plover Dr",
   "1147-1149 ODD Duck Rd"

]

#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#Class definitions 
#--------------------------------------------------------------------------------

class NumberModifier(Enum):
   ALL = 0
   ODD = 1
   EVEN = 2

class RouteSegment:
   def __init__(self, address):
      self.street = address
      self.startRange = -1
      self.endRange = -1
      self.isforward = True
      self.numberModifier = NumberModifier.ALL
      self.apt = "" # this will be a A B or C etc...


      first_char = address[0]
      if first_char.isdigit():
        # we have a range of numbers
        list = address.split(" ",1)
        self.street = list[1]

        if "ODD" in self.street:
          self.numberModifier = NumberModifier.ODD
          streetList = self.street.split(" ", 1)
          self.street = streetList[1]
        elif "EVEN" in self.street:
          self.numberModifier = NumberModifier.EVEN
          streetList = self.street.split(" ", 1)
          self.street = streetList[1]
  

        range = list[0]

        last_char = range[len(range)-1]
        if last_char.isalpha():
           self.apt = last_char
           range = range[0:len(range)-1]
        if "-" in range:
           #range as a start and end
           rangeList = range.split("-", 1)
           self.startRange = int (rangeList[0])
           self.endRange  = int (rangeList[1])
           if self.startRange > self.endRange:
              self.isforward = False
        else:
           #range is just a singe value
           self.startRange = int(range)
           self.endRange = int(range)

       

   def print(self):
      if verbose:
         print(self.street + " " +  str(self.startRange) + " " + str(self.endRange) + " " +  str(self.isforward))


# This method will check the given number and street to see if this routesegments matches the given address]
# This method returns true if its a match and false if not
 
   def match(self, number, street):
        #Check the street
        #Check if the number is in Range being careful of backwords ranges.
        #Case sensitive 
      if street.lower() == self.street.lower():
         if self.isforward:
            if number >= self.startRange and number <= self.endRange:
               return True
         else:
            if number >= self.endRange and number <= self.startRange:
               return True
            
            
           
      return False
         
        

       







   
       

class CustomerAddress:
  def __init__(self, number, apt, street):

    self.number = number
    self.street = street
    self.routeSegmentNumber = -1
    self.isforward = True 
    self.apt = apt
    
    




    
  
  def print(self):
     print(str(self.number) + self.apt + " " + self.street+ " " + str(self.routeSegmentNumber) + " " +  str(self.isforward))  
#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#Functions
#-----------------------------------------------------------------------------------------------------------------------------------------------------     
def streetmatch(customerAddressStreet, routeSegmentStreet):
   
    if customerAddressStreet.lower() == routeSegmentStreet.lower():
       return True
    #Translate the street type in the route segment to full expanded name and then recompare to the customer street.
    temp = customerAddressStreet.rsplit(" ",1)
    type = temp[1]
    type = type.lower()
    newType = ""
    
    if type == "road":
       newType = "Rd"
    elif type == "lane":
       newType = "Ln"
    elif type == "drive":
       newType = "Dr"
    elif type == "Drive":
       newType = "Dr"      
    elif type == "avenue":
       newType = "Ave"   
    elif type == "wy":
       newType = "way"
    elif type == "way":
       newType = "wy"   
    elif type == "street":
       newType = "St"
    elif type == "court":
       newType = "Ct"
    elif type == "str":
       newType = "st"   
    elif type == "boulevard": 
       newType = "Blvd"
    elif type == "pond":
       newType = "Pd"
    elif type == "circle":
       newType = "Cir"
    elif type == "north":
       newType = "N"
    
    newCustomerAdressStreet = temp[0] + " " + newType
    if newCustomerAdressStreet.lower() == routeSegmentStreet.lower():
       return True
    
   #Compare the customer street, it has to no road, lane ,drive...
    temp = routeSegmentStreet.rsplit(" ",1 )
    newRouteSegmentStreet = temp[0]
    if customerAddressStreet.lower() == newRouteSegmentStreet.lower():
      return True
    


   #todo there are certain strees where we cannot match becuase they contain the same name
   # 114 Sea tern
    temp = routeSegmentStreet.rsplit(" ",2 )
    newRouteSegmentStreet = temp[0]
    if customerAddressStreet.lower() == newRouteSegmentStreet.lower():
      return True
    
    
    return False
    
    





# this function will take given, customer address represented by number and street
# And loop through the list of route segments untill it finds a match, returning the index of the match.
# Or loops through the entire list without finding a match returning -1
# Presently this is a linear search, which is not optimal. 
# Todo: Replace with a hash Search
# --------------------------------------------------------------------------
def findRouteSegmentNumber(customerAddress, routeSegmentList):

  
   index = 0
   
   for routeSegment in routeSegmentList:
      #determine if this candidate route segment matches the given customer address
      isMatch = False #routesegment.match(customerAddress.number,customerAddress.street)
      #Check the street
      #Only check number if route segment has a range
      #Check if the number is in Range being careful of backwords ranges.
      #Case sensitive
       
      if streetmatch(customerAddress.street, routeSegment.street):
         if int(routeSegment.startRange) != -1:
            if routeSegment.isforward:
                if int(customerAddress.number) >= int(routeSegment.startRange) and int(customerAddress.number) <= int(routeSegment.endRange):
                    if routeSegment.numberModifier == NumberModifier.ODD:
                       if customerAddress.number % 2 == 1:
                          isMatch=True
                    
                    elif routeSegment.numberModifier == NumberModifier.EVEN:
                       if customerAddress.number % 2 == 0:
                          isMatch=True
                    else:
                       isMatch = True   
            else:
                if int(customerAddress.number) >= int(routeSegment.endRange) and int(customerAddress.number) <= int(routeSegment.startRange):
                    if routeSegment.numberModifier == NumberModifier.ODD:
                       if customerAddress.number % 2 == 1:
                          isMatch=True
                    
                    elif routeSegment.numberModifier == NumberModifier.EVEN:
                       if customerAddress.number % 2 == 0:
                          isMatch=True
                    else:
                       isMatch = True

         else:
            isMatch = True

      if isMatch == True:
         return index
      index = index + 1

   return -1

def routeSegmentParsingODDRangeTest():
   #This unit test Checks the parsing of the route segment constructor
   rs = RouteSegment("169-159 ODD Ocean Blvd")
   success  = 0
   if rs.endRange != 159:
      success = 1
      print("Error Test Failed: End Range")
   if rs.numberModifier != NumberModifier.ODD:
      success = 1
      print("Error Test Failed: Not Equal to odd")
      
   if rs.startRange != 169:
      success = 1
      print("Error Test Failed: Start Range")
      
   if rs.apt != "":
      success = 1
      print("Error Test Failed: Apt Number")
      
   if rs.street != "Ocean Blvd":
      success = 1
      print("Error Test Failed Street " + rs.street)   
      
   if rs.isforward == True:
      success = 1
      print("Error Test Failed")    
             
   return success

def routeSegmentParsingnoRangeTest():
   #This unit test Checks the parsing of the route segment constructor
   rs = RouteSegment("Sandfiddler Ct")
   success  = 0
   if rs.endRange != -1:
      success = 1
      print("Error Test Failed: End Range")
   if rs.numberModifier != NumberModifier.ALL:
      success = 1
      print("Error Test Failed: Not Equal to odd")
      
   if rs.startRange != -1:
      success = 1
      print("Error Test Failed: Start Range")
      
   if rs.apt != "":
      success = 1
      print("Error Test Failed: Apt Number")
      
   if rs.street != "Sandfiddler Ct":
      success = 1
      print("Error Test Failed Street " + rs.street)   
      
   if rs.isforward != True:
      success = 1
      print("Error Test Failed is forward")    
             
   return success

def routeSegmentParsingsingleRangeTest():
   #This unit test Checks the parsing of the route segment constructor
   rs = RouteSegment("232 Duck Rd")
   success  = 0
   if rs.endRange != 232:
      success = 1
      print("Error Test Failed: End Range")
   if rs.numberModifier != NumberModifier.ALL:
      success = 1
      print("Error Test Failed: Not Equal to odd")
      
      
   if rs.startRange != 232:
      success = 1
      print("Error Test Failed: Start Range")
      
   if rs.apt != "":
      success = 1
      print("Error Test Failed: Apt Number")
      
   if rs.street != "Duck Rd":
      success = 1
      print("Error Test Failed Street " + rs.street)   
      
   if rs.isforward != True:
      success = 1
      print("Error Test Failed is forward")    
             
   return success

def routeSegmentParsingaptRangeTest():
   #This unit test Checks the parsing of the route segment constructor
   rs = RouteSegment("148A Ocean Blvd")
   success  = 0
   if rs.endRange != 148:
      success = 1
      print("Error Test Failed: End Range")
   if rs.numberModifier != NumberModifier.ALL:
      success = 1
      print("Error Test Failed: Not Equal to odd")
      
   if rs.startRange != 148:
      success = 1
      print("Error Test Failed: Start Range")
      
   if rs.apt != "A":
      success = 1
      print("Error Test Failed: Apt Number")
      
   if rs.street != "Ocean Blvd":
      success = 1
      print("Error Test Failed Street " + rs.street)   
      
   if rs.isforward != True:
      success = 1
      print("Error Test Failed is forward")    
             
   return success

def routeSegmentParsingevenRangeTest():
   #This unit test Checks the parsing of the route segment constructor
   rs = RouteSegment("180-198 EVEN Duck Rd")
   success  = 0
   if rs.endRange != 198:
      success = 1
      print("Error Test Failed: End Range")
   if rs.numberModifier != NumberModifier.EVEN:
      success = 1
      print("Error Test Failed: Not Equal to odd")
      
   if rs.startRange != 180:
      success = 1
      print("Error Test Failed: Start Range")
      
   if rs.apt != "":
      success = 1
      print("Error Test Failed: Apt Number")
      
   if rs.street != "Duck Rd":
      success = 1
      print("Error Test Failed Street " + rs.street)   
      
   if rs.isforward != True:
      success = 1
      print("Error Test Failed is forward")    
             
   return success




def runUnitTests():
# This function will call all the unit tests.
# There will be 1 function for each unit test
# This function will keep track of the tests that pass and those that fail
# This function will emit a summary after all the unit tests have run
   totalTests = 0
   totalFailures = 0
   
   
   totalTests += 1
   totalFailures += routeSegmentParsingODDRangeTest()
   
   totalTests += 1
   totalFailures += routeSegmentParsingnoRangeTest()
   
   totalTests += 1
   totalFailures += routeSegmentParsingsingleRangeTest()
   
   totalTests += 1
   totalFailures += routeSegmentParsingaptRangeTest()
   
   totalTests += 1
   totalFailures += routeSegmentParsingevenRangeTest()
   
   print('total Tests: ' + str(totalTests) ,'total Failures:' + str(totalFailures))
   return 


def findAndReverseDuplicateBackwardsRouteSegments(list):
   index = 0
   length = len(list)
   while index < length:
      customerAddress = list[index]
      if customerAddress.isforward == False:
         
         # If there are multiple customer addresses that follow with the same RouteSgement number
         # All those customer addresses objects need to be reverse in the final customer list

         routeSegmentNumber = customerAddress.routeSegmentNumber
         lookAheadIndex = index
         while lookAheadIndex + 1 < length and list[lookAheadIndex+1].routeSegmentNumber == routeSegmentNumber:
            lookAheadIndex = lookAheadIndex+1
            
         if(lookAheadIndex != index):
            if verbose:
               print('Repeated Backwards route segments Found '+ str(index) + " " + str(lookAheadIndex))
             
             # Reverse the Repeated Backwards route segments
             # Create a Temp array of the ranges to reverse
             # Reverse the Temp Array, then put back into the original array 

            tempArray = list[index: lookAheadIndex+1]
            new_lst = tempArray[::-1]
            list[index: lookAheadIndex+1] = new_lst
         
            index = lookAheadIndex+1
            
         else:
            #There is only one record for this backwards route segment
            # So because there is only one record there is nothing to reverse
            # #check the next one
            index = index +1   
            
         
      else:
            #This route segment is forward so already in the correct order
            #check the next one
            index = index +1   
   
   
   
   return

#==========================================
#This function will compute the routes. 
#==========================================

def computeRoutes():
   #iterate through the raw data source and create objects for each
   routesegmentintownducklist = []
   for i in inTownDuckData:
      routesegment = RouteSegment(i)
      routesegmentintownducklist.append(routesegment)

   for i in routesegmentintownducklist:
      i.print()

   routesegmentnorthducklist = []
   for i in northDuckData:
      routesegment = RouteSegment(i)
      routesegmentnorthducklist.append(routesegment)

   for i in routesegmentnorthducklist:
      i.print()   


   routesegmentpineislandlist = []
   for i in pineIslandData:
      routesegment = RouteSegment(i)
      routesegmentpineislandlist.append(routesegment)

   for i in routesegmentpineislandlist:
      i.print()   

   routesegmentsouthernshoreslist = []
   for i in southernShoresData:
      routesegment = RouteSegment(i)
      routesegmentsouthernshoreslist.append(routesegment)

   for i in routesegmentsouthernshoreslist:
      i.print()


   file = open("CustomerDropoffList.txt", "r")
   content = file.readlines()
   #print(content)
   file.close()

   #walk the list of customer addresses. and convert each customer address into an object
   # with a sequence number and an is forward boolean
   unroutedCustomerList = []
   for i in content:
      customerAddress = i.replace("\n","")
      customerAddress = customerAddress.strip()
      #print(customerAddress)
      list = customerAddress.split(" ",1)
      temp = list[0]
      last_char = temp[len(temp)-1]
      if last_char.isalpha():
         apt = last_char
         number = int(temp[0:len(temp)-1])
      else:
         apt = ""
         number = int(temp)
      street = list[1]
      

      # print(number + " " + street)
      customerAddress = CustomerAddress(number, apt, street)
      unroutedCustomerList.append(customerAddress)

   # iterate through the list of customer address objects and find the route and the route segment number for each customer address
   # then assign the route segment number to the customer address    
   customerListForInTownDuck = []
   customerListForNorthDuck = []
   customerListForPineIsland = []
   customerListForSouthernShores = [] 
   for customerAddress in unroutedCustomerList:
      #compute the route segment number for this address
      routeSegmentNumber = findRouteSegmentNumber(customerAddress, routesegmentintownducklist)
      if routeSegmentNumber == -1:
         routeSegmentNumber = findRouteSegmentNumber(customerAddress, routesegmentnorthducklist)
         if routeSegmentNumber == -1:
            routeSegmentNumber = findRouteSegmentNumber(customerAddress, routesegmentpineislandlist)
            if routeSegmentNumber == -1:
               routeSegmentNumber = findRouteSegmentNumber(customerAddress, routesegmentsouthernshoreslist)
               if routeSegmentNumber != -1:
                  
                  customerListForSouthernShores.append(customerAddress)
                  customerAddress.isforward = routesegmentsouthernshoreslist[routeSegmentNumber].isforward


               
            else:
               customerListForPineIsland.append(customerAddress)
               customerAddress.isforward = routesegmentpineislandlist[routeSegmentNumber].isforward
      
         
               
         else:
            customerListForNorthDuck.append(customerAddress)
            customerAddress.isforward = routesegmentnorthducklist[routeSegmentNumber].isforward

      
         
      else:
         customerListForInTownDuck.append(customerAddress)
         customerAddress.isforward = routesegmentintownducklist[routeSegmentNumber].isforward

            
      
         



      if routeSegmentNumber == -1:
         print("ERROR: Cannot Find this Customer Address " + str(customerAddress.number)+ " " + customerAddress.street)
      else:
         customerAddress.routeSegmentNumber = routeSegmentNumber
         

   #We have moved each customer address to its correct routing array
   # And given each customer address a route segment number

   #Sort each list of customer addresses based on the routing number attribute
   customerListForInTownDuck.sort(key=lambda x: (x.routeSegmentNumber, x.number), reverse=False)
   customerListForNorthDuck.sort(key=lambda x: (x.routeSegmentNumber, x.number), reverse=False)
   customerListForPineIsland.sort(key=lambda x: (x.routeSegmentNumber, x.number), reverse=False)
   customerListForSouthernShores.sort(key=lambda x: (x.routeSegmentNumber, x.number), reverse=False)       

   #check for duplicate routingSegmentnumbers, and whose isFoward attribute is false
   # these need to be put in reverse order

   findAndReverseDuplicateBackwardsRouteSegments(customerListForInTownDuck)
   findAndReverseDuplicateBackwardsRouteSegments(customerListForNorthDuck)
   findAndReverseDuplicateBackwardsRouteSegments(customerListForPineIsland)
   findAndReverseDuplicateBackwardsRouteSegments(customerListForSouthernShores)

   
      
   print('---------------------------------------')
   print("THIS IS THE FINAL SOUTHERN SHORES ROUTE")
   print('---------------------------------------')
   print('')

   for customerAddress in customerListForSouthernShores:
      customerAddress.print() 
      
   print('---------------------------------------')
   print("THIS IS THE FINAL IN TOWN DUCK ROUTE")
   print('---------------------------------------')
   print('')

   for customerAddress in customerListForInTownDuck:
      customerAddress.print()
      
   print('---------------------------------------')
   print("THIS IS THE FINAL NORTH DUCK ROUTE")
   print('---------------------------------------')
   print('')

   for customerAddress in customerListForNorthDuck:
      customerAddress.print()

   print('---------------------------------------')
   print("THIS IS THE FINAL PINE ISLAND ROUTE")
   print('---------------------------------------')
   print('')

   for customerAddress in customerListForPineIsland:
      customerAddress.print()
      return

#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#Main program starts here
#-----------------------------------------------------------------------------------------------------------------------------------------------------   
#-----------------------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------------------------------------------------------------- 
parser = argparse.ArgumentParser(description='Filter addresses')
parser.add_argument('-v', '--verbose',action="store_true", help='filter addresses')
parser.add_argument('-u','--unitTests',action="store_true")
args = parser.parse_args() 
verbose  = args.verbose
unitTests  = args.unitTests 
if unitTests:
   runUnitTests()
else:
   computeRoutes()

#this is the end of the program

