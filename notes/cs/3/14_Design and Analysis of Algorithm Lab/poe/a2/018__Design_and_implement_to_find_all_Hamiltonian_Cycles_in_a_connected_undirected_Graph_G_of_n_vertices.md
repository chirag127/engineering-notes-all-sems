 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- Hamiltonian Cycle: A Hamiltonian cycle (or Hamiltonian circuit) is a graph cycle that visits each vertex exactly once.
- Backtracking: Backtracking is a general algorithmic technique that considers searching through the solution space by trying to construct candidates to the solutions incrementally, while removing those candidates that fail to satisfy the problem constraints.
- Steps:
    1. Check if graph G is connected and has n vertices. If not, print "No Hamiltonian Cycle exists" and return.
    2. Initialize a boolean array of size n to mark visited vertices.
    3. Call the recursive Hamiltonian Cycle function with parameter as 0 (Starting vertex).
    4. Hamiltonian Cycle function:
        - If all n vertices are visited, print the Hamiltonian cycle.
        - Else, do following for every vertex v:
            - If v is not visited, mark it as visited and recursively call the function v (Next vertex in Hamiltonian cycle).
            - Unmark v as visited (Backtrack) in case the Hamiltonian cycle is not complete.
- Implementation: Here is a sample implementation in C++:
/* C++ program to print all Hamiltonian Cycles in a given undirected graph using backtracking */
#include <bits/stdc++.h>
using namespace std;

// Check if graph G has a Hamiltonian Cycle or not
bool isHamiltonian(vector<int> adj[], int s, vector<bool>& visited)
{
    // Mark the source vertex as visited
    visited[s] = true;

    // If there are no more vertices to be visited
    if (s == adj.length - 1) {
        // Print the Hamiltonian path
        for (int v = 0; v <= s; ++v)
            cout << adj[v].front() << " ";
        cout << endl;
        return true;
    }

    // Recur for all the vertices adjacent to s
    for (int i = 0; i < adj[s].size(); ++i) {
        int v = adj[s][i];
        // If the adjacent vertex is already visited, then continue
        if (visited[v]) continue;

        // If Hamiltonian path exists from the adjacent vertex, then print it
        if (isHamiltonian(adj, v, visited))
            return true;
    }

    // If no adjacent vertex results in a Hamiltonian path, then unmark s and return false
    visited[s] = false;
    return false;
}

// Prints all Hamiltonian Cycles in the given graph
void printHamiltonianCycles(vector<int> adj[])
{
    // Mark all the vertices as not visited
    vector<bool> visited(adj.length, false);

    // Find Hamiltonian Cycle starting from each vertex
    for (int i = 0; i < adj.length; ++i)
        isHamiltonian(adj, i, visited);
}

// Driver code
int main()
{
    // Let us create a sample graph
    int n = 4;
    vector<int> adj[n];
    adj[0].push_back(1);
    adj[0].push_back(2);
    adj[1].push_back(0);
    adj[1].push_back(3);
    adj[2].push_back(0);
    adj[2].push_back(3);
    adj[3].push_back(1);
    adj[3].push_back(2);

    printHamiltonianCycles(adj);

    return 0;
}