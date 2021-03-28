# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QFileDialog,QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon  
from tools import Ui_MainWindow
from install import Ui_Install
from logcat import Ui_Logcat
import time
import os
import subprocess



class excute(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(excute,self).__init__(parent)
        global device_id
        try:
            device_id = subprocess.Popen('adb get-serialno')
        except:
            device_id = ''
        self.setupUi(self)

        self.install=Install()
        self.logcat = Logcat()

        self.pushButton_clear_data.clicked.connect(self.clear_data)
        self.pushButton_screenshot.clicked.connect(self.screen_shot)
        self.pushButton_uninstall.clicked.connect(self.uninstall)


        self.pushButton_logcat.clicked.connect(self.logcat_ui)

        self.pushButton_anr.clicked.connect(self.get_anr)
        self.pushButton_deviceinfo.clicked.connect(self.get_deviceinfo)


        self.pushButton_install.clicked.connect(self.install_ui)
        self.pushButton_exit.clicked.connect(QCoreApplication.instance().quit)

        self.pushButton_clear_data.setIcon(QIcon("./images/clear.jpg"))
        self.pushButton_screenshot.setIcon(QIcon("./images/screenshot.jpg"))
        self.pushButton_uninstall.setIcon(QIcon("./images/uninstall.jpg"))
        self.pushButton_anr.setIcon(QIcon("./images/anr.jpg"))
        #self.pushButton_csh.setIcon(QIcon("./images/csh.jpg"))
        self.pushButton_install.setIcon(QIcon("./images/install.jpg"))
        self.pushButton_deviceinfo.setIcon(QIcon("./images/deviceinfo.jpg"))
        #self.pushButton_8.setIcon(QIcon("./images/monkey.jpg"))
        self.pushButton_exit.setIcon(QIcon("./images/exit.jpg"))
        self.center()


    def edit_box_tips(self,text):
        '''
        QTextEdit控件输出内容
        '''
        self.textEdit_output.clear()
        self.textEdit_output.setText(text)

    def edit_box_packageName(self,text):
        '''
        QTextEdit
        显示当前界面Activity名
        '''
        self.textEdit_output_2.clear()
        self.textEdit_output_2.setText(text)

    
    def clear_data(self):
        '''
        adb shell pm clear xxx
        '''
        sys.stderr.write("卸载!"+'\n')
        package = self.textEdit_output.toPlainText()
        clear_cmd = "adb shell pm clear  %s" % (package)
        try:
            subprocess.Popen(clear_cmd)
            time.sleep(5)
            print ("clear data!")
            cmd2='adb shell rm -R /sdcard/iReader'
            subprocess.Popen(cmd2)        
            time.sleep(5)
            print ("clear success!")
            text="清除数据成功:%s"%(clear_cmd)
            #self.pushButton.clicked.connect(partial(self.edit_box_tips,text))
            self.edit_box_tips(text)
        except Exception as e:
            text="清除数据失败"
            self.edit_box_tips(text)


    def get_deviceinfo(self):
        '''
        adb shell get getprop xxx
        获取设备号、品牌、机型、分辨率、IMEI号
        '''
        try:
            cmd0='adb shell getprop ro.build.version.release'
            version=subprocess.Popen(cmd0)            

            cmd1='adb get-serialno'
            deviceid=subprocess.Popen(cmd1)           

            cmd2='adb shell  cat /sys/class/net/wlan0/address'
            mac_address=subprocess.Popen(cmd2)            

            cmd3='adb shell getprop ro.product.brand'
            brand=subprocess.Popen(cmd3)          

            cmd4='adb shell getprop ro.product.model'
            model=subprocess.Popen(cmd4)          

            cmd5='adb shell wm size'
            wm_size=subprocess.Popen(cmd5) 
            wm_size=wm_size[wm_size.find(':')+1:]           

            cmd6='adb shell getprop persist.sys.updater.imei'
            imei=subprocess.Popen(cmd6) 
            text="设备ID:%s\n品牌:%s\n型号:%s\n分辨率:%s\n系统版本:%s\nIMEI:%s\nMAC地址:%s" % (deviceid,brand,model,wm_size,version,imei,mac_address)  
    

            currentPath=os.getcwd()
            if not os.path.exists(currentPath+"/deviceinfo"):
                os.popen("mkdir deviceinfo")
            else:
                pass        

            filename =currentPath+"/deviceinfo/"+deviceid+'_'+brand+'_'+model+'_'+"info.txt"                  #日志文件名添加当前时间
            device_info_file =open(filename,'w')
            device_info_file.write(text)
            #device_info_file.save()
            device_info_file.close()    


            text2=text+'\n\n'+'设备文件:'+filename
            self.edit_box_tips(text2)
        except Exception as e:
            text='获取设备信息失败'
            self.edit_box_tips(text)
    

    def screen_shot(self):
        '''
        adb shell screenshot 截图
        '''
        try:
            currentPath=os.getcwd()
            if not os.path.exists(currentPath+"/screenshot"):
                os.popen("mkdir screenshot")
            else:
                pass
            timeslap=time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
            file_name=device_id+'_'+timeslap+".png"
            cmd="adb shell /system/bin/screencap -p /sdcard/"+file_name
            subprocess.Popen(cmd)     

            cmd1="adb pull /sdcard/"+file_name+" "+currentPath+"/screenshot"
            subprocess.Popen(cmd1)
            time.sleep(2)
            text='截图成功:'+currentPath+"/screenshot/"+file_name
            self.edit_box_tips(text)
        except Exception as e:
            text='截图失败:'
            self.edit_box_tips(text)
        

    def start_logcat(self):
        try:
            filename=self.generateLogFile()
            text='生成日志文件：'+filename+'成功!'
            self.edit_box_tips(text)
            currentPath = os.getcwd()
        except Exception as e:
            text='生成日志文件失败!'
            self.edit_box_tips(text)

    def generateLogFile(self):
        sys.stderr.write("打印日志!"+'\n') 
        currentPath = os.getcwd()
        if not os.path.exists(currentPath+"/logcat"):
            os.popen("mkdir logcat")
        else:
            pass
        path=os.getcwd() 
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))    #获取当前时间
        filename =path+"/logcat/"+device_id+'_'+now+r".txt"                  #日志文件名添加当前时间
        logcat_file =open(filename,'w')
        logcmd ="adb logcat -v time"
        Poplog =subprocess.Popen(logcmd,stdout=logcat_file,stderr=subprocess.PIPE,shell=True)
        return filename

    def get_anr(self):
        '''
        adb pull /data/anr ./
        '''
        try:
            cmd="adb shell ls /data/anr | grep trace.txt"
            anr = subprocess.Popen(cmd)
            currentPath = os.getcwd()
            if anr != '':
                if not os.path.exists(currentPath+"/anr"):
                    os.popen("mkdir anr")
                else:
                    pass
                if not os.path.exists(currentPath+'/anr/'+device_id):
                    s.popen("mkdir "+device_id)
                else:
                    pass
                t = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
                cmd1 = 'adb pull '+'/data/anr ./'+'/anr/' +device_id+'/'+t
                sys.stderr.write(cmd1+'\n')
                subprocess.Popen(cmd1)
                text='获取Anr成功!'
                self.edit_box_tips(text)
            else:
                text='没有anr文件!'
                self.edit_box_tips(text)

        except Exception as e:
            text='获取anr失败!'
            self.edit_box_tips(text)

    def uninstall(self):
        '''
        adb uninstall packageName
        '''
        sys.stderr.write("卸载!"+'\n')
        package = self.textEdit_output.toPlainText()
        uninstall_cmd = "adb uninstall %s" % (package)
        try:
            uninstall_cmd =subprocess.Popen(uninstall_cmd,stdout=uninstall_cmd,stderr=subprocess.PIPE,shell=True)
            text = '卸载成功：%s'%(uninstall_cmd)
            self.edit_box_tips(text)
        except:
            text = '卸载失败'
            self.edit_box_tips(text)

    def install_ui(self):
        '''
        安装二级页面
        '''
        self.install.show()

    def logcat_ui(self):
        '''
        logcat二级页面
        '''
        self.logcat.show()

    def getPackageName(self):
        '''return packagename activity'''
        try:
            cmd = 'adb shell dumpsys window w'
            out = subprocess.Popen(cmd).communicate()[0]
            out=out.decode('utf-8')
            for line in out.strip().splitlines():
                result=re.match(r'.*Surface\(name=com.*/',line)
                if result:
                    package_activity = line[(line.find("name=") + 5):-1].split('/')
                    packageName = package_activity[0]
                    self.edit_box_packageName(packageName)
        except:
            text="获取包名失败!"
            self.edit_box_packageName(text)

    def center(self):
        '''
        居中显示
        '''
        screen = QDesktopWidget().screenGeometry()  
        size = self.geometry()  
        self.move((screen.width() - size.width()) / 2,    
        (screen.height() - size.height()) / 2)

