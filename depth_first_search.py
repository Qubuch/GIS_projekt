def depth_first_search(graph, start_node, visited=None):
    assert start_node < len(graph)
    nodes_queue = [start_node]
    if visited is None:
        visited = [False] * len(graph)
    visited[start_node] = True
    while nodes_queue:
        current_node = nodes_queue.pop()
        yield current_node
        children = graph[current_node]
        not_visited_children = filter(lambda x: not visited[x], children)
        nodes_queue.extend(not_visited_children)
        for child in not_visited_children:
            visited[child] = True


def postorder_depth_first_search(graph, current_node, visited=None):
    assert current_node < len(graph)
    if visited is None:
        visited = [False] * len(graph)
    visited[current_node] = True
    children = graph[current_node]
    not_visited_children = filter(lambda x: not visited[x], children)
    for child in not_visited_children:
        yield from postorder_depth_first_search(graph, child, visited)
    yield current_node
