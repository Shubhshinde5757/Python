

import psutil
import sys
import os
import time


def platformSurvillance(FolderName):
    Border = "-"*50

    Ret = False
    
    Ret = os.path.exists(FolderName)
    
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        
        if(Ret == False):
            print("Unable to proceed as folder name is existing but its not directory")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory for the Log File  gets created Sucessfully")


    timestamp =time.strftime("%Y-%m-%d_%H-%M-%S")
    
    FileName = os.path.join(FolderName,"Marvellous_%s.log"%timestamp)
    fobj = open(FolderName,"w")
    
    print(f"Log file get Succesfully Created  with name {fileName}")
def main():
    Border = "-"*50
    print(Border)
    print("----Marvellous Platform Survillence System ---")
    print(Border)
    
    if(len(sys.argv)== 2):
                if(sys.argv[1] == "__h" or sys.argv[1] =="__H"):
                    print("This Automation script is use to perform")
                    print("1 : it fetch the information of running processess")
                    print("2 : it fetch the information about the primary storage as RAM")
                    print("3 : it fetch the information About the secondarystorage as HDD")
                    print("4 : it fetch the information About the Microprocess")
        
    # __h & __u
    elif(len(sys.argv) == 3):
        
        if(sys.argv[1] == "__u" or sys.argv[1] =="__U"):
            print("Use the Automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time inminute fo")            
            
    else:
        print("Invalid Number Fo Argument")
        print("Unable to proceed as argument are not matching")
        print("Please use __h or __u flag for getting more details") 
        
    
    
    print(Border)
    print("---Thank you for yosinf Automation System  ---")
    print(Border)
    

if __name__=="__main__":
    main()