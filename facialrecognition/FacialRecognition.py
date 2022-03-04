#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file FacialRecognition.py
 @brief The image input from the camera is used for face detection and identification of specific faces.
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import numpy as np
import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml') #顔検出
face_cascade = cv2.CascadeClassifier('trainer/haarcascade_frontalface_default.xml') #顔分類

i = 0
temperature = [round(35.8 + np.random.rand(),1) ,38.2]



# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
facialrecognition_spec = ["implementation_id", "FacialRecognition",
		 "type_name",		 "FacialRecognition",
		 "description",	   "The image input from the camera is used for face detection and identification of specific faces.",
		 "version",		   "1.0.0",
		 "vendor",			"OdaTetsuya",
		 "category",		  "FacialRecognition",
		 "activity_type",	 "STATIC",
		 "max_instance",	  "1",
		 "language",		  "Python",
		 "lang_type",		 "SCRIPT",
		 ""]
# </rtc-template>

##
# @class FacialRecognition
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
class FacialRecognition(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_in = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		Input an image of type RTC::CameraImage
		 - Type: RTC::CameraImage
		"""
		self._inIn = OpenRTM_aist.InPort("in", self._d_in)
		self._d_bool = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		When set to "True", the movie will be output.
		"""
		self._boolIn = OpenRTM_aist.InPort("bool", self._d_bool)
		self._d_out = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		Add BBox and body temperature display to the image received from the
		camera, and then output the image.
		 - Type: RTC::CameraImage
		"""
		self._outOut = OpenRTM_aist.OutPort("out", self._d_out)





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
		self.addInPort("in",self._inIn)
		self.addInPort("bool",self._boolIn)

		# Set OutPort buffers
		self.addOutPort("out",self._outOut)

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
		print("Activated!!")
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
		print("Deactivated!!")
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

		while(True):
			if self._boolIn.isNew():
				bool = self._boolIn.read()
				if bool.data == 1:
					break


		if self._inIn.isNew():
			img = self._inIn.read()
			npimg = np.frombuffer( img.pixels, dtype=np.uint8 ).reshape( img.height, img.width, -1 )
			frame = cv2.flip(npimg, cv2.ROTATE_90_COUNTERCLOCKWISE)

			img_GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(img_GRAY, 1.3, 5)

			global i
			i += 1
			if i % 100 == 0:
				global temperature
				temperature = [round(35.8 + np.random.rand(),1) ,38.2]
				i = 0

			if 0 < len(faces):
				for (x,y,w,h) in faces:
					id, confidence = recognizer.predict(img_GRAY[y:y+h,x:x+w])
					if (confidence < 45):
						id = 1
						color = (0, 0, 255)
					else:
						id = 0
						color = (255, 0, 0)

				confidence = "  {0}%".format(round(100 - confidence))
				cv2.rectangle(frame, (x, y), (x+w, y+h), color, 7)
				cv2.rectangle(frame, (x-5, y-30), (x+80, y), color, -1)
				cv2.putText(frame, str(temperature[id]), (x+3, y-3), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2)
				# cv2.putText(frame, str(confidence), (x+5,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 1)

			self._d_out.pixels = frame.tobytes()
			self._d_out.width = frame.shape[1]
			self._d_out.height = frame.shape[0]
			self._outOut.write()

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




def FacialRecognitionInit(manager):
	profile = OpenRTM_aist.Properties(defaults_str=facialrecognition_spec)
	manager.registerFactory(profile,
							FacialRecognition,
							OpenRTM_aist.Delete)

def MyModuleInit(manager):
	FacialRecognitionInit(manager)

	# Create a component
	comp = manager.createComponent("FacialRecognition")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()
