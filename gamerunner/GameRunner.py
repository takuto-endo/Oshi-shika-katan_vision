#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file GameRunner.py
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
from pygame.locals import *
import pygame
import sys
import random
import time

# Global Valiable ===========================================================
alpha = 0.9

# =================== images/title/ ====================
TITLE_MILK_SIZE = (875*alpha, 875*alpha)
TITLE_MILK_POSI = (912*alpha, 97*alpha)

TITLE_LOGO_SIZE = (922*alpha, 712*alpha)
TITLE_LOGO_POSI = (116*alpha, 177*alpha)

TITLE_BUTTON_SIZE = (364*alpha, 99*alpha)
TITLE_BUTTON_POSI1 = (1440*alpha, 727*alpha)
TITLE_BUTTON_POSI2 = (1440*alpha, 845*alpha)

# =================== images/story/bg/ ====================
SC_SIZE = (1920*alpha, 1080*alpha)

# =================== images/story/button/ ====================
BUTTON_SIZE = (68*alpha, 38*alpha)
BUTTON_POSI = (1753*alpha, 988*alpha)

BUTTON_ANSWER_SIZE = (372*alpha, 107*alpha)
BUTTON_ANSWER_POSI = (779*alpha, 900*alpha)

BUTTON_CHOICE_SIZE = (534*alpha, 130*alpha)
BUTTON_CHOICE1_POSI = (408*alpha, 244*alpha)
BUTTON_CHOICE2_POSI = (1046*alpha, 244*alpha)
BUTTON_CHOICE3_POSI = (408*alpha, 442*alpha)
BUTTON_CHOICE4_POSI = (1046*alpha, 442*alpha)

# =================== images/story/border/ ====================
BORDER_SIZE = (1921*alpha, 302*alpha)
BORDER_POSI = (0*alpha, 778*alpha)

BORDER_SPEAK_SIZE = (1799*alpha, 320*alpha)
BORDER_SPEAK_POSI = (64*alpha, 737*alpha)

# =================== images/story/icon/ ====================
BAD_SIZE = (728*alpha, 705*alpha)
BAD_POSI = (597*alpha, 177*alpha)

CLEAR_SIZE = (1921*alpha, 625*alpha)
CLEAR_POSI = (0*alpha, 204*alpha)

LETTER_1_SIZE = (988*alpha, 741*alpha)
LETTER_1_POSI = (467*alpha, 224*alpha)

LETTER_2_SIZE = (1143*alpha, 857*alpha)
LETTER_2_POSI = (388*alpha, 111*alpha)

CHEKI_SIZE = (957*alpha, 624*alpha)
CHEKI_POSI = (451*alpha, 108*alpha)

TWEET_SIZE = (556*alpha, 916*alpha)
TWEET_POSI = (683*alpha, 164*alpha)

TEXT_MILK_SIZE = (1632*alpha, 173*alpha)
TEXT_MILK_POSI = (144*alpha, 828*alpha)

# =================== images/story/chara/ ====================
DOUTAN_BACK_SIZE = (1043*alpha, 852*alpha)
DOUTAN_BACK_POSI = (438*alpha, 228*alpha)

DOUTAN_DOYA_SIZE = (1040*alpha, 1040*alpha)
DOUTAN_DOYA_POSI = (375*alpha, 78*alpha)

DOUTAN_LOVE_SIZE = (1040*alpha, 1002*alpha)
DOUTAN_LOVE_POSI = (375*alpha, 78*alpha)

DOUTAN_TURN_SIZE = (782*alpha, 676*alpha)
DOUTAN_TURN_POSI = (569*alpha, 134*alpha)

ME_SIZE = (894*alpha, 1014*alpha)
ME_POSI = (503*alpha, 67*alpha)

MILK_SIZE = (875*alpha, 875*alpha)
MILK_POSI = (522*alpha, 103*alpha)

# =================== images/story/QA/ ====================
S_SIZE = (1921*alpha, 240*alpha)
S_POSI = (0, 420*alpha)

Q_SIZE = (1462*alpha, 560*alpha)
Q_POSI = (210*alpha, 133*alpha)

A_SIZE = SC_SIZE
A_POSI = (0,0)

Q_GRAY_SIZE = (957*alpha, 624*alpha)
Q_GRAY_POSI = (451*alpha, 108*alpha)

HINT_Q2_SIZE = (1269*alpha, 117*alpha)
HINT_Q2_POSI = (325*alpha, 884*alpha)

