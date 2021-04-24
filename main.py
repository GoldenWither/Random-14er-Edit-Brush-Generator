#########################
#init ###################
#########################
#import libraries
from tkinter import *
from tkinter import ttk
import random, os

#change current working directory to where the script was ran
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("Block Palettes")

#########################
#the start of everthing #
#########################
def main():
    #create variables
    global brMin, brMax

    #get variables
    brMin = int(brMinBox.get())
    brMax = int(brMaxBox.get())

    #start printing
    outputTxt.delete("1.0", END)

    for i in range(int(numBrushesBox.get())):
        outputTxt.insert(END, "Brush " + str(i + 1) + ":\n")
        outputTxt.insert(END, " ".join((brushType(), operation())))
        outputTxt.insert(END, "\n\n")

#########################
#generate brush type ####
#########################
def brushType():
    brushChosen = random.randint(0, 10)
    #brushChosen = 6

    if (brushChosen == 0):
        return(" ".join(("b", str(random.randint(brMin, brMax)), str(random.randint(1, 10)), str(random.randint(brMin, brMax)))))
    elif (brushChosen == 1):
        return(" ".join(("col", )))
    elif (brushChosen == 2):
        return(" ".join(("cube", str(random.randint(brMin, brMax)))))
    elif (brushChosen == 3):
        return(" ".join(("cyl", str(random.randint(brMin, brMax)), str(random.randint(brMin, brMax)), random.choice(["x","y","z"]), "0.5")))
    elif (brushChosen == 4):
        return(" ".join(("d", str(random.randint(brMin, brMax)))))
    elif (brushChosen == 5):
        return(" ".join(("e", str(random.randint(brMin, brMax)), str(random.randint(brMin, brMax)), str(random.randint(brMin, brMax)), "0.15")))
    elif (brushChosen == 6):
        return(" ".join(("hs", str(random.randint(brMin, brMax)), str(random.randint(brMin, brMax)), "0.5")))
    elif (brushChosen == 7):
        return(" ".join(("rote", roteParams())))
    elif (brushChosen == 8):
        return(" ".join(("s", str(random.randint(brMin, brMax)), "0.5")))
    elif (brushChosen == 9):
        return(" ".join(("sp", str(random.randint(brMin, brMax)), str(random.randint(brMin, brMax)), str(random.randint(brMin, brMax)))))
    elif (brushChosen == 10):
        return("v")

def roteParams():
    halfDist = random.randint(brMin, brMax)
    stringLength = random.randint(halfDist, brMax) * random.randint(int(stringLengthMinBox.get()) * 10 + 1, int(stringLengthMaxBox.get()) * 10) / 10
    return(" ".join((str(halfDist), str(stringLength))))

#########################
#generate operation #####
#########################
def operation():
    return(" ".join((link(), condition(random.randint(int(ifMinBox.get()), int(ifMaxBox.get()))))))

#generate links #########################
def link():
    return("")

#generate if statements #########################
def condition(count):
    if (count > 0):
        return(" ".join(("if", operator(), condition(count - 1))))
    return(action())

#generate if operators #########################
def operator():
    operatorChosen = random.randint(0, 19)

    #normal operators
    if (operatorChosen == 0):
        return(" ".join(("above", rangeNode(1, 5), getBlock())))
    elif (operatorChosen == 1):
        return(" ".join(("adj", rangeNode(0, 6), getBlock())))
    elif (operatorChosen == 2):
        return(" ".join(("adjh", rangeNode(0, 4), getBlock())))
    elif (operatorChosen == 3):
        return(" ".join(("adjv", rangeNode(0, 4), getBlock())))
    elif (operatorChosen == 4):
        return(" ".join(("ang", rangeNode(0, 90), numberNode(1, 5))))
    elif (operatorChosen == 5):
        return(" ".join(("at", numberNode(0, 5), numberNode(0, 5), numberNode(0, 5), getBlock())))
    elif (operatorChosen == 6):
        return(" ".join(("below", rangeNode(1, 5), getBlock())))
    elif (operatorChosen == 7):
        return(" ".join(("bl", numberNode(0, 15))))
    elif (operatorChosen == 8):
        return(" ".join(("exposed", numberNode(0, 6))))
    elif (operatorChosen == 9):
        return(" ".join(("near", getBlock(), numberNode(1, 5), rangeNode(1, 5))))
    elif (operatorChosen == 10):
        return(" ".join(("noise", noiseNode())))
    elif (operatorChosen == 11):
        return(" ".join(("odds", numberNode(0, 100))))
    elif (operatorChosen == 12):
        return(" ".join(("simplex", numberNode(2, 4), numberNode(0, 255), numberNode(1, 5))))
    elif (operatorChosen == 13):
        return(" ".join(("sky", numberNode(0, 15))))
    #logic operators
    elif (operatorChosen == 14):
        return(" ".join(("and", operator(), operator())))
    elif (operatorChosen == 15):
        return(" ".join(("anyof", anyof())))
    elif (operatorChosen == 16):
        return(" ".join(("not", operator())))
    elif (operatorChosen == 17):
        return(" ".join(("or", operator(), operator())))
    elif (operatorChosen == 18):
        return(" ".join(("xor", operator(), operator())))
    #no special operator
    elif (operatorChosen == 19):
        return(getBlock())

