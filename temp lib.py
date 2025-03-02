import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph for the flowchart
G = nx.DiGraph()

# Add nodes
nodes = ["Data Aggregation", "Data Preprocessing", "Factor Construction & Normalization", 
         "Adaptive Weighting (HMM & GBM)", "Composite Rating (R = αF + βT + γQ + δL)", "Back-Testing & Performance Evaluation"]
G.add_nodes_from(nodes)

# Add edges
edges = [("Data Aggregation", "Data Preprocessing"),
         ("Data Preprocessing", "Factor Construction & Normalization"),
         ("Factor Construction & Normalization", "Adaptive Weighting (HMM & GBM)"),
         ("Adaptive Weighting (HMM & GBM)", "Composite Rating (R = αF + βT + γQ + δL)"),
         ("Composite Rating (R = αF + βT + γQ + δL)", "Back-Testing & Performance Evaluation")]
G.add_edges_from(edges)

# Position nodes using a hierarchical layout
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, arrows=True, font_size=10)
plt.title("Model Framework Flowchart")
plt.savefig("flowchart.png")
plt.show()
