from lect9_graph import *

'''
Write a WeightedEdge class that extends Edge. Its constructor requires a weight parameter, 
as well as the parameters from Edge. You should additionally include a getWeight method. 
The string value of a WeightedEdge from node A to B with a weight of 3 should be "A->B (3)".
'''

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.weight) + ")"