class Install(QWidget,Ui_Install):
    """docstring for ChildFrom"""
    def __init__(self):
        super(Install, self).__init__()
        self.setupUi(self)


    def get_apkname_and_path(self):
        return self.lineEdit.text().strip()
    
    def install_apk(self):
        try:
            text='开始安装~~~'
            self.edit_box_tips(text)    

            apkname_path=self.get_apkname_and_path()
            #text='start install...'
            #self.pushButton9.clicked.connect(partial(self.edit_box_tips,text)) 
            subprocess.Popen(['adb','install','-r',apkname_path])
            brand=subprocess.Popen("adb shell getprop ro.product.brand").strip()
            model=subprocess.Popen("adb shell getprop ro.product.model").strip()
            if brand=='Meizu':
                time.sleep(5)
            else:
                time.sleep(3)
            if brand=='Meizu' and d(text='正在通过USB自动安装以下应用').exists:
                d(text='允许').click()
            if brand=='vivo' and d(text='安全警告').exists:
                sys.stderr.write("vivo")
                d(text='好').click.wait()
                time.sleep(1)
            if brand=='vivo':
                time.sleep(2)
                print ("the product is vivo,wait for 2 seconds.")    
            else:
                time.sleep(15)
                print ("the product is other except vivo,wait for 15 seconds.")             

            if d(text='解析错误').exists:
                time.sleep(2)
                d(text='确定').click.wait()
                time.sleep(1)
            if d(text='安装').wait.exists(timeout=3000):
                time.sleep(1)
                d(text='安装').click.wait()
                time.sleep(10)
            if d(text='是否要安装该应用程序？').wait.exists(timeout=3000):
                time.sleep(1)
                d(text='安装').click.wait()
                time.sleep(10)
            time.sleep(2)
            #Note3安装时出现此提示
            if d(text='确认').exists:
                d(text='确认').click.wait()
            text='安装完成~~~'
            self.edit_box_tips(text)
        except Exception as e:
            text='安装失败!'
            self.edit_box_tips(text)

    def edit_box_tips(self,text):
        self.textEdit_output.setText(text)

    def changePath(self):
        open = QFileDialog()
        self.path=open.getOpenFileName()
        print(self.path)
        #self.path = open.getExistingDirectory()
        self.lineEdit.setText(self.path[0])


