import plotly.express as px
import streamlit as st
import pandas as pd


def comb_sort (lst) :
    size = len(lst)
    frames = []

    gap = size

    swapped = True

    while swapped == True or gap != 1 :

        gap = (gap * 10)/13
        if gap < 1 :
            gap = 1

        swapped = False

        for i in range(0, size-gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap]=lst[i + gap], lst[i]
                swapped = True

    frames.append(lst)

    return frames


def visualise_comb_sort(x,lst):
    frames = comb_sort(lst)
    figure = px.bar(x=x, y=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n^2)', 'O(n)', 'O(n^2)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_comb():
    st.sidebar.dataframe(complexity_df,hide_index=True)