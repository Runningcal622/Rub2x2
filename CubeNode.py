#Caleb Vanorio
#Cube Node
# this is designed to be the Nodes that we will use for the tree search A*

class CubeNode:
    def __init__(self, cube,theParent,theAction,costFromStart):
        self.__curState = cube
        self.__parent = theParent
        self.__actionToCur = theAction
        self.__pathCost = costFromStart
        if theAction!=None:
            self.__splitMove = self.__actionToCur.split(" ")
            #each component of the move, face and direction
            #does the action to make it into the new current state
            self.__curState.move(self.__splitMove[0],self.__splitMove[1])
        self.__heuristic = self.heurFunc(self.__curState)
        #print("the cost is "+str(self.__pathCost))
        self.__score = self.__heuristic+self.__pathCost

    def __lt__(self, other):
        ###this makes the CubeNode Comparable
        selfPriority = self.getScore()
        otherPriority = other.getScore()
        return selfPriority > otherPriority
            
    def getCurState(self):
        return self.__curState
    def getParent(self):
        return self.__parent
    def getActionToCur(self):
        return self.__actionToCur
    def getPathCost(self):
        return self.__pathCost
    def getScore(self):
        return self.__score


    def heurFunc(self, rubik):
        #This is the heuristic evaluator for each state
        #Input: the cube to be evaluated
        #output: the heuristic based on the number of spots out of place
        wrongSpots=0
        for side in range(6):
            faces = rubik.getFaces()
            curFace = faces[side]
            curCount = dict()
            for row in range(2):
                for col in range(2):
                    if curFace[row][col] in curCount:
                        curCount[curFace[row][col]] +=1
                    else:
                        curCount[curFace[row][col]] = 1
                        
            mostSpaces=0    
            for key in curCount.keys():
                if curCount[key]>mostSpaces:
                    mostSpaces = curCount[key]

            wrongSpots+=4-mostSpaces

        heur = wrongSpots//8
        if wrongSpots>0 and heur==0:
            heur=1
        return heur
                
                                 
                                
                    




                        
                    
