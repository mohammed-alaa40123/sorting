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
    figure = px.bar(x=x, y=frames[0],color=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n ^ 2)', 'O(n)', 'O(n ^ 2)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_bubble():
    st.sidebar.dataframe(complexity_df,hide_index=True)



def show_bubble_code(lang):
    if lang == "Python":
        code = """
\ndef bubble_sort(lst):
    n = len(lst)
    sorted=False
    
    for i in range(n):
        if not sorted:
            sorted=True
            for j in range(i+1, n ):
                if lst[j] < lst[i]:
                    sorted=False
                    lst[j], lst[i] = lst[i], lst[j]
        """
    elif lang == "CPP":
        code = """
\nvoid bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    bool sorted = false;

    for (int i = 0; i < n; ++i) {
        if (!sorted) {
            sorted = true;
            for (int j = i + 1; j < n; ++j) {
                if (arr[j] < arr[i]) {
                    sorted = false;
                    std::swap(arr[j], arr[i]);
                }
            }
        }
    }
}
"""

    else:
        code="""
\npublic class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean sorted = false;

        for (int i = 0; i < n; ++i) {
            if (!sorted) {
                sorted = true;
                for (int j = i + 1; j < n; ++j) {
                    if (arr[j] < arr[i]) {
                        sorted = false;
                        int temp = arr[j];
                        arr[j] = arr[i];
                        arr[i] = temp;
                    }
                }
            }
        }
    }
}
""" 
    return code


def show_bubble_explaination():
    content =  """<div><article>
    
    
<h2>What Is a Bubble Sort Algorithm?</h2>

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. As a fun fact it is called bubble sort because it treats every two adjacent elements as bubbles and sorts them. This sorting technique is mostly used for educational purposes due to its simplicity.


<h2>The Complexity of Bubble Sort Algorithm</h2>
It is always O(n^2) since it has nested loops and iterates over them. However, with a simple optimization where there isn't any swaps taking place it becomes O(n) due to a simple if condition.
<p>The time complexity of the selection sort algorithm is:</p>

<h3>Best Use Cases:</h3>

Bubble Sort is a simple sorting algorithm that works well for small datasets.
It is easy to understand and implement, making it suitable for educational purposes and scenarios where simplicity is a priority.
Bubble Sort is not the most efficient sorting algorithm for large datasets, as its time complexity is O(n^2) in the worst case.
When to Use:

Use Bubble Sort when dealing with small datasets or when simplicity is more important than efficiency.
Avoid using Bubble Sort for large datasets or real-world applications where faster sorting algorithms (e.g., QuickSort or MergeSort) would be more suitable.
Overall:
Bubble Sort is a basic sorting algorithm that is easy to understand but not the most efficient for large datasets. It serves as a good introductory algorithm for learning sorting concepts. However, in practical applications, more efficient algorithms are often preferred.

"""
    st.markdown(content,unsafe_allow_html=True)
    st.link_button("For More info", "https://www.geeksforgeeks.org/bubble-sort/")