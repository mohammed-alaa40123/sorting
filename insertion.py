import plotly.express as px
import streamlit as st
import pandas as pd

def insertion_sort (lst):
    size = len(lst)
    frames = []

    for x in range (1,size):
        start = lst[x]
        j = x-1

        while start < lst[j] and j >= 0 :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = start
        frames.append(lst.copy())

    return frames
        


def visualise_insertion_sort(x,lst):
    frames = insertion_sort(lst)
    figure = px.bar(x=x, y=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n^2)', 'O(n)', 'O(n^2)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_insertion():
    st.sidebar.dataframe(complexity_df,hide_index=True)


def show_insertion_code(lang):
    if lang == "Python":
        code = """
\n def insertion_sort (lst):
    size = len(lst)

    for x in range (1,size):
        start = lst[x]
        j = x-1

        while start < lst[j] and j >= 0 :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = start

    return lst
    """
    elif lang == "CPP":
        code = """
\n void insertionSort(vector<int> &arr) {
    int n = arr.size();
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
""" 

    else:
        code = """
\n public class InsertionSort {
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
"""
    return code 

def show_insertion_explaination():
    content =  """<div><article>
    <p>Indeed, insertion sort operates much like arranging a hand of playing cards.The array gets divided into two segments: a sorted section and an unsorted section.</p>
    <p>Elements from the unsorted part are chosen and inserted into the appropriate position within the sorted segment.This process continues until all elements are in their correct order. </p>
    <h2>What Is a insertion Sort Algorithm?</h2>
    <ul>
    <li>Begins with the first element considered as the sorted part and the rest as unsorted.</li>
    <li>Iterates through the unsorted section, picking elements one by one.</li>
    <li>Each element is compared with the elements in the sorted part and placed in its correct position.</li>
    <li>Continues until all elements in the unsorted part are incorporated into the sorted section.</li>
    </ul>
    <h2>The Complexity of insertion Sort Algorithm</h2>
    <p>The time complexity of the insertion sort algorithm is:</p>
    <ul>
    <li>The insertion sort algorithm is made up of two nested loops.</li>
    <li>It has an O (n2) time complexity due to the two nested loops.</li>
    </ul>
    <p>Best Case Scenario (O(n)): Occurs when the input array is already sorted. In this case, the algorithm only needs to compare each element with its predecessor and perform no swaps because the elements are already in the correct order. The time complexity is linear (O(n)) because it performs n-1 comparisons but no swaps are required.</p>
    <p>Average Case Scenario (O(n^2)): In an average case, the input array is not perfectly sorted or reversed. The algorithm, for each element in the unsorted portion, compares it with elements in the sorted portion and shifts elements to make space for the current element. This results in approximately n^2/4 comparisons and swaps on average for n elements, leading to a time complexity of O(n^2).</p>
    <p>Worst Case Scenario (O(n^2)): The worst case arises when the input array is sorted in reverse order. For each element in the unsorted part, it needs to compare and shift elements in the sorted section until it reaches the appropriate position. This results in roughly n^2/2 comparisons and swaps for n elements, leading to a time complexity of O(n^2).</p>
    <p>Space Complexity: Insertion sort is an in-place sorting algorithm, meaning it requires only a constant amount of additional memory space. Space Complexity: O(1)</p>
    </article>
    </div>"""
    st.markdown(content,unsafe_allow_html=True)
    st.link_button("For More info", "https://www.geeksforgeeks.org/insertion-sort/")