from enum import Enum

#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#raw data
#---------------------------------------------------------------
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
    "Chip Ct",
    "Duck Ridge Village Court",
    "Wampum Dr",
    "Marlin Dr",
    "Marlin Ct",
    "Cook Dr",
    "117-135 Speckle Trout Dr",
    "1000-0 BayBerry Dr",
    "Gifford Cir",
    "RockFish Ln",
    "115-0 Speckle Trout Dr",
    "153-148 Speckle Trout Dr",
    "1000-0 Dune Rd",
    "Sea Colony Dr",
    "Olde Duck Rd",
    "Barrier Island Station",
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
   "Sunfish Ct",
   "Snipe Ct",
   "122 Nor'Banks Dr",
   "Puffer Ct",
   "WindSurfer Ct",
   "137-0 Spindrift Ln",
   "129-112 Spyglass Rd",
   "Sandcastle Ct",
   "111-0 Spyglass Rd",
   "S Snow Geese Dr",
   "N Snow Geese Dr",
   "1309 Duck Rd",
   "1311 Duck Rd",
   "0-105 Wideon Dr",
   "Bald Pate Dr",
   "106-137 Wideon Dr",
   "153-169 Bufflehead Rd",
   "Whistling Swan Dr",
   "151-143 Bufflehead Rd",
   "130 Bufflehead Dr",
   "1317 Duck Rd",
   "Pintail Dr",
   "141-133 Bufflehead Rd",
   "126 Bufflehead Rd",
   "Wood Duck Rd",
   "1331 Duck Rd",
   "Canvasback Dr",
   "131-114 Bufflehead Rd",
   "Spigtail Dr",
   "1345-1351 ODD Duck Rd",
   "Old Squaw Dr",
   "113-100 Bufflehead Rd",
   "1353-1355 ODD Duck Rd",
   "Dianne St",
   "Rene Ct",
   "Frazier Ct",
   "Mallard Dr",
   "Wild Duck Dunes Rd",
   "Trinitie Dr",
   "Quarterdeck Dr",
   "Skipjack Ct",
   "1365-1371 ODD Duck Rd",
   "Sea Tern Dr E",
   "1377-1379 ODD Duck Rd",
   "Carroll Dr",
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
   "432-434 Myrtle Pond Rd",
   "Kitsy's Point",
   "435-1000 Myrtle Pond Rd",
   "Black Pine Rd",
   "N Cove Rd",
   "Pipsis Point Rd",
   "island Lead Rd",
   "Clarion Lp"






   
]

southernShoresData = []

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
        address = list[1]

   def print(self):
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
  def __init__(self, number, street):

    self.number = number
    self.street = street


    self.routeSegmentNumber = -1
    self.isforward = True 


  def print(self):
     print(str(self.number) + " " + self.street + " " + str(self.routeSegmentNumber) + " " +  str(self.isforward))  
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
    
    newCustomerAdressStreet = temp[0] + " " + newType
    if newCustomerAdressStreet.lower() == routeSegmentStreet.lower():
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

    


#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#Main program starts here
#-----------------------------------------------------------------------------------------------------------------------------------------------------     

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
    number = int(list[0])
    street = list[1]
    

   # print(number + " " + street)
    customerAddress = CustomerAddress(number, street)
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

index = 0
length = len(customerListForInTownDuck)
while index < length:
   customerAddress = customerListForInTownDuck[index]
   if customerAddress.isforward == False:
      
      # If there are multiple customer addresses that follow with the same RouteSgement number
      # All those customer addresses objects need to be reverse in the final customer list

      routeSegmentNumber = customerAddress.routeSegmentNumber
      lookAheadIndex = index
      while lookAheadIndex + 1 < length and customerListForInTownDuck[lookAheadIndex+1].routeSegmentNumber == routeSegmentNumber:
         lookAheadIndex = lookAheadIndex+1
         
      if(lookAheadIndex != index):
        print('Problem Found '+ str(index) + " " + str(lookAheadIndex))
        # Create a Temp array of the ranges to reverse
        # Reverse the Temp Array, then put back into the original array 

        tempArray = customerListForInTownDuck[index: lookAheadIndex+1]
        new_lst = tempArray[::-1]
        customerListForInTownDuck[index: lookAheadIndex+1] = new_lst
       
        index = lookAheadIndex+1
         
      else:
         #No Problem, check the next one
         index = index +1   
         
      
   else:
         #No Problem, check the next one
         index = index +1   
