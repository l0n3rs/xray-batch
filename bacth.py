import os
filename=input("请输入url文件(或直接拖拽):")
urls=open(filename,'r')
list=urls.readlines()
for i in list:
  #这里未使用的是高级别支持爬虫,如果是普通版把--browser-crawler改成--url-file即可
  #脚本放在xray根目录运行
	cmd="xray.exe webscan --browser-crawler "+i.replace('\n', '')+" --html-output "+i.rsplit('.')[1]+".html" 
	os.system(cmd)
