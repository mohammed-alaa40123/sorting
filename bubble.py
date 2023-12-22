import plotly.express as px
import streamlit as st
import pandas as pd

def bubble_sort(lst):
    n = len(lst)
    frames = []
    sorted=False
    
    for i in range(n):
        if not sorted:
            sorted=True
            for j in range(i+1, n ):
                if lst[j] < lst[i]:
                    sorted=False
                    lst[j], lst[i] = lst[i], lst[j]
                    frames.append(lst.copy())

    return frames

def visualise_bubble_sort(x,lst):
    frames = bubble_sort(lst)
    figure = px.bar(x=x, y=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n ^ 2)', 'O(n)', 'O(n ^ 2)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_bubble():
    st.sidebar.dataframe(complexity_df,hide_index=True)
