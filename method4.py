import math
import random

class methodFour:
    def __init__(self, ):
        global point1
        global point2
        self.point1 = []
        self.point2 = []
        self.isSuccess = methodFour.findSuccess(self)

    def findSuccess(self):
        while(True):
            x1 = random.uniform(-1,1)
            y1 = random.uniform(-1,1)
            x2 = random.uniform(-1,1)
            y2 = random.uniform(-1,1)
            if(math.pow(x1,2) + math.pow(y1,2) <= 1 and math.pow(x2,2) + math.pow(y2,2) <= 1):
                if(x1 == x2 and y1 == y2):
                    continue
                else:
                    break
        self.point1 = [x1,y1]
        self.point2 = [x2,y2]
        methodFour.findEndpoints(self)
        length = math.sqrt(math.pow(self.point2[0]-self.point1[0], 2) + math.pow(self.point2[1]-self.point1[1], 2))

        if length > math.sqrt(3):
            return True
        else:
            return False


    def findEndpoints(self):
        m = (self.point2[1] - self.point1[1])/(self.point2[0] - self.point1[0])
        b = self.point1[1] - m*self.point1[0]

        x1 = (-b * m + math.sqrt(math.pow(b,2)* math.pow(m,2) - (math.pow(m,2) + 1)*(math.pow(b,2)-1))) / (math.pow(m,2)  + 1)
        x2 = (-b * m - math.sqrt(math.pow(b,2)  * math.pow(m,2)  - (math.pow(m,2)  + 1)*(math.pow(b,2) -1))) / (math.pow(m,2)  + 1)
        y1 = m*x1 + b
        y2 = m*x2 + b
        self.point1 = [x1,y1]
        self.point2 = [x2,y2]   
        
    
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