#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#NOTES please read


###~~~~THIS PROGRAM RUNS ON PYTHON3~~~~###
#NEXT IMPROVEMENT WOULD BE TO SPILT EACH FUNCTION UP INTO INDIVIDUAL FILES RATHER THAN A PROCEDRAL FILE
#The ~ separates chunks of categorized code
#




#INDEX
#Any reference to 'geometry manager' is just the way tkinter manages how widgets interact in a box. Basically defines what the layout of a box is. There are two types of manager .pack and .grid (both work in simmilar ways)
# .delete and .insert is used a lot in this code. .delete will remove what ever text is in a tkinter widget (like a entry box) and .insert will insert any text into a widget.
# return() is also used a lot in this code aswell. if nothing is in the brackets of return() it simply exits the function. anything inside the return e.g return(value) means you can set a variable to the outcome of a function because the function returns the value
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#The following commands import modules the program may need
#Also some prechecks



#THIS CODE REQUIRES ALL OF THE FOLLOWING MODULES/LIBRARIES. IF YOU DONT HAVE THEM INSTALLED FEEL FREE TO USE PIP TO INSTALL IT OR USE THE EXECUTEABLE IN THE FILE.

try:#trys to import all modules
    import logging #for logging program history
    import tkinter#imports tkinter
    from tkinter import *#imports all tkinter widgets
    from tkinter import ttk#tk libs for GUI
    from tkinter import messagebox#messagebox for tk
    from tkinter import filedialog#file search for tk
    import os#Os libs for file management
    import os.path#directory manager
    from os import listdir#directory control, allows dynamic path splitting
    from os.path import isfile, join#allows adding and analysing paths
    import math
    import smtplib  # for emails
    import string  # for getting lists of punctuation or letters 
    import re  # for removingmulitple spaces in a string module known as regular expression
    from itertools import groupby  # This is used to remove multiple punctuation from a string
    from difflib import SequenceMatcher #For matching keywords together
except Exception as e:#if error in import stage #shows 
    print('''WARNING!!! YOU DO NOT HAVE ALL THE MODULES REQUIRED FOR THIS PROGRAM TO RUN
THIS MAY LEAD TO INSTABILITY IN PROGRAM OR FATAL ERRORS. CONTINUE USING THIS PROGRAM WITH CAUTION. CONTACT THE DEVELOPER IF YOU HAVE ISSUE INSTALLING MODULES.
PLEASE SEE README IN PROGRAMFILES TO SEE HOW TO INSTALL THE MODULES REQUIRED. YOU CAN ALSO USE THE EXECUTEABLE FILE ATTACHED IN THE PROGRAM FILES. THIS WILL ALWAYS RUN REGARDLESS. USE THE NEXT LINE
TO FIND OUT WHAT MODULE YOU NEED.\n''',e) #prints warning first incase error with tkinter

    messagebox.showwarning(title = "FATAL WARNING",message = ('''WARNING!!! YOU DO NOT HAVE ALL THE MODULES REQUIRED FOR THIS PROGRAM TO RUN
THIS MAY LEAD TO INSTABILITY IN PROGRAM OR FATAL ERRORS. CONTINUE USING THIS PROGRAM WITH CAUTION. CONTACT THE DEVELOPER IF YOU HAVE ISSUE INSTALLING MODULES.
PLEASE SEE README IN PROGRAMFILES TO SEE HOW TO INSTALL THE MODULES REQUIRED. YOU CAN ALSO USE THE EXECUTEABLE FILE ATTACHED IN THE PROGRAM FILES. THIS WILL ALWAYS RUN REGARDLESS. USE THE NEXT LINE
TO FIND OUT WHAT MODULE YOU NEED.\n''',e))#shows message box


#Here the program finds all of the directories of folders the program needs

programfilesdir = os.getcwd()#Gets the folder where program files are stored
desktop = (programfilesdir, os.path.join(os.environ["HOMEPATH"], "Desktop"))[1] #Gets desktop of users pc

icon = programfilesdir +"\icon.ico"  #directory of icon for window
tutDir = programfilesdir + r"\tutorialcheck.txt" #directory of the file that checks if this is a new installation
tutorialImgsDir = programfilesdir + "\TutorialPics"#Pictures for tutorial


os.chdir('..') #Goes back a directory
root = os.getcwd()#Gets path 
#directories of the required system files
iaDir = root + r"\USERCREATEDFILES\IntendedAge" 
keywordDir = root + r"\USERCREATEDFILES\Keywords"
textsDir = root + r"\USERCREATEDFILES\Texts"



#
#
#
#
#
#
#
#These two variables are for dyanmic windows due to python3 handling global vars
labelCount = 0
tutSC = 0
#
logging.basicConfig(filename="programlogs.log", level=logging.INFO)#this runs in background and logs events.

tutCheck = True ###Tells program if its the first time the program is used. Chnaged depending on textfile
##
os.chdir(root)
#checking tutorial file
with open(tutDir,'r') as file:
    if file.read() == '0':
        tutCheck = True
    else:
        tutCheck = False
