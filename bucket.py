# # # # import plotly.graph_objects as go

# # # # # Define the linked list node structure
# # # # class Node:
# # # #     def __init__(self, data):
# # # #         self.data = data
# # # #         self.next = None

# # # # # Function to add a node to the linked list
# # # # def add_node(head, data):
# # # #     new_node = Node(data)
    
# # # #     if head is None:
# # # #         head = new_node
# # # #     else:
# # # #         current = head
# # # #         while current.next is not None:
# # # #             current = current.next
# # # #         current.next = new_node
    
# # # #     return head

# # # # # Function to visualize the array of linked lists
# # # # def visualize_linked_lists(linked_lists):
# # # #     fig = go.Figure()

# # # #     # Create nodes and edges for each linked list
# # # #     y = 0  # y-coordinate for positioning nodes
# # # #     for i, linked_list in enumerate(linked_lists):
# # # #         current = linked_list
# # # #         x = 0  # x-coordinate for positioning nodes
# # # #         while current is not None:
# # # #             fig.add_trace(go.Scatter(
# # # #                 x=[x],
# # # #                 y=[y],
# # # #                 mode='markers+text',
# # # #                 marker=dict(size=20, color='lightblue'),
# # # #                 text=[f" {current.data}"],
# # # #                 textposition='middle center',
# # # #                 hoverinfo='text',
# # # #                 hovertext=[f"{current.data}"],
# # # #             ))
# # # #             if current.next is not None:
# # # #                 fig.add_trace(go.Scatter(
# # # #                     x=[x, x + 1],
# # # #                     y=[y, y],
# # # #                     mode='lines',
# # # #                     line=dict(color='gray', width=1),
# # # #                     hoverinfo='none',
# # # #                 ))
# # # #             current = current.next
# # # #             x += 1

# # # #         y -= 1

# # # #     # Configure layout
# # # #     fig.update_layout(
# # # #         title="Array of Linked Lists",
# # # #         showlegend=False,
# # # #         hovermode='closest',
# # # #         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
# # # #         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
# # # #     )

# # # #     # Show the figure
# # # #     fig.show()

# # # # # Example usage
# # # # array_of_lists = []

# # # # # Create three linked lists
# # # # linked_list1 = None
# # # # linked_list1 = add_node(linked_list1, 1)
# # # # linked_list1 = add_node(linked_list1, 2)
# # # # linked_list1 = add_node(linked_list1, 3)

# # # # linked_list2 = None
# # # # linked_list2 = add_node(linked_list2, 4)
# # # # linked_list2 = add_node(linked_list2, 5)
# # # # linked_list2 = add_node(linked_list2, 6)

# # # # linked_list3 = None
# # # # linked_list3 = add_node(linked_list3, 7)
# # # # linked_list3 = add_node(linked_list3, 8)
# # # # linked_list3 = add_node(linked_list3, 9)

# # # # # Add the linked lists to the array
# # # # array_of_lists.append(linked_list1)
# # # # array_of_lists.append(linked_list2)
# # # # array_of_lists.append(linked_list3)
# # # # array_of_lists.append(linked_list3)
# # # # # Visualize the array of linked lists
# # # # visualize_linked_lists(array_of_lists)



























# # # import plotly.graph_objects as go

# # # # Define the linked list node structure
# # # class Node:
# # #     def __init__(self, data=None):
# # #         self.data = data
# # #         self.next = None

# # # # Function to add a node to the linked list
# # # def add_node(head, data):
# # #     new_node = Node(data)
    
# # #     if head is None:
# # #         head = new_node
# # #     else:
# # #         current = head
# # #         while current.next is not None:
# # #             current = current.next
# # #         current.next = new_node
    
# # #     return head

# # # # Function to visualize the array of linked lists
# # # def visualize_linked_lists(linked_lists):
# # #     fig = go.Figure()

