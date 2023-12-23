# EX-11: Copy-file
## AIM:
To write a python program for copying the contents from one file to another file.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
### Step 1:
Use open function to open the file in which we want to copy from and access it in read mode.
### Step 2: 
 Read the file and store in a variable.
### Step 3: 
Now create a new file in which we want to paste the content using write access mode.
### Step 4:  
Use write function to copy the read file that has been stored in the variable.
### Step 5: 
The content in the original file will be copied in the new file.
### Step 6: 
End the program.
## PROGRAM:
```
with open('original.txt','r')as fp:
	msg1=fp.read()
with open('copy.txt','a')as fp1:
	fp1.write(msg1)
```
### OUTPUT:
![image](https://github.com/KeerthanaaSaravanan/EX-11_copy-file/assets/145742596/ed70447f-5316-43e5-a863-2eff42bc9c56)
![image](https://github.com/KeerthanaaSaravanan/EX-11_copy-file/assets/145742596/67083ffd-00a5-49e4-b360-55a95f7111eb)
![image](https://github.com/KeerthanaaSaravanan/EX-11_copy-file/assets/145742596/7ceac6c2-10f2-407d-9419-dba545fb4ee4)

## RESULT:
Thus the program is written to copy the contents from one file to another file.