#making the main gui. Its in a fucntion so that it can be stopped easily.
def mainbox():


    main = Tk() #This creates the main box
    main.iconbitmap(icon)#sets icon on box
    main.state("normal")#Sets window to a normal state. Make sures it doesnt disable at some point
    main.configure(background="black")#Stes background colour

    #
    #
    #
    #
    #
    #
    #
    #ALL OF THE FOLLOWING FUNCTIONS ARE COMPLEX ONES/ ONES THAT REQUIRE THEIR OWN WINDOW.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    def tutorial():#Tutorial function
        tutBox = Tk()#Creates a box
        tutBox.attributes("-topmost", True)

        def refreshLabels():#A function that changes text and pictures depending on stage in the tutorial
            #an if statement for each stage in the tutorial
            if tutSC == 0:
                backButton['state'] = 'disabled'
                textLabel['text'] = '''Welcome to the Reading Age Calculator. This is the tutorial for the program. Click continue.'''
            if tutSC == 1:
                backButton['state'] = 'normal'
                picLabel['image'] = img1
                textLabel['text'] = '''You will be greeted with this window when the program opens.'''
            if tutSC == 2:
                backButton['state'] = 'normal'
                picLabel['image'] = img2
                textLabel['text'] = '''Simply fill in the two entry boxes and click 'Calculate' to get your results.
The big text entry box is for your text and the little one on the bottom right is for your intended reading grade'''
            if tutSC == 3:
                backButton['state'] = 'normal'
                picLabel['image'] = img3
                textLabel['text'] = '''If you want to save your text on the programs database simply click the 'Save' button on the top Left
A window will pop up asking for the keywords and the name of the text'''
            if tutSC == 4:
                backButton['state'] = 'normal'
                picLabel['image'] = img4
                textLabel['text'] = '''Simply click 'Yes' to save your file!'''
            if tutSC == 5:
                backButton['state'] = 'normal'
                picLabel['image'] = img5
                textLabel['text'] = '''If you want to open your own text file from somewhere else, click 'Open'.
You have to navigate to your file to caclulate its reading age.'''
            if tutSC == 6:
                backButton['state'] = 'normal'
                picLabel['image'] = img7
                textLabel['text'] = '''To search for a file in the database by a keyword;
Click 'Search' then 'Search By Keywords'. Type in a keyword and click 'Search'. '''
            if tutSC == 7:
                backButton['state'] = 'normal'
                picLabel['image'] = img9
                textLabel['text'] = '''To view all saved files click 'Search' then 'Search in Existing Library'.'''
            if tutSC == 8:
                backButton['state'] = 'normal'
                picLabel['image'] = img10
                textLabel['text'] = '''A pop up will show all the stored files'''
            if tutSC == 9:
                backButton['state'] = 'normal'
                picLabel['image'] = img11
                textLabel['text'] = '''To send the results to an email simply click 'Send Results' and
type in your email. Click 'Send' and its done!'''
            if tutSC == 10:
                backButton['state'] = 'normal'
                picLabel['image'] = img12
                textLabel['text'] = '''To report a bug click 'Report' and explain your problem.'''
            if tutSC == 11:
                backButton['state'] = 'normal'
                picLabel['image'] = img14
                textLabel['text'] = '''Use the Clear boxes on the bottom of the window for easy use.'''
            if tutSC == 12:
                backButton['state'] = 'normal'
                picLabel['image'] = img15
                textLabel['text'] = '''If you want to view this Tutorial again click 'Tutorial'.'''
            if tutSC == 13:
                backButton['state'] = 'normal'
                continueButton['text'] = 'Finish'
                picLabel['image'] = ''
                textLabel['text'] = '''Thats the tutorial! A lot of work went into
this program so please enjoy!
PLEASE NOTE THIS! - THE READING AGE VALUE IS A US GRADE. OPEN TOOLS AND CHECK THE CONVERSION CHART
If entering a large text (300-400 pages) you may need a higher performance PC'''
            if tutSC == 14:#Means that tutorial is finished
                tutBox.destroy()#deletes box
                DisplayCodeInfo()

                
        #A function for the back and continue button. Just changes the counter. and refreshes the page         
        def contFunc():
            global tutSC#Looks for this var since its outside scope of function
            tutSC += 1
            refreshLabels()
        def backFunc():
            global tutSC
            tutSC = tutSC-1
            refreshLabels()
        #Constructing tutorial gui
        tutBox.title("Tutorial")#Sets title
        tutBox.resizable(0, 0)#Makes it un sizeable by user
        os.chdir(tutorialImgsDir)#changes dir
        #Following sets a variable to each image
        img1 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\1.png')
        img2 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\2.png')
        img3 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\3.png')
        img4 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\4.png')
        img5 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\5.png')
        img6 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\6.png')
        img7 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\7.png')
        img8 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\8.png')
        img9 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\9.png')
        img10 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\10.png')
        img11 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\11.png')
        img12 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\12.png')
        img13 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\13.png')
        img14 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\14.png')
        img15 = PhotoImage(master = tutBox, file = tutorialImgsDir+r'\15.png')
        

        picLabel = Label(tutBox,image = '')#text in box
        picLabel.grid(row = 0,column = 0,columnspan = 2)#geometry manager
        textLabel = Label(tutBox,text = 'hello world')#text in box
        textLabel.grid(row=1,column=0,columnspan=2)#Geometru manager
        backButton = Button(tutBox,text = "Back",width=50,state = "normal",command = backFunc)#back button
        backButton.grid(row=2,column = 0)#geometry manager
        continueButton = Button(tutBox,text = "Continue",width=50,command = contFunc)#continue button
        continueButton.grid(row=2,column=1)#geometry manager

        refreshLabels()#a refresh


        



        tutBox.mainloop()#keeps box running until otherwise

    #
    #
    #
    #
    #
    #
    #
    #Here I am making functions that require extra windows


    def displayGtoA():
        displaybox = Tk()#makes box
        displaybox.attributes("-topmost", True)#Keeps box at top
        img = PhotoImage(master = displaybox, file = programfilesdir+r'\agetogradechart.png')
        Label(displaybox,text='''The picture displays a chart of conversions between the reading age provided by the program and the real age
(since the reading age equation produces an US GRADE. Find your value in the US GRADE and that will tell you the REAL AGE.
A value to high means that it is difficult to read.
A value far below means a text that is easy to read.''').pack()#Info label
        Label(displaybox,image = img).pack()#image label creation

        displaybox.mainloop()#keeps box running
    def DisplayCodeInfo():#function that displays some info on the program
        messagebox.showinfo(title = "Info", message = '''Developed Solely By Rajib Ahmed
Created in 2018
Program is currently in Version 2
Running on Python 3 - No support for Python 2(You may have some luck running it)

Recommended System Requirements:
    Processors:
        Intel® Core™ i5 processor 4300M at 2.60 GHz or 2.59 GHz (1 socket, 2 cores, 2 threads per core), 8 GB of DRAM
        Intel® Xeon® processor E5-2698 v3 at 2.30 GHz (2 sockets, 16 cores each, 1 thread per core), 64 GB of DRAM
        Intel® Xeon Phi™ processor 7210 at 1.30 GHz (1 socket, 64 cores, 4 threads per core), 32 GB of DRAM, 16 GB of MCDRAM (flat mode enabled)
    Disk space: 2 to 3 GB
    Operating systems: Windows® 10, macOS*, and Linux*
You may need a higher end pc for calculating large texts (300+ pages long)
You may get unexpected errors when trying to input and calculate a text with foreign symbols (not the english alphabet etc)


    


''')
    def report():#Function for a report box
        reportbox = Tk()#creates box
        reportbox.attributes("-topmost", True)

        def reportsend():  #Creating a function to actually send the report
            try:
                
                # sending the report to myself
                os.chdir('...')#goes back a dir
                with open('programlogs.log','r') as file:
                    log = file.read()#gets logs
                fullreportinfo = (reportinfo.get(),log)  #GRABS INFO
                email = "readingagecalculator@gmail.com"   #THE EMAIL THAT WILL BE SENT TO
                server = smtplib.SMTP('smtp.gmail.com', 587)  #CONNECTION TO SERVER
                server.starttls()#starts connection
                server.login("readingagecalculator@gmail.com", "HelloWorld.123")  #SERVER LOGIN
                # sending a message
                msg = 'Subject: {}\n\n{}'.format("Report Info",
                                                 fullreportinfo)  # this adds a header/subject in the email #msg creates the message
                server.sendmail("readingagecalculator@gmail.com", email, msg)  #Sending the message
                server.quit()  #Safe disconnection from server
                reportbox.destroy()  #Removing the box
            except Exception as e:
                # incase there is an error whilst sending
                messagebox.showwarning(title="Error 2",message=e)


        #
        #
        #
        #
        #
        #
        #
        #
        #Creating the box to report in

        messagebox.showinfo(title="Report Notice",
                            message="Please report responisbly. These reports go straight to the developer")#warning message
        reportbox.title("Report")#text in box
        Label(reportbox, text="Please explain your problem down below. Add any error codes you see").pack(side=TOP)#text in box
        reportinfo = Entry(reportbox)#Entry box 
        reportinfo.pack(side=TOP)#geometry manager

        Button(reportbox, text="Click here to report", command=reportsend).pack(side=TOP)#A button to finsh
        
        reportbox.mainloop()#keeps box running


    #FunCtion to send results
    def sendresults():
        messagebox.showinfo(title = "Notice",message = "The email will not contain the intended grade or grade difference")#Quick notice
        emailbox = Tk()#Creating a box
        emailbox.attributes("-topmost", True)#Keeps box at top

        def sendmail():#Func to send the email
            try:
                # access the server
                FullMessage = createmessage()#makes the message
                email = emailentrybox.get()#Gets the email entered
                server = smtplib.SMTP('smtp.gmail.com', 587)#Configs server connection
                server.starttls()#Starting connection
                
                server.login("readingagecalculator@gmail.com", "HelloWorld.123")#Logging in
                # sending a message
                msg = 'Subject: {}\n\n{}'.format("Info From The Reading Age Calculator", FullMessage)#Making mesasge
                msg = str(msg)
                server.sendmail("readingagecalculator@gmail.com", email, msg)#Sends mail
                server.quit()#End connection
                emailbox.destroy()#Destory box
            except Exception as e:#If fail occurs. This is for debug
                messagebox.showwarning(title="Error 2",message=e)

                # defing a new window

        Label(emailbox, text="Enter your email below please").pack(side=TOP)#Top label
        emailentrybox = Entry(emailbox)#Entry box for user
        emailentrybox.pack(side=TOP)#Geometry manager
        Button(emailbox, text="Click here to send", command=sendmail).pack(side=TOP)#Button to send email
        emailbox.mainloop()

    #SAVE HERE
    def save():#Function for saving
        global labelCount#Grabbing global vars
        labelCount = 0#Reset counter
        checknum = calculate()#Checking if the user entered anything
        if checknum == 1:
            return()
        text = retrieveInput()#Grabbing user input text
        keywordList = []#Creating keyowrd list
        filename1 = ''#Creating filename var
        intendedage = IntendedAge.get(0.0,"end-1c")#Grabbing intended age
        #Error checking intended age
        if intendedage.isalpha() == True:
            messagebox.showarning(title="Error 3",message="Enter a number for the intended age")
            return()
        if intendedage.replace(" ","") == "":
            messagebox.showwarning(title="Error 4",message="Enter an intended age")
            return()
        if intendedage == "Enter Intended Age  Here":
            messagebox.showwarning(title="Error 4",message="Enter an intended age")
            return()

        savebox = Tk()#Creating box
        savebox.attributes("-topmost", True)#Keeping box at top



            

        def saveContinue():#Function for continue button
            global labelCount#Grabbing global var
            checkValue = entrybox.get()#Grabbing value entered by user
            
            
            if labelCount != 5:#checks if entering filename or keyword
                if checkValue in keywordList:#checks if keyword has already been entered
                    messagebox.showwarning(title = "Error 5",message = "Choose a different keyword")#shows warning
                    return()#stops function
            

            if checkValue.replace(" ","") == "":#checks if nothing has been entered
                messagebox.showwarning(title = "Error 6",message = "Enter something into the entrybox")#shows warning
                return()#stops function
            #following checks at what stage in the save process you are
            #0-4 represents keywords 1-5
            #5 represents the filename
            
            if labelCount == 0:
                keywordList.append(checkValue)#adds value to keyword list
            if labelCount == 1:
                keywordList.append(checkValue)
            if labelCount == 2:
                keywordList.append(checkValue)
            if labelCount == 3:
                keywordList.append(checkValue)
            if labelCount == 4:
                keywordList.append(checkValue)
            if labelCount == 5:
                filename = checkValue#assigns filename
                YNBox = messagebox.askquestion("Save?","Would you like to save?")#asks to save
                if YNBox == 'yes':
                    saveInfo()#calls func to save everything
                    labelCount = 0#reset vars
                    return()#exit func
                else:
                    return()#exits func without calling save

            labelCount = labelCount+1#increases count to show what stage the user is on
            changeLabel()#calls func to reset labels
            entrybox.delete(0,'end')#erases current box value for user

            



        def saveInfo():#func to actually save what the user entered

            filename = entrybox.get()#aquires filename from user input
            savebox.destroy()#destroys box used to enter info

            os.chdir(textsDir)#changes current directory to where texts are stored
            
            try:
                with open(filename, 'w') as file:#saves text
                    file.write(text)

                os.chdir(keywordDir)#changes current dir to keywords dir


                with open(filename,'w') as file:#saves the keywords with new lines separating each line
                    for i in keywordList:
                        file.write(i)
                        file.write('\n')#

                os.chdir(iaDir)#changes current dir to intended age dir

                with open(filename,'w') as file:#saves intended age
                    file.write(intendedage)
            except:
                messagebox.showwarning(message = "An error occured with text conversion. You likely have foreign symbols in your text.",title="Error 15")
                

            message = "Saved under filename --  " + filename#generates a confirmation message

            messagebox.showinfo(message = message)#shows confirm message
            

        def saveBack():#function for the back button
            global labelCount #grabs global var
            del keywordList[-1]#removes the leading value in keyword list since the user is going back to enter another
                
            labelCount = labelCount - 1#changes what stage the user is on. (goes back one rather than forward 1)
            entrybox.delete(0,'end')#removes any input in user entry box
            changeLabel()#updates labels


        #creating a box for the user to enter the details in
        savebox.title("Save details")#sets box title
        commandLabel = Label(savebox,text='',width=60)#creates dynamic label for what to tell the user(dynamic because it changes)
        commandLabel.grid(row=0,column=0,columnspan=3)#geometry manager
        entrybox = Entry(savebox,width=60)#creates input box
        entrybox.grid(row=1,column=0,columnspan=3)#geometry manager
        backButton = Button(savebox,width=30,text="Back",command=saveBack,state='normal')#dynamic back button(only dynamic becuase we dont want the user to click back when entering keyword 1)
        backButton.grid(row=2,column=0)#geometry manager
        continueButton= Button(savebox,width=30,text="Continue",command = saveContinue)#dynamic continue button (dynamic so i can change text from 'continue' to 'save'
        continueButton.grid(row=2,column=1)#geometry manager



        def changeLabel():#function to update labels
            global labelCount #grabs global check var
            #if statements to check the labelCount to see what stage the user is at
            
            if labelCount == 0:
                commandLabel['text'] = 'Enter the 1st keyword'#updates label
                backButton["state"] = 'disabled'#updates state of button . sets it to disabled at keyword 1 since the user cant go back at that stage
            if labelCount == 1:
                commandLabel['text'] = 'Enter the 2nd keyword'
                backButton["state"] = 'normal'#reverts button to normal state (can be used)
            if labelCount == 2:
                commandLabel['text'] = 'Enter the 3rd keyword'
                backButton["state"] = 'normal'
            if labelCount == 3:
                commandLabel['text'] = 'Enter the 4th keyword'
                backButton["state"] = 'normal'
            if labelCount == 4:
                commandLabel['text'] = 'Enter the 5th keyword'
                backButton["state"] = 'normal'
            if labelCount == 5:
                commandLabel['text'] = 'Enter the name of the text'
                backButton["state"] = 'normal'
                continueButton['text'] = 'Save'

        changeLabel()#updates labels once all functions and boxes have been assigned

            

        savebox.mainloop()#keeps box running


            
            
        


                
    #OPEN HERE
    def openfile():#function to open file
        dirname = filedialog.askopenfilename(parent = main, title = "Please open a textfile")#opens file explorer inside program
        extension = os.path.splitext(dirname)[1]#grabs file extension
        if extension != ".txt":#checks file extentions
            messagebox.showwarning(title = "Error 7",message = "Please select a text file")#warning message
            return()#exit func

        with open(dirname,'r') as file:#reads file
            text = file.read()#grabs file text

        maintextbox.delete(0.0,END)#delete whatever in mainbox
        maintextbox.insert(0.0,text)#insert selected text

        

    def keywordSearch():#func for keyword searching

        


        def searchKeywords():#func to actually perform searching
            finalValue = 0#variable that Stores keyword metrics
            query = searchQuery.get()#gets search query
            os.chdir(keywordDir)#changes directory to keyword dir
            files = [f for f in listdir(keywordDir) if isfile(join(keywordDir, f))]#gets all files stored in dir
            if files == []:#checks if empty
                messagebox.showwarning(title = "Error 8", message="There are no stored files")#warning
                return()#exit func

            if query.replace(" ","") == "":#checks if no search query
                messagebox.showwarning(title = "Error 9",message="Enter a search query")#warning
                return()#exit func
            matchingfiles = []#variable stores the files and the keyword metric together in a multi dimensional list
            matchCheckList = []#just stores the metric to see if the search query is even close
            for i in files:#goes through each file
                finalValue = 0
                keywords = []#variable to store the keywords
                with open(i,'r') as file:
                    keywords = (file.read()).split('\n')#get keywords 

                keywords = [i.lower() for i in keywords]#turn each one to lower case
                tempList = []##variable to temporarily store one file plus its keyword metric
                
                for k in keywords:#goes through the keywords
                    value = SequenceMatcher(None, k, query).ratio()#this calculates keyword metric -- this metric is how much the query matches the keyword. Highest value is 1.)
                    if value>finalValue:#finalValue will only store the highest metric value
                        finalValue = value#changes final value
                    matchCheckList.append(value)#adds metric to checklist

                tempList.append(i)#adds filename to temporary list
                tempList.append(finalValue)#adds metric to temp list
                matchingfiles.append(tempList)#adds temp list to final list. This main list will have many every filename with its corresponding highets keyword metric value
                print(matchingfiles)
            print(matchCheckList)
            for i in matchCheckList:#Goes through list with only metrics
                if i>0.5:#checks if any file had a match of higher than 0.5
                    displayQuery('Keyword Metric (1 = 100%)',matchingfiles)#calls on display query with the data supplied
                    searchbox.destroy()#remove search box
                    return()#exit funtion

            messagebox.showinfo(message = "No matches found!")#if no good match-
            return()#-exit function

        def displayQuery(column2,treeVal):#function that displays results
            tree_columns = ("Filename",column2)#sets column titles with provided info
            tree_data = treeVal#sets the data in table with provided info
            root = Tk()#creates box
            root.attributes("-topmost", True)#keeps box above all
            msg = ttk.Label(root,wraplength="4i", justify="left", anchor="n",#creates a title above table
                padding=(10, 2, 10, 6),
                text=("These are the results yielded. The metric is a measure of how much your search query matches the keywords. Click an item to select it"))
            msg.grid(sticky='n',row=0)#geometry manager
            tree = ttk.Treeview(root,columns=tree_columns, show="headings")#Calls on tkinter treeview to make the table
            def selectItem(a):#func for when user selects a file
                curItem = tree.focus()#gets the position in table the user clicked
                filename = ((tree.item(curItem)['values'])[0])#gets corresponding filename attached to position
                os.chdir(textsDir)#changes dir to texts
                with open(filename,'r') as file:
                    text = file.read()#gets texts
                os.chdir(iaDir)#changes dir to intended reading age
                with open(filename,'r') as file:
                    intendedAge = file.read()#gets ira
                
                root.destroy()#delete select box

                #Following inserts the text and ira into the main boxes
                maintextbox.delete(0.0,END)
                maintextbox.insert(0.0,text)

                IntendedAge.delete(0.0,END)
                IntendedAge.insert(0.0,intendedAge)
                calculate()#calls on calculate to display all values
            tree.grid(column=0, row=1, sticky='nsew')#geometry manager for table
            tree.bind('<ButtonRelease-1>',selectItem)#binds the select item button to the mouse click
            for col in tree_columns:#for each column in table
                tree.heading(col, text=col.title(),
                    command=lambda c=col: sortby(self.tree, c, 0))#sets heading
            for item in tree_data:#for each item in the table
                tree.insert('', 'end', values=item)#inserts data from list provided

            root.mainloop()#keeps box running

                        
   
        searchBox = Tk()#create box for user to enter search query
        searchBox.attributes("-topmost", True)#keeps box above all other boxes
        Label(searchBox,text = "Search for a keyword below",width = 20).pack()#create label
        searchQuery = Entry(searchBox,width=20)#create entry box for user
        searchQuery.pack()#geometry manager
        Button(searchBox,command = searchKeywords,width = 20,text = "Search").pack()#button for user to click 
        searchBox.mainloop()#keeps box running



