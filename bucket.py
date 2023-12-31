import plotly.graph_objects as go
from quicksort import *
import time
import numpy as np
import streamlit as st

# st.session_state.sidebar_state = 'collapsed'


def visualize_linked_lists(linked_lists,length):
    fig = go.Figure()
    y = 0  
    for i, linked_list in enumerate(linked_lists):
        
        x = 0  
        
        fig.add_shape(
            type='rect',
            x0=-5,
            y0=y-0.4,  
            x1=1.5, 
            y1=y+0.4,  
            line=dict(color='black', width=2),
            fillcolor='red',
            layer='below',
        )

        fig.add_annotation(
            x=-3,  
            y=y,
            text=f"Bucket {i+1}",
            showarrow=False,
            font=dict(color='black', size=12),
            align='right'
        )
        
        x += 1  
        
        for i in range(len(linked_list)):
            fig.add_trace(go.Scatter(
                x=[x],
                y=[y],
                mode='markers+text',
                marker=dict(size=10, color='blue'),
                text=[f"{linked_list[i]}"],
                textposition='middle center',
                hoverinfo='text',
                hovertext=[f"List {i+1}: {linked_list[i]}"],
            ))
            if i!= len(linked_list)-1:
                fig.add_trace(go.Scatter(
                    x=[x, x + 1],
                    y=[y, y],
                    mode='lines',
                    line=dict(color='gray', width=1),
                    hoverinfo='none',
                ))
            
            x += 1

        y -= 1


    fig.update_layout(
        title="Array of Linked Lists",
        showlegend=False,
        hovermode='closest',
        autosize=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    )

    return fig
def vis_quick_sort(x,lst,ind):
   
    frames=[lst.copy()]
    figures=[]
    quick_sort(lst,0,len(lst)-1,frames)
    
    for i in frames:
        figure = px.bar(x=x, y=i,title=f"Sorting Bucket #{ind}")
        figure.update_layout(showlegend=False)
        figure.update_xaxes(visible=False)
        figure.update_yaxes(visible=False)
        figures.append([figure,'Q'])
    
    return figures

def bucket_sort(nb,l):
    length=len(l)
    bucket=[]
    for i in range(nb+1):
        bucket.append([])
    
    max=l[0]
    for i in l:
        if i>max:
            max=i
    indexfactor=(nb)/max
    frames=[]
    for i in l:
        indx=int(i*indexfactor)
        
        bucket[indx].append(i)
        frames.append([visualize_linked_lists(bucket,length),'B'])
    array=[]
    index=0
    for i in bucket:
        index=index+1
        sz=len(i)
        if sz!=0:
            x=np.arange(0,sz,1)
            frames.extend(vis_quick_sort(x,i,index))
            for j in i:
                array.append(j)
                frames.append([array.copy(),'L'])
            frames.append([visualize_linked_lists(bucket,length),'B'])
    
    return frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n × k)', 'O(n)', 'O(n^2)', 'O(n+k)']
}
import pandas as pd
complexity_df = pd.DataFrame(data)
def show_complexity_bucket():
    st.sidebar.dataframe(complexity_df,hide_index=True)
    



