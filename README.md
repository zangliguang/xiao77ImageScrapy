# xiao77ImageScrapy




## new project

```
scrapy startproject xiao77

```

## new crawl

```
cd  xiao77
scrapy genspider imageCrawl http://x77525.com/bbs/

```

## start crawl

```
scrapy crawl imageCrawl

```


## Analyze WebPage
###Get catlog page

```
python3
from bs4 import BeautifulSoup
import requests
r=requests.get('http://x77525.com/bbs/')
soup = BeautifulSoup(r.content,'lxml')
all_a=soup.find_all('a',class_='mr10')

for a in all_a:
   print(a.contents[0] + ":" +self.allowed_domains[0]+ a.get('href'))


```

###Get detail page

```
python3
from bs4 import BeautifulSoup
import requests
r=requests.get('http://x77525.com/bbs/thread.php?fid=60')
soup = BeautifulSoup(r.content,'lxml')
all_a=soup.find_all('a',class_='subject_t f14')

for a in all_a:
   print(a.contents[0] + ":" +self.allowed_domains[0]+ a.get('href'))
   
pagesSpan = soup.find('div',class_='pages')
pageAs=pagesSpan.findAll('a')
lastPage=pageAs[len(pageAs)-1].get('href')


```

###Get image 

```
python3
from bs4 import BeautifulSoup
import requests
r=requests.get('http://x77525.com/bbs/read.php?tid=1439867')
soup = BeautifulSoup(r.content,'lxml')
divs=soup.find('div',class_='f14 mb10')
images=divs.find_all('img')

for a in all_a:
   print(a.contents[0] + ":" +self.allowed_domains[0]+ a.get('href'))


```



###download image 

```
import requests
import threading


def saveImage(imgUrl, imgName, DstDir):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    print("保存文件" + DstDir + imgName + "\n")
    try:
        with open(DstDir + "/" + imgName, "wb") as jpg:
            jpg.write(image)
        return
    except IOError:
        print("IO Error\n")
        return
    finally:
        jpg.close


def downImageViaMutiThread(filelist, DstDir):
    task_threads = []  # 存储线程
    count = 1
    index = 0
    for file in filelist:
        split = file.split('/')
        filename = split[len(split) - 1]
        t = threading.Thread(target=saveImage, args=(file, filename, DstDir))
        count = count + 1
        index += 1
        task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join()



```




####BaseWebSite:
<http://x77525.com/bbs/>

####BaseCatLogWebSite:
<http://x77525.com/bbs/thread.php?fid=60>