# =================== font/ ====================
LINE_SIZE = int(48*alpha)
LINE_POSI = (105*alpha, 847*alpha)
LINE_SPEAK_POSI = (144*alpha, 828*alpha)

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
gamerunner_spec = ["implementation_id", "GameRunner",
		 "type_name",         "GameRunner",
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
# @class GameRunner
# @brief ModuleDescription
#
#
class GameRunner(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_detection_is_true = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._detection_is_trueIn = OpenRTM_aist.InPort("detection_is_true", self._d_detection_is_true)
		self._d_ssd_is_true = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._ssd_is_trueIn = OpenRTM_aist.InPort("ssd_is_true", self._d_ssd_is_true)
		self._d_binarization_is_true = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._binarization_is_trueIn = OpenRTM_aist.InPort("binarization_is_true", self._d_binarization_is_true)
		self._d_movenet_is_true = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
		"""
		"""
		self._movenet_is_trueIn = OpenRTM_aist.InPort("movenet_is_true", self._d_movenet_is_true)
		self._d_button = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._buttonOut = OpenRTM_aist.OutPort("button", self._d_button)

		self.title_running = True
		self.running = False
		self.page_changed = True
		self.Q4_choice = 0

		self.TEST_MODE = False
		self.reach_ending = False


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
		self.addInPort("detection_is_true",self._detection_is_trueIn)
		self.addInPort("ssd_is_true",self._ssd_is_trueIn)
		self.addInPort("binarization_is_true",self._binarization_is_trueIn)
		self.addInPort("movenet_is_true",self._movenet_is_trueIn)

		# Set OutPort buffers
		self.addOutPort("button",self._buttonOut)

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

		self.gamescene = 55
		pygame.init()
		self.screen = pygame.display.set_mode(SC_SIZE)

		pygame.display.update()
		pygame.display.set_caption("sample game")

		pygame.mixer.music.load("sounds/main_bgm.mp3")
		pygame.mixer.music.set_volume(0.36)
		pygame.mixer.music.play(-1)

		# =================== images/title/ ====================

		# titleの背景
		self.title_bg = pygame.image.load("images/title/background.png")
		self.title_bg = pygame.transform.scale(self.title_bg, (SC_SIZE))
		# titleの装飾
		self.title_header_footer = pygame.image.load("images/title/hf.png").convert_alpha()
		self.title_header_footer = pygame.transform.scale(self.title_header_footer, (SC_SIZE))
		# titleのミルク様
		self.title_milk = pygame.image.load("images/title/milk.png").convert_alpha()
		self.title_milk = pygame.transform.scale(self.title_milk, (TITLE_MILK_SIZE))
		# titleのロゴ
		self.title_logo = pygame.image.load("images/title/title_logo.png").convert_alpha()
		self.title_logo = pygame.transform.scale(self.title_logo, (TITLE_LOGO_SIZE))

		# 次に進む用のボタン
		self.title_button = pygame.image.load("images/title/button_NEWGAME.png").convert_alpha()
		self.title_button = pygame.transform.scale(self.title_button, TITLE_BUTTON_SIZE)
		self.rect_title = pygame.Rect(TITLE_BUTTON_POSI1, self.title_button.get_rect().size)

		self.title_button2 = pygame.image.load("images/title/button_CONTINUE.png").convert_alpha()
		self.title_button2 = pygame.transform.scale(self.title_button2, TITLE_BUTTON_SIZE)

		# ==========================================================================================

		# =================== images/story/bg/ ====================

		# blackout
		self.blackout = pygame.image.load("images/story/bg/blackout.png")

		# whiteout
		self.whiteout = pygame.image.load("images/story/bg/whiteout.png")

		# story中の背景1
		self.story_bg1 = pygame.image.load("images/story/bg/story_bg1.png")
		self.story_bg1 = pygame.transform.scale(self.story_bg1, (SC_SIZE))

		# story中の背景2
		self.story_bg2 = pygame.image.load("images/story/bg/story_bg2.png")
		self.story_bg2 = pygame.transform.scale(self.story_bg2, (SC_SIZE))

		# story中の背景3
		self.story_bg3 = pygame.image.load("images/story/bg/story_bg3.png")
		self.story_bg3 = pygame.transform.scale(self.story_bg3, (SC_SIZE))

		# story中の背景4
		self.story_bg4 = pygame.image.load("images/story/bg/story_bg4.png")
		self.story_bg4 = pygame.transform.scale(self.story_bg4, (SC_SIZE))

		# story中の背景5
		self.story_bg5 = pygame.image.load("images/story/bg/story_bg5.png")
		self.story_bg5 = pygame.transform.scale(self.story_bg5, (SC_SIZE))

		# 同担拒否マン参上!!!
		self.doutan_sanjou = pygame.image.load("images/story/bg/doutan_sanjou.png")
		self.doutan_sanjou = pygame.transform.scale(self.doutan_sanjou, (SC_SIZE))

		# 同担拒否マンを倒そう!!!
		self.doutan_taosou = pygame.image.load("images/story/bg/doutan_taosou.png")
		self.doutan_taosou = pygame.transform.scale(self.doutan_taosou, (SC_SIZE))

		# =================== images/story/button/ ====================

		# 次に進む用のボタン
		self.next_button = pygame.image.load("images/story/button/pushbutton.png").convert_alpha()
		self.next_button = pygame.transform.scale(self.next_button, BUTTON_SIZE)
		self.rect_next_button = pygame.Rect(BUTTON_POSI, self.next_button.get_rect().size)

		# 次に進む用のボタン
		self.answer_button = pygame.image.load("images/story/button/button_answer.png").convert_alpha()
		self.answer_button = pygame.transform.scale(self.answer_button, BUTTON_ANSWER_SIZE)
		self.rect_answer_button = pygame.Rect(BUTTON_ANSWER_POSI, self.answer_button.get_rect().size)

		# 問3 選択肢11
		self.choice_11 = pygame.image.load("images/story/button/Q3/choice11.png").convert_alpha()
		self.choice_11 = pygame.transform.scale(self.choice_11, BUTTON_CHOICE_SIZE)
		self.rect_choice_1 = pygame.Rect(BUTTON_CHOICE1_POSI, self.choice_11.get_rect().size)
		# 問3 選択肢12
		self.choice_12 = pygame.image.load("images/story/button/Q3/choice12.png").convert_alpha()
		self.choice_12 = pygame.transform.scale(self.choice_12, BUTTON_CHOICE_SIZE)
		self.rect_choice_2 = pygame.Rect(BUTTON_CHOICE2_POSI, self.choice_12.get_rect().size)
		# 問3 選択肢13
		self.choice_13 = pygame.image.load("images/story/button/Q3/choice13.png").convert_alpha()
		self.choice_13 = pygame.transform.scale(self.choice_13, BUTTON_CHOICE_SIZE)
		self.rect_choice_3 = pygame.Rect(BUTTON_CHOICE3_POSI, self.choice_13.get_rect().size)
		# 問3 選択肢14
		self.choice_14 = pygame.image.load("images/story/button/Q3/choice14.png").convert_alpha()
		self.choice_14 = pygame.transform.scale(self.choice_14, BUTTON_CHOICE_SIZE)
		self.rect_choice_4 = pygame.Rect(BUTTON_CHOICE4_POSI, self.choice_14.get_rect().size)

		# 問3 選択肢21
		self.choice_21 = pygame.image.load("images/story/button/Q3/choice21.png").convert_alpha()
		self.choice_21 = pygame.transform.scale(self.choice_21, BUTTON_CHOICE_SIZE)
		# 問3 選択肢22
		self.choice_22 = pygame.image.load("images/story/button/Q3/choice22.png").convert_alpha()
		self.choice_22 = pygame.transform.scale(self.choice_22, BUTTON_CHOICE_SIZE)
		# 問3 選択肢23
		self.choice_23 = pygame.image.load("images/story/button/Q3/choice23.png").convert_alpha()
		self.choice_23 = pygame.transform.scale(self.choice_23, BUTTON_CHOICE_SIZE)
		# 問3 選択肢24
		self.choice_24 = pygame.image.load("images/story/button/Q3/choice24.png").convert_alpha()
		self.choice_24 = pygame.transform.scale(self.choice_24, BUTTON_CHOICE_SIZE)

		# =================== images/story/border/ ====================

		# text用の枠
		self.border = pygame.image.load("images/story/border/border.png").convert_alpha()
		self.border = pygame.transform.scale(self.border, BORDER_SIZE)

		# 僕用の枠
		self.border_me = pygame.image.load("images/story/border/border_me.png").convert_alpha()
		self.border_me = pygame.transform.scale(self.border_me, BORDER_SPEAK_SIZE)

		# 受付用の枠
		self.border_recep = pygame.image.load("images/story/border/border_recep.png").convert_alpha()
		self.border_recep = pygame.transform.scale(self.border_recep, BORDER_SPEAK_SIZE)

		# 僕用の枠
		self.border_doutan = pygame.image.load("images/story/border/border_doutan.png").convert_alpha()
		self.border_doutan = pygame.transform.scale(self.border_doutan, BORDER_SPEAK_SIZE)

		# =================== images/story/icon/ ====================

		# 不正解時
		self.bad = pygame.image.load("images/story/icon/bad.png").convert_alpha()
		self.bad = pygame.transform.scale(self.bad, BAD_SIZE)

		# 正解時
		self.clear = pygame.image.load("images/story/icon/clear.png").convert_alpha()
		self.clear = pygame.transform.scale(self.clear, CLEAR_SIZE)

		# 手紙1
		self.letter1 = pygame.image.load("images/story/icon/letter_1.png").convert_alpha()
		self.letter1 = pygame.transform.scale(self.letter1, LETTER_1_SIZE)

		# 手紙2
		self.letter2 = pygame.image.load("images/story/icon/letter_2.png").convert_alpha()
		self.letter2 = pygame.transform.scale(self.letter2, LETTER_2_SIZE)

		# チェキ券
		self.cheki = pygame.image.load("images/story/icon/cheki.png").convert_alpha()
		self.cheki = pygame.transform.scale(self.cheki, CHEKI_SIZE)

		# チェキ券2
		self.cheki2 = pygame.image.load("images/story/icon/cheki_2.png").convert_alpha()
		self.cheki2 = pygame.transform.scale(self.cheki2, CHEKI_SIZE)

		# tweet
		self.tweet = pygame.image.load("images/story/icon/tweet.png").convert_alpha()
		self.tweet = pygame.transform.scale(self.tweet, TWEET_SIZE)

		# text milk
		self.text_milk = pygame.image.load("images/story/icon/text_milk.png").convert_alpha()
		self.text_milk = pygame.transform.scale(self.text_milk, TEXT_MILK_SIZE)

		# =================== images/story/chara/ ====================

		# 自分
		self.me = pygame.image.load("images/story/chara/me.png").convert_alpha()
		self.me = pygame.transform.scale(self.me, ME_SIZE)

		# ミルク様
		self.milk = pygame.image.load("images/story/chara/milk.png").convert_alpha()
		self.milk = pygame.transform.scale(self.milk, MILK_SIZE)

		# 同担 帰る
		self.doutan_back = pygame.image.load("images/story/chara/doutan_back.png").convert_alpha()
		self.doutan_back = pygame.transform.scale(self.doutan_back, DOUTAN_BACK_SIZE)

		# 同担 ドヤ顔
		self.doutan_doya = pygame.image.load("images/story/chara/doutan_doya.png").convert_alpha()
		self.doutan_doya = pygame.transform.scale(self.doutan_doya, DOUTAN_DOYA_SIZE)

		# 同担 love
		self.doutan_love = pygame.image.load("images/story/chara/doutan_love.png").convert_alpha()
		self.doutan_love = pygame.transform.scale(self.doutan_love, DOUTAN_LOVE_SIZE)

		# 同担 振り向き
		self.doutan_turn = pygame.image.load("images/story/chara/doutan_turn.png").convert_alpha()
		self.doutan_turn = pygame.transform.scale(self.doutan_turn, DOUTAN_TURN_SIZE)

		# =================== images/story/QA/ ====================


		# 提示1
		self.s1 = pygame.image.load("images/story/QA/start_Q1.png").convert_alpha()
		self.s1 = pygame.transform.scale(self.s1, S_SIZE)
		# 問題1
		self.q1 = pygame.image.load("images/story/QA/Q1.png").convert_alpha()
		self.q1 = pygame.transform.scale(self.q1, Q_SIZE)
		# 問題用画像
		self.q1_gray = pygame.image.load("images/story/QA/Q1_gray.png").convert_alpha()
		self.q1_gray = pygame.transform.scale(self.q1_gray, Q_GRAY_SIZE)
		# 解答1
		self.a1 = pygame.image.load("images/story/QA/A1.png").convert_alpha()
		self.a1 = pygame.transform.scale(self.a1, A_SIZE)

		# 提示1
		self.s2 = pygame.image.load("images/story/QA/start_Q2.png").convert_alpha()
		self.s2 = pygame.transform.scale(self.s2, S_SIZE)
		# 問題2
		self.q2 = pygame.image.load("images/story/QA/Q2.png").convert_alpha()
		self.q2 = pygame.transform.scale(self.q2, Q_SIZE)
		# ヒント2
		self.hint2 = pygame.image.load("images/story/QA/hint_Q2.png").convert_alpha()
		self.hint2 = pygame.transform.scale(self.hint2, HINT_Q2_SIZE)
		# 解答2
		self.a2 = pygame.image.load("images/story/QA/A2.png").convert_alpha()
		self.a2 = pygame.transform.scale(self.a2, A_SIZE)

		# 提示1
		self.s3 = pygame.image.load("images/story/QA/start_Q3.png").convert_alpha()
		self.s3 = pygame.transform.scale(self.s3, S_SIZE)
		# 問題3
		self.q3 = pygame.image.load("images/story/QA/Q3.png").convert_alpha()
		self.q3 = pygame.transform.scale(self.q3, Q_SIZE)
		# 解答3
		self.a3 = pygame.image.load("images/story/QA/A3.png").convert_alpha()
		self.a3 = pygame.transform.scale(self.a3, A_SIZE)


		# =================== sounds/ ====================
		# text用のsound
		self.text_sound = pygame.mixer.Sound("sounds/serif_bgm.mp3")

		# オタscreem用のsound
		self.screem_sound = pygame.mixer.Sound("sounds/screem.mp3")

		# 体温測定器error用のsound
		self.error_sound = pygame.mixer.Sound("sounds/error.mp3")

		# last ホラー用のsound
		self.suspicion_sound = pygame.mixer.Sound("sounds/suspicion.mp3")
		self.suspicion_sound.set_volume(0.36)

		# 正解表示 ボタンのsound
		self.next_button_sound = pygame.mixer.Sound("sounds/next_button.mp3")

		# 問4 選択肢 ボタンのsound
		self.choice_button_sound = pygame.mixer.Sound("sounds/choice_button.mp3")		

		# =================== font/ ====================

		# 文字関連
		self.line_space = LINE_SIZE
		self.font = pygame.font.Font("fonts/NotoSansJP-Bold.otf", LINE_SIZE)
		self.font2 = pygame.font.SysFont(None, LINE_SIZE)
	
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

		if self.title_running:
			self.screen.blit(self.title_bg, (0,0))
			self.screen.blit(self.title_header_footer, (0,0))
			if self.reach_ending:
				self.screen.blit(self.me, (TITLE_MILK_POSI))
			else:
				self.screen.blit(self.title_milk, (TITLE_MILK_POSI))
			self.screen.blit(self.title_logo, (TITLE_LOGO_POSI))
			self.screen.blit(self.title_button, (TITLE_BUTTON_POSI1))
			self.screen.blit(self.title_button2, (TITLE_BUTTON_POSI2))

			pygame.display.update()
			for event in pygame.event.get():
				if event.type == QUIT:
					self.title_running=False
					pygame.quit()
					sys.exit()
				if (event.type==pygame.MOUSEBUTTONUP) and (event.button==1):
					# processing when clicked
					if self.rect_title.collidepoint(event.pos):
						self.title_running=False
						self.running=True

						# 次の画面準備
						pygame.mixer.music.set_volume(0.12)
						self.screen.blit(self.story_bg1, (0,0))
						pygame.display.update()


		elif self.running:

			if self.gamescene==0:
				# ======================================== PHASE1 ========================================
				# ===== Normal page =====
				self.screen.blit(self.story_bg1, (0,0))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "今日、ぼくは推しのみるくたんのチェキ会に行く"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==1:
				# ===== Normal page =====
				self.screen.blit(self.story_bg1, (0,0))

				self.screen.blit(self.milk, (MILK_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "ほんとに可愛い…"
				text2 = "みるくたんのために生きてる…"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==2:
				# ===== Normal page =====
				self.screen.blit(self.story_bg1, (0,0))

				self.screen.blit(self.milk, (MILK_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "そろそろチェキ会の準備をしなくちゃなぁ…"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==3:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.letter1, (LETTER_1_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "チェキ会に行く準備をしようとしたら謎の封筒が届いた"
				text2 = "何だこれ？開けてみるか"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==4:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.letter2, (LETTER_2_POSI))

			elif self.gamescene==5:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.letter2, (LETTER_2_POSI))
				self.screen.blit(self.q1, (Q_POSI))

			elif self.gamescene==6:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.letter2, (LETTER_2_POSI))
				self.screen.blit(self.q1, (Q_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "え？謎解き？"
				text2 = "急すぎで草"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==7:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.letter2, (LETTER_2_POSI))
				self.screen.blit(self.q1, (Q_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "裏にもなんか書いてあるな…"
				text2 = "「成功したらみるくたんのチェキ券プレゼント！」"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==8:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.letter2, (LETTER_2_POSI))
				self.screen.blit(self.q1, (Q_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "まじ！？"
				text2 = "こんなんやるしか！！！！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==9:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q1_gray, (Q_GRAY_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "何だこりゃ"
				text2 = "一緒に入ってたけどまぁいっか"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))


			elif self.gamescene==10:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q1, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "答えを入力してください"
				text2 = "_ _ _"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

				self.screen.blit(self.blackout, (0,0))
				self.screen.blit(self.s1, (S_POSI))

			elif self.gamescene==11:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q1, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "現れた言葉を入力してください"
				text2 = "_ _ _"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

				# 正解判定が届いた場合の処理
				if self._binarization_is_trueIn.isNew():
					# 正解判定が届いた
					self._d_binarization_is_true=self._binarization_is_trueIn.read()
					if self._d_binarization_is_true.data:
						# 正解した場合「正解！」の画面へ
						print("1問目 正解!!!")
						self.gamescene=12
						self.page_changed = True
					else:
						# 不正解の場合「残念」の画面へ
						print("1問目 残念!!!")
						self.gamescene=13
						self.page_changed = True
				elif self.TEST_MODE:
					print("test_mode")
					self.gamescene=12
					self.page_changed = True
				else:
					# 正解判定がまだ届いてない
					pass

			elif self.gamescene==12:
				# ===== Normal page =====
				# 1問目 正解画面
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q1, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "答えを入力してください"
				text2 = "_ _ _"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

				self.screen.blit(self.whiteout, (0,0))
				self.screen.blit(self.clear, (CLEAR_POSI))

			elif self.gamescene==13:
				# ===== Normal page =====
				# 1問目 不正解画面
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q1, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "答えを入力してください"
				text2 = "_ _ _"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

				self.screen.blit(self.blackout, (0,0))
				self.screen.blit(self.bad, (BAD_POSI))

			elif self.gamescene==14:
				# ===== Normal page =====
				# 1問目 答え提示
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.whiteout, (0,0))
				self.screen.blit(self.a1, (A_POSI))
				self.screen.blit(self.answer_button, (BUTTON_ANSWER_POSI))

			elif self.gamescene==15:
				# ======================================== PHASE2 ========================================
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.letter2, (LETTER_2_POSI))
				self.screen.blit(self.cheki, (CHEKI_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "さっきの紙の色が変わった！"
				text2 = "CHEKI…？"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==16:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.cheki2, (CHEKI_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "！！！！！！！！！"
				text2 = "裏がチェキ券になってるぅ！！！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==17:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.cheki2, (CHEKI_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "本当にみるくたんのチェキ券はゲットできた…"
				text2 = "ヤベェ…"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==18:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "さて、チェキ会に行く前にポーズの練習でもするか"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==19:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q2, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "謎解きをしてポーズ練習をクリアしよう"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.blackout, (0,0))
				self.screen.blit(self.s2, (S_POSI))

			elif self.gamescene==20:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q2, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "謎解きをしてポーズ練習をクリアしよう"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==21:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q2, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				self.screen.blit(self.hint2, (HINT_Q2_POSI))

				if self._detection_is_trueIn.isNew():
					# 正解判定が届いた場合の処理(分類器ver)
					# 正解判定が届いた
					self._d_detection_is_true=self._detection_is_trueIn.read()
					if self._d_detection_is_true.data:
						# 正解した場合「正解！」の画面へ
						print("2問目 正解!!!")
						self.gamescene=22
						self.page_changed = True
					else:
						# 不正解の場合「残念」の画面へ
						print("2問目 残念!!!")
						self.gamescene=23
						self.page_changed = True

				elif self._movenet_is_trueIn.isNew():
					# 正解判定が届いた場合の処理(Movenet ver)
					# 正解判定が届いた
					self._d_movenet_is_true=self._movenet_is_trueIn.read()
					if self._d_movenet_is_true.data:
						# 正解した場合「正解！」の画面へ
						print("2問目 正解!!!")
						self.gamescene=22
						self.page_changed = True
					else:
						# 不正解の場合「残念」の画面へ
						print("2問目 残念!!!")
						self.gamescene=23
						self.page_changed = True

				elif self.TEST_MODE:
					print("test_mode")
					self.gamescene=22
					self.page_changed = True

				else:
					# 正解判定がまだ届いてない
					pass

			elif self.gamescene==22:
				# ===== Normal page =====
				# 問題2正解
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q2, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "謎解きをしてポーズ練習をクリアしよう"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.whiteout, (0,0))
				self.screen.blit(self.clear, (CLEAR_POSI))

			elif self.gamescene==23:
				# ===== Normal page =====
				# 問題3正解
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q2, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "謎解きをしてポーズ練習をクリアしよう"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.blackout, (0,0))
				self.screen.blit(self.bad, (BAD_POSI))

			elif self.gamescene==24:
				# ===== Normal page =====
				# 2問目 答え提示
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.whiteout, (0,0))
				self.screen.blit(self.a2, (A_POSI))
				self.screen.blit(self.answer_button, (BUTTON_ANSWER_POSI))

			elif self.gamescene==25:
				# ======================================== PHASE3 ========================================
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "よし、ポーズのイメージもついたぞ！"
				text2 = "少し時間あるからTL警備でもしよう"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==26:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))
				self.screen.blit(self.tweet, (TWEET_POSI))
				
			elif self.gamescene==27:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.tweet, (TWEET_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "ん・・・？？？"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==28:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.tweet, (TWEET_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "何こいつ、新参の分際で何言ってんだ？"
				text2 = "よし、少し立場をわからせてやるとするか・・・。"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==29:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q3, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "古参アピールできるものが教室のどこかにあるかも？"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.blackout, (0,0))
				self.screen.blit(self.s3, (S_POSI))

			elif self.gamescene==30:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q3, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "古参アピールできるものが教室のどこかにあるかも？"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				# 正解判定が届いた場合の処理
				if self._ssd_is_trueIn.isNew():
					# 正解判定が届いた
					self._d_ssd_is_true=self._ssd_is_trueIn.read()
					if self._d_ssd_is_true.data:
						# 正解した場合「正解！」の画面へ
						print("3問目 正解!!!")
						self.gamescene=31
						self.page_changed = True
					else:
						# 不正解の場合「残念」の画面へ
						print("3問目 残念!!!")
						self.gamescene=32
						self.page_changed = True
				elif self.TEST_MODE:
					print("test_mode")
					self.gamescene=31
					self.page_changed = True
				else:
					# 正解判定がまだ届いてない
					pass

			elif self.gamescene==31:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q3, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "古参アピールできるものが教室のどこかにあるかも？"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.whiteout, (0,0))
				self.screen.blit(self.clear, (CLEAR_POSI))

			elif self.gamescene==32:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.q3, (Q_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				text = "古参アピールできるものが教室のどこかにあるかも？"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.blackout, (0,0))
				self.screen.blit(self.bad, (BAD_POSI))

			elif self.gamescene==33:
				# ===== Normal page =====
				# 3問目 答え提示
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.whiteout, (0,0))
				self.screen.blit(self.a3, (A_POSI))
				self.screen.blit(self.answer_button, (BUTTON_ANSWER_POSI))

			elif self.gamescene==34:
				# ======================================== PHASE4 ========================================
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "ぼくのチェキを見せつけたら返信が来なくなったｻﾞﾏｧm9 (^Д^)"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==35:
				# ===== Normal page =====
				self.screen.blit(self.story_bg2, (0,0))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "そんなこんなでそろそろ家を出る時間だな"
				text2 = "現場に向かうとするか"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==36:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

			elif self.gamescene==37:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "いい天気だな〜"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==38:
				# ===== Normal page =====
				pygame.mixer.music.fadeout(1000)

				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_back, (DOUTAN_BACK_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "ん…？あの後ろ姿は…もしかして…"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==39:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_back, (DOUTAN_BACK_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "同担拒否マン…"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==40:
				# ===== Normal page =====

				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_DOYA_POSI))

				self.screen.blit(self.border_doutan, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "あれあれ〜？君はいつもいる貧乏人くんじゃないか〜"
				text2 = "どうせ数枚しかチェキ撮らないくせにまた現場に行くのかい？"
				if self.page_changed:
					pygame.mixer.music.load("sounds/main_bgm2.mp3")
					pygame.mixer.music.set_volume(0.24)
					pygame.mixer.music.play(-1)

					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==41:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_love, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.border_doutan, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "みるくたんは僕のものなんだ！"
				text2 = "僕が一番お金払ってるんだ！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==42:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_DOYA_POSI))

				self.screen.blit(self.border_doutan, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "ふふ…だから君は帰ってもいいんだよ？"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==43:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "む、むかつく…。"
				text2 = "こいつには負けたくない…。"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==44:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.doutan_sanjou, (0,0))

				if self.page_changed:
					pygame.mixer.music.set_volume(0.48)
					self.page_changed=False
				else:
					pass

			elif self.gamescene==45:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.doutan_taosou, (0,0))

			elif self.gamescene==46:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_love, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.border, (BORDER_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "教室にあるヒントを探そう"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==47:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "僕にできることは…？"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==48:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))
				self.screen.blit(self.blackout, (0,0))

				self.screen.blit(self.choice_11, BUTTON_CHOICE1_POSI)
				self.screen.blit(self.choice_12, BUTTON_CHOICE2_POSI)
				self.screen.blit(self.choice_13, BUTTON_CHOICE3_POSI)
				self.screen.blit(self.choice_14, BUTTON_CHOICE4_POSI)

				self.screen.blit(self.border, (BORDER_POSI))
				text = "____________________を____________________"
				text2 = "一つ目に当てはまるものを選ぼう！"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==49:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))
				self.screen.blit(self.blackout, (0,0))

				self.screen.blit(self.choice_21, BUTTON_CHOICE1_POSI)
				self.screen.blit(self.choice_22, BUTTON_CHOICE2_POSI)
				self.screen.blit(self.choice_23, BUTTON_CHOICE3_POSI)
				self.screen.blit(self.choice_24, BUTTON_CHOICE4_POSI)

				self.screen.blit(self.border, (BORDER_POSI))
				if self.Q4_choice==1:
					text = "「体温測定器」 を ____________________"
				elif self.Q4_choice==2:
					text = "「マスク」 を ____________________"
				elif self.Q4_choice==3:
					text = "「チェキ」 を ____________________"
				elif self.Q4_choice==4:
					text = "「消毒液」 を ____________________"

				text2 = "一つ目に当てはまるものを選ぼう！"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==50:
				# ===== Normal page =====
				# 問題4 正解
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				text = "僕にできることは…？"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.whiteout, (0,0))
				self.screen.blit(self.clear, (CLEAR_POSI))

			elif self.gamescene==51:
				# ===== Normal page =====
				# 問題4 不正解
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				text = "僕にできることは…？"
				if self.page_changed:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

				self.screen.blit(self.blackout, (0,0))
				self.screen.blit(self.bad, (BAD_POSI))

			elif self.gamescene==52:
				# ===== Normal page =====
				self.screen.blit(self.story_bg3, (0,0))

				self.screen.blit(self.doutan_doya, (DOUTAN_LOVE_POSI))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "体温測定器をハッキングしてヤツの体温を捏造してやる！"
				text2 = "そうと決まれば会場に先回りだ！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==53:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))

			elif self.gamescene==54:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))

				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "よし、会場についたぞ！"
				text2 = "体温測定器をハッキングしてやる…！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==55:
				# ===== Normal page =====
				pygame.mixer.music.stop()

				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "・・・・・"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==56:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "よし、あとは同担拒否マンが来るのを待つだけだ"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==57:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_back, (DOUTAN_BACK_POSI))
				
			elif self.gamescene==58:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_back, (DOUTAN_BACK_POSI))
				
				self.screen.blit(self.border, (BORDER_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "（エラー音）"
				if self.page_changed:
					self.error_sound.play(loops=0)
					self.screen.blit(self.font.render(text, True, (242, 78, 30)), LINE_SPEAK_POSI)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (242, 78, 30)), LINE_SPEAK_POSI)


			elif self.gamescene==59:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_back, (DOUTAN_BACK_POSI))
				
				self.screen.blit(self.border_recep, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "ちょっとちょっとお兄さん！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==60:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_turn, (DOUTAN_TURN_POSI))
				
				self.screen.blit(self.border_doutan, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "え？俺？"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==61:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_turn, (DOUTAN_TURN_POSI))
				
				self.screen.blit(self.border_recep, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "そうそう！君！体温測定器が反応してるよ！"
				text2 = "体温が高い人は会場入れないよ！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==62:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_turn, (DOUTAN_TURN_POSI))
				
				self.screen.blit(self.border_doutan, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "え？いや、でも…"
				text2 = "家で測った時は正常だったんだ…！"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==63:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_turn, (DOUTAN_TURN_POSI))
				
				self.screen.blit(self.border_recep, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "そんなこと言われてもねー。"
				text2 = "測定器がダメって言ってるからダメだよー。お帰りくださーい。"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					text_speak_ani(text2, (LINE_SPEAK_POSI[0], 1), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)
					self.screen.blit(self.font.render(text2, True, (84,84,84)), (LINE_SPEAK_POSI[0], LINE_SPEAK_POSI[1]+LINE_SIZE*1.8))

			elif self.gamescene==64:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.doutan_turn, (DOUTAN_TURN_POSI))
				
				self.screen.blit(self.border_doutan, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "そ、そんな…"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==65:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.border_doutan, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				self.screen.blit(self.text_milk, (TEXT_MILK_POSI))
				if self.page_changed:
					self.screem_sound.play(loops=0)
					self.page_changed=False
				else:
					pass

			elif self.gamescene==66:
				# ===== Normal page =====

				self.screen.blit(self.story_bg4, (0,0))
				
				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "これで邪魔者は消えた…"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.text_sound)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (84,84,84)), LINE_SPEAK_POSI)

			elif self.gamescene==67:
				# ===== Normal page =====
				self.screen.blit(self.story_bg4, (0,0))

				self.screen.blit(self.me, (ME_POSI))
				
				self.screen.blit(self.border_me, (BORDER_SPEAK_POSI))
				self.screen.blit(self.next_button, (BUTTON_POSI))
				text = "さて、ぼくのみるくたんに会いに行こう"
				if self.page_changed:
					text_speak_ani(text, (LINE_SPEAK_POSI[0], 0), self.line_space, self.font, self.screen, self.suspicion_sound, color=(242,78,30), stop_sound=False)
					self.page_changed=False
				else:
					self.screen.blit(self.font.render(text, True, (242, 78, 30)), LINE_SPEAK_POSI)

			elif self.gamescene==100:
				# ===== Normal page =====
				self.screen.blit(self.story_bg5, (0,0))

				if self.page_changed:
					pygame.mixer.music.load("sounds/main_bgm.mp3")
					pygame.mixer.music.set_volume(0.24)
					pygame.mixer.music.play(-1, start=830)
					self.page_changed=False
					self.reach_ending=True
				else:
					pass

			else:
				print("error.")
				exit()


			# ================== running2: event処理 ==================
			for event in pygame.event.get():
				if event.type == QUIT:
					self.running=False
					pygame.quit()
					sys.exit()
					
				if event.type == KEYDOWN:
					if self.gamescene==21:
						# ===== 2問目 問題画面 =====
						if event.key == K_RETURN:
							self._d_button.data = 9
							self._buttonOut.write()

					elif self.gamescene==30:
						# ===== 3問目 問題画面 =====
						if event.key == K_RETURN:
							self._d_button.data = 9
							self._buttonOut.write()

				if (event.type==pygame.MOUSEBUTTONUP) and (event.button==1):
					# processing when clicked
					# 画面遷移処理
					if self.gamescene==0:
						# ======================================== PHASE1 ========================================
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=1
							self.page_changed = True

					elif self.gamescene==1:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=2
							self.page_changed = True

					elif self.gamescene==2:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=3
							self.page_changed = True

					elif self.gamescene==3:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=4
							self.page_changed = True

					elif self.gamescene==4:
						# 画面のどこでも押せば次へ
						self.gamescene=5
						self.page_changed = True

					elif self.gamescene==5:
						# 画面のどこでも押せば次へ
						self.gamescene=6
						self.page_changed = True

					elif self.gamescene==6:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=7
							self.page_changed = True

					elif self.gamescene==7:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=8
							self.page_changed = True

					elif self.gamescene==8:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=9
							self.page_changed = True

					elif self.gamescene==9:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=10
							self.page_changed = True

					elif self.gamescene==10:
						# 画面のどこでも押せば次へ
						self.gamescene=11
						self.page_changed = True

					elif self.gamescene==11:
						# ===== 1問目 問題画面 =====
						pass

					elif self.gamescene==12:
						# ===== 1問目 正解 =====
						self.gamescene=14
						self.page_changed = True

					elif self.gamescene==13:
						# ===== 1問目 不正解 =====
						self.gamescene=11
						self.page_changed = True

					elif self.gamescene==14:
						# ======================================== PHASE2 ========================================
						if self.rect_answer_button.collidepoint(event.pos):
							self.next_button_sound.play(loops=0)
							self.gamescene=15
							self.page_changed = True

					elif self.gamescene==15:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=16
							self.page_changed = True

					elif self.gamescene==16:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=17
							self.page_changed = True

					elif self.gamescene==17:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=18
							self.page_changed = True

					elif self.gamescene==18:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=19
							self.page_changed = True

					elif self.gamescene==19:
						# 画面のどこでも押せば次へ
						self.gamescene=20
						self.page_changed = True

					elif self.gamescene==20:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=21
							self.page_changed = True

					elif self.gamescene==21:
						# ===== 2問目 問題画面 =====
						pass

					elif self.gamescene==22:
						# ===== 2問目 正解 =====
						self.gamescene=24
						self.page_changed = True

					elif self.gamescene==23:
						# ===== 2問目 不正解 =====
						self.gamescene=20
						self.page_changed = True

					elif self.gamescene==24:
						if self.rect_answer_button.collidepoint(event.pos):
							self.next_button_sound.play(loops=0)
							self.gamescene=25
							self.page_changed = True

					elif self.gamescene==25:
						# ======================================== PHASE3 ========================================
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=26
							self.page_changed = True

					elif self.gamescene==26:
						# 画面のどこでも押せば次へ
						self.gamescene=27
						self.page_changed = True

					elif self.gamescene==27:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=28
							self.page_changed = True

					elif self.gamescene==28:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=29
							self.page_changed = True

					elif self.gamescene==29:
						# 画面のどこでも押せば次へ
						self.gamescene=30
						self.page_changed = True

					elif self.gamescene==30:
						# ===== 3問目 問題画面 =====
						pass

					elif self.gamescene==31:
						# ===== 3問目 正解 =====
						self.gamescene=33
						self.page_changed = True

					elif self.gamescene==32:
						# ===== 3問目 不正解 =====
						self.gamescene=30
						self.page_changed = True

					elif self.gamescene==33:
						if self.rect_answer_button.collidepoint(event.pos):
							self.next_button_sound.play(loops=0)
							self.gamescene=34
							self.page_changed = True

					elif self.gamescene==34:
						# ======================================== PHASE4 ========================================
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=35
							self.page_changed = True

					elif self.gamescene==35:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=36
							self.page_changed = True

					elif self.gamescene==36:
						# 画面のどこでも押せば次へ
						self.gamescene=37
						self.page_changed = True

					elif self.gamescene==37:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=38
							self.page_changed = True

					elif self.gamescene==38:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=39
							self.page_changed = True

					elif self.gamescene==39:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=40
							self.page_changed = True

					elif self.gamescene==40:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=41
							self.page_changed = True

					elif self.gamescene==41:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=42
							self.page_changed = True

					elif self.gamescene==42:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=43
							self.page_changed = True

					elif self.gamescene==43:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=44
							self.page_changed = True

					elif self.gamescene==44:
						# 画面のどこでも押せば次へ
						self.gamescene=45
						self.page_changed = True

					elif self.gamescene==45:
						# 画面のどこでも押せば次へ
						self.gamescene=46
						self.page_changed = True

					elif self.gamescene==46:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=47
							self.page_changed = True

					elif self.gamescene==47:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=48
							self.page_changed = True

					elif self.gamescene==48:
						if self.rect_choice_1.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							self.Q4_choice = 1
							self.gamescene=49
							self.page_changed = True
						elif self.rect_choice_2.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							self.Q4_choice = 2
							self.gamescene=49
							self.page_changed = True
						elif self.rect_choice_3.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							self.Q4_choice = 3
							self.gamescene=49
							self.page_changed = True
						elif self.rect_choice_4.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							self.Q4_choice = 4
							self.gamescene=49
							self.page_changed = True

					elif self.gamescene==49:
						if self.rect_choice_1.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							self.gamescene=51
							self.page_changed = True
						elif self.rect_choice_2.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							self.gamescene=51
							self.page_changed = True
						elif self.rect_choice_3.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							if self.Q4_choice==1:
								self.gamescene=50
							else:
								self.gamescene=51
							self.page_changed = True
						elif self.rect_choice_4.collidepoint(event.pos):
							self.choice_button_sound.play(loops=0)
							self.gamescene=51
							self.page_changed = True

					elif self.gamescene==50:
						# ===== 4問目 正解 =====
						self.gamescene=52
						self.page_changed = True

					elif self.gamescene==51:
						# ===== 4問目 不正解 =====
						self.gamescene=47
						self.page_changed = True

					elif self.gamescene==52:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=53
							self.page_changed = True

					elif self.gamescene==53:
						# 画面のどこでも押せば次へ
						self.gamescene=54
						self.page_changed = True

					elif self.gamescene==54:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=55
							self.page_changed = True

					elif self.gamescene==55:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=56
							self.page_changed = True

					elif self.gamescene==56:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=57
							self.page_changed = True

					elif self.gamescene==57:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=58
							self.page_changed = True

					elif self.gamescene==58:
						# 画面のどこでも押せば次へ
						self.gamescene=59
						self.page_changed = True

					elif self.gamescene==59:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=60
							self.page_changed = True

					elif self.gamescene==60:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=61
							self.page_changed = True

					elif self.gamescene==61:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=62
							self.page_changed = True

					elif self.gamescene==62:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=63
							self.page_changed = True

					elif self.gamescene==63:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=64
							self.page_changed = True

					elif self.gamescene==64:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=65
							self.page_changed = True

					elif self.gamescene==65:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=66
							self.page_changed = True

					elif self.gamescene==66:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=67
							self.page_changed = True

					elif self.gamescene==67:
						if self.rect_next_button.collidepoint(event.pos):
							self.gamescene=100
							self.page_changed = True

					elif self.gamescene==100:
						self.gamescene=0
						self.running = False
						self.title_running = True
						self.page_changed = True

					else:
						print("error: ", self.gamescene)
						self.gamescene=-1
						exit()

			pygame.display.update()
		
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


