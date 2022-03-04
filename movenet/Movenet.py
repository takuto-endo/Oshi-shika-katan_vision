#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file Movenet.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import indeividual module
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import cv2

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.patches as patches

import warnings
warnings.simplefilter('ignore')

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
movenet_spec = ["implementation_id", "Movenet",
		 "type_name",         "Movenet",
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
# @class Movenet
# @brief ModuleDescription
#
#
class Movenet(OpenRTM_aist.DataFlowComponentBase):

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
		self._d_output_score = OpenRTM_aist.instantiateDataType(RTC.TimedFloat)
		"""
		"""
		self._output_scoreOut = OpenRTM_aist.OutPort("output_score", self._d_output_score)





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
		self.addOutPort("output_score",self._output_scoreOut)

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
		self.model_name = "movenet_thunder"
		self.module = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
		self.input_size = 256
		# Load the input image.
		answer_path = "image/answer.png"
		answer_img = tf.io.read_file(answer_path)
		answer_img = tf.image.decode_png(answer_img)
		
		# Resize and pad the image to keep the aspect ratio and fit the expected size.
		input_image = tf.expand_dims(answer_img, axis=0)
		input_image = tf.image.resize_with_pad(input_image, self.input_size, self.input_size)
		
		# Run model inference.
		self.keypoints_with_scores_A = self.movenet(input_image)
		
		print(self.keypoints_with_scores_A)

		answer_check = True
		if answer_check:
			display_image = tf.expand_dims(answer_img, axis=0)
			display_image = tf.cast(tf.image.resize_with_pad(display_image, 1280, 1280), dtype=tf.int32)
			output_overlay = draw_prediction_on_image(np.squeeze(display_image.numpy(), axis=0), self.keypoints_with_scores_A)
			plt.figure(figsize=(15, 15))
			plt.imshow(output_overlay)
			_ = plt.axis('off')
			plt.show()
		
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
			image = image[:,:,(2,1,0)]

			
			# Resize and pad the image to keep the aspect ratio and fit the expected size.
			input_image = tf.expand_dims(image, axis=0)
			
			input_image = tf.image.resize_with_pad(input_image, self.input_size, self.input_size)
			

			# Run model inference.
			keypoints_with_scores_B = self.movenet(input_image)
			

			output_value = euclidean_similarity(self.keypoints_with_scores_A, keypoints_with_scores_B)
			
			print(type(output_value))
			self._d_output_score.data = float(output_value)
			print("aaa")
			self._output_scoreOut.write()
			
			print("output_value:", output_value)

			display_image = tf.expand_dims(image, axis=0)
			display_image = tf.cast(tf.image.resize_with_pad(display_image, 1280, 1280), dtype=tf.int32)
			output_overlay = draw_prediction_on_image(np.squeeze(display_image.numpy(), axis=0), keypoints_with_scores_B)
			plt.figure(figsize=(15, 15))
			plt.imshow(output_overlay)
			_ = plt.axis('off')
			plt.show()

			print("h")


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

def euclidean_similarity(keypoints_with_scores_A, keypoints_with_scores_B, keypoint_threshold=0.11):
	# 画像に写っているのは1人と仮定
	# 2人以上映っている場合は左上が優先される
	# Aについて
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

	return  np.mean(np.array(values))

# Dictionary that maps from joint names to keypoint indices.
KEYPOINT_DICT = {
	'nose': 0,
	'left_eye': 1,
	'right_eye': 2,
	'left_ear': 3,
	'right_ear': 4,
	'left_shoulder': 5,
	'right_shoulder': 6,
	'left_elbow': 7,
	'right_elbow': 8,
	'left_wrist': 9,
	'right_wrist': 10,
	'left_hip': 11,
	'right_hip': 12,
	'left_knee': 13,
	'right_knee': 14,
	'left_ankle': 15,
	'right_ankle': 16
}

# Maps bones to a matplotlib color name.
KEYPOINT_EDGE_INDS_TO_COLOR = {
	(0, 1): 'm',
	(0, 2): 'c',
	(1, 3): 'm',
	(2, 4): 'c',
	(0, 5): 'm',
	(0, 6): 'c',
	(5, 7): 'm',
	(7, 9): 'm',
	(6, 8): 'c',
	(8, 10): 'c',
	(5, 6): 'y',
	(5, 11): 'm',
	(6, 12): 'c',
	(11, 12): 'y',
	(11, 13): 'm',
	(13, 15): 'm',
	(12, 14): 'c',
	(14, 16): 'c'
}

def _keypoints_and_edges_for_display(keypoints_with_scores,height,width, keypoint_threshold=0.11):
	"""Returns high confidence keypoints and edges for visualization.
	
	Args:
		keypoints_with_scores: A numpy array with shape [1, 1, 17, 3] representing
			the keypoint coordinates and scores returned from the MoveNet model.
		height: height of the image in pixels.
		width: width of the image in pixels.
		keypoint_threshold: minimum confidence score for a keypoint to be
			visualized.
	
	Returns:
		A (keypoints_xy, edges_xy, edge_colors) containing:
			* the coordinates of all keypoints of all detected entities;
			* the coordinates of all skeleton edges of all detected entities;
			* the colors in which the edges should be plotted.
	"""
	keypoints_all = []
	keypoint_edges_all = []
	edge_colors = []
	num_instances, _, _, _ = keypoints_with_scores.shape
	for idx in range(num_instances):
		kpts_x = keypoints_with_scores[0, idx, :, 1]
		kpts_y = keypoints_with_scores[0, idx, :, 0]
		kpts_scores = keypoints_with_scores[0, idx, :, 2]
		kpts_absolute_xy = np.stack([width * np.array(kpts_x), height * np.array(kpts_y)], axis=-1)
		kpts_above_thresh_absolute = kpts_absolute_xy[
			kpts_scores > keypoint_threshold, :]
		keypoints_all.append(kpts_above_thresh_absolute)

		for edge_pair, color in KEYPOINT_EDGE_INDS_TO_COLOR.items():
			if (kpts_scores[edge_pair[0]] > keypoint_threshold and
			kpts_scores[edge_pair[1]] > keypoint_threshold):
				x_start = kpts_absolute_xy[edge_pair[0], 0]
				y_start = kpts_absolute_xy[edge_pair[0], 1]
				x_end = kpts_absolute_xy[edge_pair[1], 0]
				y_end = kpts_absolute_xy[edge_pair[1], 1]
				line_seg = np.array([[x_start, y_start], [x_end, y_end]])
				keypoint_edges_all.append(line_seg)
				edge_colors.append(color)
	if keypoints_all:
		keypoints_xy = np.concatenate(keypoints_all, axis=0)
	else:
		keypoints_xy = np.zeros((0, 17, 2))

	if keypoint_edges_all:
		edges_xy = np.stack(keypoint_edges_all, axis=0)
	else:
		edges_xy = np.zeros((0, 2, 2))
	return keypoints_xy, edges_xy, edge_colors


def draw_prediction_on_image(
		image, keypoints_with_scores, crop_region=None, close_figure=False,
		output_image_height=None):
	"""Draws the keypoint predictions on image.
	
	Args:
		image: A numpy array with shape [height, width, channel] representing the
			pixel values of the input image.
		keypoints_with_scores: A numpy array with shape [1, 1, 17, 3] representing
			the keypoint coordinates and scores returned from the MoveNet model.
		crop_region: A dictionary that defines the coordinates of the bounding box
			of the crop region in normalized coordinates (see the init_crop_region
			function below for more detail). If provided, this function will also
			draw the bounding box on the image.
		output_image_height: An integer indicating the height of the output image.
			Note that the image aspect ratio will be the same as the input image.
	
	Returns:
		A numpy array with shape [out_height, out_width, channel] representing the
		image overlaid with keypoint predictions.
	"""
	height, width, channel = image.shape
	aspect_ratio = float(width) / height
	fig, ax = plt.subplots(figsize=(12 * aspect_ratio, 12))
	# To remove the huge white borders
	fig.tight_layout(pad=0)
	ax.margins(0)
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	plt.axis('off')

	im = ax.imshow(image)
	line_segments = LineCollection([], linewidths=(4), linestyle='solid')
	ax.add_collection(line_segments)
	# Turn off tick labels
	scat = ax.scatter([], [], s=60, color='#FF1493', zorder=3)

	(keypoint_locs, keypoint_edges, edge_colors) = _keypoints_and_edges_for_display(keypoints_with_scores, height, width)

	line_segments.set_segments(keypoint_edges)
	line_segments.set_color(edge_colors)
	if keypoint_edges.shape[0]:
		line_segments.set_segments(keypoint_edges)
		line_segments.set_color(edge_colors)
	if keypoint_locs.shape[0]:
		scat.set_offsets(keypoint_locs)

	if crop_region is not None:
		xmin = max(crop_region['x_min'] * width, 0.0)
		ymin = max(crop_region['y_min'] * height, 0.0)
		rec_width = min(crop_region['x_max'], 0.99) * width - xmin
		rec_height = min(crop_region['y_max'], 0.99) * height - ymin
		rect = patches.Rectangle(
			(xmin,ymin),rec_width,rec_height,
			linewidth=1,edgecolor='b',facecolor='none')
		ax.add_patch(rect)

	fig.canvas.draw()
	image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
	image_from_plot = image_from_plot.reshape(
			fig.canvas.get_width_height()[::-1] + (3,))
	plt.close(fig)
	if output_image_height is not None:
		output_image_width = int(output_image_height / height * width)
		image_from_plot = cv2.resize(
			image_from_plot, dsize=(output_image_width, output_image_height),
				interpolation=cv2.INTER_CUBIC)
	return image_from_plot


def MovenetInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=movenet_spec)
    manager.registerFactory(profile,
                            Movenet,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    MovenetInit(manager)

    # Create a component
    comp = manager.createComponent("Movenet")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

