from Tkinter import *

ModuleList = [] #stored modules

#watermelone module system

class wmModule:
	def __init__(self,name):
		ModuleList.append((name,self))
		self.active = False

	def onActivated(self): #callback
		pass

	def onDeactivated(self): #callback
		pass

	def __ToggleActive(self): #activate deactivate
		self.active = not self.active
		if self.active:
			self.onActivated()
		else:
			self.onDeactivated()

	def Update(self):
		pass

class wmTestmodule(wmModule):
	def onActivated(self):
		print 'test module activated'

	def onDeactivated(self):
		print 'test module deactivated'

wmTestMdle = wmTestmodule()
ModuleList.append(wmTestMdle)