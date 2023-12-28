import streamlit as st
import numpy as np
from time import time
from codeexplaination import *
import plotly.express as px
st.set_page_config(layout='wide',
                   initial_sidebar_state=st.session_state.get('sidebar_state','expanded'))

st.sidebar.title("Select sorting type")
sortingOption = st.sidebar.selectbox("Sorting Algoritms", options=["Selection Sort","Bubble Sort","Merge Sort", "Quick Sort", "Insertion Sort","Heap Sort","Comb Sort","Bucket Sort"])
st.title(f"{sortingOption} Visualisation")
amount = 0

if sortingOption != "Heap Sort" and sortingOption != "Bucket Sort":
    amount = st.slider("Select number of elements", min_value=5, max_value=100)
col1,col3 = st.columns([3,1])

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)
with col3:
    cont = st.container(border=True)
    with cont:
        speed = st.slider("Speed",0,100,50)
with col1:
    figure,frames=show_visualisation_and_complexity(sortingOption,x,lst,speed)  
    if figure is not None:        
        figure.update_layout(showlegend=False)
        figure.update_xaxes(visible=False)
        figure.update_yaxes(visible=False)
        plot_spot = st.empty()
        with plot_spot:
                    st.plotly_chart(figure)
        with cont:
            play_button = st.button(f"{sortingOption}",key=f"{0}")

        if play_button:
            for frame in frames[1:]:
                figure = px.bar(x=x, y=frame,color=frame)
                figure.update_layout(showlegend=False)
                figure.update_xaxes(visible=False)
                figure.update_yaxes(visible=False)
                time.sleep(1 - speed/100)
                with plot_spot:
                    st.plotly_chart(figure)
try:
    show_code_and_explaination(sortingOption)
except Exception as e:
    print(e)
