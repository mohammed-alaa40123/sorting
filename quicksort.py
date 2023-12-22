
import plotly.express as px
import streamlit as st
import pandas as pd

def quick_sort(lst, low, high, frames):
    
   
    if low < high:
      
        pivot,l = partition(lst, low, high)
        frames.extend(l)
        
        quick_sort(lst, low, pivot - 1,frames)
        quick_sort(lst, pivot + 1, high, frames)
        frames.append(lst.copy())
       
 
     

def partition(lst, low, high):
    frames = []
    pivot = lst[high]
    
    i = low - 1
   
    for j in range(low, high):
        
        
        if lst[j] <= pivot:
           
            i += 1
            
            lst[i], lst[j] = lst[j], lst[i]
            frames.append(lst.copy())
   
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    frames.append(lst.copy())
    return i + 1, frames

def visualise_quick_sort(x,lst):

    frames=[lst.copy()]
    
    quick_sort(lst,0,len(lst)-1,frames)
    print(frames)
    figure = px.bar(x=x, y=frames[0])
    
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n × log n)', 'O(n × log n)', 'O(n^2)', 'O(logn)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_quicksort():
    st.sidebar.dataframe(complexity_df,hide_index=True)