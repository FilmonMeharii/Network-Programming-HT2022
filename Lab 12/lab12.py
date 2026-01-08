from pyrebase import pyrebase 

import tkinter as tk
import tkinter.messagebox as tkmsgbox
import tkinter.scrolledtext as tksctxt


class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
    
        #-------------------------------------------------------------------
        # row 1: connection stuff (and a clear-messages button)
        #-------------------------------------------------------------------
        self.groupCon = tk.LabelFrame(bd=0)
        self.groupCon.pack(side="top")
        #
        self.nameLabel = tk.Label(self.groupCon, text='Name', padx=10)
        self.nameLabel.pack(side="left")
        #
        self.nameInput = tk.Entry(self.groupCon, width=40)
        self.nameInput.insert(tk.END, 'lab12')
        self.nameInput.bind('<Return>', sendMessage)
        self.nameInput.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=5)
        padder.pack(side="left")


        ## activate below for subscribe button
            #self.subscribeBtn = tk.Button(self.groupCon, command = connectButtonClick, width=10)
            #self.subscribeBtn.pack(side="left")
        
        padder = tk.Label(self.groupCon, padx=1)
        padder.pack(side="left")
          
        #-------------------------------------------------------------------
        # row 2: the message field (chat messages + status messages)
        #-------------------------------------------------------------------
        self.msgText = tksctxt.ScrolledText(height=15, width=42,
            state=tk.DISABLED)
        self.msgText.pack(side="top")

        
        #-------------------------------------------------------------------
        # row 3: sending messages
        #-------------------------------------------------------------------
        self.groupSend = tk.LabelFrame(bd=0)
        self.groupSend.pack(side="top")
        #
        self.textInLbl = tk.Label(self.groupSend, text='message', padx=10)
        self.textInLbl.pack(side="left")
        #
        self.textIn = tk.Entry(self.groupSend, width=38)
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) send
        self.textIn.bind('<Return>', sendMessage)
        self.textIn.pack(side="left")
        #
        padder = tk.Label(self.groupSend, padx=5)
        padder.pack(side="left")
        #
        self.sendButton = tk.Button(self.groupSend, text = 'Send',
            command = sendButtonClick)
        self.sendButton.pack(side="left")
        
        
        # set the focus on the nameInput field
        self.nameInput.focus_set()

def connectButtonClick():
    # forward to the connect handler
    connectHandler(g_app)

def sendButtonClick():
    # forward to the sendMessage method
    sendMessage(g_app)

# the connectHandler toggles the status between connected/disconnected
def connectHandler(master):
    tryToConnect()

# a utility method to print to the message field        
def printToMessages(message):
    g_app.msgText.configure(state=tk.NORMAL)
    g_app.msgText.insert(tk.END, message + '\n')
    # scroll to the end, so the new message is visible at the bottom
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)

# if attempt to close the window, it is handled here
def on_closing():
    if g_bConnected:
        if tkmsgbox.askokcancel("Quit",
            "You are still connected. If you quit you will be"
            + " disconnected."):
            myQuit()
    else:
        myQuit()

# when quitting, do it the nice way    
def myQuit():
    disconnect()
    g_root.destroy()

# utility address formatting
def myAddrFormat(addr):
    return '{}:{}'.format(addr[0], addr[1])

config = {
    "apiKey": "AIzaSyBcQAvzNCOXUkcfW0VgldMEktPbe-MlU4A",
    "authDomain": "filmonmeharilab12.firebaseapp.com",
    "databaseURL": "https://filmonmeharilab12.firebaseio.com",
    "projectId": "lab12-23c40",
    "storageBucket": "filmonmeharilab12.appspot.com",
    "messagingSenderId": "96146714887",
    "appId": "1:96146714887:android:5a0ea52c48f3ada0bcd5a2",
    "measurementId": "G-WBJ26N5QQJ"
}

firebase = pyrebase.initialize_app(config)
db= firebase.database()

def streamHandler(incomingData):
    if incomingData["event"] == "put":
        if incomingData["path"] == "/":
            # This is the very first reading just after
            # subscription: we get all messages
            # or None (if no messages exists).
            if incomingData["data"] != None:
                for key in incomingData["data"]:
                    message = incomingData["data"][key]
                    handleMessage(message)
        else:
             # Not the first reading.
            # Someone wrote a new message that we just got.
            message = incomingData["data"]
            handleMessage(message)



def handleMessage(message):

    incoming = []
    for key in message.keys():
        incoming.append(message[key])
    pushed = incoming[0] + ' : '+ incoming [1]
    print('HandleMessage function call!')
    print(pushed)
    printToMessages(pushed)


# 3. You subscribe to pushes regarding the messages tag with

messages_stream = db.child('messages').stream(streamHandler)

# 4. You unsubscribe by calling

# messages_stream.close()

# set the state of the programm to 'disconnected'

def disconnect():
    g_bConnected = False
    #messages_stream.close()
    #g_app.subscribeBtn['text'] = 'subscribe
  
def tryToConnect():

    try:
        print('You are subscribed')
        g_bConnected = True
        g_app.subscribeBtn['text'] = 'unsubscribe'
    except:
        printToMessages("Error: thrown during subscription...!")

    
def sendMessage(master):

    try:
        data = g_app.textIn.get()
        name = g_app.nameInput.get()
        print('SendMessage function call!')
        yourMessage = {'name' : name, 'text' : data}
        db.child('messages').push(yourMessage)

    except:
        printToMessages("Error in sendMessage!")
        #disconnect()


# by default we are not connected, needed when subscribe button activated
g_bConnected = False
g_sock = None

# launch the gui
g_root = tk.Tk()
g_app = Application(master=g_root)

# make sure everything is set to the status 'disconnected' at the beginning
disconnect()

# if attempt to close the window, handle it in the on-closing method
g_root.protocol("WM_DELETE_WINDOW", on_closing)

# start the main loop
# (which handles the gui and will frequently call pollMessages)
g_app.mainloop()


"""
cred = firebase_admin.credentials.Certificate("lab12.json")
firebase_admin.initialize_app(cred, {'databaseURL':"https://console.firebase.google.com/project/lab12-23c40/database/lab12-23c40-default-rtdb/data/~2F"})
ref = firebase_admin.db.reference('/')

ref.push(newData)
ref.child('messages').push(newMessage)

newMessage = {'name': 'Filmon', 'text': 'hello world'}
ref.child('messages').push(newMessage)

messages_stream = ref.child('messages').listen(streamHandler)

messages_stream.close()



"""