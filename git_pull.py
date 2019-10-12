import os

path = "E:\\work\\for-git-work\\ake-microservice-new" #文件夹目录
datas = []
def eachFile(filepath):
    fileNames = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for file in fileNames:
        newDir = filepath + '\\' + file # 将文件命加入到当前文件路径后面
        # print(newDir)
        if os.path.isdir(newDir): # 如果是文件夹
            print(newDir)
            os.getcwd()
            os.chdir(newDir)
            os.popen('git pull').readlines()
        if os.path.isfile(newDir):  # 如果是文件
            if os.path.splitext(newDir)[1] == ".txt":  # 判断是否是txt
                f = open(newDir)
                str = ""
                for line in f.readlines():
                    str = str + line # 读文件
                datas.append(str)
        #else:
            #eachFile(newDir)                #如果不是文件，递归这个文件夹的路径

if __name__ == "__main__":
    eachFile(path)
    print(datas)