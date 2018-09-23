#!/usr/bin/env python3
#-*-coding: utf-8 -*-
import os

#########################################
#########################################
###  yazar  : burakbüyükyüksel        ###
###  e-mail : bbuyukyuksel@gmail.com  ###
###  tarih  : 23.09.2018              ###
#########################################
#########################################

serverip = input("\033[01;33m#Server IP        : \033[00m")
hostname = input("\033[01;33m#Kullanıcı Adı    : \033[00m")
password = input("\033[01;33m#Kullanıcı Parola : \033[00m")


cmd = "rdesktop -k tr -u '{}' -p '{}' -f -a 16 {}".format(hostname,password,serverip)

os.system(cmd)
	
print("\033[01;31m#Program Sonlandırıldı!\033[00m")

