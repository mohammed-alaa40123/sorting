import plotly.graph_objects as go
from quicksort import *
import time
import numpy as np
import streamlit as st

# Define the linked list node structure
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Function to add a node to the linked list
def add_node(head, data):
    new_node = Node(data)
    
    if head is None:
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    return head

# Function to visualize the array of linked lists
def visualize_linked_lists(linked_lists):
    fig = go.Figure()
    y = 0  
    for i, linked_list in enumerate(linked_lists):
        x = 0  
        fig.add_shape(
            type='rect',
            x0=-0.4,
            y0=y-0.4,
            x1=0,
            y1=y+0.4,
            line=dict(color='black', width=2),
            fillcolor='white',
            layer='below',
        )
        fig.add_annotation(
            x=-0.2,
            y=y,
            text=f"Bucket {i+1}",
            showarrow=False,
            font=dict(color='black', size=12),
            align='right'
        )
        x += 1
        for i in range(len(linked_list)):
            fig.add_trace(go.Scatter(
                x=[x],
                y=[y],
                mode='markers+text',
                marker=dict(size=25, color='blue'),
                text=[f"{linked_list[i]}"],
                textposition='middle center',
                hoverinfo='text',
                hovertext=[f"List {i+1}: {linked_list[i]}"],
            ))
            if i!= len(linked_list)-1:
                fig.add_trace(go.Scatter(
                    x=[x, x + 1],
                    y=[y, y],
                    mode='lines',
                    line=dict(color='gray', width=1),
                    hoverinfo='none',
                ))
            x += 1
        y -= 1

    # Configure layout
    fig.update_layout(
        title="Array of Linked Lists",
        showlegend=False,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )

    # Show the figure
    return fig

def vis_quick_sort(x, lst):
    frames = [lst.copy()]
    figures = []
    quick_sort(lst, 0, len(lst)-1, frames)
    for i in frames:
        figures.append(px.bar(x=x, y=i))
    return figures

# Example usage
def bucket_sort(nb, l):
    bucket = []
    for i in range(nb+1):
        bucket.append([])
    
    max_val = l[0]
    for i in l:
        if i > max_val:
            max_val = i
    index_factor = nb / max_val
    frames = []
    
    for i in l:
        indx = int(i * index_factor)
        bucket[indx].append(i)
        frames.append(visualize_linked_lists(bucket))
    
    for i in bucket:
        sz = len(i)
        if sz != 0:
            x = np.arange(0, sz, 1)
            frames.extend(vis_quick_sort(x, i))
            frames.append(visualize_linked_lists(bucket))
         
    return frames

# Create three linked lists
l = [503, 32, 12, 4213, 213, 23, 31]
frames = bucket_sort(10, l)

# Split the screen into three columns
col1, col2, col3 = st.columns(3)

# Display the first column (buckets)
with col1:
    st.plotly_chart(frames[0])

# Display the second column (linked list visualization)
with col2:
    st.plotly_chart(frames[0])

# Display the third column (quick sort)
with col3:
    st.plotly_chart(frames[0])

# Loop over the frames and update the charts in each column
for frame in frames[1:]:
    time.sleep(1)
    
    # Update the first column
    with col1:
        st.plotly_chart(frame)
    
    # Update the second column
    with col2:
        st.plotly_chart(frame)
    
    # Update the third column
    with col3:
        st.plotly_chart(frame)