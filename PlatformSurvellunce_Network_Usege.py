import psutil
import sys
import os
import time
import schedule


def platformSurvillance(FolderName):
    Border = "-" * 50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as folder name is existing but its not directory")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for the Log File gets created Successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    print(f"Log file get Successfully Created with name {FileName}")

    fobj.write(Border + "\n")
    fobj.write("----Marvellous Platform Survillence System ---\n")

    fobj.write("Log file get created at : " + timestamp + "\n")

    fobj.write(Border + "\n\n")

    fobj.write("---System Report---\n")
# CPU Information 
    fobj.write("Number of Activet CPU Usage : %s\n" %psutil.cpu_percent())
    fobj.write(" CPU Usage :%s %%\n" %psutil.cpu_percent())
    fobj.write(Border + "\n")
    
    
#RAM information
    memory = psutil.virtual_memory()
    
    fobj.write("RAM Usage : %s %%\n" %memory.percent())
    fobj.write("Total RAM  Available : %s\n" %memory.percent())
    fobj.write(Border + "\n")

# Network Usege
    netobj = psutil.net_io_counters()
    
    fobj.write("NetworkUsage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 *1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 *1024)))

    
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n")
    

    fobj.write(Border + "\n")
    fobj.write("---End of Log File---\n")
    fobj.write(Border + "\n")

    fobj.close()


def main():
    Border = "-" * 50

    print(Border)
    print("----Marvellous Platform Survillence System ---")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "__h" or sys.argv[1] == "__H"):
            print("This Automation script is use to perform")
            print("1 : it fetch the information of running processes")
            print("2 : it fetch the information about the primary storage as RAM")
            print("3 : it fetch the information About the secondary storage as HDD")
            print("4 : it fetch the information About the Microprocessor")

        elif(sys.argv[1] == "__u" or sys.argv[1] == "__U"):
            print("Usage : python Assignment32_5.py Time FolderName")
            print("Example : python Assignment32_5.py 1 Log")

    elif(len(sys.argv) == 3):
        #print("CPU Usege : ", psutil.cpu_percent())
        print("Scheduler Started Successfully")
        print("Press Ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(platformSurvillance, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number Of Argument")
        print("Unable to proceed as arguments are not matching")
        print("Please use __h or __u flag for getting more details")

    print(Border)
    print("---Thank you for using Automation System---")
    print(Border)


if __name__ == "__main__":
    main()