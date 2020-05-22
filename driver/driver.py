# coding=utf-8
# 登录模块
from selenium import webdriver
import time
import os


def browser():
    # os.system("taskkill /F /iM iexplore.exe") #启动之前杀掉IE浏览器j进程
    driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    browser()
