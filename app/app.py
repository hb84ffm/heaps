# streamlit heapq app to calcualte median values
import streamlit as st
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (store negative values)
        self.large = []  # min heap

    def appendNum(self, num: int) -> None:
        # Balance heaps and maintain size invariant
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def getMedian(self) -> float:
        # Even number of elements
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        # Odd number of elements (large has one more)
        return float(self.large[0])

st.title("Median Finder")

# Initialize state for median finder and stored lists
if 'median_finder' not in st.session_state:
    st.session_state.median_finder = MedianFinder()
if 'number_list' not in st.session_state:
    st.session_state.number_list = []
if 'median_list' not in st.session_state:
    st.session_state.median_list = []

new_number = st.sidebar.number_input("Type whole number:", value=0, step=1)

if st.sidebar.button("Add number"):
    st.session_state.median_finder.appendNum(new_number)
    st.session_state.number_list.append(new_number)
    st.session_state.median_list.append(st.session_state.median_finder.getMedian())

if st.session_state.median_list:
    st.write(f"Current median: {st.session_state.median_list[-1]}")
    st.write(f"Number list: {st.session_state.number_list}")
    st.write(f"Median list: {st.session_state.median_list}")
    st.line_chart(st.session_state.median_list, x_label="Iterations", y_label="Median values")
