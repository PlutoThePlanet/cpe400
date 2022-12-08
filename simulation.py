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
nodes = dict({'a': 0.02, 'b': 0.05, 'c': 0.01, 'd': 0.03, 'e': 0.01, 'f': 0.15}) # dictionary of nodes {nodeName: percentFailure (0-1)}
edges = dict({
         'ab': [1, 0.01],
         'ac': [3, 0.01],
         'bd': [1, 0.04],
         'cd': [2, 0.02],
         'de': [5, 0.01],
         'df': [2, 0.15]}) # dictionary of edges {nodePair: [edgeWeight (distance), percentFailure]}		# could also set this up another way: https://www.pythonpool.com/dijkstras-algorithm-python/


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
    # randomize/calculate which node will fail
    # remove node
    # print('node ' + node + ' failed')
    # run dijkstras
    # run breadth-first
    # print('the shortest path found by dijkstras is ' + path_d)
    # print('the shortest path found by breadth-first is ' + path_bf)

#when a link failure is simulated, remove failed link, remove nodes attached to the link (if they arent attached to any other nodes), display which links/nodes have been removed.
def linkFailure(graph):
    # randomize/calculate which link will fail
    # remove link
    # print('link ' + link + ' failed')
    # run dijkstras
    # run breadth-first
    # print('the shortest path found by dijkstras is ' + path_d)
    # print('the shortest path found by breadth-first is ' + path_bf)
    

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
