import plotly.express as px
import streamlit as st
import pandas as pd

def selection_sort(lst):
    n = len(lst)
    frames = []

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                frames.append(lst.copy())

    return frames

def visualise_selection_sort(x,lst):
    frames = selection_sort(lst)
    figure = px.bar(x=x, y=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n ^ 2)', 'O(n)', 'O(n ^ 2)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_selection():
    st.sidebar.dataframe(complexity_df,hide_index=True)
