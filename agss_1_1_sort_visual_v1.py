import time
import tkinter as tk
import random
from random import shuffle
import numpy as np
import math

def cNoSample():
    global noSample
    inp = inputText.get(1.0, "end-1c")
    noSample = int(inp)

def cRandomize():
    global noArray, widgetList
    if len(widgetList)>0:
        for i in range(len(widgetList)):
            widgetList[i].destroy()
    noArray = np.random.randint(1,noSample,noSample)
    for i in range(len(noArray)):
        tNo = tk.Label(win, text = noArray[i], font=("Arial", winFontSize))
        tNo.place(relx=(i+1)/(len(noArray)+1), rely=0.15, anchor='n')
        widgetList.append(tNo)
        #widgetList[i].place(relx=(i+1)/(len(noArray)+1), rely=0.5, anchor='n')

def cAnimationDelay():
    global stepDelay
    inp = inputSpeed.get(1.0, "end-1c")
    stepDelay = float(inp)
    animationDelay=0.25*stepDelay
        
def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(a <= b for a, b in zip(data, data[1:]))

def cBogo():
    global noArray, noList
    for i in range(len(noList)):
        noList[i].destroy()
    L=noArray.copy()
    noList=[]
    markerList=[]
    
    for i in range(len(noArray)):
        tNo = tk.Label(win, text = L[i], font=("Arial", winFontSize))
        tNo.place(relx=(i+1)/(len(noArray)+1), rely=yLineUp, anchor='n')
        noList.append(tNo)
    win.update()
    time.sleep(stepDelay)

    for i in range(len(noArray)-1):
        tMk = tk.Label(win, text = "", font=("Arial", winFontSize))
        tMk.place(relx=(i+1.5)/(len(noArray)+1), rely=yLineUp, anchor='n')
        markerList.append(tMk)


    while not is_sorted(L):
        for i in range(len(noArray)):
            noList[i].config(text = L[i])

        for i in range(len(noArray)-1):
            if L[i]<=L[i+1]:
                sComp="<="
                sColor="blue"
            else:
                sComp=">"
                sColor="red"
            markerList[i].config(text = sComp, fg = sColor)
            
        win.update()
        time.sleep(stepDelay)
        shuffle(L)
    #final result
    for i in range(len(noArray)):
        noList[i].config(text = L[i])

    for i in range(len(noArray)-1):
        if L[i]<=L[i+1]:
            sComp="<="
            sColor="blue"
        else:
            sComp=">"
            sColor="red"
        markerList[i].config(text = sComp, fg = sColor)
        win.update()
        time.sleep(stepDelay)

    for i in range(len(noArray)-1):
        markerList[i].destroy()

        #return data


