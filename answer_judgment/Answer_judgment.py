#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file Answer_judgment.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import Individual module
import numpy as np
import torch


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
answer_judgment_spec = ["implementation_id", "Answer_judgment",
		 "type_name",         "Answer_judgment",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "Endo Takuto",
		 "category",          "Game",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class Answer_judgment
# @brief ModuleDescription
#
#
class Answer_judgment(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_predict_label = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._predict_labelIn = OpenRTM_aist.InPort("predict_label", self._d_predict_label)
		self._d_predict_detections = OpenRTM_aist.instantiateDataType(RTC.TimedFloatSeq)
		"""
		"""
		self._predict_detectionsIn = OpenRTM_aist.InPort("predict_detections", self._d_predict_detections)
		self._d_movenet_score = OpenRTM_aist.instantiateDataType(RTC.TimedFloat)
		"""
		"""
		self._movenet_scoreIn = OpenRTM_aist.InPort("movenet_score", self._d_movenet_score)
		self._d_binarization_str = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._binarization_strIn = OpenRTM_aist.InPort("binarization_str", self._d_binarization_str)
		self._d_detection_judge = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._detection_judgeOut = OpenRTM_aist.OutPort("detection_judge", self._d_detection_judge)
		self._d_SSD_judge = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._SSD_judgeOut = OpenRTM_aist.OutPort("SSD_judge", self._d_SSD_judge)
		self._d_movenet_judge = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._movenet_judgeOut = OpenRTM_aist.OutPort("movenet_judge", self._d_movenet_judge)
		self._d_binarization_judge = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._binarization_judgeOut = OpenRTM_aist.OutPort("binarization_judge", self._d_binarization_judge)

		
		self.detection_answer = 8
		self.movenet_score_answer = 0.10
		# self.movenet_score_answer = 1.0
		self.binarization_answer = "cheki"
		self.ssd_answer = 2


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
		self.addInPort("predict_label",self._predict_labelIn)
		self.addInPort("predict_detections",self._predict_detectionsIn)
		self.addInPort("movenet_score",self._movenet_scoreIn)
		self.addInPort("binarization_str",self._binarization_strIn)

		# Set OutPort buffers
		self.addOutPort("detection_judge",self._detection_judgeOut)
		self.addOutPort("SSD_judge",self._SSD_judgeOut)
		self.addOutPort("movenet_judge",self._movenet_judgeOut)
		self.addOutPort("binarization_judge",self._binarization_judgeOut)

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

		# 二値化パート
		if self._binarization_strIn.isNew():
			self._d_binarization_str = self._binarization_strIn.read()

			if self._d_binarization_str.data==self.binarization_answer:
				self._d_binarization_judge.data = True
			else:
				self._d_binarization_judge.data = False
			print("binarization_judge: ", self._d_binarization_judge.data)
			self._binarization_judgeOut.write()

		# movenetパート
		if self._movenet_scoreIn.isNew():
			self._d_movenet_score = self._movenet_scoreIn.read()

			if self._d_movenet_score.data<self.movenet_score_answer:
				self._d_movenet_judge.data = True
			else:
				self._d_movenet_judge.data = False
			print("movenet_judge: ", self._d_movenet_judge.data)
			self._movenet_judgeOut.write()
			
		# 画像分類パート
		if self._predict_labelIn.isNew():
			self._d_predict_label = self._predict_labelIn.read()

			if self._d_predict_label.data==self.detection_answer:
				# 画像分類 正解
				self._d_detection_judge.data = True
			else:
				# 画像分類 不正解
				self._d_detection_judge.data = False

			print("detection_judge: ", self._d_detection_judge)
			self._detection_judgeOut.write()


		# SSDパート
		if self._predict_detectionsIn.isNew():
			self._d_predict_detections = self._predict_detectionsIn.read()

			detections = torch.tensor(list(self._d_predict_detections.data))
			detections = torch.reshape(detections, (1,21,200, 5))
			
			SSD_judge = False
			
			predict_bbox, predict_label_index, scores = select_bbox(detections, confidence_threshold=0.5)
			

			if self.ssd_answer==0:
				# predict_bboxとpredit_label_indexを合わせて正解判定
				# 人が2人入っているかどうか
				human_count = sum(np.array(predict_label_index)==14)
				dog_count = sum(np.array(predict_label_index)==11)
				
				if ((human_count==2) and (dog_count==1)):
					# bboxの選定
					human_bbox = np.array(predict_bbox)[np.array(predict_label_index)==14]
					dog_bbox = np.array(predict_bbox)[np.array(predict_label_index)==11]
					print(human_bbox)
					print(dog_bbox)
					
					# 条件確認
					# 人が被っているか否か
					if human_bbox[0][2]<human_bbox[1][0] or human_bbox[1][2]<human_bbox[0][0]:
						print("1.横軸での被りなし")
						# 犬が人に被っているか
						for d_i, d_bbox in enumerate(dog_bbox):
							for h_i, h_bbox in enumerate(human_bbox):
								if d_bbox[2] < h_bbox[0] or h_bbox[2] < d_bbox[0]:
									print("2.横軸での被りなし")
								elif d_bbox[2] > h_bbox[0] or h_bbox[2] > d_bbox[0]:
									SSD_judge = True
									print("3.横軸での被りあり")
									
					elif human_bbox[1][0]<human_bbox[0][2] or human_bbox[0][0]<human_bbox[1][2]:
						# 別にelseでよかったわ
						print("4.横軸での被りあり")
				else:
					print("0. else")

			elif self.ssd_answer==1:
				# predict_bboxとpredit_label_indexを合わせて正解判定
				# 人が1人入っているかどうか
				# test用
				human_count = sum(np.array(predict_label_index)==14)
				
				if (human_count==1):
					# bboxの選定
					human_bbox = np.array(predict_bbox)[np.array(predict_label_index)==14]
					print(human_bbox)
					SSD_judge = True
				else:
					print("0. else")

			elif self.ssd_answer==2:
				# predict_bboxとpredit_label_indexを合わせて正解判定
				# 人が1人と犬が一匹入っているかどうか
				# 本番用
				human_count = sum(np.array(predict_label_index)==14)
				dog_count =sum(np.array(predict_label_index)==11)
				if (human_count==1):
					# bboxの選定
					human_bbox = np.array(predict_bbox)[np.array(predict_label_index)==14]
					print(human_bbox)
					if dog_count==1:
						dog_bbox = np.array(predict_bbox)[np.array(predict_label_index)==11]
						print(dog_bbox)
						SSD_judge = True
				else:
					print("0. else")
				

			self._d_SSD_judge.data = SSD_judge
			print("SSD_judge: ", self._d_SSD_judge)
			self._SSD_judgeOut.write()
	
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


# 送信先での処理
def select_bbox(detections, confidence_threshold=0.5):
	
	# confidence_threshold:
	predict_bbox = []
	predict_label_index = []
	scores = []
	detections = detections.cpu().detach().numpy()

	# 予測結果から物体を検出したとする確信度の閾値以上のBBoxのインデックスを抽出
	# find_index(tuple): (［0次元のインデックス］,
	#                     ［1次元のインデックス],
	#                     [2次元のインデックス],
	#                     [3次元のインデックス],)
	find_index = np.where(detections[:, 0:, :, 0] >= confidence_threshold)
	
	# detections: (閾値以上のBBox数, 5)
	detections = detections[find_index]

	# find_index[1]のクラスのインデックスの数(21)回ループする
	for i in range(len(find_index[1])):
		if (find_index[1][i]) > 0: # クラスのインデックス0以外に対して処理する
			sc = detections[i][0]  # detectionsから確信度を取得
			print("detections: ", detections[i][1:])
			bbox = detections[i][1:]
			# find_indexのクラスの次元の値から-1する(背景0を引いて元の状態に戻す)
			lable_ind = find_index[1][i]-1

			# BBoxのリストに追加
			predict_bbox.append(bbox)
			# 物体のラベルを追加
			predict_label_index.append(lable_ind)
			# 確信度のリストに追加
			scores.append(sc)

	# 1枚の画像のRGB値、BBox、物体のラベル、確信度を返す
	return predict_bbox, predict_label_index, scores


def Answer_judgmentInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=answer_judgment_spec)
    manager.registerFactory(profile,
                            Answer_judgment,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    Answer_judgmentInit(manager)

    # Create a component
    comp = manager.createComponent("Answer_judgment")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

