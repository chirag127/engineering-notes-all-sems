from pydoc_data.topics import topics
import webbrowser

from time import sleep

# open syllabus\m.txt
# # 1 KCS501 Database Management System 3 1 0 30 20 50 100 150 4
# 2 KCS502 Compiler Design 3 1 0 30 20 50 100 150 4
# 3 KCS503 Design and Analysis of
# Algorithm 3 1 0 30 20 50 100 150 4
# 4
# Deptt.
# Elective-I
# Departmental Elective-I 3 0 0 30 20 50 100 150 3
# 5
# Deptt.
# Elective-II
# Departmental Elective-II 3 0 0 30 20 50 100 150 3
# 6 KCS551 Database Management System
# Lab 0 0 2 25 25 50 1
# 7 KCS552 Compiler Design Lab 0 0 2 25 25 50 1
# 8 KCS553 Design and Analysis of
# Algorithm Lab 0 0 2 25 25 50 1
# 9 KCS554 Mini Project or Internship
# Assessment*
# 0 0 2 50 50 1
# 10 KNC501/
# KNC502
# Constitution of India, Law and
# Engineering /
# Indian Tradition, Culture and
# Society
# 2 0 0 15 10 25 50
# 11 MOOCs (Essential for Hons.
# Degree)
# Total 17 3 8 950 2

files = ['dbms.txt',"cd.txt","daa.txt","wd.txt","ml.txt","coile.txt"]

import random

files = random.sample(files, len(files))

for file in files:

    with open(f"syllabus/{file}", 'r') as f:
        m = f.read()

        topics = m.split(',')

        print(topics)

        for topic in topics:

            topic = topic.strip()

            print(topic)

            webbrowser.open('https://www.youtube.com/results?search_query=' + topic)

            import pyautogui

            pyautogui.FAILSAFE = False

            pyautogui.hotkey('ctrl', 'w')

            sleep(1)

            # move to previous tab
            pyautogui.hotkey('ctrl', "shift", 'tab')

            sleep(1)
