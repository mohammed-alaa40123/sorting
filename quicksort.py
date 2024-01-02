
import plotly.express as px
import streamlit as st
import pandas as pd

def quick_sort(lst, low, high, frames,colors):
    color=len(lst)*["blue"]

    if low < high:
        pivot,l,col = partition(lst, low, high)
        frames.extend(l)
        colors.extend(col)
        quick_sort(lst, low, pivot - 1,frames,colors)
        quick_sort(lst, pivot + 1, high, frames,colors)
        frames.append(lst.copy())
        c = color.copy()
        c[pivot]="black"
        colors.append(c.copy())
       

def partition(lst, low, high):
    frames = []
    pivot = lst[high]
    colors=[]
    color=len(lst)*["blue"]
    i = low - 1
   
    for j in range(low, high): 
        
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            frames.append(lst.copy())
            colors.append(save_color(color,lst,pivot))
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    frames.append(lst.copy())
    colors.append(save_color(color,lst,pivot))
    return i + 1, frames,colors

def save_color(color,lst,pivot):
    c = color.copy()
    ll = lst.copy().tolist()
    c[ll.index(pivot)]="black"
    return c.copy()

def visualise_quick_sort(x,lst):
    frames=[lst.copy()]
    color=len(lst)*["blue"]
    colors=[]
    colors.append(color)
    quick_sort(lst,0,len(lst)-1,frames,colors)
    print("----")
    print(colors)
    figure = px.bar(x=x, y=frames[0],color=colors[0])
    figure.update_layout(showlegend=False)
    figure.update_xaxes(visible=False)
    figure.update_yaxes(visible=False)
    return figure, frames,colors

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n × log n)', 'O(n × log n)', 'O(n^2)', 'O(logn)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_quicksort():
    st.sidebar.dataframe(complexity_df,hide_index=True)
    
    

def show_quick_code(lang):
    if lang == "Python":
        code = """
\ndef partition(array, low, high):

	pivot = array[high]
	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:

			i = i + 1
			(array[i], array[j]) = (array[j], array[i])


	(array[i + 1], array[high]) = (array[high], array[i + 1])

	
	return i + 1

def quicksort(array, low, high):
	if low < high:

		pi = partition(array, low, high)

		quicksort(array, low, pi - 1)
		quicksort(array, pi + 1, high)
        """
    elif lang == "CPP":
        code = """
\nint partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[i + 1], arr[high]);

    return i + 1;
}

void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);

        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}
"""

    else:
        code="""
\npublic class QuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivot = partition(arr, low, high);

            quickSort(arr, low, pivot - 1);
            quickSort(arr, pivot + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }
}
""" 
    return code

def show_quick_explaination():
    content =  """<div><article>
    

<h2>What Is a Quick Sort Algorithm?</h2>

QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

<h2>The Complexity of quick Sort Algorithm</h2>
The average and worst cases are O(nlogn) and this is thanks to the divide and conquer technique. However, the worst case is O(n^2) and here comes the irony you may think that it takes this huge time because the array is so messed up, but actually this happens only if the array is already sorted. Funny, isn't it?

<h3>Best Use Cases:</h3>

QuickSort is a highly efficient and widely used sorting algorithm for general-purpose sorting.
It has an average-case time complexity of O(n log n), making it faster than many other sorting algorithms.
QuickSort is often preferred in practice for large datasets due to its speed.

<h3>When to Use:</h3>

Use QuickSort when you need a fast and efficient sorting algorithm for general-purpose sorting.
It is suitable for both small and large datasets, and its average-case performance is often better than other sorting algorithms like Bubble Sort or Insertion Sort.
Avoid quick sort if the array is already sorted or nearly sorted.
Overall:
QuickSort is a versatile and efficient sorting algorithm with widespread use. It is particularly well-suited for scenarios where fast sorting is required, making it a popular choice in various applications and programming environments.

"""
    st.markdown(content,unsafe_allow_html=True)
    st.link_button("For More info", "https://www.geeksforgeeks.org/quick-sort/")
