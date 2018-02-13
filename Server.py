import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import os

class Server:
	
	def __init__(self, macAddress, serverName, interfaceName, ipAddress, strippedIp):
		self.macAddress = macAddress
		self.serverName = serverName
		self.interfaceName = interfaceName
		self.ipAddress = ipAddress
		self.strippedIp = strippedIp

	

	
