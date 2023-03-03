#in case you dont have a good opnegl version
import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'

import math
from kivy.app import App
from  kivy.uix.screenmanager import Screen,ScreenManager

class Home(Screen):
	
	signchange=chr(177)
	divisionsign=chr(247)
	deletionsign="<---"
	dotsign=chr(183)
	settings=u"\u221A"
	colorl = [0.05, 0.04, 0.2, 1]
	
	def __init__(self,**kwargs):
		super(Home, self).__init__(**kwargs)
		self.num1=0
		self.num2=0
		self.sign=''
		
		
	def blue(colorl):
		colorl=list()
		
		
	def one(self):
		
		if self.ids.bottomlabel.text!='0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "1"
		else:
			self.ids.bottomlabel.text =''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "1"
		
	def two(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "2"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "2"
		
	def three(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "3"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "3"
	
	def four(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "4"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "4"
		
	def five(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "5"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "5"
		
	def six(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "6"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "6"
		
	def seven(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "7"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "7"
		
	def eight(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "8"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "8"
		
	def nine(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "9"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "9"
		
	def zero(self):
		if self.ids.bottomlabel.text != '0':
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "0"
		else:
			self.ids.bottomlabel.text = ''
			self.ids.bottomlabel.text = self.ids.bottomlabel.text + "0"
		
	def add(self):
		try:
			self.sign="+"
			self.num1=float(self.ids.bottomlabel.text)
			self.ids.toplabel.text = self.ids.bottomlabel.text+"+"
			self.ids.bottomlabel.text = ""
		except:
			self.ids.bottomlabel.text = ''
			pass
	
	def subtract(self):
		try:
			self.sign = "-"
			self.num1 = float(self.ids.bottomlabel.text)
			self.ids.toplabel.text = self.ids.bottomlabel.text + "-"
			self.ids.bottomlabel.text = ""
		except:
			self.ids.bottomlabel.text = ''
			pass
	
	def multiply(self):
		try:
			self.sign="x"
			self.num1=float(self.ids.bottomlabel.text)
			self.ids.toplabel.text = self.ids.bottomlabel.text+"x"
			self.ids.bottomlabel.text = ""
		except:
			self.ids.bottomlabel.text = ''
			pass
	
	def divide(self):
		try:
			self.sign="/"
			self.num1=float(self.ids.bottomlabel.text)
			self.ids.toplabel.text = self.ids.bottomlabel.text+"/"
			self.ids.bottomlabel.text = ""
		except:
			self.ids.bottomlabel.text = ''
			pass
	
	def answer(self):
		
		try:
			self.num2=float(self.ids.bottomlabel.text)
			self.ids.toplabel.text =self.ids.toplabel.text +self.ids.bottomlabel.text
			
			if self.sign=="+":
				ans=self.num1 + self.num2
			elif self.sign=="-":
				ans = self.num1 - self.num2
			elif self.sign=="/":
				ans = self.num1 / self.num2
			elif self.sign=="x":
				ans = self.num1 * self.num2
			elif "sqrt" in self.ids.toplabel.text:
				ans=math.sqrt(self.num2)
				self.ids.toplabel.text=self.ids.bottomlabel.text
				
			finalStr=str(ans)
			self.ids.bottomlabel.text=finalStr[:10]
		except (ZeroDivisionError,ValueError,UnboundLocalError):
			
			self.ids.bottomlabel.text = ''
		
	def squareRoot(self):
		if self.ids.bottomlabel.text != '0':
			
			self.ids.toplabel.text = "sqrt({0})".format(self.ids.bottomlabel.text)
		else:
			self.ids.bottomlabel.text = ''
			
	
	def clearAll(self):
		self.ids.bottomlabel.text=''
		self.ids.toplabel.text =''
		
	def backspace(self):
		bottomstr=self.ids.bottomlabel.text
		topstr=self.ids.toplabel.text
		bottomlast=len(bottomstr)-1
		toplast = len(topstr)- 1
		
		if bottomstr=='':
			self.ids.toplabel.text = topstr[:toplast]
		else:
			self.ids.bottomlabel.text=bottomstr[:bottomlast]
		
		#from minus to plus sign
	def changeSign(self):
		if self.ids.bottomlabel.text != '0':
			try:
				snum=self.ids.bottomlabel.text
				if snum[0]!="-":
					snum="-" + snum
					self.ids.bottomlabel.text=snum
				elif snum[0]=="-":
					snum[0]=''
					self.ids.bottomlabel.text=snum
			except:
				self.ids.bottomlabel.text = ''
				
		else: self.ids.bottomlabel.text =''
		try:
			snum = self.ids.bottomlabel.text
			if snum[0] != "-":
				snum = "-" + snum
				self.ids.bottomlabel.text = snum
			elif snum[0] == "-":
				snum[0] = ''
				self.ids.bottomlabel.text = snum
		except:
			self.ids.bottomlabel.text = '-'
		
		
	
	def putDot(self):
		self.ids.bottomlabel.text=self.ids.bottomlabel.text+"."

class About(Screen):
	def __init__(self,**kwargs):
		super(About, self).__init__(**kwargs)
		
		
class CalculatorApp(App):
	icon = "Calc.png"
	def build(self):
		
		self.icon="Calc.png"
		root=ScreenManager()
		root.add_widget(Home())
		root.add_widget(About())
		return root			
	
if __name__=="__main__":
	CalculatorApp().run()
	