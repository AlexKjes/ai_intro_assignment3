from model import Model
from graph import Graph
from a_star import BestFirst


# Wrapper for algorithm cases
def solve(visualize_progress=True, g=None, h=None, window_name='title',
          visualize_expanded=True, visualize_frontier=True):
    for i in range(1, 3):
        for j in range(1, 5):
            model = Model(str(i)+'-'+str(j), window_name=window_name)   # Model of the problem
            graph = Graph(model.start_pos, model.expand_state)  # A regular graph
            searcher = BestFirst(graph,
                                 model.h if h is None else h,
                                 model.is_solution,
                                 model.g if g is None else g)   # Search algorithm

            while searcher.solution is None:
                searcher.next()  # Open next node
                if visualize_progress:  # Visualize progress
                    model.visualize_progress([n.state for n in searcher.expanded], [n for n in searcher.frontier])

            solution = [n.state for n in searcher.solution]
            frontier = [n for n in searcher.frontier] if visualize_frontier else None
            expanded = [(n.state if n.state not in solution else (-100, -100)) for n in graph.expanded] if visualize_expanded else None
            model.visualize_solution(solution, expanded, frontier)

# A*
solve(window_name='A*')
# Dijkstra
solve(h=lambda x: 1, window_name='Dijkstra')
# Breadth first
solve(g=lambda x: 1, h=lambda x: 1, window_name='Breadth first')
