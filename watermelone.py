#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the button, the oval moves to the left or right

from Tkinter import *
root = Tk()

class MyApp:
    def __init__(self, parent):
        self.modules = []
        self.drawpad = Canvas(root, width=480,height=320, background='white')
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.drawpad.pack(side=BOTTOM)
    
    def Update(self):
        for mod in self.modules:
            mod.Update()
		
myapp = MyApp(root)
root.mainloop()