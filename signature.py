import pandas as pd
import streamlit as st
from imageconverter import img_to_bytes
def show_signatures():

    data = {
        'Contributions': ['Bola Yosry', 'Mohamed Alaa', 'Omar Rushdy', 'Omar Walid'],
        # 'ID': ['21-101147', '21-101142', '21-101051', '21-101031']
    }

    df = pd.DataFrame(data)
    st.sidebar.write(img_to_bytes("images/eui.png"), unsafe_allow_html=True)
    st.sidebar.divider()        
    st.sidebar.dataframe(df,hide_index=True,use_container_width=True)
