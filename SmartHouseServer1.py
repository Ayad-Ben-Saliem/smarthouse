#!/usr/local/bin/python3

import os, subprocess, requests, time

def wait_for_internet_connection():
	while True:
		try:
			response = requests.get('http://216.58.205.206',timeout=1)
			return
		except Exception as e:
			pass

def connect_to_serveo_dot_net():
	while True:
		try:
			wait_for_internet_connection()
			return subprocess.Popen(['/bin/sh', '/home/pi/smarthouse/sshTask.sh'])
		except Exception as e:
			pass

connect_to_serveo_dot_net()

