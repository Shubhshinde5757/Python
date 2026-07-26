import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    
    if Ret == False:
        print("Path is Invalide")
        return
    Ret = os.path.isdir(DirectoryName)
    
    if Ret == False:
            print("it is not a Directory")
            return
        
    Duplicate = {}
   
        
    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
           
            fname = os.path.join(FolderName, fname)
            
            Checksum = CalculateChecksum(fname)
            
            
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

                
    return Duplicate 
  
def DeleteDuplicate(DirectoryName):  
    print = FindDuplicate(DirectoryName)
    
    Result = MyDict.values()
    
    
    Result = list(filter(lambda x : len(x) > 1),MyDict.values())
    Count =0
    TotalDeleted = 0
    
    for value in Result:
        for subvalue in value:
            
            Count = Count + 1
            if(Count > 1 ):
                print("Duplicate found :",subvalue)
                TotalDeleted = TotalDeleted + 1
                
        Count = 0
   
            
def main():
    Data  =  DeleteDuplicate("Test")
    

if __name__ == "__main__":
    main()