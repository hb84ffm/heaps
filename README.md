# A streamlit app to iteratively calculate median values  

## Description 
This project implements a simple streamlit app allowing the user to iteratively create integer values, add them to a list and calculate for each iteration the median. This apps aims to minizime runtime when computing the median, using commands provided by heapq package.   

## Features 1. 
1. Interactive UI to create integers and send these to an backend that runs the calculation 
2. Direct calculation of median values on button click 
3. Direct visualization of median values as a simple line chart
4. Runtime reduction by finding for each iteration the median in O(1) time & applying appendNum in O(logN)

## Technical 1. 
1. Use of heapq package to mimick a balanced binary tree search
2. Create the class MedianFinder with methods appendNum() & getMedian() applied on the iterations
3. Use of streamlit package to create a simple UI
  
## Requirements 1. 
1. Python 3.x 
2. proper setup of a working directory
3. Streamlit
4. heapq

## How to use 
1. pip install the streamlit package
2. Make sure to save "app.py" to your venv
3. Have a proper browser installed (chrome, firefox or edge)
4. From your console run the command "streamlit run app.py" and press ENTER on notification
5. If asked to verify email in console, press ENTER again (to move on) --> URL should be shown then
6. If app does not appear in web browser -> copy the stated URL (localhost) -> paste it to new web browser window --> press ENTER
7. Use (left) sidebar to input whole number manually
8. Click "Add number" to append number to a list & start median calculation (number list, median, median list and line chart appear)
9. To empty the browser refresh URL again

## Installation 
1. Clone this repository
2. Install required packages (see above)