def cFirstComesFirst():
    global noArray, noList
    for i in range(len(noList)):
        noList[i].destroy()
    L=noArray.copy()
    noList=[]
    
    for i in range(len(noArray)):
        tNo = tk.Label(win, text = noArray[i], font=("Arial", winFontSize))
        tNo.place(relx=(i+1)/(len(noArray)+1), rely=yLineUp, anchor='n')
        noList.append(tNo)
    win.update()
    time.sleep(stepDelay)
        
    for i in range(len(L)-1):
        noList[i].config(fg = 'red')
        noList[i].place(relx=(i+1)/(len(noArray)+1), rely=yCompare)
        win.update()
        time.sleep(stepDelay)
        minValue = L[i]
        minIndex = i
        for j in range(len(L) - i -1):
            tI = i + j + 1
            #noList[tI].config(fg = 'b')
            noList[tI].place(relx=(tI + 1)/(len(noArray)+1), rely=yCompare)
            win.update()
            time.sleep(stepDelay)
            if L[tI]<minValue:
                minValue = L[tI]
                noList[tI].config(fg = 'red')
                marker = tk.Label(win, text = '>', font=("Arial", winFontSize), fg = 'red')
                marker.place(relx=(minIndex + 1.5)/(len(noArray)+1), rely=yCompare, anchor='n')
                win.update()
                time.sleep(stepDelay)
                #Update min index
                prevMinIdx = minIndex
                minIndex = tI
                #neutralize previous minimum
                noList[prevMinIdx].config(fg = 'black')
                noList[prevMinIdx].place(rely=yLineUp, anchor='n')
            else:
                noList[tI].config(fg = 'blue')
                marker = tk.Label(win, text = '<=', font=("Arial", winFontSize), fg = 'blue')
                marker.place(relx=(minIndex + 1.5)/(len(noArray)+1), rely=yCompare, anchor='n')
                win.update()
                time.sleep(stepDelay)
                noList[tI].config(fg = 'black')
                noList[tI].place(relx=(tI + 1)/(len(noArray)+1), rely=yLineUp)
    
            marker.destroy()            
            win.update()
            time.sleep(stepDelay)
            
        #return the minimum value to array
        noList[minIndex].place(rely=yLineUp, anchor='n')
        win.update()
        time.sleep(stepDelay)

        if i < minIndex:
            #swap positions
            noList[i].place(rely=yLineUp+0.05)
            noList[minIndex].place(rely=yLineUp-0.05)
            win.update()
            time.sleep(animationDelay)
            x1=(i+1)/(len(noArray)+1)
            x2=(minIndex+1)/(len(noArray)+1)

            #animation
            for k in range(10):
                noList[i].place(relx=(k+1)/10*(x2-x1)+x1)
                noList[minIndex].place(relx=(k+1)/10*(x1-x2)+x2)
                win.update()
                time.sleep(animationDelay)

            #finish animation and get ready for next round
            L[minIndex] = L[i]
            L[i] = minValue

            noList[i].place(relx=(i + 1)/(len(noArray)+1), rely=yLineUp)
            noList[i].config(text = L[i], fg = 'gray')
            noList[minIndex].place(relx=(minIndex + 1)/(len(noArray)+1), rely=yLineUp)
            noList[minIndex].config(text = L[minIndex], fg = 'black')
        else:
            noList[i].place(relx=(i + 1)/(len(noArray)+1), rely=yLineUp)
            noList[i].config(text = L[i], fg = 'gray')
        win.update()
        time.sleep(stepDelay)

    #Finish last entries
    noList[i].place(relx=(i + 1)/(len(noArray)+1), rely=yLineUp)
    noList[i].config(text = L[i], fg = 'gray')
    noList[i+1].place(relx=(i + 1 + 1)/(len(noArray)+1), rely=yLineUp)
    noList[i+1].config(text = L[i+1], fg = 'gray')
    win.update()
    time.sleep(stepDelay)

