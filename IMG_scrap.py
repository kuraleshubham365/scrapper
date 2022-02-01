import requests, os
from bs4 import BeautifulSoup

#user socket for timeout problem
class ScrapperImage:
    l=list()
    def __init__(self):
        """initiate"""
        print('__init__')
    
    def cdir(self, path, dname):
        """path for creating dir and storing data"""
        self.path = path
        self.dirn = dname
        #print(self.path,"\n",self.dirn)
        if os.path.exists(self.path + self.dirn) == False: 
            os.mkdir(self.path + self.dirn)
            os.chdir(self.path + self.dirn)
            print(f"Directory created {self.dirn}\n pwd -> {os.getcwd()}")
        else:
            print("Directory Exsisted...!\t swithing to Directory")
            os.chdir(self.path+self.dirn)
            print(f"pwd -> {os.getcwd()}")
        #print('cdir')
    
    def extractor(self, url):
        """usnig bs4 libarary image scrapping"""
        self.url = url
        src = requests.get(self.url)
        soup = BeautifulSoup(src.content, 'html.parser')
        obj = soup.find_all('img',attrs={'class':'thumb'})
        for i in obj: 
            img_url = 'https:'+str(i).split()[3][15:-1]
            self.download(img_url)
    
    def download(self, img_url):
        """file downloader in chunk"""
        self.img = img_url
        get_response = requests.get(self.img, stream=True)
        self.file_name  = self.img.split("/")[-1]
        with open(self.file_name, 'wb') as f:
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk: f.write(chunk)
        #print('download')
        
    def method(self):
        """method for inputting multiple url and file input"""
        in_method = int(input("Enter input method\t: 1 ->URL list\t2 ->File\t-:"))
        while 1:
            if in_method:
                if in_method == 1: 
                    #create pickle file
                    self.l = list()
                    print("input \'done\' when url\'s get end for starting download")
                    while 1:
                        s=input("Ener URL\t:")
                        if s == 'done': break
                        else: pass #l.append(s) 
                elif in_method == 2:
                    try:
                        path = input("Enter file name with it\'s absolute path\t->")
                        for i in open(path,'rt'):
                            self.extractor(str(i).strip())
                    except Exception as e:
                        print(e)
                else: print("Enter correct input...!")
            else: 
                print('Exit...!')
                break
        
    def status(self):
        """status of every activity soket timeout, retry, current url, no of file, file existance if yes then 'esc'"""
        pass
   
if __name__=='__main__': 
    fetch = ScrapperImage() 
    fetch.cdir(input("Enter path\t:"),input("Enter Directory name\t:"))
    fetch.method()
    
