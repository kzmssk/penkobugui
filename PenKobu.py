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

import emergency_idl
#import penkobu_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from emergency_idl_example import *

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import _GlobalIDL, _GlobalIDL__POA

import penkobugui

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
	def __init__(self, manager):
		self.x=0
		self.y=0
		self.p=0
		self.cb=None
		
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_penPosition = RTC.TimedPoint2D(RTC.Time(0,0), RTC.Point2D(0, 0))
		"""
		"""
		self._penPositionIn = OpenRTM_aist.InPort("penPosition", self._d_penPosition)
		self._d_penPressure = RTC.TimedUShort(RTC.Time(0,0),0)
		"""
		"""
		self._penPressureIn = OpenRTM_aist.InPort("penPressure", self._d_penPressure)

		"""
		"""
		self._command_routePort = OpenRTM_aist.CorbaPort("command_route")
		"""
		"""
		self._emergencyPort = OpenRTM_aist.CorbaPort("emergency")

		"""
		"""
		self._emergency = Emergency_IDL_i(self)
		

		"""
		"""
		self._command = OpenRTM_aist.CorbaConsumer(interfaceType=_GlobalIDL.RunButton_IDL)

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
		self._emergencyPort.registerProvider("emergency", "Emergency_IDL", self._emergency)
		
		# Set service consumers to Ports
		self._command_routePort.registerConsumer("command", "RunButton_IDL", self._command)
		
		# Set CORBA Service Ports
		self.addPort(self._command_routePort)
		self.addPort(self._emergencyPort)
		
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
		self._data = False
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


	def setData(self, data):
		self._data = data
		pass

	def onExecute(self, ec_id):
		if self._penPositionIn.isNew():
			ret = self._penPositionIn.read()
			self.x = ret.data.x
			self.y = ret.data.y
#			self.x=self._d_penPositon.data.x
#			self.y=self._d_penPosition.data.y
#			[self.x, self.y]=self._d_penPosition.data
		if self._penPressureIn.isNew():
			ret_p = self._penPressureIn.read()
#			print ret_p.data
			self.p= ret_p.data
		
		if self.callback != None:
			self.callback(self.x, self.y, self.p, self._data)
			
		if self._data:
			#emergency case is occuured
			print ' - Data is True'
			self.setData(False)
#		self.x+=1
#		self.y+=1
#		if self.x > 200:
#			print "self.x>75"
#			self.p=1
			
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
		self.callback=cb
		print self.callback
	
	def get_service_port(self):	
		print 'get_service_port'
#		self._command._ptr().flush()
		print '============================='
		return self._command

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
	penkobuCanvas=penkobugui.PenKobuGui()
	penkobuCanvas.master.title("penkobugui")
	
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	
	comp=mgr.createComponent("PenKobu")
	comp.set_callback(penkobuCanvas.set_pos)
	penkobuCanvas.set_comp(comp.get_service_port())
	
	mgr.runManager(True)
	
	penkobuCanvas.mainloop()

if __name__ == "__main__":
	main()

