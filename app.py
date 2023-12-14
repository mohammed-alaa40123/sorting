import streamlit as st
import numpy as np
from selection import *
import plotly.express as px

st.title("Bubble Sort Animation with Streamlit")
st.sidebar.title("Select sorting type")
sortingOption = st.sidebar.selectbox("Sorting Algoritms", options=["Selection Sort","Bubble Sort", "Quick Sort"])
amount = st.slider("Select number of elements", min_value=5, max_value=100)

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

if sortingOption == "Selection Sort":
    figure,frames=visualise_selection_sort(x,lst)
    show_complexity_selection()

    
plot_spot = st.empty()
with plot_spot:
            st.plotly_chart(figure)

play_button = st.button("Sort")

if play_button:
    for frame in frames[1:]:
        figure = px.bar(x=x, y=frame)
        with plot_spot:
            st.plotly_chart(figure)

       

        
    

