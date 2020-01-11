# Write 1
#f = open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile.txt", "w")
#for i in range(1,11):
#    data = "%d \n" % i
#    f.write(data)
#f.close()

# Read1
#f = open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile.txt", "r")
#while True:
#    line = f.readline()
#    if not line: break
#    print(line)    
#f.close()

# Read2
#f = open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile.txt", "r")
#lines = f.readlines()
#for line in lines:
#    print(line)
#f.close()

## Read3
#f = open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile.txt", "r")
#data = f.read()
#print(data)
#f.close()

##Edit
#f = open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile.txt", "a")
#for i in range(11,20):
#    data = "%d \n" % i
#    f.write(data)
#f.close()

##Open with With write
#with open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile1.txt", "w") as f:
#    f.write("YOLO!!!!")

##using sys module

#import sys

#args = sys.argv[1:]
#for i in args:
#    print(i)
### notworking




##Example

with open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile3.txt","w") as w:
    w.write("""
    Life is too short
    java
    """)




with open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile3.txt","r") as r:
    data = r.readlines();
    for i in data:
       i.replace("java", "python")
    
with open("C:/Users/Administrator.Sc-201909231805/Desktop/James/newFile3.txt","a") as a:
    for i in data:
        a.write(i.replace("java", "python"))
    

"""
r : Opens a file for reading only. The file pointer is placed at the beginning of the file
this is the default mode.


rb: Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

r+ : Opens a file for both reading and writing . The file pointer placed at the beginning of the file

rb+ : Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.

w : Opens a file for writing only. Overwrites the file if the file exists. if the file does not exist , creates a new file for writing

wb : Opens a file for writing only in binaryformat. Overwrites the file if the file exsits. if the file does not exist, creates a new file for writing

w+ : opens a file for both writing and reading. Overwrites the existing file if the file exists. if the file does not exist, creates a new file for reading and writing

wb+ : Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists . if the file does not exist, creates a new file for reading and writing

a : Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

a+ Opens a file for both appending and reading. 
The file pointer is at the end of the file if the file
exists. The file opens in the append mode. 
If the file does not exist, 
it creates a new file for reading and writing.

"""


#File Positinos

"""
    seek method changes the current file position.
   The The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved.

If from is set to 0, it means use the beginning of the file as the reference position and 1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.

"""