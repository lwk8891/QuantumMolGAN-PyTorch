import numpy as np
from collections import deque
import copy

def add_edge(source_index, dest_index, edges):
    edges[source_index, dest_index] = 1
    edges[dest_index, source_index] = 1

def remove_edge(source_index, dest_index, edges):
    edges[source_index, dest_index] = 0
    edges[dest_index, source_index] = 0

def adj(node_index, edges):
    adj_row = edges[:, node_index]
    return np.where(adj_row != 0)[0]

def dfs(start_index, nodes, edges):
    return_nodes = deque()
    stack = deque()
    visited = np.zeros(edges.shape[0])
    adj_0 = adj(start_index, edges)
    visited[start_index] = 1
    return_nodes.append(nodes[start_index])
    for i in range(len(adj_0)):
        stack.append(adj_0[i])

    while(len(stack) != 0):
        next = stack.pop()
        adj_next = adj(next, edges)
        visited[next] = 1
        for i in range(len(adj_next)):
            if visited[adj_next[i]] == 0:
                stack.append(adj_next[i])
                visited[adj_next[i]] == 1
        visited[next] = 1
        return_nodes.append(nodes[next])

    return return_nodes

def connectivity(nodes, edges):
    nodes_indices = list(range(len(nodes)))
    visited = np.zeros(edges.shape[0])

    connectivity_list = []

    for start_index in nodes_indices:
        if visited[start_index] == 0:
            return_nodes = deque()
            stack = deque()
            adj_0 = adj(start_index, edges)
            visited[start_index] = 1
            return_nodes.append(nodes[start_index])

            for i in range(len(adj_0)):
                stack.append(adj_0[i])

            while(len(stack) != 0):
                next = stack.pop()
                adj_next = adj(next, edges)
                visited[next] = 1
                for i in range(len(adj_next)):
                    if visited[adj_next[i]] == 0:
                        stack.append(adj_next[i])
                        visited[adj_next[i]] == 1
                visited[next] = 1
                return_nodes.append(nodes[next])

            connectivity_list.append(return_nodes)

    return connectivity_list

def connectivity_without_zero(nodes, edges, zero_val):
    nodes_indices = list(range(len(nodes)))
    visited = np.zeros(edges.shape[0])

    zero_nodes = np.where(np.array(nodes) == zero_val)
    zero_edges = copy.deepcopy(edges)
    for i in zero_nodes:
        zero_edges[:, i] = 0
        zero_edges[i, :] = 0

    connectivity_list = []

    for start_index in nodes_indices:
        if visited[start_index] == 0:
            return_nodes = deque()
            stack = deque()
            adj_0 = adj(start_index, zero_edges)
            visited[start_index] = 1
            return_nodes.append(nodes[start_index])

            for i in range(len(adj_0)):
                stack.append(adj_0[i])

            while(len(stack) != 0):
                next = stack.pop()
                adj_next = adj(next, zero_edges)
                visited[next] = 1
                for i in range(len(adj_next)):
                    if visited[adj_next[i]] == 0:
                        stack.append(adj_next[i])
                        visited[adj_next[i]] == 1
                visited[next] = 1
                return_nodes.append(nodes[next])

            connectivity_list.append(return_nodes)

    return connectivity_list

def is_connected(nodes, edges):
    connectivity_list = connectivity(nodes, edges)
    if len(connectivity_list) == 1:
        connected = True
    else:
        connected = False

    return connected

def is_connected_without_zero(nodes, edges, zero_val):
    trim_nodes = nodes
    trim_edges = edges
    #for i in range(len(nodes)):
    #    tail_nodes = nodes[i:]
    #    if all(x == 0 for x in tail_nodes):
    #        trim_nodes = nodes[0:i]
    #        trim_edges = edges[0:i, 0:i]
    #        break

    connectivity_list = connectivity_without_zero(trim_nodes, trim_edges, zero_val)
    if len(connectivity_list) == 1:
        connected = True
    else:
        connected = False

    return connected


if __name__ == '__main__':
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    edges = np.zeros((len(nodes), len(nodes)), dtype=int)

    add_edge(0, 1, edges)
    add_edge(0, 2, edges)
    add_edge(1, 3, edges)
    add_edge(3, 4, edges)
    add_edge(3, 5, edges)
    add_edge(2, 6, edges)
    add_edge(2, 7, edges)
    add_edge(2, 8, edges)
    add_edge(8, 9, edges)

    dfs_nodes = dfs(0, nodes, edges)
    print(dfs_nodes)

    print(connectivity(nodes, edges))
    print(is_connected(nodes, edges))

    nodes2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    edges2 = np.zeros((len(nodes), len(nodes)), dtype=int)

    add_edge(0, 1, edges2)
    add_edge(0, 2, edges2)
    add_edge(5, 8, edges2)
    add_edge(8, 1, edges2)

    print(connectivity(nodes2, edges2))
    print(is_connected(nodes2, edges2))
