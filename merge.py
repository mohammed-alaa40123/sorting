import plotly.express as px
import streamlit as st
import pandas as pd
def merge(arr, l, m, r):
    frames=[]
    n1 = m - l + 1
    n2 = r - m
 

    L = [0] * (n1)
    R = [0] * (n2)
 

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0    
    j = 0  
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        frames.append(arr.copy())
        k += 1
 
   
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        frames.append(arr.copy())
 
   
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        frames.append(arr.copy())
    return frames

 
 
def mergeSort(arr, l, r,frames):
    
    if l < r:
 
        
        m = l+(r-l)//2
 
        
        mergeSort(arr, l, m,frames)
        mergeSort(arr, m+1, r,frames)
        frames.extend(merge(arr, l, m, r))
    
def visualize_mergesort(x,lst):
    frames = []
    print("new test")
    
    frames.append(lst.copy())
    
    mergeSort(lst,0,len(lst)-1,frames)
   
    # print(lst)
    # print(frames)
    figure = px.bar(x, y=frames[0],color=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n × log n)', 'O(n × log n)', 'O(n × log n)', 'O(n)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_merge():
    st.sidebar.dataframe(complexity_df,hide_index=True)
def show_merge_code(lang):
    if lang == "Python":
        code = """
\n# Python program for implementation of MergeSort


def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# Into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is")
	printList(arr)
	mergeSort(arr)
	print("\nSorted array is ")
	printList(arr)

# This code is contributed by Mayank Khanna

        """
    elif lang == "CPP":
        code = """
\n// C++ program for Merge Sort
#include <bits/stdc++.h>
using namespace std;

// Merges two subarrays of array[].
// First subarray is arr[begin..mid]
// Second subarray is arr[mid+1..end]
void merge(int array[], int const left, int const mid,
		int const right)
{
	int const subArrayOne = mid - left + 1;
	int const subArrayTwo = right - mid;

	// Create temp arrays
	auto *leftArray = new int[subArrayOne],
		*rightArray = new int[subArrayTwo];

	// Copy data to temp arrays leftArray[] and rightArray[]
	for (auto i = 0; i < subArrayOne; i++)
		leftArray[i] = array[left + i];
	for (auto j = 0; j < subArrayTwo; j++)
		rightArray[j] = array[mid + 1 + j];

	auto indexOfSubArrayOne = 0, indexOfSubArrayTwo = 0;
	int indexOfMergedArray = left;

	// Merge the temp arrays back into array[left..right]
	while (indexOfSubArrayOne < subArrayOne
		&& indexOfSubArrayTwo < subArrayTwo) {
		if (leftArray[indexOfSubArrayOne]
			<= rightArray[indexOfSubArrayTwo]) {
			array[indexOfMergedArray]
				= leftArray[indexOfSubArrayOne];
			indexOfSubArrayOne++;
		}
		else {
			array[indexOfMergedArray]
				= rightArray[indexOfSubArrayTwo];
			indexOfSubArrayTwo++;
		}
		indexOfMergedArray++;
	}

	// Copy the remaining elements of
	// left[], if there are any
	while (indexOfSubArrayOne < subArrayOne) {
		array[indexOfMergedArray]
			= leftArray[indexOfSubArrayOne];
		indexOfSubArrayOne++;
		indexOfMergedArray++;
	}

	// Copy the remaining elements of
	// right[], if there are any
	while (indexOfSubArrayTwo < subArrayTwo) {
		array[indexOfMergedArray]
			= rightArray[indexOfSubArrayTwo];
		indexOfSubArrayTwo++;
		indexOfMergedArray++;
	}
	delete[] leftArray;
	delete[] rightArray;
}

// begin is for left index and end is right index
// of the sub-array of arr to be sorted
void mergeSort(int array[], int const begin, int const end)
{
	if (begin >= end)
		return;

	int mid = begin + (end - begin) / 2;
	mergeSort(array, begin, mid);
	mergeSort(array, mid + 1, end);
	merge(array, begin, mid, end);
}

// UTILITY FUNCTIONS
// Function to print an array
void printArray(int A[], int size)
{
	for (int i = 0; i < size; i++)
		cout << A[i] << " ";
	cout << endl;
}

// Driver code
int main()
{
	int arr[] = { 12, 11, 13, 5, 6, 7 };
	int arr_size = sizeof(arr) / sizeof(arr[0]);

	cout << "Given array is \n";
	printArray(arr, arr_size);

	mergeSort(arr, 0, arr_size - 1);

	cout << "\nSorted array is \n";
	printArray(arr, arr_size);
	return 0;
}

// This code is contributed by Mayank Tyagi
// This code was revised by Joshua Estes

"""

    else:
        code="""
\n// Java program for Merge Sort
import java.io.*;

class MergeSort {

	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r)
	{
		// Find sizes of two subarrays to be merged
		int n1 = m - l + 1;
		int n2 = r - m;

		// Create temp arrays
		int L[] = new int[n1];
		int R[] = new int[n2];

		// Copy data to temp arrays
		for (int i = 0; i < n1; ++i)
			L[i] = arr[l + i];
		for (int j = 0; j < n2; ++j)
			R[j] = arr[m + 1 + j];

		// Merge the temp arrays

		// Initial indices of first and second subarrays
		int i = 0, j = 0;

		// Initial index of merged subarray array
		int k = l;
		while (i < n1 && j < n2) {
			if (L[i] <= R[j]) {
				arr[k] = L[i];
				i++;
			}
			else {
				arr[k] = R[j];
				j++;
			}
			k++;
		}

		// Copy remaining elements of L[] if any
		while (i < n1) {
			arr[k] = L[i];
			i++;
			k++;
		}

		// Copy remaining elements of R[] if any
		while (j < n2) {
			arr[k] = R[j];
			j++;
			k++;
		}
	}

	// Main function that sorts arr[l..r] using
	// merge()
	void sort(int arr[], int l, int r)
	{
		if (l < r) {

			// Find the middle point
			int m = l + (r - l) / 2;

			// Sort first and second halves
			sort(arr, l, m);
			sort(arr, m + 1, r);

			// Merge the sorted halves
			merge(arr, l, m, r);
		}
	}

	// A utility function to print array of size n
	static void printArray(int arr[])
	{
		int n = arr.length;
		for (int i = 0; i < n; ++i)
			System.out.print(arr[i] + " ");
		System.out.println();
	}

	// Driver code
	public static void main(String args[])
	{
		int arr[] = { 12, 11, 13, 5, 6, 7 };

		System.out.println("Given array is");
		printArray(arr);

		MergeSort ob = new MergeSort();
		ob.sort(arr, 0, arr.length - 1);

		System.out.println("\nSorted array is");
		printArray(arr);
	}
}
/* This code is contributed by Rajat Mishra */

""" 
    return code

