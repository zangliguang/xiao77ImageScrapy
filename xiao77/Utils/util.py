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