class Logcat(QWidget,Ui_Logcat):
    """docstring for ChildFrom"""
    def __init__(self):
        super(Logcat, self).__init__()
        self.setupUi(self)

    def killLogcat(self):
        try:
            cmd1="adb shell ps | grep logcat"
            a=subprocess.Popen(cmd1)
            d=[]
            if a !='':
                b=a.split('\r')
                for item in b:
                    c=item.split(' ')
                    while '' in c:
                        c.remove('')          
                    d.append(c)
                pid_list=[]
                for i in range(len(d)-1):
                    pid_list.append(d[i][1])
                for pid in pid_list:
                    cmd2="adb shell kill -9 "+pid
                    subprocess.Popen(cmd2)
                    time.sleep(3)
                text='停止logcat成功!'
                self.edit_box_tips(text)
            else:
                text='没有logcat进程!'
                self.edit_box_tips(text)                
        except Exception as e:
            text='停止logcat失败!'
            self.edit_box_tips(text)    

    def get_csh(self):
        """
        Method of check csh file. Used in teardown.
        """
        try:
            text='开始获取获取csh~~~'
            self.edit_box_tips(text)

            cmd="adb shell ls /sdcard/iReader/logs | grep csh"
            csh = subprocess.Popen(cmd)
            if csh != '':
                currentPath=os.getcwd()
                if not os.path.exists(currentPath+"/logcat"):
                    os.popen("mkdir logcat")
                else:
                    pass
                t = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))
                cmd1 = 'adb pull '+'/sdcard/iReader/logs'+'*'+ ' ' + currentPath + '/logcat/' +device_id+'_csh'+'/'+ t
                sys.stderr.write(cmd1+'\n')
                subprocess.Popen(cmd1)
                time.sleep(5)
                text='获取csh成功!'
                self.edit_box_tips(text)
            else:
                text='没有csh文件!'
                self.edit_box_tips(text)
        except Exception as e:
            text='生成日志文件失败!'
            self.edit_box_tips(text)

    def edit_box_tips(self,text):
        self.textEdit.setText(text)


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    ui=excute()
    ui.show()
    sys.exit(app.exec_())       



