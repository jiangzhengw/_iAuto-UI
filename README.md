# iAuto-UI自动化框架

##### 设计思路

待补充……

##### 项目结构

- case：存放业务相关的执行用例
- common：util功能，进行配置文件，环境读取等
- data：后期的数据准备工作
- driver：后期区分mac、linux、win10，然后直接在common里将chrome driver存入环境变量，刷新环境，替代手工的配置driver到环境变量
- log：log的存放，后期可区分all.log、error.log等
- pageObject：PO层，存放底层元素操作，base_page存放二次封装的公共方法
- output：results存放allure生成的json数据格式的报告；reports存放html相关的报告文件

##### 使用说明

待补充……

###### 环境搭建

待补充……

```python
# 安装所需的依赖环境(阿里源安装)

pip install -r requirements.txt https://mirrors.aliyun.com/pypi/simple  

    
# 安装配置Allure(官网下载解压包)

# 解压allure-commandline-2.13.6.zip 包到对应目录

# 把 allure-commandline-2.13.6/bin 加入到环境变量

# 打开控制台输入:  allure --version   出来版本代表安装成功
    
# 运行(run.py 文件即可)

python3 run.py
```

###### 编写用例

待补充……

###### 执行用例

待补充……

##### 后期更新

待补充……


## 更新日志

待补充……