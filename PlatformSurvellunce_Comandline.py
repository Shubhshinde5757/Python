# python ProcessSurvellunce.py 2 MarvellousLog
## python ProcessSurvellunce.py time_ interval Folder_Name
#              0                      1             2
# len(ysy.argv)  ->3
# python ProcessSurvellunce.py__h
# python ProcessSurvellunce.py__u



import psutil
import sys
import os


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