import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import os
import Server
from threading import Thread
from sys import stdout
from sys import stderr
import sys

#from termcolor import colored
#import termcolor
#from PyQt4 import QtGui
#SNM DAB
#ExCALIBUR
#Executable Controller for Automating Large Implementations ofBack-end Units Remotely


class AllServers:

	#constructor method that takes arguments
        def __init__(self, ipCases, SMIpList, fileText, currentServer, IpCasesFile, ServerMacIp, ECUT, channelToTerminal, channelToPipe, pipeList, possibleExistence, booleanInit, booleanEx, booleanFin, iCounter, bStop):

                self.ipCases = ipCases
                self.SMIpList = SMIpList
                self.fileText = fileText
                self.currentServer=currentServer
                self.IpCasesFile = IpCasesFile
                self.ServerMacIp = ServerMacIp
                self.ECUT=ECUT
                self.channelToTerminal = channelToTerminal
                self.channelToPipe = channelToPipe
		self.pipeList = pipeList
		self.possibleExistence = possibleExistence
		self.booleanInit = booleanInit
		self.booleanEx = booleanEx
		self.booleanFin = booleanFin
		self.iCounter = iCounter
		self.bStop = bStop

	#constructor method without arguments.
	def __init__(self):

                self.ipCases = 0
                self.SMIpList = 0
                self.fileText = 0
                self.currentServer=0
                self.IpCasesFile = 0
                self.ServerMacIp = 0
                self.ECUT=0
                self.channelToTerminal = 0
                self.channelToPipe = 0
		self.pipeList = 0
		self.possibleExistence = 0
		self.booleanInit = 0
		self.booleanEx = 0
		self.booleanFin = 0
		self.iCounter = 0
		self.bStop = 0
	
	

        def readIpCases(self):
                ipCasesRaw = open(self.IpCasesFile, 'r')

                self.ipCases = ipCasesRaw.read().split() #Turns the text into list with IP-elements
                 

        def setCurrentServer(self):



                self.currentServer = Server.Server(0,0,0,0,0)


        def stripIp(self):
                strippedIpNoPeriod = (self.currentServer.ipAddress[::-1].split('.',1)[1])[::-1]
                self.currentServer.strippedIp = "".join((strippedIpNoPeriod, '.'))
 


        def createSMIpList(self):
                self.SMIpList = []
                SMIpListRaw = open(self.ServerMacIp, 'r')
                SMIpListLong = SMIpListRaw.read().split()

                k = 0
                while k <= (len(SMIpListLong) -3):
                        self.SMIpList.append([SMIpListLong[k], SMIpListLong[k+1].lower(), SMIpListLong[k+2]])
                        k = k+3



        def checkIp(self):

                if self.currentServer.strippedIp not in self.ipCases:
                        self.wannaContinue
 


        def prepareText(self):
        	"prepare text running"
                 
                
                fileTextRaw = open(self.ECUT, 'r')
                self.fileText= fileTextRaw.read().replace('IpAddress', self.currentServer.ipAddress)
                self.fileText=self.fileText.replace('splittedIp', self.currentServer.strippedIp)
                self.fileText=self.fileText.replace('interfaceName', str(self.currentServer.interfaceName))
                 
                


        def createFile(self):
        	print 'createFile running'
        	
        	self.prepareText()
                fileToCreate="ifcfg-"+str(self.currentServer.interfaceName)
                a = raw_input()
                
                self.channelToTerminal.write("touch "+fileToCreate +"\r")
                self.channelToTerminal.flush()
                print fileToCreate
                
                a = raw_input()
                self.channelToTerminal.write("echo \'"+str(self.fileText)+"\'>"+fileToCreate+ "\r")
                self.channelToTerminal.flush()
                
               
        	

        def doInitialThings(self):
                  
                self.booleanInit = True
                t1 = Thread(target=self.interfaceFun)

                if len(self.pipeList) > 1:
                        self.channelToTerminal = open(self.pipeList[0],"w+") 
                        stdout.flush() 
                else:
                        self.channelToTerminal = sys.stdout

       		


		data = ["connect\r","\r", "USER\r", "PASS\r", "cd /root\r"]

                t1.start()		
		
			
		i = 0
		while i < len(data):  
			a=raw_input()
			
                        if not a == "":
                                self.channelToTerminal.write(a + "\r")

                        else:
				                             
				self.channelToTerminal.write(data[i])
                                i += 1

			self.channelToTerminal.flush()
			
			
                    
                a = raw_input()
                self.booleanInit = False
                t1.join() 
                
                
                
                
                
        def interfaceFun(self):
		
				
		s = ""
                self.channelToPipe = open(self.pipeList[1], "r")
                
	
                while self.booleanInit:
			if self.bStop: self.booleanInit = False
                        a = self.channelToPipe.read(1)
                        stdout.write(a)
                        stdout.flush()

		ifconfigString = "ifconfig -a | grep "+str(self.currentServer.macAddress)+"\r"
                self.channelToTerminal.write("ifconfig -a | grep "+str(self.currentServer.macAddress)+"\r")
             
		
                self.channelToTerminal.flush()
                a =  raw_input()

                for i in range(len(ifconfigString)):
          
                	k=self.channelToPipe.read(1)
                	
                        stdout.write(k)
                        stdout.flush()

                for p in range(20):
                        k=self.channelToPipe.read(1)
                        s = s+k			
                        stdout.write(k)
                        stdout.flush()
		try:
        		self.currentServer.interfaceName = s.split()[0]  
		except IndexError:
			print "Something went wrong with the interface name, the string from which it is normally derived is currently: "+str(s)+"."
			self.wannaContinue()
                


        def getIpAddress(self):
                readLine = subprocess.Popen(['nslookup', self.currentServer.serverName ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                outputString, err = readLine.communicate()
                self.currentServer.ipAddress = outputString.split()[-1]



	def fileFun(self):
                fileString = ""
             	
                while self.booleanEx:
			if self.bStop: self.booleanEx = False
			d = self.channelToPipe.read(1)
                   	stdout.write(d)
                  	stdout.flush()	
			self.channelToTerminal.write("ls | grep ifcfg-"+str(self.currentServer.interfaceName) +" --color=never\r")
			print "This is the interfacename from grep: "+str(self.currentServer.interfaceName) 
			self.channelToTerminal.flush()
			a = raw_input()
	
			for i in range(len("ls | grep ifcfg-"+str(self.currentServer.interfaceName) +" --color=never\r")+len("ifcfg-")+len("\r")+len(str(self.currentServer.interfaceName))):
				d = self.channelToPipe.read(1)
			   	fileString = fileString+d
			   	stdout.write(d)
			    	stdout.flush()	

			a=raw_input()

			try:
				self.possibleExistence=fileString.split()[-1]
			except IndexError:
				self.possibleExistence=""
				pass
                
                
                

	def doesFileExist(self):
		if not self.bStop:
			self.booleanEx = True
		else: 
			self.booleanEx=False
            	

		data1 = ["cd ..\r", "cd etc/network/interfaces.d \r"]
            	t2=Thread(target=self.fileFun)
            	j = 0
            	t2.start()
           	while j < len(data1):
                	a = raw_input()

                	""" If something went wrong, allow manual access """
                	if not a == "":
                    		self.channelToTerminal.write(a + "\r")
  
                	else:
                    		self.channelToTerminal.write(data1[j])
                    		j += 1

                	self.channelToTerminal.flush()


		a=raw_input()

            	self.booleanEx=False
            
            	t2.join()
            	
            	
            	
            	try:
            		if str(self.possibleExistence) == 'ifcfg-' + str(self.currentServer.interfaceName):
                	
				inf=1/0 #this will raise the an exception which we catch below
			
                except ZeroDivisionError:
			print "It seems like the file we're trying to create: "+str(self.possibleExistence)+" already exists."
			self.wannaContinue()
				
                

	
	

		
	
        def doFinalThings(self):
        	t3 = Thread(target=self.finFun)
            	finalData = ["cd /root\r", "logout\r"]
		
            	self.booleanFin=True
            	i = 0
            	t3.start()
            	
            	while i < len(finalData):
                	a = raw_input()
        
                	# If something went wrong, allow manual access 
                	if not a == "":
                    		self.channelToTerminal.write(a + "\r")
            
                	# Otherwise (if enter-key pressed), continue with commands in data-list 
                	else:
                    		self.channelToTerminal.write(finalData[i])
                    		i += 1
                	self.channelToTerminal.flush()
         
            	a = raw_input()
            	self.booleanFin = False
            	t3.join()

	def finFun(self):

        	while self.booleanFin:
			d = self.channelToPipe.read(1)
                   	stdout.write(d)
                  	stdout.flush()

                a=raw_input()		
		

        def prepareOnceForAll(self):
                self.readIpCases()
                self.createSMIpList()


        def wannaContinue(self):

                answer = raw_input('Do you want to continue with the next server? (y/n)')
                if answer == 'y':
			bStop=True
			self.doFinalThings()	
						
		
                elif answer == 'n':
			bStop=True
			self.doFinalThings()
                        self.iCounter= len(self.SMIpList)+1

                else:                        
                        self.wannaContinue()


	
		
					
	
        def doAllThings(self):
                
              	try:
			self.getIpAddress()
                	self.stripIp()
			if not self.bStop:	
                		self.checkIp()         			                	
				self.doInitialThings()             
                		self.doesFileExist()        
                		self.createFile()                                	
                        
		except:
			self.wannaContinue()
			
			
                	

                self.doFinalThings()
                print str('Finished with server '+self.currentServer.serverName+'.')