def cInsertionSort():
    global noArray, noList
    for i in range(len(noList)):
        noList[i].destroy()    
    L=noArray.copy()
    noList=[]
    yLineUp=0.5
    yCompare=0.6
    radius=0.5/(len(noArray)+1)
    animationAngleStep=20
    
    for i in range(len(noArray)):
        tNo = tk.Label(win, text = noArray[i], font=("Arial", winFontSize), fg='gray')
        tNo.place(relx=(i+1)/(len(noArray)+1), rely=yLineUp, anchor='n')
        noList.append(tNo)
    win.update()
    time.sleep(stepDelay)
    
    i = 1
    while i < len(L):
        #
        noList[i].config(fg = 'black')
        noList[i].place(relx=(i+1)/(len(noArray)+1), rely=yCompare)
        noList[i-1].config(fg = 'black')
        noList[i-1].place(relx=(i-1+1)/(len(noArray)+1), rely=yCompare)
        win.update()
        time.sleep(stepDelay)
        #
        x=L[i]
        j=i
                        
        while j > 0 and L[j-1] > L[j]:
            #
            noList[j].config(fg = 'red')
            noList[j].place(relx=(j+1)/(len(noArray)+1), rely=yCompare)
            noList[j-1].config(fg = 'red')
            noList[j-1].place(relx=(j-1+1)/(len(noArray)+1), rely=yCompare)
            marker = tk.Label(win, text = '>', font=("Arial", winFontSize), fg = 'red')
            marker.place(relx=(j + 0.5)/(len(noArray)+1), rely=yCompare, anchor='n')
            win.update()
            time.sleep(stepDelay)
            marker.destroy()

            for angle in range(animationAngleStep,181,animationAngleStep):
                pAngle=angle-animationAngleStep
                dX=math.cos(angle*math.pi/180) * radius
                dY=math.sin(angle*math.pi/180) * radius
                noList[j-1].place(relx=(j+0.5)/(len(noArray)+1)-dX, rely=yCompare-dY)
                noList[j].place(relx=(j+0.5)/(len(noArray)+1)+dX, rely=yCompare+dY)
                win.update()
                time.sleep(animationDelay)

            #
            t = L[j]
            L[j] = L[j-1]
            L[j - 1] = t
            #
            noList[j].config(text = L[j], fg = 'blue')
            noList[j].place(relx=(j+1)/(len(noArray)+1), rely=yCompare)
            noList[j-1].config(text = L[j-1], fg = 'blue')
            noList[j-1].place(relx=(j-1+1)/(len(noArray)+1), rely=yCompare)
            marker = tk.Label(win, text = '<', font=("Arial", winFontSize), fg = 'blue')
            marker.place(relx=(j + 0.5)/(len(noArray)+1), rely=yCompare, anchor='n')
            win.update()
            time.sleep(stepDelay)
            marker.destroy()
            noList[j].config(fg = 'gray')
            noList[j].place(relx=(j+1)/(len(noArray)+1), rely=yLineUp)
            noList[j-1].config(fg = 'gray')
            noList[j-1].place(relx=(j-1+1)/(len(noArray)+1), rely=yLineUp)
            win.update()
            time.sleep(stepDelay)
            #
            j = j - 1
        #need final comparison
        if j>0:
            noList[j].config(text = L[j], fg = 'blue')
            noList[j].place(relx=(j+1)/(len(noArray)+1), rely=yCompare)
            noList[j-1].config(text = L[j-1], fg = 'blue')
            noList[j-1].place(relx=(j-1+1)/(len(noArray)+1), rely=yCompare)
            marker = tk.Label(win, text = '<=', font=("Arial", winFontSize), fg = 'blue')
            marker.place(relx=(j + 0.5)/(len(noArray)+1), rely=yCompare, anchor='n')
            win.update()
            time.sleep(stepDelay)
            marker.destroy()
            noList[j].config(fg = 'gray')
            noList[j].place(relx=(j+1)/(len(noArray)+1), rely=yLineUp)
            noList[j-1].config(fg = 'gray')
            noList[j-1].place(relx=(j-1+1)/(len(noArray)+1), rely=yLineUp)
            win.update()
            time.sleep(stepDelay)            
            
            #print(L)
        i = i + 1
    #print(L)   

