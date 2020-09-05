# Product Availability Checker

## Description
Queries each website, checks product availability, and send an email if one of the products is available.  

Can be run on a local computer with `__main.py__` or on **AWS Lambda** with `lambda_function.py`


## Components
- Python 3.8
- various Python libraries: Beautiful Soup, Requests, YagMail, etc.
- AWS Lambda
- AWS EventBridge (CloudWatch Events)


## Usage
Instructions are for running the code on AWS Lambda.
- on the local computer, create a new folder and put `lambda_function.py` there
- copy all the required Python packages from `C:\Users\gdavitiani\AppData\Local\Programs\Python\Python38-32\Lib\site-packages` to this new folder
- archive all the packages and the `lambda_functions.py` file into a **zip** file  
!(/explorer.png)


## Things to add
- automate to run daily - **DONE** - using Windows Task Scheduler
- email only if status =/= Out of Stock - **DONE**
- email only the products that are available


### Issues
 - ~~when the email code is inside the for loop, it emails 6 separate messages~~
 - ~~when it's outside of the loop, it emails once with the status of the first item only~~
