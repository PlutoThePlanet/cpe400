#
#
#
#
#
#

#library imports

#Declare node + edge data globally here

#Graph Class
class Graph:
	#attributes: nodes, edges, failure likelihoods, distance, delay
	#functions: add node, remove node, add edge, remove edge, display/compare?

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
