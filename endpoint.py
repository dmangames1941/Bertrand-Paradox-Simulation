import math
import random
#Completed
class endpoint:
    #initiates a new endpoint test
    def __init__(self):
        global point1
        global point2
        self.point1 = []
        self.point2 = []
        self.isSuccess = endpoint.findSuccess(self)
        
    #uniformly generates 2 points on the circumference of the circle
    #finds the length between the two endpoints
    #checks if line is greater than sqrt(3) in length and returns true or false
    def findSuccess(self):
        ep1 = random.uniform(0, 2*math.pi)
        self.point1 = [math.cos(ep1), math.sin(ep1)]
        ep2 = random.uniform(0, 2*math.pi)
        self.point2 = [math.cos(ep2), math.sin(ep2)]
        length = 2*math.sin(abs(ep1 - ep2)/2)

        if length > math.sqrt(3):
            return True
        else:
            return False

    #Getters    
    def getX1(self):
        return self.point1[0]
    
    def getY1(self):
        return self.point1[1]
    
    def getX2(self):
        return self.point2[0]
    
    def getY2(self):
        return self.point2[1]
    
    def getSuccess(self):
        return self.isSuccess
    