#-------------------------------------------------------------------------------------------------------------------
index = 0
length = len(customerListForNorthDuck)
while index < length:
   customerAddress = customerListForNorthDuck[index]
   if customerAddress.isforward == False:
      
      # If there are multiple customer addresses that follow with the same RouteSgement number
      # All those customer addresses objects need to be reverse in the final customer list

      routeSegmentNumber = customerAddress.routeSegmentNumber
      lookAheadIndex = index
      while lookAheadIndex + 1 < length and customerListForNorthDuck[lookAheadIndex+1].routeSegmentNumber == routeSegmentNumber:
         lookAheadIndex = lookAheadIndex+1
         
      if(lookAheadIndex != index):
        print('Problem Found '+ str(index) + " " + str(lookAheadIndex))
        # Create a Temp array of the ranges to reverse
        # Reverse the Temp Array, then put back into the original array 

        tempArray = customerListForNorthDuck[index: lookAheadIndex+1]
        new_lst = tempArray[::-1]
        customerListForNorthDuck[index: lookAheadIndex+1] = new_lst
       
        index = lookAheadIndex+1
         
      else:
         #No Problem, check the next one
         index = index +1   
         
      
   else:
         #No Problem, check the next one
         index = index +1   
#-------------------------------------------------------------------------------------------------------------------            
index = 0
length = len(customerListForPineIsland)
while index < length:
   customerAddress = customerListForPineIsland[index]
   if customerAddress.isforward == False:
      
      # If there are multiple customer addresses that follow with the same RouteSgement number
      # All those customer addresses objects need to be reverse in the final customer list

      routeSegmentNumber = customerAddress.routeSegmentNumber
      lookAheadIndex = index
      while lookAheadIndex + 1 < length and customerListForPineIsland[lookAheadIndex+1].routeSegmentNumber == routeSegmentNumber:
         lookAheadIndex = lookAheadIndex+1
         
      if(lookAheadIndex != index):
        print('Problem Found '+ str(index) + " " + str(lookAheadIndex))
        # Create a Temp array of the ranges to reverse
        # Reverse the Temp Array, then put back into the original array 

        tempArray = customerListForPineIsland[index: lookAheadIndex+1]
        new_lst = tempArray[::-1]
        customerListForPineIsland[index: lookAheadIndex+1] = new_lst
       
        index = lookAheadIndex+1
         
      else:
         #No Problem, check the next one
         index = index +1   
         
      
   else:
         #No Problem, check the next one
         index = index +1   
#-------------------------------------------------------------------------------------------------------------------   
index = 0
length = len(customerListForSouthernShores)
while index < length:
   customerAddress = customerListForSouthernShores[index]
   if customerAddress.isforward == False:
      
      # If there are multiple customer addresses that follow with the same RouteSgement number
      # All those customer addresses objects need to be reverse in the final customer list

      routeSegmentNumber = customerAddress.routeSegmentNumber
      lookAheadIndex = index
      while lookAheadIndex + 1 < length and customerListForSouthernShores[lookAheadIndex+1].routeSegmentNumber == routeSegmentNumber:
         lookAheadIndex = lookAheadIndex+1
         
      if(lookAheadIndex != index):
        print('Problem Found '+ str(index) + " " + str(lookAheadIndex))
        # Create a Temp array of the ranges to reverse
        # Reverse the Temp Array, then put back into the original array 

        tempArray = customerListForSouthernShores[index: lookAheadIndex+1]
        new_lst = tempArray[::-1]
        customerListForSouthernShores[index: lookAheadIndex+1] = new_lst
       
        index = lookAheadIndex+1
         
      else:
         #No Problem, check the next one
         index = index +1   
         
      
   else:
         #No Problem, check the next one
         index = index +1    
               

   
   
   
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