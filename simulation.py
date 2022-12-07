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

# Declare node + edge data globally here
# Default graph structure
nodes = [['a', 0.02], ['b', 0.05], ['c', 0.1], ['d', 0.01], ['e', 0.01], ['f', 0.15]] # [node, failureProb]
edges = [['a', 'b', 0.01], ['a', 'c', 0.01], ['b', 'd', 0.01], ['c', 'd', 0.01], ['d', 'e', 0.01], ['d', 'f', 0.01], ['e', 'f', 0.01]] # [pt1, pt2, failureProb]
# nodeFailureProb = []
# edgeFailureProb = []

#Graph Class
class Graph:
	#attributes: nodes, edges, failure likelihoods, distance, delay
	#functions: add node, remove node, add edge, remove edge, display/compare?
    
    # constructor
    # def __init__(self):
        # 
    
    def addNode():
        # name your node:
        # what failure prob. would you like it to have (0-1)
        # name an adjacent node to connect your new node to
        
    def deleteNode():
        # what node do would you like to delete: 
        # delete node from nodes[]
        # iterate through edges[] and delete entire edge when encountered
        
    def addEdge():
        # name your first node: 
        # name your second node: 
        # what failure prob would you like it to have: 
        
    def deleteEdge():
        # delete the edge between what and what nodes: p, q
        # iterate through edges[] and if contains both p and q, delete entire edge
        
    # def displayGraph():
        # iterate through edges[] and nodes[] and simply print ?
        

#Loads all data into graph from graph class
def loadGraph():

#Dijkstra's algorithm to simulate pathing of the graph
def dijkstra():

#Breadth First Search algorithm to simulate pathing of the graph
def BFS():

#when a node failure is simulated, remove failed node, remove links attached to the node, display what was removed
def nodeFailure(graph):

#when a link failure is simulated, remove failed link, remove nodes attached to the link (if they arent attached to any other nodes), display which links/nodes have been removed.
def linkFailure(graph):

#displays current graph
def displayGraph(graph):

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
	
	#load graph
	
	i = 0 #userInput
	
	while i is not '4':
		i = menu()
		if i is '1':
			#display graph
		elif i is '2':
			#simulate node failure
		elif i is '3':
			#simulate link failure
		elif i is '4':
			break
		else:
			print("Please enter a valid input.\n")
	return
	
if __name__ == '__main__': main()