def text_ani(str, tuplexy, line_space, font, screen, sound):
	sound.play()
	x, y = tuplexy
	y = LINE_POSI[1]+y*line_space*1.8 ##shift text down by one line
	char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
	letter = 0
	count = 0
	pygame.display.update()
	for i in range(len(str)):
		pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
		time.sleep(0.07) ##change this for faster or slower text animation
		char = char + str[letter]
		text = font.render(char, True, (84,84,84)) #First tuple is text color, second tuple is background color
		textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
		screen.blit(text, textrect)
		pygame.display.update(textrect) ## update only the text just added without removing previous lines.
		count += 1
		letter += 1
	sound.stop()

def text_speak_ani(str, tuplexy, line_space, font, screen, sound, color=(84,84,84), stop_sound=True):
	sound.play()
	x, y = tuplexy
	y = LINE_SPEAK_POSI[1]+y*line_space*1.8 ##shift text down by one line
	char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
	letter = 0
	count = 0
	pygame.display.update()
	for i in range(len(str)):
		pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
		time.sleep(0.07) ##change this for faster or slower text animation
		char = char + str[letter]
		text = font.render(char, True, color) #First tuple is text color, second tuple is background color
		textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
		screen.blit(text, textrect)
		pygame.display.update(textrect) ## update only the text just added without removing previous lines.
		count += 1
		letter += 1
	if stop_sound:
		sound.stop()

	
def GameRunnerInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=gamerunner_spec)
    manager.registerFactory(profile,
                            GameRunner,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    GameRunnerInit(manager)

    # Create a component
    comp = manager.createComponent("GameRunner")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

