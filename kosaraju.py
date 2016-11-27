from depth_first_search import depth_first_search, postorder_depth_first_search


def kosaraju_strongly_connected_components(graph):
    vertices_number = len(graph)
    components = [0] * vertices_number
    visited = [False] * vertices_number
    stack = []
    for vertex in range(vertices_number):
        if not visited[vertex]:
            for dfs_visited_vertex in postorder_depth_first_search(graph, vertex, visited):
                stack.append(dfs_visited_vertex)
    transposed_graph = transpose_graph(graph)
    visited = [False] * vertices_number
    components_counter = 0
    while stack:
        vertex = stack.pop()
        if visited[vertex]:
            continue
        components_counter += 1
        for dfs_visited_vertex in depth_first_search(transposed_graph, vertex, visited):
            components[dfs_visited_vertex] = components_counter
    return components


def transpose_graph(graph):
    transposed_graph = [[] for _ in graph]
    for from_vertex, adjacency_list in enumerate(graph):
        for to_vertex in adjacency_list:
            transposed_graph[to_vertex].append(from_vertex)
    return transposed_graph
