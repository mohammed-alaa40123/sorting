import streamlit as st
import igraph as ig
import plotly.graph_objects as go
import time

def heapify(lst, n, i, frames):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[i] < lst[left]:  
        largest = left

    if right < n and lst[largest] < lst[right]:  
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        frames.append((lst.copy(), i, largest))  # Save frame after heapify operation
        heapify(lst, n, largest, frames)


def h_heap_sort(lst):
    lst = lst.copy()
    n = len(lst)
    frames = [(lst.copy(), -1, -1)]  
    fframes = []
    frame=[]
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, frames)

    while n > 0:
        lst[0], lst[n - 1] = lst[n - 1], lst[0]
        frames.append((lst.copy(), n - 1, 0))  # Save frame after swapping
        # print(frame)
        f = (lst.pop((lst.index(max(lst)))))
        frame.append(f)
        fframes.append(frame.copy())
        heapify(lst, n - 1, 0, frames)
        n -= 1

    return frames,fframes

def visualize_heap_sort(frames,fframes,speed):
    fig = go.Figure()
    placeholder = st.empty()
    list_placeholder = st.empty()
    j=0
    for i, (frame, arrow_start, arrow_end) in enumerate(frames):
        g = ig.Graph.Tree(len(frame), 2)
        g["number"] = frame
        g.vs["label"] = g["number"]

        layout = g.layout("rt",root=[0])  
        # print(*layout)
        edge_x = []
        edge_y = []
        for edge in g.get_edgelist():
            # edge (0,2) 
            # node 0 => 0,0 
            # node 2 => -1.25, 1 
            # edge_x = [0,1.25,None,0,-1.25]
            # edge_y = [0,1,None,0,1]
            x0, y0 = layout[edge[0]]
            x1, y1 = layout[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        # print(edge_x)
        # print(edge_y)

        node_x = [pos[0] for pos in layout]
        node_y = [pos[1] for pos in layout]

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            text=g["number"],
            textposition="middle center",
            textfont=dict(color="black"), 
            hoverinfo="none",
            marker=dict(size=40, color="lightblue", line=dict(color="blue", width=3)),  
        )

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            mode="lines",
            line=dict(width=1),
            hoverinfo="none",
        )

        arrow_trace = go.Scatter(
            x=[layout[arrow_start][0], layout[arrow_end][0]],
            y=[layout[arrow_start][1], layout[arrow_end][1]],
            mode="lines",
            line=dict(color="red", width=2),
            showlegend=False,
        )

        fig.add_trace(node_trace)
        fig.add_trace(edge_trace)
        fig.add_trace(arrow_trace)

        fig.update_layout(showlegend=False)
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)
        time.sleep(1-speed/100)
        placeholder.plotly_chart(fig, use_container_width=True)
        
        if len(frame)!=len(fframes):
            list_placeholder.metric("List", value=" ".join(map(str, reversed(fframes[len(fframes)-len(frame)-1]))))
        time.sleep(1)  
        fig.data = [] 
    placeholder.empty()
    list_placeholder.metric("List", value=" ".join(map(str, reversed(fframes[len(fframes)-1]))))


data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n × log n)', 'O(n × log n)', 'O(n × log n)', 'O(1)']
}
import pandas as pd
complexity_df = pd.DataFrame(data)
def show_complexity_heap():
    st.sidebar.dataframe(complexity_df,hide_index=True)


def mainheap(speed):
    arr = st.text_input("Enter a list of numbers (space-separated):")
    arr = list(map(int, arr.split()))

    if st.button("Heap Sort"):
        frames,fframes = h_heap_sort(arr)
        visualize_heap_sort(frames,fframes,speed)

def show_heap_explaination():
        content =  """<div><article>
<h2>Idea</h2>
<p>This algorithm mainly depends on inseting elements into a maxheap ,then we extrat the maximum element and put it in the list and we do this operation till the heap is empty and we put elements in reverse order(i.e from end of list to the beginning of it)</p>
<h2>Complexity analysis</h2>
<ul>
<li>
<h3>Average case complexity</h3>
<p>At any case the complexity will be O(n*log(n)) as we insert n items into the heap ,then we remove them ,and at each time we remove elements from the heap, the heap takes time log(n) to maxheapify</p>
</li>
<li>
<h3>Best case complexity</h3>
<p>At any case the complexity will be O(n*log(n)) as we insert n items into the heap ,then we remove them ,and at each time we remove elements from the heap, the heap takes time log(n) to maxheapify</p>
</li>
<li>
<h3>Worst case complexity</h3>
<p>At any case the complexity will be O(n*log(n)) as we insert n items into the heap ,then we remove them ,and at each time we remove elements from the heap, the heap takes time log(n) to maxheapify</p>
</li>
<li>
<h3>Space complexity</h3>
<p></p>
</li>
</ul>
</article>

</div>"""
        st.write(content,unsafe_allow_html=True)
        st.link_button("For More info", "https://www.geeksforgeeks.org/heap-sort/")
        
