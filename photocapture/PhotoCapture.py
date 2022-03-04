#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file PhotoCapture.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Inport Individual module
import numpy as np
import time

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
photocapture_spec = ["implementation_id", "PhotoCapture",
		 "type_name",         "PhotoCapture",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "Endo Takuto",
		 "category",          "ImageProcessiong",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 "conf.default.delay", "3",

		 "conf.__widget__.delay", "spin.1",
		 "conf.__constraints__.delay", "0<=x<=10",

         "conf.__type__.delay", "int",

		 ""]
# </rtc-template>

##
# @class PhotoCapture
# @brief ModuleDescription
#
#
class PhotoCapture(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_in_image = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		"""
		self._in_imageIn = OpenRTM_aist.InPort("in_image", self._d_in_image)
		self._d_button = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		 - Semantics: if "q" is passed from the standard input, output the image.
		"""
		self._buttonIn = OpenRTM_aist.InPort("button", self._d_button)
		self._d_out_image = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		"""
		self._out_imageOut = OpenRTM_aist.OutPort("out_image", self._d_out_image)

		self._start_time = 0.0
		self._on_shatter = False



		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  delay
		 - DefaultValue: 3
		"""
		self._delay = [3]

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
		self.bindParameter("delay", self._delay, "3")

		# Set InPort buffers
		self.addInPort("in_image",self._in_imageIn)
		self.addInPort("button",self._buttonIn)

		# Set OutPort buffers
		self.addOutPort("out_image",self._out_imageOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
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

		print("if \"9\" is passed, output the image.")
		print("delay from input(sec): ",self._delay)
	
		return RTC.RTC_OK

	###
	##
	## The deactivated action (Active state exit action)
	## former rtc_active_exit()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK

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

		if self._buttonIn.isNew():
			self._d_button = self._buttonIn.read()
			if (self._d_button.data == 9):
				self._on_shatter=True
				self._start_time=time.time()

		if self._on_shatter:
			now_time = time.time()
			if self._delay[0]<=(now_time-self._start_time):
				if self._in_imageIn.isNew():
					# set the image for output
					self._d_in_image = self._in_imageIn.read()
					print("image height: ", self._d_in_image.height)
					print("image width: ", self._d_in_image.width)
					frame = np.frombuffer(self._d_in_image.pixels, dtype=np.uint8)
					frame = frame.reshape(self._d_in_image.height, self._d_in_image.width, 3)
					print("frame shape: ", frame.shape)
					self._d_out_image.width = self._d_in_image.width
					self._d_out_image.height = self._d_in_image.height
					self._d_out_image.pixels = self._d_in_image.pixels
					self._out_imageOut.write()
					self._on_shatter=False
			else:
				print(now_time-self._start_time)

		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def PhotoCaptureInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=photocapture_spec)
    manager.registerFactory(profile,
                            PhotoCapture,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    PhotoCaptureInit(manager)

    # Create a component
    comp = manager.createComponent("PhotoCapture")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

