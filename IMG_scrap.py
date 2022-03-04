import requests, os, sys
from bs4 import BeautifulSoup

#user socket for timeout problem
class ScrapperImage:
    l=list()
    def __init__(self):
        """initiate"""
        print('__init__')
    
    def cdir(self, path:'str', dir_nm:'str'):
        """path for creating dir and storing data"""
        self.path = path
        self.dirn = dir_nm
        path = os.path.join(self.path, self.dirn)
        if os.path.exists(path) == False: 
            os.mkdir(path)
            os.chdir(path)
            print(f"Directory created {self.dirn}\n pwd -> {os.getcwd()}")
        else:
            print("Directory Exsisted...!\t swithing to Directory")
            os.chdir(path)
            print(f"pwd -> {os.getcwd()}")
    
    def existance(self, name:'str') -> bool:
        """this checks file exist or not if yes then escape the download"""
        self.f_nm = name
        if os.path.exists(self.f_nm) == True: return True
        else: return False
    
    def extractor(self, url):
        """usnig bs4 libarary image scrapping"""
        self.url = url
        src = requests.get(self.url)
        soup = BeautifulSoup(src.content, 'html.parser')
        self.obj = soup.find_all('img', attrs={'class':'thumb'})
        print(f'\r{self.url} -> {len(self.obj)}')
        for i in self.obj: 
            img_url = 'https:'+str(i).split()[3][15:-1]
            self.download(img_url)
    
    def download(self, img_url):
        """file downloader in chunk"""
        #self.flag=''
        self.img = img_url
        get_resp = requests.get(self.img, stream=True)
        self.file_name  = self.img.split("/")[-1]
        if self.existance(self.file_name) == True: 
            #self.flag='*' 
            print('*',end='')
        else:
            print('#',end='')
            with open(self.file_name, 'wb') as f:
                for chunk in get_resp.iter_content(chunk_size=8192):
                    if chunk: f.write(chunk)
                    #if self.existance(self.file_name) == True: flag='#'
                #else: flag='*'
        #print(self.flag,end='')
        #self.status(self.url, self.flag, len(self.obj))
        #print('download')
        
    def file_in(self):
        """this function provides file handling utility"""
        #try:
        path = input("Enter file name with it\'s absolute path\t->")
        if self.existance(path) == True: return open(path, 'rt')
        else: return f"{FileNotFoundError}"
            #for i in open(path, 'rt'):
            #    return str(i).strip()
        #except FileNotFoundError as e:
            #return e
         
    def method(self):
        """method for inputting multiple url or file input"""
        in_method = int(input("Enter input method\t: 1 ->URL list\t2 ->File\t-:"))
        while 1:
            if in_method:
                if in_method == 1: 
                    for i in self.mk_list(): self.extractor(i)
                elif in_method == 2:
                    for i in self.file_in(): self.extractor(str(i).strip())
                else: print("Enter correct input...!")
            else: 
                print('Exit...!')
                sys.exit()
                
    def mk_list(self) -> 'list':
        """this methods handles run-time input data"""
        global l
        print("input \'done\' when url\'s get end for starting download")
        while 1:
            s=input("Ener URL\t:")
            if s == 'done': break
            else: l.append(s)
        return l
    
    def status(self, url:'str', flag:'str', ttl:'int'):
        """status of every activity soket timeout, retry, current url, no of file, file existance if yes then 'esc'"""
        print(f'{url}\t{ttl}')
        print(flag,end='')
   
    def writer(self, name:str, status:bool):
        """this function creates file depending on status"""
        with open(name, 'wb') as f:
            for chunk in requests.get(self.img, stream=status).iter_content(chunk_size=4096):
                if chunk: 
                    f.write(chunk)
                    
if __name__=='__main__': 
    fetch = ScrapperImage() 
    fetch.cdir(input("Enter path\t:"),input("Enter Directory name\t:"))
    fetch.method()
