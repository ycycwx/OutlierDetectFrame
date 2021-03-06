OutlierDetectFrame
==================

Enviroment
---------
- Works with *Python2.6+* or *Python3.3+*
- Works with *Numpy1.8*

Usage
---------
1. Create a new algorithm in outlier detection. (using `cli.py -n`)

- **Must inherit**
>   - outdetect.algorithm.OutlierBasic.OutlierBasic

- **Could inherit**
>   - outdetect.utils.distance.${Distance}
>   - outdetect.utils.log.LOG
>   - outdetect.utils.excepts.${Exception}
>   - ......

2. Create a python program using OutlierDetectFrame.

- **Must import**
>   - outdetect.datamodel.data.Data
>   - outdetect.algorithm.${Algorithm}

- **Could import**
>   - outdetect.utils.distance.${Distance}
>   - outdetect.utils.log.LOG
>   - outdetect.utils.excepts.${Exception}
>   - ......

3. Example program in `./example.py`.

Cli.py
----------------------
`cli.py` is a command line tool for the framework.

> - Create a new template of outlier detection algorithm.
> ```
> ./cli.py -n ${Name}
> ```
> - Clear log files.
> ```
> ./cli.py -c
> ```
> - Get help.
> ```
> ./cli.py -h
> ```

Structure
---------
-----------
### Folder tree
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
Input => ***Dict***
>       {
>           KEY    =>  string,  make sure KEY will be sorted
>           VALUE  =>  list,    list  =>  float
>       }

***Example***
>       {
>           '20130721': [2.1, 2.4, ...],
>           '20130722': [0.5, 2,1, ...],
>           '........': [..., ..., ...],
>           '20130730': [0.7, 2.4, ...]
>       }

-----------
### outdetect.algorithm.OutlierBasic.OutlierBasic
***Must overwrite*** 
>       {
>           set_conf           =>  set configures below
>           run                =>  run program
>           outlier_detection  =>  same as run
>       }

-----------
### outdetect.utils.log.LOG
***Log handler in outlier detection***
>       {
>           Console: Min Level INFO
>           LogFile: Min Level WARNING
>       }

***Format example***
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

***Configures***
>       {
>           target      =>  string, Default: None
>           dist        =>  string, Default: euclidean 
>           norm_range  =>  float , Default: 0.25 between 0.0-1.0 
>           threshold   =>  float , Default: 0.25 between 0.0-1.0 
>       }
