1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

## Problem
Find the city that can reach the fewest other cities within distanceThreshold.
If there's a tie, return the bigger city number.

## How it works
1. Make a table of distances between all cities (0 to itself, infinity everywhere else).
2. Add the direct roads in both directions.
3. Use Floyd-Warshall to find the shortest distance between every pair of cities.
4. Count how many cities each city can reach, then return the one with the fewest.

## Complexity
- Time: O(n³)
- Space: O(n²)

1584. Min Cost to Connect All Points

## Problem
Connect all the points with the lowest total cost.
The cost between two points is the Manhattan distance: |x1 - x2| + |y1 - y2|.

## How it works
1. Make an edge between every pair of points, with its cost.
2. Sort the edges from cheapest to most expensive.
3. Use Kruskal's algorithm with Union-Find :
   - If two points aren't connected yet, add the edge and its cost.
   - If they're already connected, skip it (it would make a cycle).
4. Return the total cost.

## Complexity
- Time: O(n² log n), mostly from sorting the edges
- Space: O(n²)


