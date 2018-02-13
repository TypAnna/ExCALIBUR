import AllServers
import Server
import sys
import os
import subprocess
class Main:
	try:
		
				
		#print "\n\n\nNow the client will logon to the connect command. \nThere are four commands that will be run, \'connect\', \'*username*\' \'*password*\' \'cd /root\'. \n You need to press enter for each one to be run. It is important that you do not run the \'connect\' command untill you se the admin-flag.\n It is also important that you do not send the username before you see a clear terminal. And that you send the password shortly after you have supplied the username.\nYou need to keep track of which command is to be run since there will be no further instruction until you have logged in successfully. \n\nIt sounds hard but it's really not, let's get started! \n\nThe first step is manually logging in in the window to the right."
		

		client=AllServers.AllServers()

		
		
		
	
		client.IpCasesFile = 'IpCasesFile.txt'
		client.ServerMacIp = 'ServerMacIp.txt'
		client.ECUT = 'ECUT_file_basic_info.txt'
		client.pipeList = [sys.argv[1], sys.argv[2]]
		print "Welcome to ExCALIBUR"
		client.prepareOnceForAll()
		client.setCurrentServer()	
	
	
		while client.iCounter<len(client.SMIpList):
		
			client.currentServer.serverName=client.SMIpList[client.iCounter][0]
			client.currentServer.macAddress=client.SMIpList[client.iCounter][1]
			
			

			os.system("gnome-terminal -e 'bash -c \"ssh -tt root@" +client.currentServer.serverName+"-idrac < en.fifo > en2.fifo; bash\" '")
			
			client.doAllThings()
			client.iCounter += 1
			
			client.fileText = 0
			client.possibleExistence=0
			client.bStop=False

			#except LookupError:
				#client.iCounter+=1
				
			
						
	
	
	#This is supposed to make the program logout from the iDRAC even if CTRL+C is pressed.
	except KeyboardInterrupt:
		print "\nJust logging out first...\n"		
		try: 
			client.doFinalThings()
		except NameError:	
			pass
		finally:
			sys.exit(0)
				

			
			

		
		
	
	
	
			
			
		
		
