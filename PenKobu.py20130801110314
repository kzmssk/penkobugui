#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file PenKobu.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import penkobugui

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
penkobu_spec = ["implementation_id", "PenKobu", 
		 "type_name",         "PenKobu", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "rtmsc2013", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.mode", "0",
		 "conf.__widget__.mode", "text",
		 ""]
# </rtc-template>

##
# @class PenKobu
# @brief ModuleDescription
# 
# 
class PenKobu(OpenRTM_aist.DataFlowComponentBase):
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	x=0
	y=0
	p=0
	cb=None
	
	def __init__(self, manager):
		self.x=0
		self.y=0
		self.p=0
		
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_penPosition = RTC.TimedPoint2D(RTC.Time(0,0),0)
		"""
		"""
		self._penPositionIn = OpenRTM_aist.InPort("penPosition", self._d_penPosition)
		self._d_penPressure = RTC.TimedUShort(RTC.Time(0,0),0)
		"""
		"""
		self._penPressureIn = OpenRTM_aist.InPort("penPressure", self._d_penPressure)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  mode
		 - DefaultValue: 0
		"""
		self._mode = [0]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("mode", self._mode, "0")
		
		# Set InPort buffers
		self.addInPort("penPosition",self._penPositionIn)
		self.addInPort("penPressure",self._penPressureIn)
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
		#read data from wacom tablet
		if self._penPositionIn.isNew():
		  self._penPositionIn.read()
		if self._penPressureIn.isNew():
		  self._penPressureIn.read()
#		print self._d_penPosition.data
#		[self.x, self.y]=self._d_penPosition.data
#		self.p=self._d_penPressure.data
		self.x+=1
		self.y+=1
		self.p=0
		if self.x>500:
			self.x=1
			self.y=1
			#self.p=1
		if self.callback != None:
		 	self.callback(self.x, self.y, self.p)		  
		  
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	def set_callback(self, cb):
		print "set_callback"
		self.callback = cb
		print self.callback
		
	def get_pos(self):
		print "===get_pos==="
		pos=[]
		pos.append(self.x)
		pos.append(self.y)
		pos.append(self.p)
		return pos

def PenKobuInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=penkobu_spec)
    manager.registerFactory(profile,
                            PenKobu,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    PenKobuInit(manager)
    # Create a component
    #comp = manager.createComponent("PenKobu")
    
def main():
	#create penkobu gui
	penkobuCanvas=penkobugui.PenKobuGui()
	penkobuCanvas.master.title("penkobugui")
	
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	
	comp=mgr.createComponent("PenKobu")
#	penkobuCanvas.get_on_update(comp.get_pos())
	comp.set_callback(penkobuCanvas.set_pos)
	penkobuCanvas.set_comp(comp)
	
	mgr.runManager(True)
	
	penkobuCanvas.mainloop()

if __name__ == "__main__":
	main()

