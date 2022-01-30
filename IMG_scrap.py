import requests, os
from bs4 import BeautifulSoup

#user socket for timeout problem
class Scrapper:
    l=list()
    def __init__(self):
        """initiating all the functions here"""
        print('__init__')
        Scrapper.download(self)
        Scrapper.multi_URL(self)
        Scrapper.existance(self)
        Scrapper.method(self)
        Scrapper.cdir(self)
    
    def cdir(self,path,dir_name):
        """path for creating dir and storing data"""
        self.path = path
        self.dirn = dir_name
        if self.existance(path+dirn) == True: 
            print("Directory Exsisted...!\t swithing to Directory")
            os.chdir(path+dirn)
        else:
           print(f"Directory created {dir_name}")
           os.mkdir(path+dirn)
        print('cdir')
    
     def existance(self,path):
         """finding file existance at current if found then do not download"""
        self.path = path
        if os.path.exists(path) == True: return True
        else: return False
        #print('existance')
    
    def extractor(self,url):
        self.url = url
        src = requests.get(url)
        soup = BeautifulSoup(src.content, 'html.parser')
        obj = soup.find_all('img',attrs={'class':'thumb'})
        for i in obj: 
            img_url = 'https:'+str(i).split()[3][15:-1]
            downloder(img_url)
    
    def download(self,img_url):
        """file downloader in chunk"""
        self.url = 'https:'+img_url
        get_response = requests.get(url,stream=True)
        file_name  = img_url.split("/")[-1]
        with open(file_name, 'wb') as f:
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk: f.write(chunk)
        print('download')
        
    def method(self):
        """method for inputting multiple url and file input"""
        in_method = int(input("Enter input method\t: 1 : URL list\t2 : File"))
        while 1:
            if in_method:
                if in_method == 1: 
                    #create pickle file
                        self.l = list()
                        print("input \'done\' when url\'s get end for starting download"):
                        while 1:
                            s=input("Ener URL\t:")
                            if s == 'done': break
                            else: #l.append(s)
                elif in_method == 2:
                    try:
                        path = input("Enter file name with it\'s absolute path")
                        file = open(path,'rt'):
                    except Exception as e:
                        print(e)
                else: print("Enter correct input...!")
            else: 
                print('Exit...!')
                break
        
        print('method')

    def status(self):
        """status of every activity soket timeout, retry, current url, no of file, file existance if yes then 'esc'"""
        pass
   
if __name__=='__main__': fetch = Scrapper() 
