import networkx as nx
import matplotlib.pyplot as plt
import json

class Graph:
    def __init__(self, edges):
        self.set_edges(edges)


    def set_edges(self, edges):
        self.edges = edges
        self.edges_to_transitions()

    
    def set_transitions(self, transitions):
        self.transitions = transitions
        self.transitions_to_edges()

    
    def get_vertices_list(self):
        vertices_list = []
        for item in self.edges:
            if item[0] not in vertices_list:
                vertices_list.append(item[0])
            if item[1] not in vertices_list:
                vertices_list.append(item[1])

        return vertices_list


    def edges_to_transitions(self):
        self.transitions = {}
        for item in self.edges:
            if item[0] in self.transitions:
                if item[1] in self.transitions[item[0]]:
                    continue
                self.transitions[item[0]].append(item[1])
            else:
                self.transitions[item[0]] = [item[1]]


    def transitions_to_edges(self):
        tmp_edges = []
        for src in self.transitions:
            for dst in self.transitions[src]:
                self.edges.append([src, dst])

        self.edges = []
        for item in tmp_edges:
            if item not in self.edges:
                self.edges.append(item)


    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        nx.draw_networkx(G)
        plt.show()


    def print(self):
        print(json.dumps(self.transitions, indent=1, sort_keys=True))