#anyof logic operator
def anyof():
    total = random.randint(int(anyofMinBox.get()), int(anyofMaxBox.get()))
    count = random.randint(1, total)
    returnString = ""

    #add operators on the end of anyof
    for i in range (total - 1):
        returnString += (operator() + " ")
    returnString += operator()
    return(" ".join((str(count), str(total), returnString)))

#noise node
def noiseNode():
    noiseChosen = random.randint(0, 10)

    if (noiseChosen == 0):
        return(" ".join(("Cellular", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5), noiseCellularDist())))
    elif (noiseChosen == 1):
        return(" ".join(("Cubic", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5))))
    elif (noiseChosen == 2):
        return(" ".join(("CubicFractal", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5), noiseFractalParams())))
    elif (noiseChosen == 3):
        return(" ".join(("Perlin", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5))))
    elif (noiseChosen == 4):
        return(" ".join(("PerlinFractal", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5), noiseFractalParams())))
    elif (noiseChosen == 5):
        return(" ".join(("Simplex", str(random.randint(2, 4)), numberNode(0, 255), numberNode(1, 5))))
    elif (noiseChosen == 6):
        return(" ".join(("SimplexFractal", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5), noiseFractalParams())))
    elif (noiseChosen == 7):
        return(" ".join(("Value", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5))))
    elif (noiseChosen == 8):
        return(" ".join(("ValueFractal", str(random.randint(2, 3)), numberNode(0, 255), numberNode(1, 5), noiseFractalParams())))
    elif (noiseChosen == 9):
        return(" ".join(("WhiteNoise", str(random.randint(2, 4)), numberNode(0, 255), numberNode(1, 5))))
    elif (noiseChosen == 10):
        return(" ".join(("WhiteNoiseInt", str(random.randint(2, 4)), numberNode(0, 255), numberNode(1, 5))))

#ditance setting for cellular noise
def noiseCellularDist():
    chosenCellularDist = random.randint(0, 2)

    if (chosenCellularDist == 0):
        return("Euclid")
    elif (chosenCellularDist == 1):
        return("Manhattan")
    elif (chosenCellularDist == 2):
        return("Natural")

#settings for fractal noise (down here to split things up)
def noiseFractalParams():
    return(" ".join((str(random.randint(0, 5)), str(random.randint(0, 5)), "0.5", "0")))

#number nodes #########################
def numberNode(numMin, numMax):
    numberChosen = random.randint(1, int(numberWeightBox.get()) + int(randrangeWeightBox.get()) + int(randnoiseWeightBox.get()))

    #pick which number node to use based off weights
    if (numberChosen <= int(numberWeightBox.get())):
        return(str(random.randint(numMin, numMax)))
    elif (numberChosen <= int(numberWeightBox.get()) + int(randrangeWeightBox.get())):
        return(" ".join(("randrange", twoRangeNums(numMin, numMax))))
    else:
        return(" ".join(("randnoise", twoRangeNums(numMin, numMax), noiseNode())))

#range node
def rangeNode(rangeMin, rangeMax):
    return(" ".join(("range", twoRangeNums(rangeMin, rangeMax))))

#two orders numbers (for range nodes)
def twoRangeNums(rangeMin, rangeMax):
    rangeNum1 = random.randint(rangeMin, rangeMax)
    rangeNum2 = random.randint(rangeMin, rangeMax)
    if (rangeNum1 < rangeNum2):
        return(" ".join((str(rangeNum1), str(rangeNum2))))
    return(" ".join((str(rangeNum2), str(rangeNum1))))

