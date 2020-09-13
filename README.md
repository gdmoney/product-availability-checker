# Product Availability Checker


## Description
Queries each website, checks product availability, and send an email if one of the products is available.  

Can be run locally, on **GitHub Actions**, on **AWS Lambda**, or on **GCP Functions**.


## Components
- Python 3.8
- various Python libraries: Beautiful Soup, Requests, YagMail, etc.
- AWS Lambda
- AWS EventBridge (CloudWatch Events)
- GCP Functions
- GCP Pub/Sub


## Usage
Insturctions for **AWS**:

- download the `python-aws.zip` file from `AWS-Lambda`
#### Create a function
- **[AWS](https://console.aws.amazon.com)** > Lambda > Create function
- Author from scratch > name > Runtime: Python 3.8 > Permissions: Create a new role with basic Lambda permissions
- Actions > upload a .zip file: `python.zip` > Save
#### Test
- Test > Create new test event > Event template: hello-world > Event name > Create
- Test
#### Automate
- Designer > Add trigger > EventBridge > Rule: Create a new rule > Rule name > Rule type: Schedule expression > Schedule expression: `cron(0 13 * * ? *)` > Add

![](AWS/aws.png)


Insturctions for **GCP**:

- download the `python-gcp.zip` file from `GCP`
#### Create a function
- **[GCP](https://console.cloud.google.com)** > Cloud Functions > Create Function > Function name ... > Region ... > Trigger type:  Cloud Pub/Sub > Create a topic ... > Create Topic
- Save > Next
- Runtime > Python 3.8 > Source code > ZIP from Cloud Storage > Browse: python-gcp.zip > Deploy
#### Test
- Actions > Test function
#### Automate
- 

![](GCP/gcp.png)

## Build
- create a new folder
- copy all the required Python packages from `C:\Users\USERNAME\AppData\Local\Programs\Python\Python38-32\Lib\site-packages` to this new folder
#### AWS
- put the `lambda_function.py` file there
- archive all of the packages and the `lambda_functions.py` file into a **zip** file
![](/aws-folder.png)
#### GCP
- put the `main.py` and `requirements.txt` files there
- archive all of the packages, the `main.py` and the `requirements.txt` files into a **zip** file
![](/gcp-folder.png)


## Things to add
- automate to run daily - **DONE** - using Windows Task Scheduler when running locally or EventBridge when running in AWS
- email only if status =/= Out of Stock - **DONE**
- email only the products that are available
- link GitHub and AWS Lambda
- run it on GCP
- add price - **DONE**
- run it with GitHub Actions - **DONE**
- add URL links in the text file


## Issues
 - sends email even when all of the products are out of stock - **FIXED**
