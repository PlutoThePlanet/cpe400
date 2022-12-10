# library imports
import random

# Default graph structure
nodes = dict({'a': 0.00, 'b': 0.05, 'c': 0.01, 'd': 0.03, 'e': 0.01, 'f': 0.00}) # note that a and f are source/target and thus cannot fail
links = dict({
        'a': {'b': 1, 'c': 3},
        'b': {'a': 1, 'd': 1},
        'c': {'a': 3, 'd': 2},
        'd': {'b': 1, 'c': 2, 'e': 5, 'f': 2},
        'e': {'d': 5},
        'f': {'d': 2}})
linkProbFailure = dict({'ab': 0.01, 'ac': 0.01, 'bd': 0.04, 'cd': 0.02, 'de': 0.01, 'df': 0.15})

nodeLabels = list(nodes.keys()) 		#converts node labels to list
nodeProbs = list(nodes.values()) 		#converts node failure probabilities to list
linkLabels = list(linkProbFailure.keys()) 	#converts link labels to list
linkProbs = list(linkProbFailure.values()) 	#converts link failure probabilities to list

#Graph Class
class Graph:
  def __init__(self): # constructor
    self.nodes = nodes
    self.links = links
    self.linkProbFailure = linkProbFailure
    self.sourceNode = 'a'
    self.targetNode = 'f'
  
  def deleteNode(self, node):
    neighbors = list(links[node].keys()) 				# get key values of what nodes 'node' can see
    if not linkLabels:
      print("Error")
    else:
      # deletes from nodes
      del self.nodes[node]

      # deletes from links
      del self.links[node]          					# delete the entirety of the node and its links
      for elem in neighbors:  
        del self.links[elem][node]  					# delete node's link from its old neighbors
      # deletes from linkProbFailure
      toDeleteLinks = []
      for elem in self.linkProbFailure.keys():  			# iterate through original list of links + failure
        if elem.__contains__(node):
          toDeleteLinks.append(elem)
      for elem in toDeleteLinks:                			# go through and delete desired links (those connected to failed node)
        del self.linkProbFailure[elem]
  
    # deletes nodes that are no
    # longer connected to the graph
    nonLinkedNodes = []
    for elem in self.links:
      list(self.links[elem].values())
      if (len(list(self.links[elem].values())) == 0):
        nonLinkedNodes.append(elem)
    for elem in nonLinkedNodes:
      del self.links[elem]
      del self.nodes[elem]
  
    print("Node", node, "has been removed from the graph.")
    print("Remaining nodes: ", list(self.nodes.keys()))
    print("Remaining links: ", list(self.linkProbFailure.keys()), "\n\n")
      
  def deleteLink(self, link):
    # delete from links
    linkNodes = list(link)
    firstNode = linkNodes[0]
    secondNode = linkNodes[1]
    del self.links[firstNode][secondNode]
    del self.links[secondNode][firstNode]
    
    # delete from linkProbFailure
    del self.linkProbFailure[link]

    # deletes nodes that are no
    # longer connected to the graph
    nonLinkedNodes = []
    for elem in self.links:
      list(self.links[elem].values())
      if (len(list(self.links[elem].values())) == 0):
        nonLinkedNodes.append(elem)
    for elem in nonLinkedNodes:
      del self.links[elem]
      del self.nodes[elem]

    print("Link", link, "has been removed from the graph.")
    print("Remaining links: ", list(self.linkProbFailure.keys()), "\n\n")
    
  def displayGraph(self):
    n = list(self.nodes.keys())
    l = list(self.linkProbFailure.keys())
    print("Current Nodes:", n)
    print("Current Links:", l, "\n\n")
    

#Dijkstra's algorithm to simulate pathing of the graph
def dijkstra():
	print("Do dijkstra's here")

#Breadth First Search algorithm to simulate pathing of the graph
def bfs():
	print("Do BFS here")

#when a node failure is simulated, remove failed node, remove links attached to the node, display what was removed
def nodeFailure(graph):
  population = list(nodes.keys()) 					#converts node labels to list
  probability = list(nodes.values())  					#converts node failure probabilities to list
  failedNode = random.choices(population, weights=probability, k=1)   	#randomly picks a node to fail based on weighted probabilities
  print("Node", failedNode[0], "has failed.")   			#random.choices returns an array so the failed node is at index 0 (and should be the only element in that list)
  graph.deleteNode(failedNode[0]) 					#need to somehow connect failed node to the graph.nodes idk how atm

#when a link failure is simulated, remove failed link, remove nodes attached to the link (if they arent attached to any other nodes), display which links/nodes have been removed.
def linkFailure(graph):
  pop = list(linkProbFailure.keys())  			#converts link labels to list
  prob = list(linkProbFailure.values())   		#converts link failure probabilities to list
  failedLink = random.choices(pop, weights=prob, k=1) 	#randomly picks an edge to fail based on weighted probabilities
  print("Link", failedLink[0], "has failed.")   	#same issue as above. how to connect this failedLink to the graph.links?
  graph.deleteLink(failedLink[0])

def findShortestPath(graph):
	print("find shortest path here")
    # run dijkstras
    # run breadth-first
    # print('the shortest path found by dijkstras is ' + path_d)
        # total the weight of the entire path
        # time to find ?
    # print('the shortest path found by breadth-first is ' + path_bf)
        # total the weight of the entire path
        # time to find ?
    
#Menu function to allow user to simulate either node or link failure, as well as display the current graph.
def menu():
	print("Select an Option:")
	print("1. Display Graph")
	print("2. Simulate Node Failure")
	print("3. Simulate Link Failure")
	print("4. Run Pathing Algorithms")
	print("5. Exit\n\n")
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
	
	while userInput != '5':
		userInput = menu()
		if userInput == '1':
			# display graph
			graph.displayGraph()
		elif userInput == '2':
			# simulate node failure
			nodeFailure(graph)
		elif userInput == '3':
			# simulate link failure
			linkFailure(graph)
		elif userInput == '4':
			#Dijkstra's vs. BFS
			findShortestPath(graph)
		elif userInput == '5':
			break
		else:
			print("Please enter a valid input.\n")
	return
	
if __name__ == '__main__': main()
