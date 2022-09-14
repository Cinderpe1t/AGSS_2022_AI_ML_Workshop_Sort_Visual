import time
import tkinter as tk
import random
import numpy as np
import math

def cNoSample():
    global noSample, noArray, noList, dispListIn
    inp = inputText.get(1.0, "end-1c")
    noSample = int(inp)
    noArray = np.random.randint(1,noSample,noSample)
    #display first 20 samples
    
    if len(dispListIn)>0:
        for k in range(len(dispListIn)):
            dispListIn[k].destroy()
    dispListIn=[]
    tDisp = tk.Label(win, text = "First 20 numbers", font=("Arial", winFontSize))
    tDisp.place(relx=0.2, rely=0.3, anchor='n')
    dispListIn.append(tDisp)
    for i in range(20):
        tDisp = tk.Label(win, text = noArray[i], font=("Arial", listFontSize))
        tDisp.place(relx=0.2, rely=0.35+(i+1)/35, anchor='n')
        dispListIn.append(tDisp)
    win.update()

    #First comes first sort
def cFirstComesFirst():
    global noArray, noList, dispListOut, timeFirst
    #
    if len(dispListOut)>0:
        for k in range(len(dispListOut)):
            dispListOut[k].destroy()
    timeFirst.config(text = "")
    win.update()
    #
    noList=noArray.copy()
    startTime=time.time()
    noList=sortFirstComesFirst(noList)
    endTime=time.time()
    print(endTime-startTime)
    timeFirst.config(text = '{:.3f}'.format(endTime-startTime)+'sec')
    #
    dispListOut=[]
    tDisp = tk.Label(win, text = "Sorted first 20 numbers", font=("Arial", winFontSize))
    tDisp.place(relx=0.4, rely=0.3, anchor='n')
    dispListOut.append(tDisp)
    for i in range(20):
        tDisp = tk.Label(win, text = noList[i], font=("Arial", listFontSize))
        tDisp.place(relx=0.4, rely=0.35+(i+1)/35, anchor='n')
        dispListOut.append(tDisp)    
    win.update()


def sortFirstComesFirst(L):
    for i in range(len(L)-1):
        minValue = L[i]
        minIndex = i
        for j in range(len(L) - i -1):
            if L[i + j + 1]<minValue:
                minValue = L[i + j + 1]
                minIndex = i + j + 1
        L[minIndex] = L[i]
        L[i] = minValue
        #print(L)
    return L


def cInsertionSort():
    global noArray, noList, dispListOut, timeInsert
    #
    if len(dispListOut)>0:
        for k in range(len(dispListOut)):
            dispListOut[k].destroy()
    timeInsert.config(text = "")
    win.update()
    #

    noList=noArray.copy()
    startTime=time.time()
    noList=sortInsert(noList)
    endTime=time.time()
    print(endTime-startTime)
    timeInsert.config(text = '{:.3f}'.format(endTime-startTime)+'sec')
    #
    dispListOut=[]
    tDisp = tk.Label(win, text = "Sorted first 20 numbers", font=("Arial", winFontSize))
    tDisp.place(relx=0.4, rely=0.3, anchor='n')
    dispListOut.append(tDisp)
    for i in range(20):
        tDisp = tk.Label(win, text = noList[i], font=("Arial", listFontSize))
        tDisp.place(relx=0.4, rely=0.35+(i+1)/35, anchor='n')
        dispListOut.append(tDisp)    
    win.update()


#Insertion sort
def sortInsert(L):
    i = 1
    while i < len(L):
        x=L[i]
        j=i
        while j > 0 and L[j-1] > L[j]:
            t = L[j]
            L[j] = L[j-1]
            L[j - 1] = t
            j = j - 1
        i = i + 1
    return L


def cBubbleSort():
    global noArray, noList, dispListOut, timeBubble
    #
    if len(dispListOut)>0:
        for k in range(len(dispListOut)):
            dispListOut[k].destroy()
    timeBubble.config(text = "")
    win.update()
    #
    noList=noArray.copy()
    startTime=time.time()
    noList=sortBubble(noList)
    endTime=time.time()
    print(endTime-startTime)
    timeBubble.config(text = '{:.3f}'.format(endTime-startTime)+'sec')
    #
    dispListOut=[]
    tDisp = tk.Label(win, text = "Sorted first 20 numbers", font=("Arial", winFontSize))
    tDisp.place(relx=0.4, rely=0.3, anchor='n')
    dispListOut.append(tDisp)
    for i in range(20):
        tDisp = tk.Label(win, text = noList[i], font=("Arial", listFontSize))
        tDisp.place(relx=0.4, rely=0.35+(i+1)/35, anchor='n')
        dispListOut.append(tDisp)    
    win.update()
    
