import requests
from requests import get  

down_url = "http://jreddy1.w3.uvm.edu/cs166/accounts/" 

#download url to local file
def download(url, file_name = None):
	#split file name from the url (the end of url)
	if not file_name:
		file_name = url.split('/')[-1]

	print(file_name)

	#if url file exist,  create local file and write 
	response = get(url) 
	if response.status_code == 200:
		with open(file_name, "wb") as file:            
		    file.write(response.content)      

#open words_to_test.txt file and read every line(csv file name)
f = open("words_to_test.txt", "r")
while True:
	line = f.readline()
	if not line :
		break
	#call url download function
	download(down_url + line.replace('\n','') + '.csv')

f.close()

