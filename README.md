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
![Screenshot 2023-12-23 131905](https://github.com/KeerthanaaSaravanan/EX-11_copy-file/assets/145742596/c64a3d71-ef12-4f8c-bcfc-8e59050393a4)
![Screenshot 2023-12-23 131853](https://github.com/KeerthanaaSaravanan/EX-11_copy-file/assets/145742596/0cc21521-09ba-4e6a-bce3-8662acf4cdd5)
![Screenshot 2023-12-23 131857](https://github.com/KeerthanaaSaravanan/EX-11_copy-file/assets/145742596/827d55c3-b134-4051-9733-1350890503d0)

## RESULT:
Thus the program is written to copy the contents from one file to another file.
