异常检测框架
==================

环境
---------
- 需要 *Python2.6+* 或者 *Python3.3+*
- 需要 *Numpy1.8*

用法
---------
1. 创建一新的异常检测算法 (可以使用 `cli.py -n ${算法名称}`)

- **必须继承**
>   - outdetect.algorithm.OutlierBasic.OutlierBasic

- **可以import**
>   - outdetect.utils.distance.${Distance}
>   - outdetect.utils.log.LOG
>   - outdetect.utils.excepts.${Exception}
>   - ......

2. 使用本框架建立一个python异常检测程序

- **必须import**
>   - outdetect.datamodel.data.Data
>   - outdetect.algorithm.${Algorithm}

- **可以import**
>   - outdetect.utils.distance.${Distance}
>   - outdetect.utils.log.LOG
>   - outdetect.utils.excepts.${Exception}
>   - ......

3. `./example.py`里是一个示例程序

Cli.py
----------------------
`cli.py` 是本框架的命令行工具

> - 创建一个新的异常检测算法，生成的模版会在`/outdetect/Algorithm/`下
> ```
> ./cli.py -n ${Name}
> ```
> - 清除所有日志文件
> ```
> ./cli.py -c
> ```
> - 获得帮助
> ```
> ./cli.py -h
> ```

结构
---------
-----------
### 文件夹目录
    .
    ├── README.md
    ├── README_CHS.md
    ├── cli.py
    ├── example.py
    ├── log
    ├── outdetect
    │   ├── __init__.py
    │   ├── algorithm
    │   │   ├── HourDetect.py
    │   │   ├── OutlierBasic.py
    │   │   └── __init__.py
    │   ├── datamodel
    │   │   ├── __init__.py
    │   │   └── data.py
    │   ├── template
    │   │   └── algorithm.py.tmpl
    │   └── utils
    │       ├── __init__.py
    │       ├── distance.py
    │       ├── excepts.py
    │       └── log.py
    └── test
        └── data

-----------
### outdetect.datamodel.data.Data
输入 => ***字典(Dict)***
>       {
>           KEY    =>  string,  会根据KEY排序
>           VALUE  =>  list,    list  =>  float
>       }

***示例***
>       {
>           '20130721': [2.1, 2.4, ...],
>           '20130722': [0.5, 2,1, ...],
>           '........': [..., ..., ...],
>           '20130730': [0.7, 2.4, ...]
>       }

-----------
### outdetect.algorithm.OutlierBasic.OutlierBasic
***必须覆写*** 
>       {
>           set_conf           =>  set configures below
>           run                =>  run program
>           outlier_detection  =>  same as run
>       }

-----------
### outdetect.utils.log.LOG
***日志处理***
>       {
>           Console: Min Level INFO
>           LogFile: Min Level WARNING
>       }

***输出示例***
>       {
>           [2014-08-21 23:45:56,977] (ERROR) - error
>           [2014-08-21 23:45:56,978] (WARNING) - warn
>           [2014-08-21 23:45:56,978] (INFO) - info
>       }

-----------
### outdetect.utils.distance.Distance
***Classmethod***
>       {
>           cosine                =>  Cosine Distance
>           euclidean             =>  Euclidean Distance
>           cross_correlation     =>  Cross Correlation
>           dynamic_time_wraping  =>  Dynamic Time Wraping
>       }

-----------
### outdetect.utils.excepts
***Exception***
>       {
>           DataFormatError
>       }

-----------
### outdetect.algorithm.HourDetect.HourDetect
***API***
>       {
>           set_conf           =>  set configures below
>           run                =>  run program
>           outlier_detection  =>  same as run
>       }

***配置***
>       {
>           target      =>  string, Default: None
>           dist        =>  string, Default: euclidean 
>           norm_range  =>  float , Default: 0.25 between 0.0-1.0 
>           threshold   =>  float , Default: 0.25 between 0.0-1.0 
>       }