# # #     # Create nodes and edges for each linked list
# # #     y = 0  # y-coordinate for positioning nodes
# # #     for i, linked_list in enumerate(linked_lists):
# # #         current = linked_list
# # #         x = 0  # x-coordinate for positioning nodes
# # #         while current is not None:
# # #             fig.add_trace(go.Scatter(
# # #                 x=[x],
# # #                 y=[y],
# # #                 mode='markers+text',
# # #                 marker=dict(size=10, color='lightblue'),
# # #                 text=[f"List {i+1}: {current.data}"],
# # #                 textposition='middle center',
# # #                 hoverinfo='text',
# # #                 hovertext=[f"List {i+1}: {current.data}"],
# # #             ))
# # #             if current.next is not None:
# # #                 fig.add_trace(go.Scatter(
# # #                     x=[x, x + 1],
# # #                     y=[y, y],
# # #                     mode='lines',
# # #                     line=dict(color='gray', width=1),
# # #                     hoverinfo='none',
# # #                 ))
# # #             current = current.next
# # #             x += 1

# # #         fig.add_annotation(
# # #             x=(x-1) / 2,  # x-coordinate for the text box
# # #             y=y,
# # #             text=f"List {i+1}",
# # #             showarrow=False,
# # #             font=dict(color='black', size=12),
# # #         )

# # #         y -= 1

# # #     # Configure layout
# # #     fig.update_layout(
# # #         title="Array of Linked Lists",
# # #         showlegend=False,
# # #         hovermode='closest',
# # #         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
# # #         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
# # #     )

# # #     # Show the figure
# # #     fig.show()

# # # # Example usage
# # # array_of_lists = []

# # # # Create three linked lists
# # # linked_list1 = None
# # # linked_list1 = add_node(linked_list1, 1)
# # # linked_list1 = add_node(linked_list1, 2)
# # # linked_list1 = add_node(linked_list1, 3)

# # # linked_list2 = None
# # # linked_list2 = add_node(linked_list2, 4)
# # # linked_list2 = add_node(linked_list2, 5)
# # # linked_list2 = add_node(linked_list2, 6)

# # # linked_list3 = None
# # # linked_list3 = add_node(linked_list3, 7)
# # # linked_list3 = add_node(linked_list3, 8)
# # # linked_list3 = add_node(linked_list3, 9)

# # # # Add the linked lists to the array
# # # array_of_lists.append(linked_list1)
# # # array_of_lists.append(linked_list2)
# # # array_of_lists.append(linked_list3)

# # # # Visualize the array of linked lists
# # # visualize_linked_lists(array_of_lists)
































# # import plotly.graph_objects as go

# # # Define the linked list node structure
# # class Node:
# #     def __init__(self, data=None):
# #         self.data = data
# #         self.next = None

# # # Function to add a node to the linked list
# # def add_node(head, data):
# #     new_node = Node(data)
    
# #     if head is None:
# #         head = new_node
# #     else:
# #         current = head
# #         while current.next is not None:
# #             current = current.next
# #         current.next = new_node
    
# #     return head

# # # Function to visualize the array of linked lists
# # def visualize_linked_lists(linked_lists):
# #     fig = go.Figure()

# #     # Create nodes and edges for each linked list
# #     y = 0  # y-coordinate for positioning nodes
# #     for i, linked_list in enumerate(linked_lists):
# #         current = linked_list
# #         x = 0  # x-coordinate for positioning nodes
# #         while current is not None:
# #             fig.add_trace(go.Scatter(
# #                 x=[x],
# #                 y=[y],
# #                 mode='markers+text',
# #                 marker=dict(size=10, color='lightblue'),
# #                 text=[f"List {i+1}: {current.data}"],
# #                 textposition='middle center',
# #                 hoverinfo='text',
# #                 hovertext=[f"List {i+1}: {current.data}"],
# #             ))
# #             if current.next is not None:
# #                 fig.add_trace(go.Scatter(
# #                     x=[x, x + 1],
# #                     y=[y, y],
# #                     mode='lines',
# #                     line=dict(color='gray', width=1),
# #                     hoverinfo='none',
# #                 ))
# #             current = current.next
# #             x += 1

