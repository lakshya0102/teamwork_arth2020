import os
import xml.etree.ElementTree
os.system("tput setaf 3")
print("\t\t\tWelcome to hadoop Configuration !!")
os.system("tput setaf 7")
print("\t\t\t--------------")
print("""
\n
Press 1 : configure hdfs-site.xml file
Press 2 : configure core-site.xml file
Press 3 : start datanode
Press 4 : jps
Press 5 : stop datanode
Press 6 : report
Press 7 : check uploaded file
Press 8 : exit
""")
ch =1 
while(int(ch) != 9):
	ch = input("\n\nEnter ur choice : ")
	if int(ch) == 1:
             n = input('enter value for name : ')
             v = input('enter value for value : ')
             et = xml.etree.ElementTree.parse('/etc/hadoop/hdfs-site.xml')
             pro = xml.etree.ElementTree.SubElement(et.getroot(),'property')
             name = xml.etree.ElementTree.SubElement(pro,'name')
             val = xml.etree.ElementTree.SubElement(pro,'value')
             name.text = n
             val.text = v
             et.write('/etc/hadoop/hdfs-site.xml')
	elif int(ch) == 2:
             n = input('enter value for name : ')
             v = input('enter value for value/ip : ')
             et = xml.etree.ElementTree.parse('/etc/hadoop/core-site.xml')
             pro = xml.etree.ElementTree.SubElement(et.getroot(),'property')
             name = xml.etree.ElementTree.SubElement(pro,'name')
             val = xml.etree.ElementTree.SubElement(pro,'value')
             name.text = n
             val.text = v
             et.write('/etc/hadoop/core-site.xml')
	elif int(ch) == 3:
	     os.system("hadoop-daemon.sh start datanode")
	elif int(ch) == 4:
	     os.system("jps")
	elif int(ch) == 5:
	     os.system("hadoop-daemon.sh stop datanode")
	elif int(ch) == 6:
	     os.system("hadoop dfsadmin -report")
	elif int(ch) == 7:
	     os.system("hadoop fs -ls /")
	elif int(ch) == 8:
	     exit()
	else:
	     print("wrong choice")




