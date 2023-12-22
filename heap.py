import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd
import sys 
  
class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        return pos*2 > self.size 
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
 
    
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
def heap_to_tree(h):
    G=nx.Graph()
    print(h.Heap)
    array2=[-1]
    color_map=[]
    for i in range(1,h.size+1):
        if(i>1):
            color_map.append('skyblue')
        else:
            color_map.append('red')
        G.add_node(h.Heap[i])
        array2.append(h.Heap[i])
    print(array2)
    for i in range(1,len(array2)):
        if(2*i<len(array2)):
            G.add_edge(array2[i],array2[2*i])
        if(2*i+1<len(array2)):
            G.add_edge(array2[i],array2[2*i+1])
            
    return G,color_map
def visualize_heap(h):
    G,color_map=heap_to_tree(h)
    pos = nx.spring_layout(G)  # You can change the layout algorithm as needed
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=color_map, font_size=10, font_color='black', font_weight='bold', arrows=False)
    plt.show() 
# Example tree creation

def visualize_heap_sort(x,lst):
    frames=[]
    heap_frames=[]
    sz=len(lst)
    mh=MinHeap(sz)
    heap_figure=visualize_heap(mh)
    frames.append(lst.copy())
    for i in lst:
        mh.insert(i)
        lst.pop(0)
        frames.append(lst)
        heap_frames.append(mh.copy())
    for i in lst:
        lst.append(mh.remove())
        frames.append(lst)
        heap_frames.append(mh)
    figure=px.bar(x=x, y=frames[0])
    return figure,heap_figure,frames,heap_frames
        
data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n × log n)', 'O(n × log n)', 'O(n × log n)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_selection():
    st.sidebar.dataframe(complexity_df,hide_index=True)
print("hello")
