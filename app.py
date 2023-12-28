import streamlit as st
import numpy as np
from time import time
from codeexplaination import *
from selection import *
from heap import *
from bubble import *
from bucket import *
from insertion import *
from merge import *
from quicksort import *
from comb import *
import plotly.express as px

st.sidebar.title("Select sorting type")
sortingOption = st.sidebar.selectbox("Sorting Algoritms", options=["Selection Sort","Bubble Sort","Merge Sort", "Quick Sort", "Insertion Sort","Heap Sort","Comb Sort","Bucket Sort"])
st.title(f"{sortingOption} Visualisation")
amount = 0
if sortingOption != "Heap Sort" and sortingOption != "Bucket Sort":
    amount = st.slider("Select number of elements", min_value=5, max_value=100)

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

if sortingOption == "Selection Sort":
    figure,frames=visualise_selection_sort(x,lst)
    show_complexity_selection()
if sortingOption == "Bubble Sort":
    figure,frames=visualise_bubble_sort(x,lst)
    show_complexity_bubble()

if sortingOption == "Insertion Sort":
    figure,frames=visualise_insertion_sort(x,lst)
    show_complexity_insertion()

if sortingOption == "Merge Sort":
    figure,frames=visualize_mergesort(x,lst)
    show_complexity_insertion()

if sortingOption == "Heap Sort":
    mainheap()
    show_complexity_heap()
    st.stop()
if sortingOption == "Bucket Sort":
    mainbucket()
    st.stop()
    
if sortingOption == "Quick Sort":
    figure,frames=visualise_quick_sort(x,lst)
    show_complexity_quicksort()   

if sortingOption == "Comb Sort":
    figure,frames=visualise_comb_sort(x,lst)
    show_complexity_comb()     
    
figure.update_layout(showlegend=False)
figure.update_xaxes(visible=False)
figure.update_yaxes(visible=False)
plot_spot = st.empty()
with plot_spot:
            st.plotly_chart(figure)

play_button = st.button(f"{sortingOption}")

if play_button:
    for frame in frames[1:]:
        figure = px.bar(x=x, y=frame)
        figure.update_layout(showlegend=False)
        figure.update_xaxes(visible=False)
        figure.update_yaxes(visible=False)
        time.sleep(0.2)
        with plot_spot:
            st.plotly_chart(figure)
            
st.header("Description")            
show_selection_explaination()
show_code(sortingOption)
