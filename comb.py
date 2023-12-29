import plotly.express as px
import streamlit as st
import pandas as pd


def comb_sort (lst) :
    size = len(lst)
    frames = []

    gap = size

    swapped = True

    while swapped == True or gap != 1 :

        gap = int((gap * 10)/13)
        if gap < 1 :
            gap = 1

        swapped = False

        for i in range(0, size-gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap]=lst[i + gap], lst[i]
                swapped = True
                frames.append(lst.copy())

    
    return frames


def visualise_comb_sort(x,lst):
    frames = comb_sort(lst)
    figure = px.bar(x=x, y=frames[0])
    return figure, frames

data = {
    'Case': ['Average Complexity', 'Best Case', 'Worst Case', 'Space Complexity'],
    'Complexity': ['O(n^2)', 'O(n × log n)', 'O(n^2)', 'O(1)']
}

complexity_df = pd.DataFrame(data)
def show_complexity_comb():
    st.sidebar.dataframe(complexity_df,hide_index=True)


def show_comb_code(lang):
    if lang == "Python":
        code = """
\n size = len(lst)

    gap = size

    swapped = True

    while swapped == True or gap != 1 :

        gap = int((gap * 10)/13)
        if gap < 1 :
            gap = 1

        swapped = False

        for i in range(0, size-gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap]=lst[i + gap], lst[i]
                swapped = True

    return lst
    """
    elif lang == "CPP":
        code = """
\n int getNextGap(int gap)
{
    // Shrink gap by Shrink factor
    gap = (gap*10)/13;
 
    if (gap < 1)
        return 1;
    return gap;
}
 
// Function to sort a[0..n-1] using Comb Sort
void combSort(int a[], int n)
{
    int gap = n;

    bool swapped = true;
 
    while (gap != 1 || swapped == true)
    {
        gap = getNextGap(gap);
 
        swapped = false;
 
        for (int i=0; i<n-gap; i++)
        {
            if (a[i] > a[i+gap])
            {
                swap(a[i], a[i+gap]);
                swapped = true;
            }
        }
    }
}
""" 

    else:
        code = """
\n function getNextGap(gap)
    {
        gap = parseInt((gap*10)/13, 10);
        if (gap < 1)
            return 1;
        return gap;
    }
    function sort(arr)
    {
        let n = arr.length;
        let gap = n;
        let swapped = true;

        while (gap != 1 || swapped == true)
        {
            gap = getNextGap(gap);
  
            swapped = false;

            for (let i=0; i<n-gap; i++)
            {
                if (arr[i] > arr[i+gap])
                {
                    let temp = arr[i];
                    arr[i] = arr[i+gap];
                    arr[i+gap] = temp;
                    swapped = true;
                }
            }
        }
    }
"""
    return code

def show_comb_explaination():
    content =  """<div><article>
    <p>Comb Sort is an enhancement over Bubble Sort, aiming to address its limitations. While Bubble Sort compares adjacent values, handling one inversion at a time, Comb Sort improves this by employing a gap larger than 1. It begins with a substantial gap size, gradually decreasing it by a factor of 1.3 in each iteration until it reaches 1. Consequently, Comb Sort eliminates multiple inversions with a single swap, leading to improved performance compared to Bubble Sort. This 1.3 shrink factor was determined empirically through testing on more than 200,000 random lists.</p>
    <h2>What Is a comb Sort Algorithm?</h2>
    <ul>
    <li>Initialize Gap and Array: Set an initial gap size, typically starting with the array length. Also, have a boolean flag (swapped) to track swaps.</li>
    <li>Gap Reduction: Define a shrink factor (commonly 1.3). In each iteration, reduce the gap by multiplying it by the shrink factor. This reduction continues until the gap becomes 1.</li>
    <li>Iterative Comparison and Swapping: Begin with the initial gap and iterate through the array. Afterthat, compare elements that are gap distance apart and perform a swap if necessary to correct their order.lastly, move through the array in increments of the gap size, making comparisons and swapping elements as needed.</li>
    <li>Flag to Track Swaps:Utilize a boolean flag (swapped) to note whether any swaps occurred during a pass through the array. If a swap is performed during the comparison phase, set the flag to indicate that a swap occurred.</li>
    <li>Repeat with Reduced Gap: Continue the iterations with the reduced gap size until the gap becomes 1. At this point, the algorithm performs a final pass with a gap of 1, essentially behaving like a simple Bubble Sort.</li>
    <li>Overall Execution: Comb Sort combines the benefits of larger gap comparisons with the gradual reduction of the gap size. By employing larger gaps at the start, it targets the removal of multiple inversions with each iteration. As the gap reduces, it refines the array, leading to fewer necessary comparisons and swaps.</li>
    <li>Termination: The process terminates when the gap becomes 1, and no swaps occur in an iteration, signifying that the array is sorted.</li>
    </ul>
    <h2>The Complexity of comb Sort Algorithm</h2>
    <p>The time complexity of the comb sort algorithm is:</p>
    <ul>
    <li>The comb sort algorithm is made up of two nested loops.</li>
    <li>It has an O (n2) time complexity due to the two nested loops.</li>
    </ul>
    <p>Best Case Time Complexity (O(n * log n)): Occurs when the input array is nearly sorted. In this scenario, the larger gap sizes at the start efficiently eliminate multiple inversions, resulting in a time complexity close to O(n * log n)</p>
    <p>Average Case Time Complexity (O(n^2 / 2^p)): Involves an average-case time complexity of approximately O(n^2 / 2^p), where 'p' represents the number of increments. This scenario accounts for average sorting performance across various inputs and gap reduction factors.</p>
    <p>Worst Case Time Complexity (O(n^2)): Happens when the input array is in reverse order. Despite the larger gap sizes and reduction factors, the algorithm's performance degrades to a quadratic time complexity of O(n^2) due to the extensive number of necessary comparisons and swaps.</p>
    <p>Space Complexity: Comb Sort is an in-place sorting algorithm, meaning it sorts the elements within the given array itself.
    Space Complexity: O(1)
    The algorithm doesn’t require additional memory proportional to the size of the input; it operates using only a constant amount of extra space, regardless of the array's size.</p>
    </article>
    </div>"""
    st.markdown(content,unsafe_allow_html=True)
    st.link_button("For More info", "https://www.geeksforgeeks.org/comb-sort/")