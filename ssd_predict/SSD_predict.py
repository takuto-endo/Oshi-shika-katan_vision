#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file SSD_predict.py
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
from ssd import SSD
import warnings
warnings.simplefilter('ignore')
import cv2  # OpenCV2
from voc import DataTransform   # DataTransformクラス
from ssd_predictions import SSDPredictions

#  Global Variable
# VOC2012の正解ラベルのリスト
voc_classes = [
    'aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
    'bus', 'car', 'cat', 'chair', 'cow',
    'diningtable', 'dog', 'horse', 'motorbike',
    'person', 'pottedplant', 'sheep', 'sofa', 'train',
    'tvmonitor']
# SSDモデルの設定値
ssd_cfg = {
    'classes_num': 21,  # 背景クラスを含めた合計クラス数
    'input_size': 300,  # 画像の入力サイズ
    'dbox_num': [4, 6, 6, 6, 4, 4],  # 出力するDBoxのアスペクト比の種類
    'feature_maps': [38, 19, 10, 5, 3, 1],  # 各sourceの画像サイズ
    'steps': [8, 16, 32, 64, 100, 300],  # DBOXの大きさを決める
    'min_sizes': [30, 60, 111, 162, 213, 264],  # DBOXの大きさを決める
    'max_sizes': [60, 111, 162, 213, 264, 315],  # DBOXの大きさを決める
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
}
# 推論モードのSSDモデルを生成
net = SSD(phase="test", cfg=ssd_cfg)
# 学習済みの重みを設定
# 以下のパスは環境に合わせて変更が必要です
net_weights = torch.load(
    'weights/ssd300_mAP_77.43_v2.pth',
    map_location={'cuda:0': 'cpu'})
# 重みをロードする
net.load_state_dict(net_weights)
print('Preparation of SSD model is done')

color_mean = (104, 117, 123)
input_size = 300
transform = DataTransform(input_size, color_mean)


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
ssd_predict_spec = ["implementation_id", "SSD_predict",
		 "type_name",         "SSD_predict",
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
# @class SSD_predict
# @brief ModuleDescription
#
#
class SSD_predict(OpenRTM_aist.DataFlowComponentBase):

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
		self._d_detections = OpenRTM_aist.instantiateDataType(RTC.TimedFloatSeq)
		"""
		"""
		self._detectionsOut = OpenRTM_aist.OutPort("detections", self._d_detections)





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
		self.addOutPort("detections",self._detectionsOut)

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

		if self._input_imageIn.isNew():

			self._d_input_image = self._input_imageIn.read()
			image = np.frombuffer(self._d_input_image.pixels, dtype=np.uint8)
			image = image.reshape(self._d_input_image.height, self._d_input_image.width, 3)

			image = image.astype(np.float32)
			# image = torch.from_numpy(image[:,:,(2,1,0)]).permute(2,0,1)
			# image = torch.unsqueeze(image, 0)

			# 予測と、予測結果を画像で描画する
			ssd = SSDPredictions(eval_categories=voc_classes, net=net)
			# BBoxを抽出する際の閾値を0.6にする
			ssd.show(image, confidence_threshold=0.5)

			img_transformed, boxes, labels = transform(image, 'val', '', '')
			x = torch.from_numpy(img_transformed[:,:,(2,1,0)]).permute(2,0,1)
			net.eval()
			x = x.unsqueeze(0)
			print(x.shape)
			output = net(x)
			# self._d_detections.data = output
			print("output: ", output.size())
			output = torch.flatten(output)
			print("output size: ", output.size())
			self._d_detections.data = output.tolist()
			self._detectionsOut.write()
	
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




def SSD_predictInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=ssd_predict_spec)
    manager.registerFactory(profile,
                            SSD_predict,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SSD_predictInit(manager)

    # Create a component
    comp = manager.createComponent("SSD_predict")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

