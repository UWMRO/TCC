import wx

# twisted imports
from twisted.python import log
from twisted.internet import wxreactor, protocol
wxreactor.install()

# always goes after wxreactor install 
from twisted.internet import reactor
from twisted.protocols import basic
from twisted.internet.endpoints import TCP4ClientEndpoint



# Global varialbes 
app = None
port = 5501


def AddLinearSpacer(boxsizer, pixelSpacing) :
    """
    A one-dimensional spacer along only the major axis for any BoxSizer

    Found this on a wxPython tutorial and it has proved to be very handy.

    It takes in a box sizer as boxsizer and the spacing as pixelSpacing and expands the
    passed in sizer along its major axis.  This is used over boxsizer.AddSpacer(...) as this
    expands along both axises causing untold issues.  It also is more intuitive than
    boxsizer.AddSpacer((..,..)) where you pass a 0 to the width or height to obtain the same
    results.
    """
    orientation = boxsizer.GetOrientation()
    if   (orientation == wx.HORIZONTAL) :
        boxsizer.Add( (pixelSpacing, 0) )
    elif (orientation == wx.VERTICAL) :
        boxsizer.Add( (0, pixelSpacing) )


class TestSender(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Data Sender", size=(500, 400)) 
        
        self.protocol = None

        # main sizers
        self.vertSizer = wx.BoxSizer(wx.VERTICAL)
        self.horzSizer = wx.BoxSizer(wx.HORIZONTAL)

        # Widgets
        self.statTxt = wx.StaticText(self, id=100, label="Command Prompt")
        self.enterTxt = wx.TextCtrl(self, id=101, size=(200,-1), style=wx.TE_PROCESS_ENTER)
        self.btn = wx.Button(self, id=102, size=(100, -1), label="OK")
        

        self.vertSizer.Add(self.statTxt, flag=wx.ALIGN_CENTER)
        AddLinearSpacer(self.vertSizer, 10)
        self.vertSizer.Add(self.enterTxt, flag=wx.ALIGN_CENTER)
        AddLinearSpacer(self.vertSizer, 10)
        self.vertSizer.Add(self.btn, flag=wx.ALIGN_CENTER)

        self.Bind(wx.EVT_BUTTON, self.onButton, id=102)
        self.Bind(wx.EVT_TEXT_ENTER, self.onButton, id=101)        

        self.SetSizer(self.vertSizer)
        self.vertSizer.Fit(self)

    def onButton(self, e):
        val = str(self.enterTxt.GetValue())
        print "sending: ", val
        #print "literal: ", repr(val)
        self.protocol.sendCommand(val)

class Forwarder(basic.LineReceiver):
    def __init__(self):
        self.output = None
        
    def dataReceived(self, data):
        gui = self.factory.gui

        gui.protocol = self

        if gui:
            print "Recieved data: ", data
            

    def connectionMade(self):
        gui = self.factory.gui
        gui.protocol = self
        print "connection made"
        
    def connectionLost(self, reason):
        print "connection lost: ", reason

class Client(protocol.ClientFactory):
    def __init__(self, gui):
        self.gui = gui
        self.protocol = Forwarder

    def clientConnectionLost(self, transport, reason):
        print "connection lost"

    def clientConnectionFailed(self, transport, reason):
        reactor.stop()


class DataForwardingProtocol(basic.LineReceiver):
    def __init__(self):
        self.output = None
        self.deffers = []

    def dataReceived(self, data):
        gui = self.factory.gui

        gui.protocol = self
        print "recieved from server:", data 
        if gui:
            pass
            #print "hello"
            #val = gui.text.GetValue()
            #gui.text.SetValue(val + data)
            #gui.text.SetInsertionPointEnd()
            #if len(self.deffers) > 0:
            #    self.deffers.pop().callback(data)

    def sendCommand(self, data):
        self.transport.write(data)
        #d = defer.Deferred()
        #self.deffers.append(d)
        #reactor.call(2, d.callback, data)
        #d.callback(data)
        #return d

    def connectionMade(self):
        gui = self.factory.gui
        gui.protocol = self
        pass
        #self.output = self.factory.gui.text  # redirect Twisted's output

class ChatFactory(protocol.ClientFactory):
    def __init__(self, gui):
        self.gui = gui
        self.protocol = DataForwardingProtocol
    

    def clientConnectionLost(self, transport, reason):
        reactor.stop()

    def clientConnectionFailed(self, transport, reason):
        reactor.stop()



if __name__ == "__main__":
    
    app = wx.App(False)
    frame = TestSender()
    frame.Show()
    reactor.registerWxApp(app)
    reactor.connectTCP("localhost", port, ChatFactory(frame))
    #point = TCP4ClientEndpoint(reactor,'localhost', port)
    #point.connect(ChatFactory(frame))
    reactor.run()

    #app = wx.App(False)
    #app.frame = TestSender()
    #app.frame.Show()

    #reactor.registerWxApp(app)
    #reactor.connectTCP("localhost", 5501, Client(app.frame))

    #app.MainLoop()
    #reactor.run()
    
