import streamlit as st
import pandas as pd

from algorithms.linear_search import linear_search
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from algorithms.performance import compare_algorithms



st.title("Searching and Sorting Playground")

numbers = st.text_input(
    "Enter numbers separated by comma",
    "5,8,1,9,3,6"
)

arr = [int(x.strip()) for x in numbers.split(",")]

option = st.selectbox(
    "Choose Algorithm",
    [
        "Linear Search",
        "Merge Sort",
        "Quick Sort",
        "Heap Sort"
    ]
)

if option == "Linear Search":

    target = st.number_input("Target", value=5)

    if st.button("Search"):

        index, steps = linear_search(arr, target)

        st.write("### Steps")

        for step in steps:
            st.write(step)

        if index != -1:
            st.success(f"Found at Index {index}")
        else:
            st.error("Not Found")

else:

    if st.button("Sort"):

        if option == "Merge Sort":
            result = merge_sort(arr)

        elif option == "Quick Sort":
            result = quick_sort(arr)

        else:
            result = heap_sort(arr)

        st.success(result)

st.divider()

st.header("Performance Comparison")

size = st.slider("Dataset Size",100,5000,1000)

if st.button("Compare"):

    result = compare_algorithms(size)

    df = pd.DataFrame(result.items(), columns=["Algorithm","Time"])

    st.bar_chart(df.set_index("Algorithm"))