def cBubbleSort():
    global noArray, noList
    for i in range(len(noList)):
        noList[i].destroy()
    L=noArray.copy()
    noList=[]
    yLineUp=0.5
    yCompare=0.6
    radius=0.5/(len(noArray)+1)
    animationAngleStep=20

    for i in range(len(noArray)):
        tNo = tk.Label(win, text = noArray[i], font=("Arial", winFontSize), fg='gray')
        tNo.place(relx=(i+1)/(len(noArray)+1), rely=yLineUp, anchor='n')
        noList.append(tNo)
    win.update()
    time.sleep(stepDelay)

    BUBBLY=True
    while BUBBLY==True:
        BUBBLY=False
        for idx in range(len(L)-1):
            #item to compare order
            item0=L[idx]
            item1=L[idx+1]
            #display activated items
            noList[idx].config(fg = 'black')
            noList[idx+1].config(fg = 'black')            
            win.update()
            time.sleep(stepDelay)

            if item0>item1:
                #activate color
                noList[idx].config(fg = 'red')
                noList[idx+1].config(fg = 'red')            
                marker = tk.Label(win, text = '>', font=("Arial", winFontSize), fg = 'red')
                marker.place(relx=(idx + 1.5)/(len(noArray)+1), rely=yLineUp, anchor='n')
                win.update()
                time.sleep(stepDelay)
                marker.destroy()
                #animate
                for angle in range(animationAngleStep,181,animationAngleStep):
                    pAngle=angle-animationAngleStep
                    dX=math.cos(angle*math.pi/180) * radius
                    dY=math.sin(angle*math.pi/180) * radius
                    noList[idx].place(relx=(idx+1.5)/(len(noArray)+1)-dX, rely=yLineUp-dY)
                    noList[idx+1].place(relx=(idx+1.5)/(len(noArray)+1)+dX, rely=yLineUp+dY)
                    win.update()
                    time.sleep(animationDelay)
                #bubble sort
                L[idx]=item1
                L[idx+1]=item0
                noList[idx].config(text = L[idx], fg = 'gray')
                noList[idx].place(relx=(idx+1)/(len(noArray)+1), rely=yLineUp)
                noList[idx+1].config(text = L[idx+1], fg = 'gray')
                noList[idx+1].place(relx=(idx+2)/(len(noArray)+1), rely=yLineUp)

                win.update()
                time.sleep(animationDelay)
                BUBBLY=True
            else:
                #activate color
                noList[idx].config(fg = 'blue')
                noList[idx+1].config(fg = 'blue')            
                marker = tk.Label(win, text = '<=', font=("Arial", winFontSize), fg = 'blue')
                marker.place(relx=(idx + 1.5)/(len(noArray)+1), rely=yLineUp, anchor='n')
                win.update()
                time.sleep(stepDelay)
                marker.destroy()
                noList[idx].config(fg = 'gray')
                noList[idx+1].config(fg = 'gray')            
                win.update()
                time.sleep(stepDelay)