def show_bucket_code(lang):
    if lang == "Python":
        code = """
\n# Python3 program to sort an array
# using bucket sort

from quicksort import *
def bucket_sort(nb,l):
    length=len(l)
    bucket=[]
    for i in range(nb+1):
        bucket.append([])
    
    max=l[0]
    for i in l:
        if i>max:
            max=i
    indexfactor=(nb)/max
z    for i in l:
        indx=int(i*indexfactor)
        
        bucket[indx].append(i)

    array=[]
    index=0
    for i in bucket:
        index=index+1
        sz=len(i)
        if sz!=0:
            
            
            for j in i:
                array.append(j)
                
            
    
    return array
def main_bucket:
    n=input("Enter number of elements")
    l=[]
    print("Enter List elements:")
    for i in range (n):
        a=input()
        l.append(a)
    nb=input("Enter number of buckets:")
    array=bucket_sort(nb,l)
    print("Sorted array is",array)
        """
    elif lang == "CPP":
        code = """
\n// C++ program to sort an
// array using bucket sort
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// Function to sort arr[] of
// size n using bucket sort
void bucketSort(float arr[], int n)
{

	// 1) Create n empty buckets
	vector<float> b[n];

	// 2) Put array elements
	// in different buckets
	for (int i = 0; i < n; i++) {

		// Index in bucket
		int bi = n * arr[i];
		b[bi].push_back(arr[i]);
	}

	// 3) Sort individual buckets
	for (int i = 0; i < n; i++)
		sort(b[i].begin(), b[i].end());

	// 4) Concatenate all buckets into arr[]
	int index = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < b[i].size(); j++)
			arr[index++] = b[i][j];
}

// Driver program to test above function
int main()
{
	float arr[]
		= { 0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434 };
	int n = sizeof(arr) / sizeof(arr[0]);
	bucketSort(arr, n);

	cout << "Sorted array is \n";
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
	return 0;
}
"""
    else:
        code="""
\n// Java program to sort an array
// using bucket sort
import java.util.*;
import java.util.Collections;

class GFG {

	// Function to sort arr[] of size n
	// using bucket sort
	static void bucketSort(float arr[], int n)
	{
		if (n <= 0)
			return;

		// 1) Create n empty buckets
		@SuppressWarnings("unchecked")
		Vector<Float>[] buckets = new Vector[n];

		for (int i = 0; i < n; i++) {
			buckets[i] = new Vector<Float>();
		}

		// 2) Put array elements in different buckets
		for (int i = 0; i < n; i++) {
			float idx = arr[i] * n;
			buckets[(int)idx].add(arr[i]);
		}

		// 3) Sort individual buckets
		for (int i = 0; i < n; i++) {
			Collections.sort(buckets[i]);
		}

		// 4) Concatenate all buckets into arr[]
		int index = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < buckets[i].size(); j++) {
				arr[index++] = buckets[i].get(j);
			}
		}
	}

	// Driver code
	public static void main(String args[])
	{
		float arr[] = { (float)0.897, (float)0.565,
						(float)0.656, (float)0.1234,
						(float)0.665, (float)0.3434 };

		int n = arr.length;
		bucketSort(arr, n);

		System.out.println("Sorted array is ");
		for (float el : arr) {
			System.out.print(el + " ");
		}
	}
}

// This code is contributed by Himangshu Shekhar Jha

""" 
    return code
def show_bucket_explaination():
        content =  """<div><article>
<p>This algorithm mainly depends on dividing the list into groups of numbers(Buckets) and each bucket represents a range ,then we sort each group ,and cumulate those groups back in the array in order ;for example, if we have an array contining elements ranging form 1 to 300 ,and we want to bucket sort it by 3 buckets  ,we put elements less than or euqal to 100 in bucket 1 ,elements less than or equal to 200 in bucket 2 ,and elements less than or equal to 300 in bucket 3,then we sort buckets 1,2,and 3 ,then we place elements of each bucket from 1 to 3 back to the array </p>
<h2>Complexity analysis</h2>
<ul>
<li>
<h3>Best Case</h3>
<p>The best case complexity is o(n) which is the number of elements and this happens if all elements were stored in different buckets</p>
</li>
<li>
<h3>Worst Case</h3>
<p>The worst case complexity is o(n^2) which is the worst case complexity of quick sort and this happens when all elements are stored in one bucket</p>
</li>
<li>
<h3>Average Case</h3>
<p>The average case complexity is o(n*k) such that n is the number of list items and k is the number of buckets </p>
</li>
<li>
<h3>Space Complexity</h3>
<p>The space complexity is O(n+k) ,and this is the number of list items and buckets </p>
</li>
</ul>
<h2>Applications</h2>
<ol>
<li>
<h3>Sorting float numbers</h3>
</li>
<li>
<h3>Sorting integers with limited range</h3>
</li>
<li>
<h3>Radix sort</h3>
</li>
<li>
<h3>Histogram computations</h3>
</li>
<li>
<h3>Data Clustering</h3>
</li>
</ol>
</article>

</div>"""
        st.write(content,unsafe_allow_html=True)
        st.link_button("For More info", "https://www.geeksforgeeks.org/bucket-sort-2/")


def mainbucket(speed):   
    plot_spot = st.empty()
    l=st.text_input("Enter the elements of the list:")
    l= list(map(int, l.split()))
    np=st.text_input("Enter number of buckets:")
    
    
    
    text_holder=st.empty()
    if st.button("Bucket Sort"):
        frames=bucket_sort(int(np)-1,l)
        for frame in frames:
            with plot_spot:
                    col1,col2=st.columns([3,1])
                    if(frame[1]=='Q'):
                        
                            with col2:
                                st.plotly_chart(frame[0])
                    elif(frame[1]=='B'):
                            with col1:
                                st.plotly_chart(frame[0])
                    else:
                            with text_holder:
                                st.text_area("List",frame[0])
                    time.sleep(1-speed/100)
            