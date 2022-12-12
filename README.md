<h1>CPE 400 Final Project: Dynamic routing mechanism design in a faulty network</h1>

<h2>Authors: Marissa Floam & Paige Mortensen</h2>

<h3>Graph Class:</h3>
<ul>
 <li>Constructor</li>
 <p>The constructor of the Graph class includes initialization of the links, nodes, probability failures, and source node of the Graph.</p>
  
  <li> deleteNode </li>
 <p> deleteNode removes a node and the associated links from the graph, and displays the remaining nodes and links.</p>
  
  <li> deleteLink </li>
  <p> deleteLink removes a link and all unconnected nodes from the graph, and displays the remaining links. </p>
  
  <li> displayGraph </li>
  <p> displayGraph displays the current nodes and links in the graph. </p>
  
 </ul>

<h3>Functions:</h3>

<ul>
  <li> dijkstra </li>
  <p> In order to simulate pathing after a node or link fails, Dijkstra's algorithm is run to determine the shortest possible path.</p>
  
  <li> bellmanFord </li>
  <p> Same as above, but simulated with Bellman-Ford's algorithm of shortest pathing to compare which is more efficient.</p>
  
  <li> nodeFailure </li>
  <p> If the user wants to simulate a node failure in the graph, this function will remove the failed node, the links attached, and display which node failed.</p>
  
  <li> linkFailure </li>
    <p> If the user wants to simulate a link failure in the graph, this function will remove the failed link, the unattached nodes, and display which link failed.</p>
    
 <li> findShortestPath </li>
 <p> This function runs both Dijkstra's and Bellman-Ford on the current graph and displays each path as well as the total distance.</p>
  
  <li> menu </li>
  <p> This function displays a menu and returns the user's input.</p>
  
  <li> main </li>
  <p> The main function displays the title, loads in the graph, and calls appropiate functions based on user input. </p>
 </ul>

<h3>Error Handling:</h3>

<h3>Results:</h3>
