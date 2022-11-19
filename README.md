# AGSS_2022_AI_ML_Workshop_Sort_Visual
- AGSS 2022 Artificial Intelligence and Machine Learning Workshop - Sorting Visualized
- There are two python codes for sorting visualization
- `agss_1_1_sort_visual_v1.py` visualizes several sorting algorithms
- `agss_1_2_sort_time_v1.py` measure sorting time per algorihm
- Following are libraries needed to run the codes
```
import time
import tkinter as tk
import random
from random import shuffle
import numpy as np
import math
```
## Sorting algorithms visualized
- Can you think of a way to arrange a series of number in increasing order?
- It has been one the most basic computing tasks, and there are lots of different algorithms.
- `python3 agss_1_1_sort_visual_v1.py`
- ![Sortng algorithms visualized](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Sort_Visual/blob/main/agss_ai_ml_sort_visual.png)
- Five sorting algorithms are introduced - bogo, first come first served, insertion, bubble, and merge sorting
- First `Number of Items` then `Randomize`
- Then click to try each sorting algorithm and see how they work.
- Which one do you like most and why do you like it?
- Do you see a way that algorithms can make a mistake?
- What is a drawback of the each algorithm?
- Which one will be fastest and slowest?
## Sorting time by algorithm
- Let's measure how long each sorting algorithm takes
- `python3 agss_ai_ml_sort_time.py`
- ![Sortng time by algorithms](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Sort_Visual/blob/main/agss_ai_ml_sort_time.png)
- Input number of sample and click `Number of Items`
- Click each algorithm to sort and measure sorting time
- How many samples are good number to measure sorting time?
- What happens to sorting time of each algorithm when the number of samples increase or decrease?
## Let's plot sorting time
- First plot shows linear scale of the number of samples and sorting time. Each setup has measurement fo 100 cases of randomized numbers.
- ![Linear scale results](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Sort_Visual/blob/main/agss_sort_xlin_ylin.png)
- Sometimes, a scale of the power of 10 either/both in X and Y axis gives you better insight of the data
- We can start with X axis in log scale
- ![x log scale results](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Sort_Visual/blob/main/agss_sort_xlog_ylin.png)
- Then Y axis in log scale
- ![y log scale results](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Sort_Visual/blob/main/agss_sort_xlin_ylog.png)
- Both X and Y axes can be log scale
- ![x and y log scale results](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Sort_Visual/blob/main/agss_sort_xlog_ylog.png)
- Do you notice algorithms have similar slope, and one is different from others?
- ![asymptote](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Sort_Visual/blob/main/agss_sort_xlog_ylog_asymp.png)
- Can you guess each color belongs to which sorting algorithm?
- Can you guess how long it will take if you want to make the same plots?

[Next - AI Tic Tac Toe](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop_Tic_Tac_Toe) / [Top - AGSS 2022 AI ML Workshop](https://github.com/Cinderpe1t/AGSS_2022_AI_ML_Workshop)
