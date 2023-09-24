from getpass import getpass
from time import sleep
from sys import exit

print("Welcome to ubuntu access")
sleep(1)

unixname = input("Enter Unix name: ")
password = getpass(prompt="New password: ")
retypepassword = getpass(prompt="Retype password: ")

sleep(2)

if retypepassword == password:
    print("Created password successfully")
    sleep(1)
    print("Creating Virtual Environvment Desktop...") 
    sleep(2)
    print("Creating Virtual Environvment Apps..") 
    sleep(2)
    print("Creating Virtual Environvment Terminal setup...") 
    sleep(2)
    print("Creating Virtual Environvment All Terminal Commands...")
    sleep(2)
    print("Creating Virtual Environvment Sudo Commands...")
    sleep(2)
    print("Updating system32...")
    sleep(4)
    print("Updaing System...")
    sleep(4)

    print("Please type shutdown -h to shutdown and complete installation")
    shutdown = input(f"{unixname}@Linux:system32$ ")
    if shutdown == "shutdown -h":
        print("Completing installation...")
        sleep(6)
        print("Shuting down the computer...")
        print(2)
        exit()
    
    else:
        print("Please type shutdown -h to shutdown and complete installation")
        shutdown = input(f"{unixname}@Linux:system32$ ")
        if shutdown == "shutdown -h":
            print("Completing installtion...")
            sleep(6)
            print("Shutting down the computer...")
            sleep(2)
            exit()

else:
    print("Wrong password")
    exit() 