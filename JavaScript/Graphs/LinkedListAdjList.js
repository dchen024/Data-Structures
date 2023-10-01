// Node class to represent individual vertices in the graph
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// Graph class with adjacency list representation
class Graph {
    constructor(numVertices) {
        this.numVertices = numVertices;
        this.adjList = new Array(numVertices);
        for (let i = 0; i < numVertices; i++) {
            this.adjList[i] = null;
        }
    }

    // Add an edge between two vertices
    addEdge(src, dest) {
        // Create a new node for the destination vertex
        let newNode = new Node(dest);
        newNode.next = this.adjList[src];
        this.adjList[src] = newNode;

        // Since the graph is undirected, add an edge from dest to src as well
        newNode = new Node(src);
        newNode.next = this.adjList[dest];
        this.adjList[dest] = newNode;
    }

    // Print the adjacency list representation of the graph
    printGraph() {
        for (let i = 0; i < this.numVertices; i++) {
            let currNode = this.adjList[i];
            let list = '';
            while (currNode) {
                list += `${currNode.value} `;
                currNode = currNode.next;
            }
            console.log(`Vertex ${i}: ${list}`);
        }
    }
}

// Example usage
const graph = new Graph(5);

graph.addEdge(0, 1);
graph.addEdge(0, 4);
graph.addEdge(1, 2);
graph.addEdge(1, 3);
graph.addEdge(1, 4);
graph.addEdge(2, 3);
graph.addEdge(3, 4);

graph.printGraph();
