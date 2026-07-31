## Design and Analysis of Algorithm Lab: Real Time System

### Floyd's Algorithm for All-Pairs Shortest Paths Problem

Floyd's algorithm is an efficient algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively improving an estimate of the shortest path distances between all pairs of vertices until the estimate is accurate.

Here is an example of how to implement Floyd's algorithm in C++:

```c++
#include <iostream>
#include <algorithm>
using namespace std;
#define V 4
#define INF 99999

void floydWarshall (int graph[][V])
{
    int dist[V][V], i, j, k;
    for (i = 0; i < V; i++)
        for (j = 0; j < V; j++)
            dist[i][j] = graph[i][j];
    for (k = 0; k < V; k++)
    {
        for (i = 0; i < V; i++)
        {
            for (j = 0; j < V; j++)
            {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            if (dist[i][j] == INF)
                cout<<"INF"<<"     ";
            else
                cout<<dist[i][j]<<"     ";
        }
        cout<<endl;
    }
}

int main()
{
    int graph[V][V] = { {0, 5, INF, 10},
                        {INF, 0, 3, INF},
                        {INF, INF, 0, 1},
                        {INF, INF, INF, 0}
                      };
    floydWarshall(graph);
    return 0;
}
```

### Dynamic Programming for Travelling Sales Person Problem

The Travelling Sales Person (TSP) problem is a well-known NP-hard problem in computer science. It involves finding the shortest possible route that visits a given set of cities and returns to the starting city. Dynamic programming is a method that can be used to solve the TSP problem.

Here is an example of how to implement a dynamic programming solution to the TSP problem in C++:

```c++
#include <iostream>
#include <algorithm>
using namespace std;
#define V 4
#define INF 99999

int tsp(int graph[][V], int s) {
    int dp[1 << V][V];
    for (int i = 0; i < (1 << V); i++) {
        for (int j = 0; j < V; j++) {
            dp[i][j] = INF;
        }
    }
    dp[1 << s][s] = 0;
    for (int mask = 0; mask < (1 << V); mask++) {
        for (int i = 0; i < V; i++) {
            if (mask & (1 << i)) {
                for (int j = 0; j < V; j++) {
                    if (!(mask & (1 << j))) {
                        dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + graph[i][j]);
                    }
                }
            }
        }
    }
    int ans = INF;
    for (int i = 0; i < V; i++) {
        ans = min(ans, dp[(1 << V) - 1][i] + graph[i][s]);
    }
    return ans;
}

int main() {
    int graph[][V] = { {0, 10, 15, 20},
                        {10, 0, 35, 25},
                        {15, 35, 0, 30},
                        {20, 25, 30, 0}
                      };
    int s = 0;
    cout << tsp(graph, s) << endl;
    return 0;
}
```

These are examples of how to implement Floyd's algorithm for the All-Pairs Shortest Paths problem and a dynamic programming solution to the Travelling Sales Person problem. These algorithms can be useful for solving problems in the Design and Analysis of Algorithm Lab in the subject of Real Time System.