#generate action ####################
def action():
    #actionChosen = random.randint(0, 7)
    actionChosen = 6

    if (actionChosen == 0):
        return(" ".join(("biome", )))
    elif (actionChosen == 1):
        return(" ".join(("br", )))
    elif (actionChosen == 2):
        return(" ".join(("macro", )))
    elif (actionChosen == 3):
        return(" ".join(("multinoise", )))
    elif (actionChosen == 4):
        return(" ".join(("noiseat", )))
    elif (actionChosen == 5):
        return(" ".join(("replace", getBlock(), getBlock())))
    elif (actionChosen == 6):
        return(" ".join(("set", getBlock())))
    elif (actionChosen == 7):
        return(" ".join(("smallruin", )))

#########################
#file reading ###########
#########################
#get block from file #########################
def getBlock():
    #determine the number of blocks in the file
    with open(fileChosen.get()) as f:
        for i, line in enumerate(f):
            pass
        blockLines = i;

    #choose block
    blockChosen = random.randint(0, blockLines)
    with open(fileChosen.get()) as f:
        for i, line in enumerate(f):
            if i == blockChosen:
                strippedLine = line.strip()
                return(strippedLine)
            
#write output to file #########################
def outputToFile():
    #change directory back
    os.chdir("../")

    f = open("Brush Output.txt", "a")
    
    if (os.path.getsize("Brush Output.txt") != 0):
        f.write("----------\n\n\n")

    #check weather brush numbers should appear
    if(outputExtra.get() == 1):
        f.write(outputTxt.get("1.0", END))
    else:
        outputLines = outputTxt.get("1.0", END).splitlines()
        for i, line in enumerate(outputLines):
            if(i % 3 == 1):
                f.write(line)
                f.write("\n")
        f.write("\n\n")
    f.close()

    #change directory forward again
    os.chdir("Block Palettes")

#########################
#set up window ##########
#########################
root = Tk()
root.title("Random 14erEdit Brush Generator")

#add objects #########################

#main notebook #########################
#https://www.pythontutorial.net/tkinter/tkinter-notebook/
settingsNtb = ttk.Notebook(root)
settingsNtb.grid(column=0, row=1, rowspan=13, sticky="ns")

#main tabs
generalTab = ttk.Frame(settingsNtb)
advTab = ttk.Frame(settingsNtb)

#advanced notebook
settingsAdvNtb = ttk.Notebook(advTab)
settingsAdvNtb.grid(column=0, row=2)

#advanced tabs
brushesTab = ttk.Frame(settingsAdvNtb)
operatorsTab = ttk.Frame(settingsAdvNtb)
numberTab = ttk.Frame(settingsAdvNtb)

#add tabs
settingsNtb.add(generalTab, text="General")
settingsNtb.add(advTab, text="Advanced")
settingsAdvNtb.add(brushesTab, text="Brushes")
settingsAdvNtb.add(operatorsTab, text="Operators")
settingsAdvNtb.add(numberTab, text="Numbers")

#settings #########################
settingsLbl = Label(root, text="Settings", relief="ridge")
settingsLbl.grid(column=0, row=0, columnspan=2)

brMinLbl = Label(generalTab, text="Brush size MIN:", width=21, anchor="e")
brMinLbl.grid(column=0, row=0)

brMinBox = Entry(generalTab, width=5)
brMinBox.insert(0, "1")
brMinBox.grid(column=1, row=0)

brMaxLbl = Label(generalTab, text="Brush size MAX:", width=21, anchor="e")
brMaxLbl.grid(column=0, row=1)

brMaxBox = Entry(generalTab, width=5)
brMaxBox.insert(0, "30")
brMaxBox.grid(column=1, row=1)

ifMinLbl = Label(generalTab, text="Condition number MIN:", width=21, anchor="e")
ifMinLbl.grid(column=0, row=2)

ifMinBox = Entry(generalTab, width=5)
ifMinBox.insert(0, "0")
ifMinBox.grid(column=1, row=2)

ifMaxLbl = Label(generalTab, text="Condition number MAX:", width=21, anchor="e")
ifMaxLbl.grid(column=0, row=3)

ifMaxBox = Entry(generalTab, width=5)
ifMaxBox.insert(0, "3")
ifMaxBox.grid(column=1, row=3)

nestMinLbl = Label(generalTab, text="Nested brushes MIN:", width=21, anchor="e")
nestMinLbl.grid(column=0, row=4)

nestMinBox = Entry(generalTab, width=5)
nestMinBox.insert(0, "0")
nestMinBox.grid(column=1, row=4)

nestMaxLbl = Label(generalTab, text="Nested brushes MAX:", width=21, anchor="e")
nestMaxLbl.grid(column=0, row=5)

