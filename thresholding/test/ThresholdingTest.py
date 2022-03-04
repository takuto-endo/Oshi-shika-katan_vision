#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ThresholdingTest.py
 @brief Processes the input image with the threshold value entered by the keyboard, and outputs the processed image.
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
thresholdingtest_spec = ["implementation_id", "ThresholdingTest",
		 "type_name",         "ThresholdingTest",
		 "description",       "Processes the input image with the threshold value entered by the keyboard, and outputs the processed image.",
		 "version",           "1.0.0",
		 "vendor",            "OdaTetsuya",
		 "category",          "nazo1",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class ThresholdingTest
# @brief Processes the input image with the threshold value entered by the keyboard, and outputs the processed image.
#
# Processes the input image with the threshold value entered by the keyboard,
# and outputs the processed image.
# Values greater than the threshold are left as they were, while other values
# are replaced with 0.
#
# input
# threshold: Enter a threshold value of type RTC::TimedLong.
# input_img:Input the image to be thresholded.
# output
# output_img:Outputs an image with a threshold value entered by the keyboard,
# where values greater than the threshold value are left as they were, and other
# values are replaced with 0.
#
# Using cv2.threshold()
#
#
class ThresholdingTest(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_output_img = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		Outputs an image with a threshold value entered by the keyboard, where
		values greater than the threshold value are left as they were, and other
		values are replaced with 0.
		 - Type: RTC::CameraImage
		"""
		self._output_imgIn = OpenRTM_aist.InPort("output_img", self._d_output_img)
		self._d_input_img = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		Input the image to be thresholded.
		 - Type: RTC::CameraImage
		"""
		self._input_imgOut = OpenRTM_aist.OutPort("input_img", self._d_input_img)
		self._d_threshold = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		Enter a threshold value of type RTC::TimedLong.
		 - Type: RTC::TimedLong
		"""
		self._thresholdOut = OpenRTM_aist.OutPort("threshold", self._d_threshold)





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
		self.addInPort("output_img",self._output_imgIn)

		# Set OutPort buffers
		self.addOutPort("input_img",self._input_imgOut)
		self.addOutPort("threshold",self._thresholdOut)

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
		# Processes the input image with the threshold value entered by the keyboard,
	# and outputs the processed image.
	# Values greater than the threshold are left as they were, while other values
	# are replaced with 0.
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




def ThresholdingTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=thresholdingtest_spec)
    manager.registerFactory(profile,
                            ThresholdingTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ThresholdingTestInit(manager)

    # Create a component
    comp = manager.createComponent("ThresholdingTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

