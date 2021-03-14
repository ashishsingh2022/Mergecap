import subprocess
import threading
import os


bin_location=os.path.join(os.getcwd(),"mergecap")

def executeCommand(cmd,dir):
	split_cmd=cmd.split()
	file_name=dir+".pcap"
	split_cmd.extend(["-w",file_name])
	subprocess.run(split_cmd)
	print(split_cmd,"Completed")

def merge_and_clean(output):
	merge_cmd=["sudo",bin_location,"-w",output+".pcap","in.pcap","out.pcap"]
	subprocess.run(merge_cmd)
	#os.remove("in.pcap")
	#os.remove("out.pcap")
	
	
	
if __name__=="__main__":
	cmd1=input("Enter Command1 ")
	cmd2=input("Enter Command2 ")
	thread1=threading.Thread(target=executeCommand,args=(cmd1,"in"))
	thread2=threading.Thread(target=executeCommand,args=(cmd2,"out"))
	
	# These two should be in a block
	thread1.start()
	thread2.start()
	
	thread1.join()
	thread2.join()
	
	
	choice='!'
	while choice!='Y' and choice!='N':
		choice=input("Would you like to merge the files by timestamp[Y/N]?")
		
	
	if choice=='Y':
		output=input("Enter path with filename to save the output ")
		merge_and_clean(output)
		print("The output of commands written in ",output)
	else:
		print("cmd1 output in in.pcap and cmd2 output in out.pcap")
		
		
	
	
	