nestMaxBox = Entry(generalTab, width=5)
nestMaxBox.insert(0, "2")
nestMaxBox.grid(column=1, row=5)

numBrushesLbl = Label(generalTab, text="Brushes to generate:", width=21, anchor="e")
numBrushesLbl.grid(column=0, row=6)

numBrushesBox = Entry(generalTab, width=5)
numBrushesBox.insert(0, "3")
numBrushesBox.grid(column=1, row=6)

#advanced settings #########################
#brushes
stringLengthMinLbl = Label(brushesTab, text="rote string multiplier MIN:", width=21, anchor="e")
stringLengthMinLbl.grid(column=0, row=0)

stringLengthMinBox = Entry(brushesTab, width=5)
stringLengthMinBox.insert(0, "2")
stringLengthMinBox.grid(column=1, row=0)

stringLengthMaxlbl = Label(brushesTab, text="rote string multiplier MAX:", width=21, anchor="e")
stringLengthMaxlbl.grid(column=0, row=1)

stringLengthMaxBox = Entry(brushesTab, width=5)
stringLengthMaxBox.insert(0, "3")
stringLengthMaxBox.grid(column=1, row=1)

#operators
anyofMinLbl = Label(operatorsTab, text="anyof conditions MIN:", width=21, anchor="e")
anyofMinLbl.grid(column=0, row=0)

anyofMinBox = Entry(operatorsTab, width=5)
anyofMinBox.insert(0, "2")
anyofMinBox.grid(column=1, row=0)

anyofMaxLbl = Label(operatorsTab, text="anyof conditions MAX:", width=21, anchor="e")
anyofMaxLbl.grid(column=0, row=1)

anyofMaxBox = Entry(operatorsTab, width=5)
anyofMaxBox.insert(0, "4")
anyofMaxBox.grid(column=1, row=1)

#numbers
numberWeightLbl = Label(numberTab, text="Normal number bias:", width=21, anchor="e")
numberWeightLbl.grid(column=0, row=0)

numberWeightBox = Entry(numberTab, width=5)
numberWeightBox.insert(0, "70")
numberWeightBox.grid(column=1, row=0)

randrangeWeightLbl = Label(numberTab, text="Random range bias:", width=21, anchor="e")
randrangeWeightLbl.grid(column=0, row=1)

randrangeWeightBox = Entry(numberTab, width=5)
randrangeWeightBox.insert(0, "20")
randrangeWeightBox.grid(column=1, row=1)

randnoiseWeightLbl = Label(numberTab, text="Noise range bias:", width=21, anchor="e")
randnoiseWeightLbl.grid(column=0, row=2)

randnoiseWeightBox = Entry(numberTab, width=5)
randnoiseWeightBox.insert(0, "10")
randnoiseWeightBox.grid(column=1, row=2)

#output #########################
outputLbl = Label(root, text="Output", relief="ridge")
outputLbl.grid(column=2, row=0, columnspan=2)

#scrollbars
outputSbY = Scrollbar(root, orient="vertical")
outputSbY.grid(column=4, row=1, rowspan=10, sticky="ns")
outputSbX = Scrollbar(root, orient="horizontal")
outputSbX.grid(column=2, row=11, columnspan=2, sticky="ew")

outputTxt = Text(root, height=10, width=30, wrap="none", xscrollcommand=outputSbX.set, yscrollcommand=outputSbY.set)
outputTxt.grid(column=2, row=1, columnspan=2, rowspan=10, sticky="nsew")

outputSbX.config(command=outputTxt.xview)
outputSbY.config(command=outputTxt.yview)

generateBtn = Button(root, text="Generate", command=main)
generateBtn.grid(column=2, row=12, sticky="ew")

#dropdown
allFiles = os.listdir()
textFiles = []
for i in range (len(allFiles)):
    if (allFiles[i].endswith(".txt")):
        textFiles.append(allFiles[i])

fileChosen = StringVar(root)
fileChosen.set(textFiles[0])
fileMenu = OptionMenu(root, fileChosen, *textFiles)
fileMenu.config(width=10, anchor="w")
fileMenu.grid(column=2, row=13)

outputFileBtn = Button(root, text="Output to File", command=outputToFile)
outputFileBtn.grid(column=3, row=12, sticky="ew")

outputExtra=IntVar()
outputExtraChk = Checkbutton(root, text="Output brush numbers", variable=outputExtra, offvalue=0, onvalue=1)
outputExtraChk.grid(column=3, row=13)
outputExtraChk.select()

#run the window #########################
root.mainloop()