def show_merge_explaination():
    content =  """<div><article>
<p>Merge sort maingly is a divide and conquer approach that depends on dividing the array into two equal arrays,and the sub arrays are divided equally till we reach single elements that are merged in order to form sub arrays which are in turn merged in greater sub arrays in order till we reach the orgiginal array ,but sorted</p>
<h2>Complexity Analysis</h2>
<ul>
<li>
<h3>Best Case Complexity</h3>
<p>The array is divided log(n) times ,and in each time n items are merged ,so it will always be n*log(n)</p>
</li>
<li>
<h3>Average Case Complexity</h3>
<p>The array is divided log(n) times ,and in each time n items are merged ,so it will always be n*log(n)</p>
</li>
<li>
<h3>Worst Case Complexity</h3>
<p>The array is divided log(n) times ,and in each time n items are merged ,so it will always be n*log(n)</p>
</li>
</ul>
<h2>Applications</h2>
<ol>
<li>
<h3>External Sorting</h3>
</li>
<li>
<h3>Inversion Count</h3>
</li>
<li>
<h3>External Merging</h3>
</li>
<li>
<h3>Parallel and Distributed Computing</h3>
</li>
<li>
<h3>Stability Requirement</h3>
</li>
</ol>
</article>
</div>"""
    st.write(content,unsafe_allow_html=True)
    st.link_button("For More info", "https://www.geeksforgeeks.org/selection-sort/")
