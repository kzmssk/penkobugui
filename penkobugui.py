from Tkinter import *
import tkMessageBox

class PenKobuGui(Frame):
	def __init__(self, width=700, height=500, master=None):
		Frame.__init__(self, master)
		self.id_list=[]
		self.cX=0
		self.cY=0
		self.cP=0
		self.tmpX=0
		self.tmpY=0
		self.tmpP=0
		self.onPaint=False
		self.onPaintTmp=False
		self.id_list=[]
		
		print "create canvas"
		#paint area
		self.c0=Canvas(self, width='500', height='600')
		self.c0.grid(row=0, column=0, rowspan=4)
		self.id=self.c0.create_oval(10,10,15,15, fill="#000000")
		
		#run button
		self.run_button=Button(self, text='RUN', command=self.on_run_button)
		self.run_button.grid(row=0, column=1)
		
		#clear button
		self.clear_button=Button(self, text='CLEAR', command=self.on_clear_button)
		self.clear_button.grid(row=1, column=1)
		
		#label
		self.la_x=Label(self, text="position X", bd=2)
		self.la_x.grid(row=2, column=1)
		
		self.la_y=Label(self, text="position Y", bd=2)
		self.la_y.grid(row=3, column=1)
		
		self.grid()
				
	def set_pos(self, x, y, p, data):
	#update func
		#case of emergency
		if data:
			self.emergency()
		
		#get pan state
		if self.cP>0:
			self.onPaint=True
		else:
			self.onPaint=False	
				
		#get current point
		self.cX = x/2
		self.cY = y/2
		self.cP = p/2
		
		#draw carsor
		self.draw_carsor()
		
		#case of start paint
		if self.onPaint==True and self.onPaintTmp==False:
			print "====start painting==="			
		#case of painting 
		if self.onPaint==True and self.onPaintTmp==True:
			self.draw_line(self.c0, self.tmpX, self.tmpY, self.cX, self.cY)
		#case of end paint	
		if self.onPaint==False and self.onPaintTmp==True:
			print "====end painting==="
#			for c in self.id_list:
#				self.c0.delete(c)
			
		#draw info (x, y, p)
		self.draw_info()
		
		#update pen state
		self.onPaintTmp=self.onPaint
		
		self.tmpX=self.cX
		self.tmpY=self.cY
		self.tmpP=self.cP
			
	def draw_carsor(self):
#		print 'draw_carsor'
		self.c0.delete(self.id)
		self.id=self.c0.create_oval(self.cX-10, self.cY-10, self.cX+10, self.cY+10)

	def draw_line(self, canvas, tmpX, tmpY, cX, cY):
		self.id_list.append(canvas.create_line(tmpX, tmpY, cX, cY))
		
	def draw_info(self):
		self.la_x.configure(text="position x: %d" % self.cX)
		self.la_y.configure(text="position y: %d" % self.cY)
		
	def on_run_button(self):
		print 'pressed run button'
#		print dir(self.svcPort)
		self.svcPort._ptr().flush()
		
	def on_clear_button(self):
		print 'pressed clear button'
		self.svcPort._ptr().clear()
		for c in self.id_list:
			self.c0.delete(c)
		
	def emergency(self):
		print "case of emergency"
		self.la_x.configure(text="EMERGENCY")
		self.la_y.configure(text="EMERGENCY")
		tkMessageBox.showinfo("EMERGENCY!", "stop")

	def set_comp(self, svcport):
		print "set_comp: ",
		self.svcPort = svcport
		print self.svcPort
#		self.scvPort_command=comp._command._ptr()
