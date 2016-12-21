from depth_first_search import depth_first_search

def naive_strongly_connected_components(graph):
    vertices_number = len(graph)
    components = [0] * vertices_number
    visited = [False] * vertices_number
    stack = []
    vertices_number_i = 0
    for node in range(vertices_number):
        if not visited[node]:
            for dfs_visited_vertex in depth_first_search(graph, node, visited):
                vertices_number_i += 1
                stack.append(dfs_visited_vertex)
                visited[dfs_visited_vertex] = True
                components[dfs_visited_vertex] = vertices_number_i
    del graph[:]
    return components

# def dfs_scc(start_node, vertices_number, graph, vertices_number_i, components, visited=None):
#     assert start_node < len(graph)
#     stack = []
#     if visited is None:
#         visited = [False] * len(graph)
#     stack.append(start_node)
#     visited[start_node] = True
#     components[start_node] = vertices_number_i
#     while stack:
#         vertex = stack.pop()
#         if dfs_back(vertex, start_node, vertices_number, graph):
#             components[vertex] = vertices_number_i
#         for dfs_visited_vertex in depth_first_search(graph, vertex, visited):
#             children = graph[dfs_visited_vertex]
#             if len(children) != 0:
#                 not_visited = children.pop()
#                 if not visited[not_visited]:
#                     visited[not_visited] = True
#                     components[dfs_visited_vertex] = vertices_number_i
#     del visited[:]
#     return components
#
# def dfs_back(vertex_start, start_node, vertices_number, graph, visited=None):
#     assert start_node < len(graph)
#     stack = []
#     if visited is None:
#         visited = [False] * len(graph)
#     stack.append(vertex_start)
#     visited[vertex_start] = True
#     while stack:
#         vertex = stack.pop()
#         for dfs_visited_vertex in depth_first_search(graph, vertex, visited):
#             children = graph[dfs_visited_vertex]
#             if len(children) != 0 and children == start_node:
#                 del visited[:]
#                 return True
#             if len(children) != 0:
#                 not_visited = children.pop()
#                 if not visited[not_visited]:
#                     visited[not_visited] = True
#     del visited[:]
#     return False
