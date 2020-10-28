import os
os.system("tput setaf 1")
print("welcome")
os.system("tput setaf 3")
print("----------------")

import getpass
password=getpass.getpass("enter password:")
if password!='lw':
	print("wrng password")
	exit()

r=input("want to run remotely 0r locally? remote/local: ")
print(r)




if r=="local":

	print("""press 1:cal
	press 2:date
	press 3:firefox
	press 4:open menu.py
	press 5:to re-run the program
	press 6:create lVM
	press 7:configure apache webserver
	press 8:""")


	os.system("tput setaf 4")

	i=5
	while i>1:

		ch=input("enter yout choice : ")
	  
		if int(ch)==1:  
			os.system("cal")
		elif int(ch)==2:
			os.system("date")
	 
		elif str(ch)=="exit" :
			exit()
		elif int(ch)==4:
			os.system("gedit menu.py")
		elif int(ch)==5:
			os.system("python3 menu.py")
		elif int(ch)==6:
			hd1=input("enter hardisk name to create PV:")
			hd2=input("enter hardisk name to create pv:")
			os.system("pvcreate {}".format(hd1)) 
			os.system("pvcreate {}".format(hd2))

			vg1=input("enter vgname to create vg:")
			os.system("vgcreate {} {} {} ".format(vg1,hd1,hd2))

			lv1=input("enter lvname to create lv:")
			os.system("lvcreate --size 10G --name {} {}".format(lv1,vg1))

			os.system("mkfs.ext4 /dev/{}/{}".format(vg1,lv1))

			slavenode=input("slavenode dir name:")

			os.system("mkdir {}".format(slavenode))
			os.system("mount /dev/{}/{}  {}".format(vg1,lv1,slavenode))
		elif int(ch)==7:
			
			os.system("yum install httpd")
			os.system("y")
			os.system("cd/var/www/html")
			x=input("enter file name for webserver:")
			os.system("vi {}".format(x))
			os.system("systemctl start httpd")
			print("done!! httpd webserver configured")


		

elif r=="remote":
	

	print("""press 1:cal
	press 2:date
	press 3:firefox
	press 4:open menu.py
	press 5:to re-run the program""")
	


	os.system("tput setaf 4")
	ip=input("enter ip :")
	print(ip)

	i=5
	while i>1:

		ch=input("enter yout choice : ")
		  
		if int(ch)==1:
			os.system("ssh {} cal".format(ip))
		elif int(ch)==2:
			os.system("ssh {} date".format(ip))
		 
		elif str(ch)=="exit" :
			exit()
		elif int(ch)==4:
			os.system("gedit menu.py")
		elif int(ch)==5:
			os.system("python3 menu.py")
		elif int(ch)==6:
			os.system("ssh {} python3 l.py".format(ip))
				
			
else:
	print("wrong selection")	
	exit()

