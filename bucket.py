import plotly.graph_objects as go
from quicksort import *
import time
import numpy as np
import streamlit as st
#st.set_page_config(layout='wide')




# Function to visualize the array of linked lists
def visualize_linked_lists(linked_lists,length):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
                x=[45],
                y=[1],
                
                marker=dict(size=25, color='black'),
                
                
                
                
            ))
    
    y = 0  
    for i, linked_list in enumerate(linked_lists):
        
        x = 0  
        
        fig.add_shape(
            type='rect',
            x0=-5,
            y0=y-0.4,  
            x1=1.5, 
            y1=y+0.4,  
            line=dict(color='black', width=2),
            fillcolor='red',
            layer='below',
        )

        fig.add_annotation(
            x=-3,  # x-coordinate for the text in the square
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
                marker=dict(size=10, color='blue'),
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
def vis_quick_sort(x,lst,ind):
   
    frames=[lst.copy()]
    figures=[]
    quick_sort(lst,0,len(lst)-1,frames)
    
    for i in frames:
        figures.append([px.bar(x=x, y=i,title=f"Sorting Bucket #{ind}"),'Q'])
    
    return figures

def bucket_sort(nb,l):
    length=len(l)
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
        frames.append([visualize_linked_lists(bucket,length),'B'])
    array=[]
    index=0
    for i in bucket:
        index=index+1
        sz=len(i)
        if sz!=0:
            x=np.arange(0,sz,1)
            frames.extend(vis_quick_sort(x,i,index))
            for j in i:
                array.append(j)
                frames.append([array.copy(),'L'])
            frames.append([visualize_linked_lists(bucket,length),'B'])
    
    return frames
            
def mainbucket():   
    plot_spot = st.empty()
    l=st.text_input("Enter the elements of the list:")
    l= list(map(int, l.split()))
    np=st.text_input("Enter number of buckets:")
    
    
    
    text_holder=st.empty()
    if st.button("Bucket Sort"):
        frames=bucket_sort(int(np)-1,l)
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
                    time.sleep(0.2)