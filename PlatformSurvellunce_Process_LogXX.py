import psutil
import sys
import os
import time
import schedule

def processScan():
    listprocess = []
    
    
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()
        
        listprocess.append(info)
        
    return listprocess
       
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

    # Corrected
    fobj = open(FileName, "w")

    # Corrected
    print(f"Log file get Successfully Created with name {FileName}")

    fobj.write(Border + "\n")
    fobj.write("----Marvellous Platform Survillence System ---\n")

    # Corrected
    fobj.write("Log file get created at : " + timestamp + "\n")

    fobj.write(Border + "\n\n")

    fobj.write("---System Report---\n")

    # CPU Information
    fobj.write("Number of Active CPU : %s\n" % psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    fobj.write(Border + "\n")

    # RAM Information
    memory = psutil.virtual_memory()

    # Corrected (.percent is an attribute, not a function)
    fobj.write("RAM Usage : %s %%\n" % memory.percent)
    fobj.write("Total RAM Available : %.2f GB\n" % (memory.total / (1024 * 1024 * 1024)))
    fobj.write("Available RAM : %.2f GB\n" % (memory.available / (1024 * 1024 * 1024)))
    fobj.write(Border + "\n")

    # Network Usage
    netobj = psutil.net_io_counters()

    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Received : %.2f MB\n" % (netobj.bytes_recv / (1024 * 1024)))
    
# process log
    Data = processScan()
    
    for info in Data:
       # fobj.write(f"{info}\n")
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("User Name : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("CPU usge : %.2f\n" %info.get("cpu_percent"))
        fobj.write("RAM usage : %.2f\n" %info.get("memory_percent"))

        fobj.write(Border + "\n")

        

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
            print("Usage : python PlatformSurvellunce_Network_Usege.py Time FolderName")
            print("Example : python PlatformSurvellunce_Network_Usege.py 1 Log")

    elif(len(sys.argv) == 3):
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