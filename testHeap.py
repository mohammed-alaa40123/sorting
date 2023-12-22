import streamlit as st
import igraph as ig
import plotly.graph_objects as go
import time

def heapify(lst, n, i, frames):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[i] < lst[left]:  
        largest = left

    if right < n and lst[largest] < lst[right]:  
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        frames.append((lst.copy(), i, largest))  # Save frame after heapify operation
        heapify(lst, n, largest, frames)

def heap_sort(lst):
    n = len(lst)
    frames = [(lst.copy(), -1, -1)]  

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, frames)

    heap_size = n
    while heap_size > 0:
        lst[0], lst[heap_size - 1] = lst[heap_size - 1], lst[0]
        frames.append((lst.copy(), heap_size - 1, 0))  # Save frame after swapping
        heapify(lst, heap_size - 1, 0, frames)
        heap_size -= 1

    return frames

def visualize_heap_sort(frames):
    fig = go.Figure()

    placeholder = st.empty()
    list_placeholder = st.empty()


    for i, (frame, arrow_start, arrow_end) in enumerate(frames):
        g = ig.Graph.Tree(len(frame), 2)
        g["number"] = frame
        g.vs["label"] = g["number"]

        layout = g.layout("rt",root=[0])  
        # print(*layout)
        edge_x = []
        edge_y = []
        for edge in g.get_edgelist():
            # edge (0,2) 
            # node 0 => 0,0 
            # node 2 => -1.25, 1 
            # edge_x = [0,1.25,None,0,-1.25]
            # edge_y = [0,1,None,0,1]
            x0, y0 = layout[edge[0]]
            x1, y1 = layout[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        # print(edge_x)
        # print(edge_y)

        node_x = [pos[0] for pos in layout]
        node_y = [pos[1] for pos in layout]

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            text=g["number"],
            textposition="middle center",
            textfont=dict(color="black"), 
            hoverinfo="none",
            marker=dict(size=40, color="lightblue", line=dict(color="blue", width=3)),  
        )

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            mode="lines",
            line=dict(width=1),
            hoverinfo="none",
        )

        arrow_trace = go.Scatter(
            x=[layout[arrow_start][0], layout[arrow_end][0]],
            y=[layout[arrow_start][1], layout[arrow_end][1]],
            mode="lines",
            line=dict(color="red", width=2),
            showlegend=False,
        )

        fig.add_trace(node_trace)
        fig.add_trace(edge_trace)
        fig.add_trace(arrow_trace)

        fig.update_layout(showlegend=False)
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)

        placeholder.plotly_chart(fig, use_container_width=True)
        # break
        list_placeholder.text_area("List", value=" ".join(map(str, frame)), height=50,key=f"{i}list")

        time.sleep(1)  
        fig.data = [] 

def main():
    st.title("Heap Sort Visualization")

    arr = st.text_input("Enter a list of numbers (space-separated):")
    arr = list(map(int, arr.split()))

    if st.button("Heap Sort"):
        frames = heap_sort(arr)
        visualize_heap_sort(frames)

main()