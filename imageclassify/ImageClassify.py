#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ImageClassify.py
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
import cv2
import torch
import torch.nn as nn
from torchvision import models

import tensorflow as tf
import tensorflow_hub as hub

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.patches as patches

import warnings
warnings.simplefilter('ignore')

NUM_CLASSIES = 11

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
imageclassify_spec = ["implementation_id", "ImageClassify",
		 "type_name",         "ImageClassify",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "Endo Takuto",
		 "category",          "ImageProcessiong",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class ImageClassify
# @brief ModuleDescription
#
#
class ImageClassify(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_input_image = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		"""
		self._input_imageIn = OpenRTM_aist.InPort("input_image", self._d_input_image)
		self._d_label = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._labelOut = OpenRTM_aist.OutPort("label", self._d_label)





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
		self.addInPort("input_image",self._input_imageIn)

		# Set OutPort buffers
		self.addOutPort("label",self._labelOut)

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

		# self.selected_model="vgg16"
		# self.selected_model="EfficientNetv2-s"
		self.selected_model="EfficientNetv2-s"
		if self.selected_model=="vgg16":
			self.image_size=300
			#  Global Variable
			self.net = models.vgg16(pretrained=False)
			num_out = 11
			self.net.classifier[6] = nn.Linear(in_features=4096, out_features=num_out)
			# For now, we assume a CPU environment
			device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
			print("use device: ",device)
			self.net.load_state_dict(torch.load('detection_weights15.pth',map_location=torch.device(device)))

		elif self.selected_model=="EfficientNetv2-s":
			self.image_size = 384
			model_path = '1642335745_efficientnetv2-s_16batch_5epoch'
			export_path = 'saved_model/' + model_path
			self.reloaded = tf.keras.models.load_model(export_path)

		elif self.selected_model=="Movenet":
			self.model_name = "movenet_thunder"
			self.module = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
			self.input_size = 256
			# Load the input image.
			self.answer_list = []
			for i in range(NUM_CLASSIES):
				answer_path = "answer/answer_"+str(i)+".png"
				answer_img = tf.io.read_file(answer_path)
				answer_img = tf.image.decode_png(answer_img)
			
				# Resize and pad the image to keep the aspect ratio and fit the expected size.
				input_image = tf.expand_dims(answer_img, axis=0)
				input_image = tf.image.resize_with_pad(input_image, self.input_size, self.input_size)
			
				# Run model inference.
				keypoints_with_scores = self.movenet(input_image)
			
				self.answer_list.append(keypoints_with_scores)

		else:
			print("error.")
			exit()
	
		return RTC.RTC_OK

	def movenet(self, input_image):
		model = self.module.signatures['serving_default']
		# SavedModel format expects tensor type of int32.
		input_image = tf.cast(input_image, dtype=tf.int32)
		# Run model inference.
		outputs = model(input_image)
		# Output is a [1, 1, 17, 3] tensor.
		keypoints_with_scores = outputs['output_0'].numpy()
		return keypoints_with_scores

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

		if self._input_imageIn.isNew():

			self._d_input_image = self._input_imageIn.read()
			image = np.frombuffer(self._d_input_image.pixels, dtype=np.uint8)
			image = image.reshape(self._d_input_image.height, self._d_input_image.width, 3)

			if self.selected_model=="vgg16":

				color_mean = np.array([132,140,144],dtype=np.float32)

				image = image.astype(np.float32)
				image = cv2.resize(image,(self.image_size,self.image_size))
				image -= color_mean
				image = (image-image.min())/(image.max()-image.min())

				image = torch.from_numpy(image[:,:,(2,1,0)]).permute(2,0,1)
				image = torch.unsqueeze(image, 0)
				output = self.net(image)

				self._d_label.data = output.data.max(1)[1].item()
				print("label: ", self._d_label)
				self._labelOut.write()

			elif self.selected_model=="EfficientNetv2-s":

				image = tf.image.resize(image, (self.image_size, self.image_size))
				image = tf.cast(image, tf.float32)
				image = image/255
				input_image = tf.expand_dims(image, axis=0)
				prediction_scores = self.reloaded.predict(input_image)
				self._d_label.data = np.argmax(prediction_scores)
				print("label: ", self._d_label)
				self._labelOut.write()

			elif self.selected_model=="Movenet":

				image = image[:,:,(2,1,0)]
				# Resize and pad the image to keep the aspect ratio and fit the expected size.
				input_image = tf.expand_dims(image, axis=0)
				input_image = tf.image.resize_with_pad(input_image, self.input_size, self.input_size)
			
				# Run model inference.
				keypoints_with_scores_B = self.movenet(input_image)
				output_label = euclidean_similarity_label(self.answer_list, keypoints_with_scores_B)
			
				self._d_label.data = int(output_label)
				self._labelOut.write()
			
				print("output_label:", output_label)

			else:
				print("error.")
				exit()


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


def euclidean_distance(x, y):   
    return np.sqrt(np.sum((x - y) ** 2))

def euclidean_similarity_label(answer_list, keypoints_with_scores_B, keypoint_threshold=0.11):

	minimum_value = 100.0
	minimum_id = -1

	for class_num in range(NUM_CLASSIES):
		# 画像に写っているのは1人と仮定
		# 2人以上映っている場合は左上が優先される
		# Aについて
		keypoints_with_scores_A = answer_list[class_num]
		A_x = np.array(keypoints_with_scores_A[0, 0, :, 1])
		A_x = (A_x - np.min(A_x))/(np.max(A_x)-np.min(A_x))
		A_y = np.array(keypoints_with_scores_A[0, 0, :, 0])
		A_y = (A_y - np.min(A_y))/(np.max(A_y)-np.min(A_y))
		A_scores = np.array(keypoints_with_scores_A[0, 0, :, 2])
		# Bについて
		B_x = np.array(keypoints_with_scores_B[0, 0, :, 1])
		B_x = (B_x - np.min(B_x))/(np.max(B_x)-np.min(B_x))
		B_y = np.array(keypoints_with_scores_B[0, 0, :, 0])
		B_y = (B_y - np.min(B_y))/(np.max(B_y)-np.min(B_y))
		B_scores = np.array(keypoints_with_scores_B[0, 0, :, 2])
		assert len(A_scores)==len(B_scores)
		values = []
		for i, (score_A, score_B) in enumerate(zip(A_scores, B_scores)):
			# if i in [7,8,9,10,13,14,15,16]
			A_vec = []
			B_vec = []
			if True:
				# 特徴が出やすいポイント
				# elbow, wrist, knee, ankle
				if (score_A>=keypoint_threshold) and (score_B>=keypoint_threshold):
					A_vec.append(A_x[i])
					A_vec.append(A_y[i])
					B_vec.append(B_x[i])
					B_vec.append(B_y[i])
					A_vec = np.array(A_vec)
					B_vec = np.array(B_vec)
					values.append(euclidean_distance(A_vec, B_vec))

		temp_value = np.mean(np.array(values))
		print("class_num: ", class_num)
		print("value of similarity: ", temp_value)
		if temp_value<minimum_value:
			minimum_value = temp_value
			minimum_id = class_num

	return minimum_id

def ImageClassifyInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=imageclassify_spec)
    manager.registerFactory(profile,
                            ImageClassify,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ImageClassifyInit(manager)

    # Create a component
    comp = manager.createComponent("ImageClassify")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

