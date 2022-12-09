# Dynamic routing mechanism design in faulty network
# The team will simulate a mesh network where nodes and links may fail (Figure 5). Nodes and links may fail
# intermittently, as an input to the simulation, each node and link will have a certain probability to fail.
# When such failure occurs, the network must adapt and re-route to avoid the faulty link/node.

# code compiles and runs
# code is doccumented

# report explains  the functionality of the protocol
# novel contibution
# results and analysis of the results



# Paige Mortensen and Marissa Floam
# CPE 400
# Final Project
# Faulty Node Networking

# library imports
import random

# Default graph structure
nodes = dict({'a': 0.02, 'b': 0.05, 'c': 0.01, 'd': 0.03, 'e': 0.01, 'f': 0.15}) # dictionary of nodes {nodeName: percentFailure (0-1)}
links = dict({
                'a': {'b': 1, 'c': 3},
 				'b': {'a': 1, 'd': 1},
                'c': {'a': 3, 'd': 2},
				'd': {'b': 1, 'c': 2, 'e': 5, 'f': 2},
                'e': {'d': 5},
 				'f': {'d': 2}})
linkProbFailure = dict({'ab': 0.01, 'ac': 0.01, 'bd': 0.04, 'cd': 0.02, 'de': 0.01, 'df': 0.15})

nodeLabels = list(nodes.keys()) 			#converts node labels to list
nodeProbs = list(nodes.values()) 			#converts node failure probabilities to list
linkLabels = list(linkProbFailure.keys()) 	#converts link labels to list
linkProbs = list(linkProbFailure.values()) 	#converts link failure probabilities to list

#Graph Class
class Graph:
	#attributes: nodes, edges, failure likelihoods, distance, delay
	#functions: add node, remove node, add edge, remove edge, display/compare?
    
    # constructor
    def __init__(self):
        self.links = links
        self.nodeLabels = nodeLabels
        self.nodeFailureProb = nodeFailureProb
        self.linkLabels = linkLabels
        self.linkFailureProb = linkFailureProb
        self.sourceNode = 'a'
        self.targetNode = 'f'
    
    def addNode():
        # name your node:
        # what failure prob. would you like it to have (0-1)
        # name an adjacent node to connect your new node to
        
    def deleteNode():
        # what node do would you like to delete: 
        # delete node from nodes[]
            # del nodes[usrIn]
        # iterate through edges[] and delete entire edge when deleted node encountered
        
    def addEdge():
        # name your first node: 
        # name your second node: 
        # what failure prob would you like it to have: 
        
    def deleteEdge():
        # delete the edge between what and what nodes: p, q
        # iterate through edges[] and if contains both p and q, delete entire edge
        
    def displayGraph():
        # iterate through edges[] and nodes[] and simply print ?
        

#Loads all data into graph from graph class
def loadGraph():

#Dijkstra's algorithm to simulate pathing of the graph
def dijkstra():

#Breadth First Search algorithm to simulate pathing of the graph
def bfs():

#when a node failure is simulated, remove failed node, remove links attached to the node, display what was removed
def nodeFailure(graph):
    population = list(nodes.keys()) 									#converts node labels to list
    probability = list(nodes.values()) 									#converts node failure probabilities to list
    failedNode = random.choices(population, weights=probability, k=1) 	#randomly picks a node to fail based on weighted probabilities
    print("Node ", failedNode[0], " failed.") 							#random.choices returns an array so the failed node is at index 0 (and should be the only element in that list)
    graph.deleteNode(failedNode[0])

#when a link failure is simulated, remove failed link, remove nodes attached to the link (if they arent attached to any other nodes), display which links/nodes have been removed.
def linkFailure(graph):
    pop = list(linkProbFailure.keys()) 						#converts link labels to list
    prob = list(linkProbFailure.values()) 					#converts link failure probabilities to list
    failedLink = random.choices(pop, weights=prob, k=1) 	#randomly picks an edge to fail based on weighted probabilities
    print("Link ", failedLink[0], " failed.") 				#same issue as above. how to connect this failedLink to the graph.links?
    graph.deleteEdge(failedLink[0])

#Menu function to allow user to simulate either node or link failure, as well as display the current graph.
def menu():
	print("Select an Option:")
	print("1. Display Graph")
	print("2. Simulate Node Failure")
	print("3. Simulate Link Failure")
	print("4. Exit")
	i = input("Option: ")
	return i

#Main function displays the title, loads in the graph, and calls appropriate functions based on user input of the menu.
def main():
	#display title
	print("\n\n*~*~*~*~*~*~*~*~*")
	print("CPE 400 Final Project")
	print("Dynamic Routing Mechanism Design in Faulty Network")
	print("By: Marissa Floam & Paige Mortensen")
	print("*~*~*~*~*~*~*~*~*\n\n")
	
	#load graph
	graph = Graph()
	
	userInput = 0
	
	while userInput is not '4':
		userInput = menu()
		if userInput is '1':
			# display graph
			graph.displayGraph()
		elif userInput is '2':
			# simulate node failure
			nodeFailure(graph)
		elif userInput is '3':
			# simulate link failure
			linkFailure(graph)
		elif userInput is '4':
			break
		else:
			print("Please enter a valid input.\n")
	return
	
if __name__ == '__main__': main()