# #         fig.add_shape(
# #             type='rect',
# #             x0=x,  # x-coordinate for the square
# #             y0=y-0.4,  # y-coordinate for the square
# #             x1=x+0.4,  # x-coordinate for the opposite corner of the square
# #             y1=y+0.4,  # y-coordinate for the opposite corner of the square
# #             line=dict(color='black', width=2),
# #             fillcolor='white',
# #             layer='below',
# #         )

# #         fig.add_annotation(
# #             x=x+0.2,  # x-coordinate for the text in the square
# #             y=y,
# #             text=f"List {i+1}",
# #             showarrow=False,
# #             font=dict(color='black', size=12),
# #         )

# #         y -= 1

# #     # Configure layout
# #     fig.update_layout(
# #         title="Array of Linked Lists",
# #         showlegend=False,
# #         hovermode='closest',
# #         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
# #         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
# #     )

# #     # Show the figure
# #     fig.show()

# # # Example usage
# # array_of_lists = []

# # # Create three linked lists
# # linked_list1 = None
# # linked_list1 = add_node(linked_list1, 1)
# # linked_list1 = add_node(linked_list1, 2)
# # linked_list1 = add_node(linked_list1, 3)

# # linked_list2 = None
# # linked_list2 = add_node(linked_list2, 4)
# # linked_list2 = add_node(linked_list2, 5)
# # linked_list2 = add_node(linked_list2, 6)

# # linked_list3 = None
# # linked_list3 = add_node(linked_list3, 7)
# # linked_list3 = add_node(linked_list3, 8)
# # linked_list3 = add_node(linked_list3, 9)

# # # Add the linked lists to the array
# # array_of_lists.append(linked_list1)
# # array_of_lists.append(linked_list2)
# # array_of_lists.append(linked_list3)

# # # Visualize the array of linked lists
# # visualize_linked_lists(array_of_lists)

























# import plotly.graph_objects as go
# from quicksort import *
# import time
# import numpy as np
# import streamlit as st
# # Define the linked list node structure
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# # Function to add a node to the linked list
# def add_node(head, data):
#     new_node = Node(data)
    
#     if head is None:
#         head = new_node
#     else:
#         current = head
#         while current.next is not None:
#             current = current.next
#         current.next = new_node
    
#     return head

# # Function to visualize the array of linked lists
# def visualize_linked_lists(linked_lists):
#     fig = go.Figure()

#     # Create nodes and edges for each linked list
#     y = 0  # y-coordinate for positioning nodes
#     for i, linked_list in enumerate(linked_lists):
        
#         x = 0  # x-coordinate for positioning nodes
        
#         fig.add_shape(
#             type='rect',
#             x0=-0.4,  # x-coordinate for the square
#             y0=y-0.4,  # y-coordinate for the square
#             x1=0,  # x-coordinate for the opposite corner of the square
#             y1=y+0.4,  # y-coordinate for the opposite corner of the square
#             line=dict(color='black', width=2),
#             fillcolor='white',
#             layer='below',
#         )

#         fig.add_annotation(
#             x=-0.2,  # x-coordinate for the text in the square
#             y=y,
#             text=f"{i+1}",
#             showarrow=False,
#             font=dict(color='black', size=12),
#             align='right'
#         )
        
#         x += 1  # Increment x-coordinate for node positioning
        
#         for i in range(len(linked_list)):
#             fig.add_trace(go.Scatter(
#                 x=[x],
#                 y=[y],
#                 mode='markers+text',
#                 marker=dict(size=25, color='blue'),
#                 text=[f"{linked_list[i]}"],
#                 textposition='middle center',
#                 hoverinfo='text',
#                 hovertext=[f"List {i+1}: {linked_list[i]}"],
#             ))
#             if i!= len(linked_list)-1:
#                 fig.add_trace(go.Scatter(
#                     x=[x, x + 1],
#                     y=[y, y],
#                     mode='lines',
#                     line=dict(color='gray', width=1),
#                     hoverinfo='none',
#                 ))
            
