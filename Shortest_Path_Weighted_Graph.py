from collections import defaultdict
import heapq
from typing import Dict, List, Set, Tuple, Optional

class WeightedGraph:
    def __init__(self):
        # Using defaultdict to store the adjacency list
        self.graph = defaultdict(list)
    
    def add_edge(self, u: int, v: int, weight: int) -> None:
        """Add an undirected weighted edge between vertices u and v"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Add reverse edge for undirected graph
    
    def dijkstra(self, start: int, end: int) -> Tuple[Optional[int], List[int]]:
        """
        Find shortest path between start and end vertices using Dijkstra's algorithm
        Returns: (shortest_distance, path)
        """
        # Priority queue to store (distance, vertex, path)
        pq = [(0, start, [start])]
        # Set to keep track of visited vertices
        visited = set()
        
        while pq:
            # Get vertex with minimum distance
            (dist, current, path) = heapq.heappop(pq)
            
            # If we reached the destination
            if current == end:
                return dist, path
            
            # If we've already processed this vertex
            if current in visited:
                continue
                
            visited.add(current)
            
            # Process all neighbors
            for neighbor, weight in self.graph[current]:
                if neighbor not in visited:
                    # Calculate new distance and update path
                    new_dist = dist + weight
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (new_dist, neighbor, new_path))
        
        # If no path exists
        return None, []
    
    def get_all_paths(self, start: int, end: int, max_paths: int = 5) -> List[Tuple[int, List[int]]]:
        """
        Find multiple paths between start and end vertices, sorted by total distance
        Returns: List of (distance, path) tuples
        """
        pq = [(0, start, [start])]
        paths = []
        visited_paths = set()
        
        while pq and len(paths) < max_paths:
            (dist, current, path) = heapq.heappop(pq)
            
            if current == end:
                path_tuple = tuple(path)
                if path_tuple not in visited_paths:
                    paths.append((dist, path))
                    visited_paths.add(path_tuple)
                continue
            
            for neighbor, weight in self.graph[current]:
                if neighbor not in path:  # Avoid cycles
                    new_dist = dist + weight
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (new_dist, neighbor, new_path))
        
        return paths

def test_shortest_path():
    # Create a sample graph
    g = WeightedGraph()
    
    # Add edges (vertex1, vertex2, weight)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 2)
    
    # Test cases
    print("\nTest Case 1: Find shortest path from 0 to 4")
    distance, path = g.dijkstra(0, 4)
    print(f"Shortest distance: {distance}")
    print(f"Path: {' -> '.join(map(str, path))}")
    
    print("\nTest Case 2: Find all paths from 0 to 4")
    all_paths = g.get_all_paths(0, 4)
    for i, (dist, path) in enumerate(all_paths, 1):
        print(f"Path {i} (distance: {dist}): {' -> '.join(map(str, path))}")
    
    print("\nTest Case 3: Find shortest path in disconnected graph")
    g2 = WeightedGraph()
    g2.add_edge(0, 1, 4)
    g2.add_edge(2, 3, 2)  # Disconnected from vertices 0 and 1
    distance, path = g2.dijkstra(0, 3)
    print(f"Shortest distance: {distance}")
    print(f"Path: {path}")

if __name__ == "__main__":
    test_shortest_path()