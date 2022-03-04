#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file FacialRecognitionTest.py
 @brief The image input from the camera is used for face detection and identification of specific faces.
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
facialrecognitiontest_spec = ["implementation_id", "FacialRecognitionTest",
		 "type_name",         "FacialRecognitionTest",
		 "description",       "The image input from the camera is used for face detection and identification of specific faces.",
		 "version",           "1.0.0",
		 "vendor",            "OdaTetsuya",
		 "category",          "FacialRecognition",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class FacialRecognitionTest
# @brief The image input from the camera is used for face detection and identification of specific faces.
#
# The image input from the camera is used for face detection and identification
# of specific faces.
# For people whose faces are identified, the BBox turns red and the temperature
# display is set to heat.
# For other people, the BBox turns blue and the body temperature display is set
# to normal.
#
# input
# in: Input an image of type RTC::CameraImage
# bool: When set to "True", the movie will be output.
# output
# out:Add BBox and body temperature display to the image received from the
# camera, and then output the image.
#
# This is using the "Haar Cascade classifier".
#
# https://github.com/Mjrovai/OpenCV-Face-Recognition
#
#
class FacialRecognitionTest(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_out = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		Add BBox and body temperature display to the image received from the
		camera, and then output the image.
		 - Type: RTC::CameraImage
		"""
		self._outIn = OpenRTM_aist.InPort("out", self._d_out)
		self._d_in = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		Input an image of type RTC::CameraImage
		 - Type: RTC::CameraImage
		"""
		self._inOut = OpenRTM_aist.OutPort("in", self._d_in)
		self._d_bool = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		When set to "True", the movie will be output.
		"""
		self._boolOut = OpenRTM_aist.OutPort("bool", self._d_bool)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">

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

		# Set InPort buffers
		self.addInPort("out",self._outIn)

		# Set OutPort buffers
		self.addOutPort("in",self._inOut)
		self.addOutPort("bool",self._boolOut)

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
	#def onFinalize(self):
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
		# Display "Activated."
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
		# Display "Deactivated."
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
		# The image input from the camera will be used for face detection and
	# identification of specific faces.
	# For people whose faces are identified, the BBox turns red and an image with
	# a high body temperature display is generated.
	# For other people, the BBox will turn blue and an image will be generated
	# showing a normal body temperature.
	# The image will then be output.
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




def FacialRecognitionTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=facialrecognitiontest_spec)
    manager.registerFactory(profile,
                            FacialRecognitionTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    FacialRecognitionTestInit(manager)

    # Create a component
    comp = manager.createComponent("FacialRecognitionTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

