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
#### Local Computer
- create a new folder
- put the `lambda_function.py` file there
- copy all the required Python packages from `C:\Users\gdavitiani\AppData\Local\Programs\Python\Python38-32\Lib\site-packages` to this new folder
- archive all the packages and the `lambda_functions.py` file into a **zip** file

![](/folder.png)

#### AWS
- Lambda > Create functon
- Author from scratch > name > Python 3.8 > Permissions: Use an existing role
- Actions > upload a .zip file > Save
- Test > Create new test event > Event template: hello-world > Event name > Create

- Designer > Add trigger > EventBridge > Rule: Create a new rule > Rule name > 
- Rule type: Schedule expression > Schedule expression: cron(0 12 * * ? *)

![](/aws.png)


## Things to add
- automate to run daily - **DONE** - using Windows Task Scheduler when running locally or EventBridge when running in AWS
- email only if status =/= Out of Stock - **DONE**
- email only the products that are available


## Issues
 - sometimes sends email even when all of the products are out of stock
