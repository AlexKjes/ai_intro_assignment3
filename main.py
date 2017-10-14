from model import Model
from graph import Graph
from a_star import BestFirst


# A*
def a_star(visualize_progress=True):
    for i in range(1, 3):
        for j in range(1, 5):
            model = Model(str(i)+'-'+str(j))
            graph = Graph(model.start_pos, model.expand_state)
            searcher = BestFirst(graph, model.h, model.is_solution, model.g)

            while searcher.solution is None:
                searcher.next()
                if visualize_progress:
                    model.visualize_progress([n.state for n in searcher.expanded], [n for n in searcher.frontier])

            solution = [n.state for n in searcher.solution]
            frontier = [n for n in searcher.frontier]
            expanded = [(n.state if n.state not in solution else (-100, -100)) for n in graph.expanded]
            model.visualize_solution(solution, expanded, frontier)


# Dijkstra's
def dijkstra(visualize_progress=True):
    for i in range(1, 3):
        for j in range(1, 5):
            model = Model(str(i)+'-'+str(j))
            graph = Graph(model.start_pos, model.expand_state)
            searcher = BestFirst(graph, lambda x: 1, model.is_solution, model.g)

            while searcher.solution is None:
                searcher.next()
                if visualize_progress:
                    model.visualize_progress([n.state for n in searcher.expanded], [n for n in searcher.frontier])

            solution = [n.state for n in searcher.solution]
            frontier = [n for n in searcher.frontier]
            expanded = [(n.state if n.state not in solution else (-100, -100)) for n in graph.expanded]
            model.visualize_solution(solution, expanded, frontier)


# Breadth first
def breadth_first(visualize_progress=True):
    for i in range(1, 3):
        for j in range(1, 5):
            model = Model(str(i)+'-'+str(j))
            graph = Graph(model.start_pos, model.expand_state)
            searcher = BestFirst(graph, lambda x: 1, model.is_solution, lambda x: 1)

            while searcher.solution is None:
                searcher.next()
                if visualize_progress:
                    model.visualize_progress([n.state for n in searcher.expanded], [n for n in searcher.frontier])

            solution = [n.state for n in searcher.solution]
            frontier = [n for n in searcher.frontier]
            expanded = [(n.state if n.state not in solution else (-100, -100)) for n in graph.expanded]
            model.visualize_solution(solution, expanded, frontier)


a_star()
dijkstra()
breadth_first()
