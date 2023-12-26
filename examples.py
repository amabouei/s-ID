from main import *


######fig1-l
nodes = {"z", "x", "y", "w", "s"}
edges = {("w", "x"), ("w", "z"), ("w", "y"), ("x", "z"), ("z", "y"), ("w", "s") }
dag = create_dag(nodes, edges)

print('Figure 1 left')
print(s_ID({"x"}, {"y"}, dag))	
print("-" * 10)

######fig1-r
nodes = {"z", "x", "y", "w", "s"}
edges = {("w", "x"), ("w", "y"), ("x", "z"), ("z", "y"), ("z", "s") }
dag = create_dag(nodes, edges)

print('Figure 1 right')
print(s_ID({"x"}, {"y"}, dag))	
print("-" * 10)



######fig3-b
nodes = {"z", "x", "y", "w", "s"}
edges = {("x", "y"), ("z", "x"), ("w", "y"), ("z", "s"), ("w", "s") }
dag = create_dag(nodes, edges)

print('Figure 3-b')
print(s_ID({"x"}, {"y"}, dag))	
print("-" * 10)

###fig3-ar
nodes = {"x", "y", "s"}
edges = {("x", "y"), ("y", "s")}
dag = create_dag(nodes, edges)	

print('Figure 3-a right')
print(s_ID({"x"}, {"y"}, dag))	
print("-" * 10)


######fig4-l		
nodes = {"z", "x", "y", "s"}
edges = {("x", "y"), ("z", "x"), ("z", "y"), ("y", "s")}

dag = create_dag(nodes, edges)
print('Figure 4- left')
print(s_ID({"x"}, {"y"}, dag))
print("-" * 10)


######fig4-r	
nodes = {"z", "x", "y", "s", "w"}
edges = {("x", "y"), ("z", "x"), ("z", "w"), ("y", "w"), ("w", "s")}

dag = create_dag(nodes, edges)
print('Figure 4- right')
print(s_ID({"x"}, {"y"}, dag))
print("-" * 10)



######fig5-l		
nodes = {"z", "x1", "x2", "y" "s"}
edges = {("x1", "y"), ("x2", "y"), ("z", "y"), ("z", "x1"), ("z", "x2"), ("x1", "s")}

dag = create_dag(nodes, edges)
print('Figure 5 left')
print(s_ID({"x1", "x2"}, {"y"}, dag))
print("-" * 10)


######fig5-r	
nodes = {"z", "x1", "x2", "y", "s", "w"}
edges = {("x1", "w"), ("w", "y"), ("x2", "y"), ("z", "y"), ("z", "w"), ("z", "x2"), ("w", "s")}

dag = create_dag(nodes, edges)
print('Figure 5 right')
print(s_ID({"x1", "x2"}, {"y"}, dag))
print("-" * 10)
