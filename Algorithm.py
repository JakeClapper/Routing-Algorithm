#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#raw data
#---------------------------------------------------------------
routeSegmentData = [
    "1172-1160 Duck Rd",
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
    "1288-1723 Duck Rd"
]
#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#Class definitions 
#--------------------------------------------------------------------------------
class RouteSegment:
   def __init__(self, address):
      self.street = address
      self.startRange = -1
      self.endRange = -1
      self.isforward = True

      first_char = address[0]
      if first_char.isdigit():
        # we have a range of numbers
        list = address.split(" ",1)
        self.street = list[1]
        range = list[0]
        
        if "-" in range:
           #range as a start and end
           rangeList = range.split("-", 1)
           self.startRange = rangeList[0]
           self.endRange  = rangeList[1]
           if self.startRange > self.endRange:
              self.isforward = False
        else:
           #range is just a singe value
           self.startRange = range
           self.endRange = range
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
     print(self.number + " " + self.street + " " + str(self.routeSegmentNumber) + " " +  str(self.isforward))  
#-----------------------------------------------------------------------------------------------------------------------------------------------------     
#Functions
#-----------------------------------------------------------------------------------------------------------------------------------------------------     
# this function will take given, customer address represented by number and street
# And loop through the list of route segments untill it finds a match, returning the index of the match.
# Or loops through the entire list without finding a match returning -1
# Presently this is a linear search, which is not optimal. 
# Todo: Replace with a hash Search
# --------------------------------------------------------------------------
def findRouteSegmentNumber(customerAddress):
   index = 0
   for routeSegment in routesegmentlist:
      #determine if this candidate route segment matches the given customer address
      isMatch = False #routesegment.match(customerAddress.number,customerAddress.street)
      #Check the street
      #Only check number if route segment has a range
      #Check if the number is in Range being careful of backwords ranges.
      #Case sensitive
       
      if customerAddress.street.lower() == routeSegment.street.lower():
         if int(routeSegment.startRange) != -1:
            if routeSegment.isforward:
                if int(customerAddress.number) >= int(routeSegment.startRange) and int(customerAddress.number) <= int(routeSegment.endRange):
                    isMatch=True
            else:
                if int(customerAddress.number) >= int(routeSegment.endRange) and int(customerAddress.number) <= int(routeSegment.startRange):
                    isMatch= True

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
routesegmentlist = []
for i in routeSegmentData:
   routesegment = RouteSegment(i)
   routesegmentlist.append(routesegment)

     

for i in routesegmentlist:
   i.print()




file = open("inTownDuck.txt", "r")
content = file.readlines()
#print(content)
file.close()

#walk the list of customer addresses. and convert each customer address into an object
# with a sequence number and an is forward boolean
customerList = []
for i in content:
    customerAddress = i.replace("\n","")
    #print(customerAddress)
    list = customerAddress.split(" ",1)
    number = list[0]
    street = list[1]
   # print(number + " " + street)
    customerAddress = CustomerAddress(number, street)
    customerList.append(customerAddress)

# iterate through the list of customer address objects and find the route segment number for each customer address
# then assign the route segment number to the customer address    
for customerAddress in customerList:
    #compute the route segment number for this address
    routeSegmentNumber = findRouteSegmentNumber(customerAddress)
    if routeSegmentNumber == -1:
       print("ERROR: Cannot Find this Customer Address " + customerAddress.number + " " + customerAddress.street)
    else:
       customerAddress.routeSegmentNumber = routeSegmentNumber
    #todo isFoward

for customerAddress in customerList:
   customerAddress.print() 
   

   

