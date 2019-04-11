from ftplib import FTP
from time import sleep 
import os

def ftpDownloader(username, password, host='10.10.10.12'):	
	# create instance with the ftp_URL 
	ftp = FTP(host) #FTP("<ftp_URL>")

	# create login with username and password
	ftp.login(username, password)	

	#navigate directory
	# print(ftp.nlst()) #list all directory
	# ftp.nlst("<dir>") #list current dir
	# ftp.cwd("<dir>"); change working directory
	# ftp.cwd(".."); go back 1 directory

	# change working directory, file downloaded FROM here
	# host dir is "C:\\Users\\User\\Desktop\\EF\\"
	ftp.cwd("2018 DevSecOps Days Singapore - Presentations")

	# get all fileList
	fileList = ftp.nlst()
	l = len(fileList)
	print(ftp.nlst())

	# change to this directory, file will be downloaded TO here
	# check path, if not exist, create path
	rootPath = 'C:\\Users\\User\\Desktop\\'
	folderName = "OPEN HOUSE DATO' 2018\\"
	if not os.path.exists(rootPath+folderName):
		os.makedirs("%s%s" % (rootPath,folderName))
	os.chdir(rootPath+folderName)

	# Initial call to print 0% progress
	printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
	
	# loop each file in fileList
	for i, f in enumerate(fileList):
		# download files
		# retrive all content of ftp site
		with open(f,"wb") as file:
			ftp.retrbinary("RETR %s" % f, file.write)

		sleep(0.1)
		# Update Progress Bar
		printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

	# close ftp connection
	ftp.close()

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

# start ftpDownloader function
print('Start')

# try except block
try:
	ftpDownloader("User", "'")
except BaseException as e:
	print(e)

print('Finish')


