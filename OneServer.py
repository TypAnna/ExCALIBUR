import AllServers
import Server
import sys
import os

class OneServer:
	
	
	
	client = AllServers.AllServers(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	#client = AllServers.AllServers()
	client.IpCasesFile = 'IpCasesFile.txt'
	client.ServerMacIp = 'ServerMacIp.txt'
	client.ECUT = 'ECUT_file_basic_info.txt'
	client.pipeList = [sys.argv[1], sys.argv[2]]
	print sys.argv[2]
	client.prepareOnceForAll()
	client.setCurrentServer()	
	
	k=0
	
	
	client.currentServer.serverName=client.SMIpList[k][0]
	client.currentServer.macAddress=client.SMIpList[k][1]
	
	os.system("gnome-terminal -e 'bash -c \"ssh -tt root@" +client.currentServer.serverName+"-idrac < en.fifo > en2.fifo; bash\" '")	
		
		
	#try:
	client.doAllThings()
		
	#except StopIteration:
		#""	
