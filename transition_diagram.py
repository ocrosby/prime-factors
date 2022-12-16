from diagrams import Diagram, Edge, Node

graph_attr = {
    "bgcolor": "white",
    "splines": "spline"
}

with Diagram("Transition Diagram", show=True, graph_attr=graph_attr):
    n0 = Node("0", shape="circle", labelloc="c", style="filled", fillcolor="white")
    n1 = Node("1", shape="circle", labelloc="c", style="filled", fillcolor="white")
    n2 = Node("2", shape="circle", labelloc="c", style="filled", fillcolor="white")
    n3 = Node("3", shape="circle", labelloc="c", style="filled", fillcolor="white")
    n4 = Node("4", shape="circle", labelloc="c", style="filled", fillcolor="white", peripheries="2")
    n5 = Node("5", shape="circle", labelloc="c", style="filled", fillcolor="white")
    n6 = Node("6", shape="circle", labelloc="c", style="filled", fillcolor="white", peripheries="2")

    n0 >> Edge(label=".") >> n2
    n2 >> Edge(label="stack not empty") >> n0

    n2 >> Edge(label="stack empty") >> n6

    n0 >> Edge(label="(") >> n1
    n1 >> Edge(label="push") >> n0

    n0 >> Edge(label=")") >> n3
    n3 >> Edge(label="stack empty") >> n4

    n3 >> Edge(label="stack not empty") >> n5
    n5 >> Edge(label="pop") >> n0