#             x += 1

#         y -= 1

#     # Configure layout
#     fig.update_layout(
#         title="Array of Linked Lists",
#         showlegend=False,
#         hovermode='closest',
#         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#     )

#     # Show the figure
#     return fig
# def vis_quick_sort(x,lst):
    
#     frames=[lst.copy()]
#     figures=[]
#     quick_sort(lst,0,len(lst)-1,frames)
    
#     for i in frames:
#         figures.append(px.bar(x=x, y=i))
    
#     return figures
# # Example usage
# def bucket_sort(nb,l):
#     bucket=[]
#     for i in range(nb+1):
#         bucket.append([])
    
#     max=l[0]
#     for i in l:
#         if i>max:
#             max=i;
#     indexfactor=(nb)/max
#     frames=[]
#     for i in l:
#         indx=int(i*indexfactor)
#         print(bucket)
#         bucket[indx].append(i)
#         frames.append(visualize_linked_lists(bucket))
#     for i in bucket:
#         sz=len(i)
#         if sz!=0:
#             x=np.arange(0,sz,1)
#             frames.extend(vis_quick_sort(x,i))
#         frames.append(visualize_linked_lists(bucket))
#         figure=frames[0]
#     return frames
            
    
# plot_spot = st.empty()
# l=[503,32,12,4213,213,23,31]
# fig,frames=bucket_sort(10,l)
# for frame in frames:
#     with plot_spot:
#         st.plotly_chart(frame[0])
#     time.sleep(1)
# # Create three linked lists
import plotly.graph_objects as go
from quicksort import *
import time
import numpy as np
import streamlit as st
st.set_page_config(layout='wide')
# Define the linked list node structure
class Node:
    def _init_(self, data=None):
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
            y0=y-0.4,  # 
            x1=0, 
            y1=y+0.4,  
            line=dict(color='black', width=2),
            fillcolor='white',
            layer='below',
        )

        fig.add_annotation(
            x=-0.2,  # x-coordinate for the text in the square
            y=y,
            text=f"Bucket {i+1}",
            showarrow=False,
            font=dict(color='black', size=12),
            align='right'
        )
        
        x += 1  # Increment x-coordinate for node positioning
        
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
def vis_quick_sort(x,lst):
    
    frames=[lst.copy()]
    figures=[]
    quick_sort(lst,0,len(lst)-1,frames)
    
    for i in frames:
        figures.append([px.bar(x=x, y=i),'Q'])
    
    return figures
# Example usage
def bucket_sort(nb,l):
    bucket=[]
    for i in range(nb+1):
        bucket.append([])
    
    max=l[0]
    for i in l:
        if i>max:
            max=i;
    indexfactor=(nb)/max
    frames=[]
    #frames.append(bucket)
    for i in l:
        indx=int(i*indexfactor)
        
        bucket[indx].append(i)
        frames.append([visualize_linked_lists(bucket),'B'])
    array=[]
    for i in bucket:
        sz=len(i)
        if sz!=0:
            x=np.arange(0,sz,1)
            frames.extend(vis_quick_sort(x,i))
            for j in i:
                array.append(j)
                frames.append([array.copy(),'L'])
            frames.append([visualize_linked_lists(bucket),'B'])
    
    return frames
            
    
plot_spot = st.empty()
l=[503,32,12,4213,213,23,31]
frames=bucket_sort(10,l)
text_holder=st.empty()

for frame in frames:
        

     with plot_spot:
            col1,col2=st.columns(2)
            if(frame[1]=='Q'):
                
                    with col2:
                        st.plotly_chart(frame[0])
            elif(frame[1]=='B'):
                    with col1:
                        st.plotly_chart(frame[0])
            else:
                    with text_holder:
                        st.text_area("List",frame[0])
            time.sleep(1)
            
# Create three linked lists