def sortMergeData(Data, iLeft, iMed, iRight, Level, cNo, pNo, pILeft):
    yOut = 0.03
    yStep = 0.1
    nLeft = iMed - iLeft + 1
    nRight = iRight - iMed
    yPos = yLineUp + yStep * Level
    yOff = yLineUp + yStep * Level - yOut
 
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
    
    #gray out previous for merge graphics
    #for i in range(len(pNo)):
    #    pNo[i].config(fg = 'gray')
 
    while i < nLeft and j < nRight:
        #print("Comparing left and right")
        #print("k:", k)
        #print("iLeft:", iLeft)
        #print("size prev No:", len(pNo))
        #print("size current No:", len(cNo))
        #print("Data:", Data)
        
        #cNo[i].place(relx=(iLeft + i+1)/(len(noArray)+1), rely=yLineUp+0.1*Level-0.03, anchor='n')
        cNo[i].place(rely = yOff, anchor='n')
        cNo[i].config(fg = 'black')       
        #cNo[nLeft + j].place(relx=(iMed + 1 + j+1)/(len(noArray)+1), rely=yLineUp+0.1*Level-0.03, anchor='n')
        cNo[nLeft + j].place(rely = yOff, anchor='n')
        cNo[nLeft + j].config(fg = 'black')       
        win.update()
        time.sleep(stepDelay)
        
        if dataLeft[i] <= dataRight[j]:
            #display
            cNo[i].config(fg = 'blue')
            cNo[nLeft + j].config(fg = 'blue')
            cMarker=tk.Label(win, text = "<=", font=("Arial", winFontSize), fg = 'blue')
            tIdxMarker=(nLeft + j - i)/2 + i + iLeft + 1
            cMarker.place(relx=tIdxMarker/(len(noArray)+1), rely = yOff, anchor='n')
            win.update()
            time.sleep(stepDelay)
            #display
            cNo[i].config(fg = 'blue')
            cNo[nLeft + j].config(fg = 'black')
            cNo[nLeft + j].place(rely = yPos, anchor='n')
            cMarker.destroy()
            win.update()
            time.sleep(stepDelay)
            #sort
            Data[k] = dataLeft[i]
            cNo[i].destroy()
            pNo[k-pILeft].config(text = Data[k], fg = 'blue')
            win.update()
            time.sleep(stepDelay)
            #
            pNo[k-pILeft].config(text = Data[k], fg = 'black')
            win.update()
            time.sleep(stepDelay)

            i += 1
        else:
            #display
            cNo[i].config(fg = 'red')
            cNo[nLeft + j].config(fg = 'red')
            cMarker=tk.Label(win, text = ">", font=("Arial", winFontSize), fg = 'red')
            tIdxMarker=(nLeft + j - i)/2 + i + iLeft + 1
            cMarker.place(relx=tIdxMarker / (len(noArray)+1), rely = yOff, anchor='n')
            win.update()
            time.sleep(stepDelay)
            #display
            cNo[i].config(fg = 'black')
            cNo[nLeft + j].config(fg = 'red')
            #cNo[i].place(relx=(iLeft + i+1)/(len(noArray)+1), rely=yLineUp+0.1*Level, anchor='n')
            cNo[i].place(rely=yPos, anchor='n')
            cMarker.destroy()
            win.update()
            time.sleep(stepDelay)
            
            #sort
            Data[k] = dataRight[j]
            #
            cNo[nLeft + j].destroy()
            pNo[k-pILeft].config(text = Data[k], fg = 'red')
            win.update()
            time.sleep(stepDelay)
            #
            pNo[k-pILeft].config(text = Data[k], fg = 'black')
            win.update()
            time.sleep(stepDelay)

            
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < nLeft:
        #display
        cNo[i].config(fg = 'red')
        #cNo[i].place(relx=(iLeft + i+1)/(len(noArray)+1), rely=yLineUp+0.1*Level-0.03, anchor='n')
        cNo[i].place(rely = yOff, anchor='n')
        win.update()
        time.sleep(stepDelay)

        #sort
        Data[k] = dataLeft[i]
        
        #
        cNo[i].destroy()
        pNo[k-pILeft].config(text = Data[k], fg = 'red')
        win.update()
        time.sleep(stepDelay)
        #
        pNo[k-pILeft].config(text = Data[k], fg = 'black')
        win.update()
        time.sleep(stepDelay)
        #

        #sort
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < nRight:
        #display
        cNo[nLeft + j].config(fg = 'red')
        cNo[nLeft + j].place(rely = yOff, anchor='n')
        win.update()
        time.sleep(stepDelay)

        #sort
        Data[k] = dataRight[j]
        
        #
        cNo[nLeft + j].destroy()
        pNo[k-pILeft].config(text = Data[k], fg = 'red')
        win.update()
        time.sleep(stepDelay)
        #
        pNo[k-pILeft].config(text = Data[k], fg = 'black')
        win.update()
        time.sleep(stepDelay)
        #sort 
        j += 1
        k += 1

def sortMerge(Data, iLeft, iRight, Level, prevNoList, prevILeft):
    if iLeft < iRight:
        #set medium index
        iMed = iLeft+(iRight-iLeft)//2
        
        cNoList=[]
        # display
        for i in range(iLeft, iRight+1):
            cNo = tk.Label(win, text = Data[i], font=("Arial", winFontSize), fg = 'gray')
            cNo.place(relx=(i+1)/(len(noArray)+1), rely=yLineUp+0.1*Level, anchor='n')
            cNoList.append(cNo)
        cMarker = tk.Label(win, text = "|", font=("Arial", winFontSize))
        cMarker.place(relx=(iMed+1.5)/(len(noArray)+1), rely=yLineUp+0.1*Level, anchor='n')
        win.update()
        time.sleep(stepDelay)
        
        # Sort first and second halves
        sortMerge(Data, iLeft, iMed, Level+1, cNoList, iLeft)
        sortMerge(Data, iMed+1, iRight, Level+1, cNoList, iLeft)
        sortMergeData(Data, iLeft, iMed, iRight, Level, cNoList, prevNoList, prevILeft)
        
        #win.update()
        #time.sleep(stepDelay)
        for i in range(len(cNoList)):
            cNoList[i].destroy()
        cMarker.destroy()
        win.update()
        time.sleep(stepDelay)        
 
