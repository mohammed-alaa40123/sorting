from imageconverter import *
from selection import *
from heap import *
from bubble import *
from bucket import *
from insertion import *
from merge import *
from quicksort import *
from comb import *
# Create a mapping between sorting options and the corresponding show_code functions
sorting_options_mapping = {
    "Selection Sort": show_selection_code,
    # "Bubble Sort": show_bubble_sort_code,
    # "Insertion Sort": show_insertion_sort_code,
    # "Merge Sort": show_merge_sort_code,
    # "Heap Sort": show_heap_sort_code,
    # "Bucket Sort": show_bucket_sort_code,
    # "Quick Sort": show_quick_sort_code,
    # "Comb Sort": show_comb_sort_code,
}
def show_code(sortingOption):

    selected_show_code_function = sorting_options_mapping[sortingOption]
 
    tab1, tab2, tab3 = st.tabs(["Python", "CPP", "Java"])
    with tab1:
        col1,col2 = st.columns(2)
        with col1:
            st.code(selected_show_code_function("Python"), language='python')
        with col2:
            st.markdown(img_to_bytes("images/python.jpg"), unsafe_allow_html=True)
        
    with tab2:
        col1,col2 = st.columns(2)
        with col1:
            st.code(selected_show_code_function("CPP"), language="cpp")
        with col2:
            st.markdown(img_to_bytes("images/cpp.png"), unsafe_allow_html=True)
    with tab3:
        col1,col2 = st.columns(2)

        with col1:
            st.code(selected_show_code_function("Java"), language='java')
        with col2:
            st.markdown(img_to_bytes("images/java.png"), unsafe_allow_html=True)
