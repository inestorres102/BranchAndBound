# Search methods

# import search

# ab = search.GPSProblem('A', 'B'
#                        , search.romania)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450




import search

ab = search.GPSProblem('A', 'B', search.romania)

# BFS
node_bfs, exp_bfs = search.breadth_first_graph_search(ab)
path_bfs = [n.state for n in node_bfs.path()[::-1]]
print("BFS:", [n.state for n in node_bfs.path()[::-1]], " : ", node_bfs.path_cost)

# DFS
node_dfs, exp_dfs = search.depth_first_graph_search(ab)
path_dfs = [n.state for n in node_dfs.path()[::-1]]
print("DFS:", [n.state for n in node_dfs.path()[::-1]], " : ", node_dfs.path_cost)

# B&B
node_bb, exp_bb = search.branch_and_bound_graph_search(ab)
path_bb = [n.state for n in node_bb.path()[::-1]]
print("B&B:", [n.state for n in node_bb.path()[::-1]], " : ", node_bb.path_cost)

# B&B con Subestimación (A*)
node_astar, exp_astar = search.astar_graph_search(ab)
path_astar = [n.state for n in node_astar.path()[::-1]]
print("A*:", [n.state for n in node_astar.path()[::-1]], " : ", node_astar.path_cost)