def cMergeSort():
    global noArray, noList
    for i in range(len(noList)):
        noList[i].destroy()

    L=noArray.copy()
    noList=[]

    for i in range(len(noArray)):
        tNo = tk.Label(win, text = noArray[i], font=("Arial", winFontSize), fg = 'gray')
        tNo.place(relx=(i+1)/(len(noArray)+1), rely=yLineUp, anchor='n')
        noList.append(tNo)
    win.update()
    time.sleep(stepDelay)
    
    Level=1
    sortMerge(L, 0, len(L)-1, Level, noList, 0)

def cAnimFaster():
    global stepDelay, animationDelay
    if stepDelay>0.1:
        stepDelay=round(10*(stepDelay-0.1))/10
        animationDelay=0.25*stepDelay        
        inputSpeed.delete('1.0', tk.END)
        inputSpeed.insert(tk.END, stepDelay)
        
def cAnimSlower():
    global stepDelay, animationDelay
    if stepDelay>0.1:
        stepDelay=round(10*(stepDelay+0.1))/10
        animationDelay=0.25*stepDelay
        inputSpeed.delete('1.0', tk.END)
        inputSpeed.insert(tk.END, stepDelay)

xWinSize=1024
yWinSize=768
noSample=10
stepDelay=0.5
animationDelay=0.25*stepDelay
animationAngleStep=20
winFontSize=20
yLineUp=0.4
yCompare=0.5

noArray=[]
widgetList=[]
noList=[]

#Create an instance of tkinter frame
win=tk.Tk()
win.title("Sorting Examples")

#Define the geometry of window
win.geometry("1024x768")

#number of samples input
inputText = tk.Text(win, height = 1, width = 5, bg = "light yellow", font=("Arial", winFontSize))
inputText.place(relx=0.1, rely=0.1, anchor='n')
inputText.insert(tk.END, noSample)

bNoSample = tk.Button(win, text = "Number of items",  command = cNoSample, font=("Arial", winFontSize))
bNoSample.place(relx=0.25, rely=0.1, anchor='n')

bRandomize = tk.Button(win, text = "Randomize number",  command = cRandomize, font=("Arial", winFontSize))
bRandomize.place(relx=0.5, rely=0.1, anchor='n')

inputSpeed = tk.Text(win, height = 1, width = 5, bg = "light yellow", font=("Arial", winFontSize))
inputSpeed.place(relx=0.1, rely=0.2, anchor='n')
inputSpeed.insert(tk.END, stepDelay)

bDelay = tk.Button(win, text = "Animation delay",  command = cAnimationDelay, font=("Arial", winFontSize))
bDelay.place(relx=0.25, rely=0.2, anchor='n')

bFaster = tk.Button(win, text = "Faster",  command = cAnimFaster, font=("Arial", winFontSize))
bFaster.place(relx=0.45, rely=0.2, anchor='n')

bSlower = tk.Button(win, text = "Slower",  command = cAnimSlower, font=("Arial", winFontSize))
bSlower.place(relx=0.55, rely=0.2, anchor='n')

bSortFirst = tk.Button(win, text = "Bogo sort",  command = cBogo, font=("Arial", winFontSize))
bSortFirst.place(relx=0.1, rely=0.3, anchor='n')

bSortFirst = tk.Button(win, text = "First-comes-first sort",  command = cFirstComesFirst, font=("Arial", winFontSize))
bSortFirst.place(relx=0.3, rely=0.3, anchor='n')

bSortInsert = tk.Button(win, text = "Insertion sort",  command = cInsertionSort, font=("Arial", winFontSize))
bSortInsert.place(relx=0.5, rely=0.3, anchor='n')

bSortBubble = tk.Button(win, text = "Bubble sort",  command = cBubbleSort, font=("Arial", winFontSize))
bSortBubble.place(relx=0.7, rely=0.3, anchor='n')

bSortMerge = tk.Button(win, text = "Merge sort",  command = cMergeSort, font=("Arial", winFontSize))
bSortMerge.place(relx=0.9, rely=0.3, anchor='n')

win.mainloop()