##
        


    def ageSearch():#func to search for ages
        def searchAge():#func that does main searching
            matchingfiles = []#stores files and ra with each one
            matchCheckList = []#just stores ra for check at end
            finalValue = 0#temp storage for ra

            os.chdir(textsDir)#change to dir with all files
            files = [f for f in listdir(keywordDir) if isfile(join(keywordDir, f))]#get all files
            if files == []:#checs if none stored
                messagebox.showwarning(title = "Error 10",message="There are no stored files")

                return()#exit func

            for i in files:#goes through each file

                with open(i,'r') as file:
                    text = file.read()#gets text of file

                
                tempList = []#temporary list for a text and its reading age

                #the following basically inserts the text into the main box. Calls on the reading age func to get the reading age and repeat
                maintextbox.delete(0.0,END)
                maintextbox.insert(0.0,text)

                readAge = int(readingagecounter())#get reading age

                tempList.append(i)#add file to temp list
                tempList.append(readAge)#add age to list
                matchingfiles.append(tempList)#add temp list to main list
                maintextbox.delete(0.0,END)#removes whatever in maintextbox
                

            displayQuery("Reading Age",matchingfiles)#calls on display query to display results
            return()

        def displayQuery(column2,treeVal):#function that displays results
            tree_columns = ("Filename",column2)#sets column titles with provided info
            tree_data = treeVal#sets the data in table with provided info
            root = Tk()#creates box
            root.attributes("-topmost", True)#keeps box above all
            msg = ttk.Label(root,wraplength="4i", justify="left", anchor="n",#creates a title above table
                padding=(10, 2, 10, 6),
                text=("These are the results yielded. The metric is a measure of how much your search query matches the keywords. Click an item to select it"))
            msg.grid(sticky='n',row=0)#geometry manager
            tree = ttk.Treeview(root,columns=tree_columns, show="headings")#Calls on tkinter treeview to make the table
            def selectItem(a):#func for when user selects a file
                curItem = tree.focus()#gets the position in table the user clicked
                filename = ((tree.item(curItem)['values'])[0])#gets corresponding filename attached to position
                os.chdir(textsDir)#changes dir to texts
                with open(filename,'r') as file:
                    text = file.read()#gets texts
                os.chdir(iaDir)#changes dir to intended reading age
                with open(filename,'r') as file:
                    intendedAge = file.read()#gets ira
                
                root.destroy()#delete select box

                #Following inserts the text and ira into the main boxes
                maintextbox.delete(0.0,END)
                maintextbox.insert(0.0,text)

                IntendedAge.delete(0.0,END)
                IntendedAge.insert(0.0,intendedAge)
                calculate()#calls on calculate to display all values
            tree.grid(column=0, row=1, sticky='nsew')#geometry manager for table
            tree.bind('<ButtonRelease-1>',selectItem)#binds the select item button to the mouse click
            for col in tree_columns:#for each column in table
                tree.heading(col, text=col.title(),
                    command=lambda c=col: sortby(self.tree, c, 0))#sets heading
            for item in tree_data:#for each item in the table
                tree.insert('', 'end', values=item)#inserts data from list provided

            root.mainloop()#keeps box running

        searchAge()

        

    

        


    def showLib():#func to show what is saved already
        
        files = [f for f in listdir(textsDir) if isfile(join(textsDir, f))]#get filenames
        if files == []:#check if nothing is stored
            messagebox.showwarning(title = "Error 12",message="There are no stored files. Try create some!")
            return()#exit func
        root = Tk()#make box
        root.attributes("-topmost", True)#keep box above all
        Label(root,text ="Stored files shown below, click to select a file").pack()#create label at top of box
        def CurSelect(evt):#func for when user selects an item
            value=((listbox.get(listbox.curselection())))#gets value that user seletced

            #the following just grabs all data of file and inserts it into mainbox
            os.chdir(textsDir)#change dir to texts
            with open(value,'r') as file:
                text = file.read()#get text
            os.chdir(iaDir)#change dir to ira
            with open(value,'r') as file:
                intendedAge = file.read()#get ira
            root.destroy()#delete box
            maintextbox.delete(0.0,END)
            maintextbox.insert(0.0,text)#insert text

            IntendedAge.delete(0.0,END)
            IntendedAge.insert(0.0,intendedAge)#insert ira
            calculate()#call on calculate             
        listbox = Listbox(root)#Sets a one column table and ties it to the root box set earlier
        listbox.bind('<<ListboxSelect>>',CurSelect)#binds a mouse click to the curselet function
        listbox.pack()#geometry manager

        for i in files:#Goes though each file
            listbox.insert(END, i)#Inserts the file into the selection list
        root.mainloop()#Keeps the box running
    
        
            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    


    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #Here I am creating funtions that do not require the use of an extra box


    
    def calculate():#Function calling all of the calculation functions for simplicity

        words = wordcounter()#Gets words

        if words<20:#Checks if minimum words entered
            messagebox.showwarning(title = "Error 12",message="Please enter more text. The minimum is 20 words")#warning message
            return(1) #Simple error check number
        else:#Calls all calculation functions
            charcounter()
            charcountnospace()
            lettercounter()
            punctuationcounter()
            wordcounter()
            sentencecounter()
            readingagecounter()
            createmessage()
            agedifference()


    def exitwindow():#Function to exit window
        main.destroy()#Destroys box
        exit()#Exits all currently running code

    def charcounter():#Func to count characters. (ALL CHARS)
        wholetext = retrieveInput()#Get text
        length = len(wholetext)#gets length of text aka the characters

        #inserts character number into the main box
        Characters.delete(0.0, END)
        Characters.insert(0.0, length)
        return (length)#returns the length for use by other functions

    def charcountnospace():#Func that counts chars with no spaces included
        wholetext = retrieveInput()#Gets text
        nospace = ""#variable to hold the text without spaces
        for i in wholetext:
            if i is not " ":#Checks if char is a space
                nospace += i#If not add to nospace var
        length = len(nospace)#Gets length of text
        #following inserts the value into the main box
        CharactersNoSpace.delete(0.0, END)
        CharactersNoSpace.insert(0.0, length)
        return (length)#returns value

    
    def lettercounter():#Func that counts letters AND NUMBERS
        wholetext = retrieveInput()#Gets text
        counter = 0#Counter for letters
        for i in wholetext:
            if i.isalpha() == True:#If letter add to counter
                counter += 1
            if i.isdigit() == True:#if number add to counter
                counter += 1
        #Following inserts value into main box                          
        Letters.delete(0.0, END)
        Letters.insert(0.0, counter)
        return (counter)#returns value

    def punctuationcounter():#Function that counts punctuation
        wholetext = retrieveInput()#Gets text
        counter = 0#punc counter
        for i in wholetext:#for each char in text
            for k in string.punctuation:#if char is string add to counter. (string.punctuation is a list of punctuation)
                if i == k:
                    counter += 1
        #Inserts value into main box
        Punctuation.delete(0.0, END)
        Punctuation.insert(0.0, counter)
        return (counter)#returns value

    def wordcounter():#func that counts words
        wholetext = retrieveInput()#Gets text
        for i in string.punctuation:#For each piece of punctuation (string.punctuation is a list of punctuations)
            x = wholetext#Temporary storage for text
            wholetext = ""#resets text variable
            for k in x:#For each char in the text
                if i == k:#if the char is a punctuation mark add a space
                    wholetext += " "
                else:
                    wholetext += k #if not add the original char
        x = wholetext# again sets a temporary storage of the text
        wholetext = (re.sub('\s+', ' ', x).strip())  ##This removes extended/trailing spaces using the var x as a base. -- Each chunk of spaces is converted into one
        listofwords = wholetext.split()#makes a list of words
        length = len(listofwords)#counts list of words
        #inserts count value into main box
        Words.delete(0.0, END)
        Words.insert(0.0, length)
        return (length)#returns count value

    def sentencecounter():#func that counts sentences
        wholetext = retrieveInput()#Gets text
        x = wholetext#temp storage of text
        wholetext = (re.sub('\s+', ' ', x).strip())#removes all trailing spaces
        x = wholetext#sets temp storage of text again
        wholetext = ""#resets original variable to empty
        newtext = []#List for chunks of text
        for k, g in groupby(x):#for every two values in the text (groupby grabs separates chunks of punctuations)
            if k in string.punctuation: #if the char is a punc
                newtext.append(k)#add to list but this only adds on punc mark instead of many -  which is the goal to count sentences
            else:
                newtext.extend(g)#if not just extend add the characters until the next punctuation mark
        counter = 0#counter for sentences
        for i in newtext:#for each value of the newtext list
            wholetext += i#add the value to the original variable
        for i in wholetext:#for each value in the new text string
            if i == "!":#if char is ! mark or
                counter += 1
            if i == "?":#a ? mark or
                counter += 1
            if i == ".":#a full stop then add 1 to the counter
                counter += 1
        #adds value to main box
        Sentences.delete(0.0, END)
        Sentences.insert(0.0, counter)
        return (counter)#retuns value 

    def readingagecounter():#func that calculates the reading age (THE IMPORTANT ONE !!)

        characters = lettercounter()  # gets letters (+numbers)
        words = wordcounter()#gets words
        sentences = sentencecounter()#gets sentences
        div1 = 0#variables for values to divide
        div2 = 0#need two of them
        try:#the reason i am try excepting is because in some cases the divisions just dont work
            div1 = characters / words#dividing chars by words
            div2 = words / sentences#dividing words by sentences
        except:
            return("Enter More Text-Err13")#If it doesnt work show this message

        readingage = 4.71 * div1 + 0.5 * div2 - 21.43 #The main calculation for the reading age
        x = readingage#temp storage of reading age
        readingage = math.ceil(x)#rounds up the reading age
        #adds value to the main box
        Readingage.delete(0.0, END)
        Readingage.insert(0.0, readingage)
        return (readingage)#return value

    
    def agedifference():#Func to get age difference
        ari = Readingage.get(0.0,"end-1c")#gets the reading age
        intendari = IntendedAge.get(0.0,"end-1c")#Gets intended reading age
        try:#try excepting in case there is an error
            ari = int(ari)#convert to integer
            intendari = int(intendari)#convert to integer
            difference = abs(ari-intendari)##This calculates difference
        except Exception as e:#exception as e is to display the error
            difference = "Enter an intended age-Err14"#sets difference to this if there is an error
            #shows error
        #inserts diff value ot main box 
        AgeDifference.delete(0.0,END)
        AgeDifference.insert(0.0, difference)

    def ClearText():#func to clear box
        maintextbox.delete(0.0,END)#clears box
    def ClearIA():#func to clear ira box
        IntendedAge.delete(0.0,END)#clears box
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # Constructing the MAIN GUI

    main.resizable(0, 0)   #This stops the box from being resized by user.
    main.title("Reading Age Calculator")  #Box title
    main.iconbitmap(icon)#Sets icon to box
    main.state("normal")#sets state of box to normal (makes sure it doesnt change at all) 
    main.configure(background="black")#Sets background to black
    #
    #
    #
    #
    #
    # The following lines simply create a menu that goes along the top of the box
    mainmenu = Menu(main)#makes a menu that runs along the top

    
    Search= Menu(mainmenu)#making a search sub menu
    Search.add_command(label="Search by keyword",command=keywordSearch)#keyword sub menu
    Search.add_command(label="Search in existing library",command=showLib)#existing lib sub menu
    Search.add_command(label="Search by calculated age", command=ageSearch)#calculated age sub menu

    Tools= Menu(mainmenu)#Tools sub menu
    Tools.add_command(label="Info",command = DisplayCodeInfo)#info sub menu
    Tools.add_command(label="Grade(READING AGE) to real age conversion",command = displayGtoA)#conversion chart sub menu

    #The following just adds a menu item to the menu
    mainmenu.add_command(label="Save", command= save)#this is a one click item
    mainmenu.add_command(label="Open", command=openfile)
    mainmenu.add_cascade(label="Search",menu=Search)#this adds a submenu using the set framework above
    mainmenu.add_command(label="Send Results", command=sendresults)
    mainmenu.add_command(label="Report", command=report)
    mainmenu.add_command(label="Tutorial",command = tutorial)
    mainmenu.add_cascade(label="Tools",menu=Tools)
    mainmenu.add_command(label="Exit", command=exitwindow)

    main.configure(menu=mainmenu)#just sets all the pieces of the menu above 
    
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #This creates an input box for the user
    Label(main, text="Please Enter Your Text In The Box Below", bg="black", fg="white", width=70, ).grid(row=0,#The first label that shows instruction
                                                                                                         column=1,
                                                                                                         columnspan=4,
                                                                                                         sticky=N)
    #creating a text box for user to input in


    maintextbox = Text(main, width=60, height=18, relief="sunken",undo=True)
    maintextbox.grid(row=1, column=1, columnspan=4, sticky=N)#geometry manager
    



    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #The following creates the main bulk of the main box. They are just boxes for the program to output info on

    
    
    #



    #All of the following just creates a grid of boxes that will display information and essentially follows the same 3 lines shown below
    
    # Reading age (ACTUALLY GRADE BUT REFERENCED AS AGE IN PROGRAM) #refer to this for below
    Label(main, width=20, height=2, text="Actual Reading Grade", borderwidth=1, relief="ridge", bg="black", fg="white").grid(row=4, column=0, columnspan=2, sticky=W)#title of box
    Readingage = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")#setting the box that will display the information
    Readingage.grid(row=5, column=0, columnspan=2, sticky=W)#geometry manager






    # Word Counter #for understanding the code refer the reading age box code
    Label(main, width=20, height=2, text="Words", borderwidth=1, relief="ridge", bg="black", fg="white").grid(row=4,
                                                                                                              column=2,
                                                                                                              columnspan=2,
                                                                                                              sticky=N)
    Words = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")
    Words.grid(row=5, column=2, columnspan=2, sticky=N)







    # Character counter #for understanding the code refer the reading age box code
    Label(main, width=20, height=2, text="Characters", borderwidth=1, relief="ridge", bg="black", fg="white").grid(
        row=4, column=4, columnspan=2, sticky=E)
    Characters = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")
    Characters.grid(row=5, column=4, columnspan=2, sticky=E)






    # Counting characters without spaces #for understanding the code refer the reading age box code
    Label(main, width=20, height=2, text="Characters without spaces", borderwidth=1, relief="ridge", bg="black",
          fg="white").grid(row=6, column=0, columnspan=2, sticky=W)
    CharactersNoSpace = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")
    CharactersNoSpace.grid(row=7, column=0, columnspan=2, sticky=W)






    # Punctuation counter #for understanding the code refer the reading age box code
    Label(main, width=20, height=2, text="Punctuation", borderwidth=1, relief="ridge", bg="black", fg="white").grid(
        row=6, column=2, columnspan=2, sticky=N)
    Punctuation = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")
    Punctuation.grid(row=7, column=2, columnspan=2, sticky=N)






    # Letter counter #for understanding the code refer the reading age box code
    Label(main, width=20, height=2, text="Letters", borderwidth=1, relief="ridge", bg="black", fg="white").grid(row=6,
                                                                                                                column=4,
                                                                                                                columnspan=2,
                                                                                                                sticky=E)
    Letters = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")
    Letters.grid(row=7, column=4, columnspan=2, sticky=E)






    # The intended age #for understanding the code refer the reading age box code

    Label(main, width=20, height=2, text="Intended Reading Grade", borderwidth=1, relief="ridge", bg="black",
          fg="white").grid(row=8, column=0, columnspan=2, sticky=W)

    IntendedAge = Text(main, width=20, height=2, borderwidth=1, relief="raised", fg="black")
    IntendedAge.insert(0.0,"Enter Intended Age  Here")
    IntendedAge.grid(row=9, column=0, columnspan=2, sticky=W)







    # The age difference #for understanding the code refer the reading age box code
    Label(main, width=20, height=2, text="Grade Difference", borderwidth=1, relief="ridge", bg="black", fg="white").grid(row=8,
                                                                                                              column=2,
                                                                                                              columnspan=2,
                                                                                                              sticky=N)
    AgeDifference = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")
    AgeDifference.grid(row=9, column=2, columnspan=2, sticky=N)






    # Sentence #for understanding the code refer the reading age box code
    Label(main, width=20, height=2, text="Sentences", borderwidth=1, relief="ridge", bg="black", fg="white").grid(row=8,
                                                                                                                  column=4,
                                                                                                                  columnspan=2,
                                                                                                                  sticky=E)
    Sentences = Text(main, width=20, height=2, borderwidth=1, relief="raised", bg="red", fg="white")
    Sentences.grid(row=9, column=4, columnspan=2, sticky=E)



    #the pattern for the grid of display info ends here
    
    
    Label(main, width=60, text="STATISTICS SHOWN BELOW", height=1, bg="blue", fg="white").grid(row=2, column=0,columnspan=6)#Just a label to show where the stats come up.

    Button(main,text="Clear Intended Age Box", command=ClearIA, width=20).grid(row=10, sticky=S, column=0, columnspan=2)#button that clears ira box
    Button(main,text="Calculate", command=calculate, width=20).grid(row=10, sticky=S, column=2,columnspan=2)#button to calculate 
    Button(main,text="Clear Text Entry Box", command=ClearText, width=20).grid(row=10, sticky=S, column=4,columnspan=2)#button to clear entry box
    


    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #These functions are functions that need to aquire input from the user input box so they have to be placed down here in order to work
    def retrieveInput(): #function that gets the text and returns it 
        enteredtext = maintextbox.get(0.0, "end-1c")#get text straight from box
        return (enteredtext) #Returns text






    def createmessage():#function that creates a message that contains all the information
        message = ""
        message = (message + "These Are Your Results From The Reading Age Calculator" + "\n")
        message = (message + "This Was The Text You Entered:" + "\n" + retrieveInput() + "\n")
        message = (message + "The number of characters was:" + str(charcounter()) + "\n")
        message = (message + "The number of characters excluding spaces was:" + str(charcountnospace()) + "\n")
        message = (message + "The number of letters was:" + str(lettercounter()) + "\n")
        message = (message + "The number of punctuation used was:" + str(punctuationcounter()) + "\n")
        message = (message + "The number of words was:" + str(wordcounter()) + "\n")
        message = (message + "The number of sentences was:" + str(sentencecounter()) + "\n")
        message = (message + "The reading grade calculated was:" + str(readingagecounter()) + "\n")
        return (message)

    
    if tutCheck == True:#this just checks if the tutorial check is positive
        os.chdir(root)
        with open(tutDir,'a') as file:
            file.write("1111")#this change here makes it negative - so it wont run next time the program starts
    
        tutorial()

    main.mainloop() #This command just keeps the box running
    




mainbox() #This starts the program after everything has been initialized
