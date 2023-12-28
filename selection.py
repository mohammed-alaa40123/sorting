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
    figure = px.bar(x=x, y=frames[0],color=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n ^ 2)', 'O(n ^ 2)', 'O(n ^ 2)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_selection():
    st.sidebar.dataframe(complexity_df,hide_index=True)


def show_selection_code(lang):
    if lang == "Python":
        code = """
\ndef selection_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
        """
    elif lang == "CPP":
        code = """
\nvoid swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n) {
    int i, j, min_idx;

    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        swap(&arr[min_idx], &arr[i]);
    }
}
"""

    else:
        code="""
\nvoid selectionSort(int arr[])
{
    int n = arr.length;

    for (int i = 0; i < n-1; i++)
    {
        int min_idx = i;
        for (int j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
""" 
    return code


def show_selection_explaination():
    content =  """<div><article>
<p>The selection sort algorithm is a simple, yet effective sorting algorithm. A selection-based sorting algorithm is described as an in-place comparison-based algorithm that divides the list into two parts, the sorted part on the left and the unsorted part on the right. Initially, the sorted section is empty, and the unsorted section contains the entire list. When sorting a small list, selection sort can be used.</p>
<p>In the selection sort, the cost of swapping is irrelevant, and all elements must be checked. The cost of writing to memory matters in selection sort, just as it does in flash memory (the number of writes/swaps is O(n) as opposed to O(n2) in bubble sort).</p>
<h2>What Is a Selection Sort Algorithm?</h2>
<ul>
<li>Selection sort is an effective and efficient sort algorithm based on comparison operations.</li>
<li>It adds one element in each iteration.</li>
<li>You need to select the smallest element in the array and move it to the beginning of the array by swapping with the front element.</li>
<li>You can also accomplish this by selecting the most potent element and positioning it at the back end.</li>
<li>In each iteration, selection sort selects an element and places it in the appropriate position.</li>
</ul>
<h2>The Complexity of Selection Sort Algorithm</h2>
<p>The time complexity of the selection sort algorithm is:</p>
<ul>
<li>The selection sort algorithm is made up of two nested loops.</li>
<li>It has an O (n2) time complexity due to the two nested loops.</li>
</ul>
<p>Best Case Complexity occurs when there is no need for sorting, i.e., the array has already been sorted. The time complexity of selection sort in the best-case scenario is O(n2).</p>
<p>Average Case Complexity occurs when the array elements are arranged in a jumbled order that is neither ascending nor descending correctly. The selection sort has an average case time complexity of O(n2).</p>
<p>Worst-case complexity - Worst case occurs when array elements must be sorted in reverse order. Assume you need to sort the array elements in ascending order, but they are in descending order. Selection sort has a worst-case time complexity of O(n2).</p>
<p>The space complexity of the selection sort algorithm is:</p>
<ul>
<li>An in-place algorithm is a selection sort algorithm.</li>
<li>It performs all computations in the original array and does not use any other arrays.</li>
<li>As a result, the space complexity is O(1).</li>
</ul>
<p>You will now look at some applications of the selection sort algorithm in this tutorial.</p>
<h2>Applications of Selection Sort Algorithm</h2>
<p>The following are some applications of how to use selection sort:</p>
<ul>
<li>Selection sort consistently outperforms bubble and gnome sort.</li>
<li>When memory writing is a costly operation, this can be useful.</li>
<li>In terms of the number of writes ((n) swaps versus O(n2) swaps), selection sort is preferable to insertion sort.</li>
<li>It almost always far outnumbers the number of writes made by cycle sort, even though cycle sort is theoretically optimal in terms of the number of writes.</li>
<li>This is important if writes are significantly more expensive than reads, as with EEPROM or Flash memory, where each write reduces the memory's lifespan.</li>
</ul>
</article>
</div>"""
    st.markdown(content,unsafe_allow_html=True)
    st.link_button("For More info", "https://www.geeksforgeeks.org/selection-sort/")

