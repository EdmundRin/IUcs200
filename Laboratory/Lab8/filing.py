import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()


def outPrint(aString):
    """
    Print the string in a way to easily represent the end of a file
    """
    print("*"*30)
    print(aString,end="")
    print("*EOF*")


def readingEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("Laboratory/Lab8/blank.txt","r") as someFile:
        contents = someFile.read()
    return contents


def readingEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("Laboratory/Lab8/blank.txt","r") as someFile:
        contents = someFile.readlines()
    outPrint(contents)
    return contents


def writeEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    stuff = ["a","b","c","d","e","f"]
    with open ("Laboratory/wrong.txt","w") as fileToWrite:
        for s in stuff:
            fileToWrite.write(s+"\n")


def writeEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open ("Laboratory/Lab8/wrong.txt","a") as fileToWrite:
        for s in range(4):
            fileToWrite.write("more\n")



def FileIO_example(filePath, newFile): 
    '''
    Given a file path, we want to open the file, read each line and count
    the number of vocabs in each line. We will write to
    the newFile the lines that have more than 5 vocabs and clean them up
    (use strip). You are provided the path to the file we want to write.

    Return number of all lines that has less than or equal to 5 vocabs.
    '''
    with open(filePath,"r") as fileToR:
        wordC = fileToR.read()
    splitted_line = wordC.split("\n")
    count = 0
    goodline = []
    for line in splitted_line:
        splitted_line = line.split(" ")
        if len(splitted_line) <= 5:
            count += 1
        else:
            goodline.append(line.split())
    with open(newFile,"w") as toWrite:
        for line in goodline:
            toWrite.write(str(line) + "\n")
        return count



def calculation(filePath):
    '''
    Given a file path, we want to open the file, read each line. in each line we have a number
    we want to calculate the summation of numbers in last 2 lines and write the sum at the end of the 
    file we read from it. (eah time that we run this function we add one number of fibonacci series to the file)
    '''
    with open(filePath,"r") as fileToCal:
        numC = fileToCal.read()
    numlist = numC.split("\n")
    numlist.remove("")
    sum = 0
    for num in numlist:
        sum += int(num)
    numlist += [sum]
    with open(filePath,"w") as toWrite:
        for i in numlist:
            toWrite.write(str(i) + "\n")
    

if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readex1 = readingEx1()
    print("~"*30)
    print(readex1, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    
    readex2 = readingEx2()
    print("~"*30)
    print(readex2, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    print()

    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(FileIO_example("Laboratory/Lab8/testing.data", "Laboratory/Lab8/clean.txt")))

    calculation("Laboratory/Lab8/calculation.txt")