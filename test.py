import os
print("\t\t\t WELCOME")
print("""
press 1 :creating partition
press 2 :format partition
press 3 :creating folder and mounting
press 4 :exit""")

ch=input("Enter your choice : ")

if int(ch)==1:
    os.system("fdisk /dev/sdb")

elif int(ch)==2:
    drivename=input("choose sdb1 / sdb2 / sdb3 = ")
    os.system("mkfs.ext4  /dev/"+drivename)
    print("successfully formatted ")

elif int(ch)==3:
    foldername =input("Enter the name of folder =")
    os.system("mkdir /"+foldername)
    drivename=input("sdb1 / sdb2 /sdb3 = ")
    os.system("mount /dev/"+drivename+" /"+foldername)

elif int(ch)==4:
    os.system("exit()")
else:
    print("invalid number")
    exit()
