# pyqt5_android_tools
PyQt开发的协助安卓日常测试的小工具（截图，安装，卸载，logcat，anr，获取包名，获取设备信息）


mac开发环境配置：（https://www.jianshu.com/p/6fab1fe260d2）

1、python3.6

2、pycharm

3、PyQt5-Designer:http://download.qt.io/official_releases/qt/5.9/5.9.0/qt-opensource-mac-x64-5.9.0.dmg

4、pip3 install PyQt5

5、pip3 install pyqt5-tools

6、pip3 install pyuic5-tool

7、adb环境



8、利用pycharm将.ui转换成.py
PyCharm---Perferences---Tools--External Tools---+

<img width="734" alt="截屏2021-03-28 下午8 25 03" src="https://user-images.githubusercontent.com/33284151/112752063-ba4f6880-9003-11eb-8792-7bf632288049.png">

/Users/leixueqi/PycharmProjects/pythonProject2/venv/bin/python3.6
-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
$FileDir$



执行：
python call_tools.py


<img width="472" alt="截屏2021-03-28 下午8 16 53" src="https://user-images.githubusercontent.com/33284151/112751827-8e7fb300-9002-11eb-8333-bb6c59e36b4b.png">