def show_heap_code(lang):
    if lang == "Python":
        code = """
def heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[i] < lst[left]:  
        largest = left

    if right < n and lst[largest] < lst[right]:  
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)


def h_heap_sort(lst):
    lst = lst.copy()
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    while n > 0:
        lst[0], lst[n - 1] = lst[n - 1], lst[0]
        heapify(lst, n - 1, 0)
        n -= 1

    return lst
       """
    elif lang == "CPP":
        code = """
// C++ program for implementation of Heap Sort

#include <iostream>
using namespace std;

// To heapify a subtree rooted with node i
// which is an index in arr[].
// n is size of heap
void heapify(int arr[], int N, int i)
{

	// Initialize largest as root
	int largest = i;

	// left = 2*i + 1
	int l = 2 * i + 1;

	// right = 2*i + 2
	int r = 2 * i + 2;

	// If left child is larger than root
	if (l < N && arr[l] > arr[largest])
		largest = l;

	// If right child is larger than largest
	// so far
	if (r < N && arr[r] > arr[largest])
		largest = r;

	// If largest is not root
	if (largest != i) {
		swap(arr[i], arr[largest]);

		// Recursively heapify the affected
		// sub-tree
		heapify(arr, N, largest);
	}
}

// Main function to do heap sort
void heapSort(int arr[], int N)
{

	// Build heap (rearrange array)
	for (int i = N / 2 - 1; i >= 0; i--)
		heapify(arr, N, i);

	// One by one extract an element
	// from heap
	for (int i = N - 1; i > 0; i--) {

		// Move current root to end
		swap(arr[0], arr[i]);

		// call max heapify on the reduced heap
		heapify(arr, i, 0);
	}
}

// A utility function to print array of size n
void printArray(int arr[], int N)
{
	for (int i = 0; i < N; ++i)
		cout << arr[i] << " ";
	cout << "\n";
}

// Driver's code
int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	int N = sizeof(arr) / sizeof(arr[0]);

	// Function call
	heapSort(arr, N);

	cout << "Sorted array is \n";
	printArray(arr, N);
}

"""

    else:
        code="""
// Java program for implementation of Heap Sort

public class HeapSort {
	public void sort(int arr[])
	{
		int N = arr.length;

		// Build heap (rearrange array)
		for (int i = N / 2 - 1; i >= 0; i--)
			heapify(arr, N, i);

		// One by one extract an element from heap
		for (int i = N - 1; i > 0; i--) {
			// Move current root to end
			int temp = arr[0];
			arr[0] = arr[i];
			arr[i] = temp;

			// call max heapify on the reduced heap
			heapify(arr, i, 0);
		}
	}

	// To heapify a subtree rooted with node i which is
	// an index in arr[]. n is size of heap
	void heapify(int arr[], int N, int i)
	{
		int largest = i; // Initialize largest as root
		int l = 2 * i + 1; // left = 2*i + 1
		int r = 2 * i + 2; // right = 2*i + 2

		// If left child is larger than root
		if (l < N && arr[l] > arr[largest])
			largest = l;

		// If right child is larger than largest so far
		if (r < N && arr[r] > arr[largest])
			largest = r;

		// If largest is not root
		if (largest != i) {
			int swap = arr[i];
			arr[i] = arr[largest];
			arr[largest] = swap;

			// Recursively heapify the affected sub-tree
			heapify(arr, N, largest);
		}
	}

	/* A utility function to print array of size n */
	static void printArray(int arr[])
	{
		int N = arr.length;

		for (int i = 0; i < N; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver's code
	public static void main(String args[])
	{
		int arr[] = { 12, 11, 13, 5, 6, 7 };
		int N = arr.length;

		// Function call
		HeapSort ob = new HeapSort();
		ob.sort(arr);

		System.out.println("Sorted array is");
		printArray(arr);
	}
}

""" 
    return code

