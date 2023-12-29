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
    "Selection Sort": (show_selection_code,show_selection_explaination,visualise_selection_sort,show_complexity_selection),
    "Bubble Sort": (show_bubble_code,show_bubble_explaination,visualise_bubble_sort,show_complexity_bubble),
    "Insertion Sort": (show_insertion_code,show_insertion_explaination,visualise_insertion_sort,show_complexity_insertion),
    "Merge Sort": (show_merge_code,show_merge_explaination,visualize_mergesort,show_complexity_merge), 
    # "Heap Sort": (show_heap_code,show_heap_explaination,mainheap,show_complexity_heap),   
    "Bucket Sort": (show_bucket_code,show_bucket_explaination,mainbucket,show_complexity_bucket),
    "Quick Sort": (show_quick_code,show_quick_explaination,visualise_quick_sort,show_complexity_quicksort),
    "Comb Sort": (show_comb_code,show_comb_explaination,visualise_comb_sort,show_complexity_comb),
}
def show_visualisation_and_complexity(sortingOption,x,lst,speed=70):
    figure=frames=None
    visualise_sort = sorting_options_mapping[sortingOption][2]
    show_complexity = sorting_options_mapping[sortingOption][3]
    show_complexity()    
    if sortingOption == "Bucket Sort" or sortingOption == "Heap Sort":
        visualise_sort(speed)
    else:    
        figure,frames=visualise_sort(x,lst)
    return figure,frames
        

def show_code_and_explaination(sortingOption):
    
    try:
        selected_show_code_function = sorting_options_mapping[sortingOption][0]
        selected_show_explaination = sorting_options_mapping[sortingOption][1]
        st.header("Description")            
        selected_show_explaination()
        tab1, tab2, tab3 = st.tabs(["Python", "CPP", "Java"])
        with tab1:
            col1,col2 = st.columns(2)
            with col1:
                st.code(selected_show_code_function("Python"), language='python')
            with col2:
                st.write(img_to_bytes("images/python.jpg"), unsafe_allow_html=True)
            
        with tab2:
            col1,col2 = st.columns(2)
            with col1:
                st.code(selected_show_code_function("CPP"), language="cpp")
            with col2:
                st.write(img_to_bytes("images/cpp.png"), unsafe_allow_html=True)
        with tab3:
            col1,col2 = st.columns(2)

            with col1:
                st.code(selected_show_code_function("Java"), language='java')
            with col2:
                st.write(img_to_bytes("images/java.png"), unsafe_allow_html=True)
    except Exception as e:
        print(e)