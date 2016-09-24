from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
from tkinter import scrolledtext
import urllib.request as ul
from bs4 import BeautifulSoup as bs

root = tk.Tk()
root.title("Search Articles")
frame = Frame(master=root)

frame.pack(fill=BOTH, expand=TRUE)
# Create widgets
label = Label(frame, text="The feature of this program includes \
    1) Scraping webpage text for a URL  \
    2) Reading web URLs from a file \
    3) Reading search keywords from a file \
    ", bg="#ff9911")
search = scrolledtext.ScrolledText(master=frame, wrap=tk.WORD, width=20, height=40)
url = scrolledtext.ScrolledText(master=frame, wrap=tk.WORD, width=30, height=40)
article = scrolledtext.ScrolledText(master=frame, wrap=tk.WORD, width=60, height=40)
countLabel = Label(master=frame, text="Statistics: total")

# Place widgets in proper location on frame
label.grid(columnspan=4, row=0, sticky=W)
search.grid(column=0, row=1, sticky=W)
url.grid(column=1, row=1, sticky=(W, E))
article.grid(column=2, row=1)

cntOUT = StringVar()
tk.Label(frame, text="Statistics: total").grid(column=0,row=2, sticky=W)
tk.Label(frame, textvariable=cntOUT).grid(column=1,row=2,sticky=W)
tk.Label(frame, text="found").grid(column=2,row=2, sticky=W)

# Keep track of keyword occurrences
cnt = 0


# def appendKey():
#     print(0)
#     # implement here


def createKey():
    search.delete(1.0, END)


def openKey():
    global search
    f = askopenfile(mode='r')
    if f is None:
        return
    text2open = str(f.read())
    search.insert(INSERT, text2open)


def createURL():
    url.delete(1.0, END)


def openURL():
    # global aurl
    f = askopenfile(mode='r')
    if f is None:
        return
    text2open = str(f.read())
    url.delete(1.0, END)
    url.insert(INSERT, text2open)


def createFile():
    article.delete(1.0, END)

def file_save():
    f = asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:  # close if cancel
        return
    text2save = str(url.get(1.0, END))
    f.write(text2save)
    f.close()


def getURL(urls):
    """Return a list of proper url strings.

    Keyword arguments
    :param urls: list of possible url strings
    :return: formatted url strings
    """
    # NOTE: This does not use regex!
    global article, soup
    article.delete(1.0, END)
    readAddr = str(urls)
    for webLink in readAddr.split():
        if webLink[0:7] != "http://":
            webLink = "http://" + webLink  # check if prefix starts with http
        print(webLink)
        urlAdd = "----------------" + webLink + "----------------"
        article.insert(END, urlAdd)
        htmlFile = ul.urlopen(webLink)
        soup = bs(htmlFile, "html.parser")
        article.insert(END, soup.get_text())


def readAll():
    try:
        getURL(url.get(1.0, END))
    except TclError:
        print("Please input website address.")


def readOne():
    try:
        getURL(url.selection_get())
    except TclError:
        print("Please input website address.")


def addTags(widget, keywords, isCaseSensitive):
    """ Sets tags on the matched pattern
    :param widget: tkinter widget holding text
    :param keywords: list of keywords to search for
    :param isCaseSensitive: true if keywords search is case sensitive, false otherwise
    """
    global cnt
    cnt = 0
    widget.tag_remove("yellow", 1.0, END)
    widget.tag_configure("yellow", background="#ffff00")  # color code highlight
    for keyword in keywords:
        pos = 1.0
        while True:
            idx = widget.search(keyword, pos, END, nocase=FALSE) if isCaseSensitive \
                else widget.search(keyword, pos, END, nocase=TRUE)
            if not idx:
                break
            cnt += 1
            pos = '{}+{}c'.format(idx, len(keyword))
            widget.tag_add("yellow", idx, pos)


def getKeywords():
    """Scans the keyword column in search of keywords.

    Keyword arguments
    :return: a list of keywords
    """
    try:
        searchKeys = search.get(1.0, END)
        return searchKeys.split()
    except TclError:
        print("Please input any keyword.")


def caseHighlight():
    keywords = getKeywords()
    addTags(article, keywords, True)


def nocaseHighlight():
    keywords = getKeywords()
    addTags(article, keywords, False)


def searchStatistic():
    global cnt
    try:
        cntOUT.set(cnt)
    except ValueError:
        pass


def getOut():
    print("Good-bye")
    root.quit()


def explainHelp():
    helpwin = Toplevel (root)
    button = Button (helpwin, text ="This is a sample program \n written for IASP 505.")
    button.pack()

myMenu = Menu(root)

keyMenu= Menu (myMenu, tearoff=0)
keyMenu.add_command(label="New", command=createKey, accelerator="Ctrl+N")
# keyMenu.add_command(label="Append...", command=appendKey)
keyMenu.add_command(label="Open...", command=openKey, accelerator="Ctrl+O")
keyMenu.add_separator()
keyMenu.add_command(label="Exit", command=getOut)
myMenu.add_cascade(label="Keyword", menu=keyMenu)

urlMenu= Menu (myMenu, tearoff=0)
urlMenu.add_command(label="New", command=createURL, accelerator="Ctrl+N")
urlMenu.add_command(label="Open...", command=openURL, accelerator="Ctrl+O")
myMenu.add_cascade(label="URL", menu=urlMenu)

artiMenu= Menu (myMenu, tearoff=0)
artiMenu.add_command(label="Fetch Selected", command=readOne, accelerator="Ctrl+O")
artiMenu.add_command(label="Fetch All", command=readAll, accelerator="Ctrl+S")
artiMenu.add_command(label="Save As...", command=file_save)
artiMenu.add_separator()
artiMenu.add_command(label="Page Setup...", command=createFile)
artiMenu.add_command(label="Print...", command=createFile, accelerator="Ctrl+P")
artiMenu.add_separator()
artiMenu.add_command(label="Exit", command=getOut)
myMenu.add_cascade(label="WebPage", menu=artiMenu)

srchMenu= Menu (myMenu, tearoff=0)
srchMenu.add_command(label="Case-sensitive", accelerator="Ctrl+io", command=caseHighlight)
srchMenu.add_command(label="All Matches", accelerator="Ctrl+io", command=nocaseHighlight)
srchMenu.add_separator()
srchMenu.add_command(label="Statistics", accelerator="Ctrl+ix", command=searchStatistic)
myMenu.add_cascade(label="Search", menu=srchMenu)

helpMenu= Menu (myMenu, tearoff=0)
helpMenu.add_command(label="View Help", command=createFile)
helpMenu.add_separator()
helpMenu.add_command(label="About Notepad", command=explainHelp)
myMenu.add_cascade(label="Help", menu=helpMenu)

root.config(menu=myMenu)
root.mainloop()