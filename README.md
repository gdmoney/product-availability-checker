# Product Availability Checker

## Description
Queries each website, checks product availability, and send an email if one of the products is available.  

Can be run locally with `__main.py__` or on **AWS Lambda** with `lambda_function.py`.


## Components
- Python 3.8
- various Python libraries: Beautiful Soup, Requests, YagMail, etc.
- AWS Lambda
- AWS EventBridge (CloudWatch Events)


## Usage
Insturctions for running code in AWS:

- download the `python.zip` file from `AWS-Lambda`
- [AWS](https://console.aws.amazon.com) > Lambda > Create function
- Author from scratch > name > Runtime: Python 3.8 > Permissions: Create a new role with basic Lambda permissions
- Actions > upload a .zip file: `python.zip` > Save
- Test > Create new test event > Event template: hello-world > Event name > Create
- Test
- Designer > Add trigger > EventBridge > Rule: Create a new rule > Rule name > Rule type: Schedule expression > Schedule expression: `cron(0 13 * * ? *)` > Add

![](/aws.png)


## Build
- create a new folder
- put the `lambda_function.py` file there
- copy all the required Python packages from `C:\Users\USERNAME\AppData\Local\Programs\Python\Python38-32\Lib\site-packages` to this new folder
- archive all of the packages and the `lambda_functions.py` file into a **zip** file

![](/folder.png)


## Things to add
- automate to run daily - **DONE** - using Windows Task Scheduler when running locally or EventBridge when running in AWS
- email only if status =/= Out of Stock - **DONE**
- email only the products that are available
- link GitHub and AWS Lambda
- run it on GCP
- add price
- run it with GitHub Actions - **DONE**
- add a link in the text file


## Issues
 - sends email even when all of the products are out of stock - **FIXED**
