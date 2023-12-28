import os
# uncomment the following line if you get the relevant error.
os.environ['KMP_DUPLICATE_LIB_OK']='True' 
from pgmpy.base import DAG
import networkx as nx
import numpy as np



def s_ID(X, Y, G):
	"""
		This function returns an expression if P(Y | do(X), S) is s-ID in G; otherwise, it returns "Fail."
        Parameters
        ----------
        X: set
            Set of intervention nodes.
        Y: set
            Set of output nodes.
        G: DAG
            The main causal graph is a DAG object.
	"""

	anc_s = set(G.get_ancestral_graph("s").nodes())
	X_1 = set(anc_s).intersection(X)
	X_2 = set(X).difference(X_1)
	G_new = get_dag_after_removal(X_2, X_1, G) 
	W = set(G.nodes()).difference(X_2.union(anc_s))
	if not X_1:
		return get_formula(anc_s, W, G, X, Y)
	elif nx.d_separated(G_new, X_1, Y, X_2.union({"s"})):
		return get_formula(anc_s, W, G, X, Y)
	return "Fail"


def create_dag(nodes: set, edges: set):
	"""	
		Creating a DAG object using sets of nodes and edges.
	"""
	
	
	dag = DAG(ebunch = edges)
	dag.add_nodes_from(nodes)
	return dag
	
def get_dag_after_removal(in_remove: set, out_remove: set, G):
	"""
		This function returns the subgraph of G after removing the ingoing edges of "in_remove" 
        and outgoing edges of "out_remove."
	"""

	removing_edges = []
	for u in out_remove:
		removing_edges += [(u, v) for v in G.get_children(u)]	
	for v in in_remove:
		removing_edges += [(u, v) for u in G.get_parents(v)]	
	return create_dag(G.nodes(), G.edges() - removing_edges)



def get_formula(anc_s, W, dag, X, Y) -> str:
	"""
			This function returns an expression based on Equations (3) and (6) in the paper!
	"""

	X_1 = set(anc_s).intersection(X)
	margin_var = set(dag.nodes()).difference(X.union(Y).union({"s"}))
	expr = ""
	if X_1:
		expr += f"1/P^s({set_to_string(X_1)}) * "
	if margin_var:
		expr += f"\sum_({set_to_string(margin_var)}) "	
	
	if len(anc_s) > 1:
		anc_s.remove("s")
		expr += f"P^s({set_to_string(anc_s)})"	
		if W:
			expr += " * "
	for idx, w in enumerate(W):
		parents = dag.get_parents(w)
		par_str = set_to_string(parents)
		expr += f'P^s({str(w)} | {par_str})'
		if idx != len(W) - 1:
			expr += " * "
	return expr
	
	
def set_to_string(X):
	"""
			Helper function to show a list of nodes, separating with commas.
	"""
	
	
	X = list(X)
	X.sort()
	out_str = str(X[0]) if X else ""
	for el in X[1:]:
		out_str += str(', ') + str(el)
	return out_str	
