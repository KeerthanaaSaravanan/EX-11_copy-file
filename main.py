with open('original.txt','r')as fp:
	msg1=fp.read()
with open('copy.txt','a')as fp1:
	fp1.write(msg1)