def sortBubble(L):
    BUBBLY=True
    while BUBBLY==True:
        BUBBLY=False
        for idx in range(len(L)-1):
            #item to compare order
            item0=L[idx]
            item1=L[idx+1]
            
            if item0>item1:
                #bubble sort
                L[idx]=item1
                L[idx+1]=item0
                BUBBLY=True
                #print(listInput)
    return L


def cMergeSort():
    global noArray, noList, dispListOut, timeMerge
    #
    if len(dispListOut)>0:
        for k in range(len(dispListOut)):
            dispListOut[k].destroy()
    timeMerge.config(text = "")
    win.update()
    #
    noList=noArray.copy()
    startTime=time.time()
    mergeSort(noList, 0, len(noList)-1)
    endTime=time.time()
    print(endTime-startTime)
    timeMerge.config(text = '{:.3f}'.format(endTime-startTime)+'sec')
    #
    dispListOut=[]
    tDisp = tk.Label(win, text = "Sorted first 20 numbers", font=("Arial", winFontSize))
    tDisp.place(relx=0.4, rely=0.3, anchor='n')
    dispListOut.append(tDisp)
    for i in range(20):
        tDisp = tk.Label(win, text = noList[i], font=("Arial", listFontSize))
        tDisp.place(relx=0.4, rely=0.35+(i+1)/35, anchor='n')
        dispListOut.append(tDisp)    
    win.update()



def mergeData(Data, iLeft, iMed, iRight):
    nLeft = iMed - iLeft + 1
    nRight = iRight - iMed
 
    # create temp arrays
    dataLeft = [0] * (nLeft)
    dataRight = [0] * (nRight)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, nLeft):
        dataLeft[i] = Data[iLeft + i]
 
    for j in range(0, nRight):
        dataRight[j] = Data[iMed + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # starting index of left
    j = 0     # starting relative index of right
    k = iLeft     # starting index for merging
 
    while i < nLeft and j < nRight:
        if dataLeft[i] <= dataRight[j]:
            Data[k] = dataLeft[i]
            i += 1
        else:
            Data[k] = dataRight[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < nLeft:
        Data[k] = dataLeft[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < nRight:
        Data[k] = dataRight[j]
        j += 1
        k += 1
 
def mergeSort(Data, iLeft, iRight):
    if iLeft < iRight:
        #set medium index
        iMed = iLeft+(iRight-iLeft)//2

        # Sort first and second halves
        mergeSort(Data, iLeft, iMed)
        mergeSort(Data, iMed+1, iRight)
        mergeData(Data, iLeft, iMed, iRight)

xWinSize=1024
yWinSize=768
noSample=100
stepDelay=0.1
animationDelay=0.05
animationAngleStep=20
winFontSize=20
listFontSize=12
yLineUp=0.5
yCompare=0.6

noArray=[]
widgetList=[]
noList=[]
dispListIn=[]
dispListOut=[]


#Create an instance of tkinter frame
win=tk.Tk()
win.title("Sorting Time Measurement")

#Define the geometry of window
win.geometry("1024x768")

timeFirst =tk.Label(win, text = "", font=("Arial", winFontSize))
timeFirst.place(relx=0.2, rely=0.25, anchor='n')
timeInsert=tk.Label(win, text = "", font=("Arial", winFontSize))
timeInsert.place(relx=0.4, rely=0.25, anchor='n')
timeBubble=tk.Label(win, text = "", font=("Arial", winFontSize))
timeBubble.place(relx=0.6, rely=0.25, anchor='n')
timeMerge =tk.Label(win, text = "", font=("Arial", winFontSize))
timeMerge.place(relx=0.8, rely=0.25, anchor='n')

#number of samples input
inputText = tk.Text(win, height = 1, width = 5, bg = "light yellow", font=("Arial", winFontSize))
inputText.place(relx=0.1, rely=0.1, anchor='n')
inputText.insert(tk.END, noSample)

bNoSample = tk.Button(win, text = "Number of items",  command = cNoSample, font=("Arial", winFontSize))
bNoSample.place(relx=0.25, rely=0.1, anchor='n')

bSortFirst = tk.Button(win, text = "First-comes-first sort",  command = cFirstComesFirst, font=("Arial", winFontSize))
bSortFirst.place(relx=0.2, rely=0.2, anchor='n')

bSortInsert = tk.Button(win, text = "Insertion sort",  command = cInsertionSort, font=("Arial", winFontSize))
bSortInsert.place(relx=0.4, rely=0.2, anchor='n')

bSortBubble = tk.Button(win, text = "Bubble sort",  command = cBubbleSort, font=("Arial", winFontSize))
bSortBubble.place(relx=0.6, rely=0.2, anchor='n')

bSortMerge = tk.Button(win, text = "Merge sort",  command = cMergeSort, font=("Arial", winFontSize))
bSortMerge.place(relx=0.8, rely=0.2, anchor='n')

win.mainloop()