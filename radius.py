import math
import random

class radius:
    def __init__(self):
        global mp
        global endpoint1
        global endpoint2
        self.midpoint = []
        self.ep1 = []
        self.ep2 = []
        self.isSuccess = radius.findSuccess(self)

    def findSuccess(self):
        r = random.uniform(0,1)
        theta = random.uniform(0,2*math.pi)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        self.midpoint = [x,y]

        #find endpoints for line graphing
        radius.findEndpoints(self, x, y)

        if r <= 0.5:
            return True
        else:
            return False

    def findEndpoints(self, mpX, mpY):
        if mpY == 0:
            x1 = mpX
            x2 = mpX
            y2 = math.sqrt((1-math.pow(mpX,2)))
            y1 = -y2
        elif mpX == 0:
            x2 = math.sqrt(1-math.pow(mpY,2))
            x1 = -x2
            y1 = mpY
            y2 = mpY
        else:
            m = -mpX/mpY
            a = math.pow(m,2)+1
            b = 2*m*mpY - 2*math.pow(m,2)*mpX
            c = math.pow(mpY,2) + math.pow(m,2)*math.pow(mpX,2) - 2*m*mpX*mpY - 1
            x1 = (-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
            x2 = (-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
            y1 = mpY + m*(x1-mpX)
            y2 = mpY + m*(x2-mpX)
        self.ep1 = [x1,y1]
        self.ep2 = [x2,y2]

        
    def getMPX(self):
        return self.midpoint[0]
    
    def getMPY(self):
        return self.midpoint[1]
    
    def getX1(self):
        return self.ep1[0]
    
    def getY1(self):
        return self.ep1[1]
    
    def getX2(self):
        return self.ep2[0]
    
    def getY2(self):
        return self.ep2[1]
    
    def getSuccess(self):
        return self.isSuccess