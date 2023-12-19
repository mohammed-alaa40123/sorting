import plotly.express as px
import streamlit as st
import pandas as pd

def insertion_sort (lst):
    size = len(lst)
    frames = []

    for x in range (size):
        start = lst[x]
        j = x-1

        while (start < lst[x] & start >= 0):
            lst[j+1] = lst[j]
            j -= 1
            lst[j+1] = start
            frames.append(lst.copy())
            
    return frames
        


def visualise_insertion_sort(x,lst):
    frames = insertion_sort(lst)
    figure = px.bar(x=x, y=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n × log n)', 'O(n × log n)', 'O(n × log n)', 'O(n)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_selection():
    st.sidebar.dataframe(complexity_df,hide_index=True)
