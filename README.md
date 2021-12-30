# Product Availability Checker


## Project Overview
Queries a list of URLs, checks product availability, and sends an email if one of the products is in stock.  

Can be run **locally**, on **AWS Lambda**, on **GCP Cloud Functions**, or on **GitHub Actions**.


## Table of Contents
- **[Solution Components](#solution-components)**
- **[Usage](#usage)**
  - **[AWS](#aws-usage-instructions)**
  - **[GCP](#gcp-usage-instructions)**
  - **[GitHub Actions](#github-actions-usage-instructions)**
- **[Build](#Build)**
  - **[AWS](#aws-build-instructions)**
  - **[GCP](#gcp-build-instructions)**
- **[Possible Improvements](#possible-improvements)**


## Solution Components
- **Python 3.8**
  - various libraries: Beautiful Soup, Boto3, Requests, Yagmail, etc.
- **AWS**
  - Lambda
  - SES
  - EventBridge
  - SNS
- **GCP**
  - Cloud Functions
  - Cloud Source Repositories
  - Pub/Sub
  - Cloud Scheduler
- **GitHub**
  - Actions


## Usage
### AWS Usage Instructions
- download the `python-aws.zip` file from the **[AWS](/AWS)** folder
#### Create a function
- **[AWS Console](https://console.aws.amazon.com)** > Lambda > Create function
- Author from scratch > Function name ... > Runtime: Python 3.8 > Permissions: Create a new role with basic Lambda permissions
  - in IAM, attach `AmazonSESFullAccess` and `AmazonSNSFullAccess` policies to the Role listed under Permissions
- Actions > upload a .zip file: `python-aws.zip` > Save
#### Test
- Code > Test  
or
- Test > Invoke
#### Automate
- Designer > Add trigger > EventBridge > Rule: Create a new rule > Rule name ... > Rule type: Schedule expression > Schedule expression: `cron(0 13 * * ? *)` > Add  
#### Update
- Automated with GitHub Actions using the [`update-lambda`](/.github/workflows/update-lambda.yml) workflow

![](AWS/aws.png)


### GCP Usage Instructions
- download the `python-gcp.zip` file from the **[GCP](/GCP)** folder
#### Sync Repos
 - **[GCP Console](https://console.cloud.google.com)** > Cloud Source Repositories > Add repository > Connect external repository > Project: ... > Git provider: GitHub > ... > Connect selected repository
#### Create a function
- **[GCP Console](https://console.cloud.google.com)** > Cloud Functions > Create Function > Function name ... > Region ... > Trigger type:  Cloud Pub/Sub > Create a topic ... > Create Topic
- Save > Next
- Runtime: Python 3.8 > Source code `*`: Cloud Source repository > Repository: ... > Branch > Branch name ... > Directory ... > Deploy  
  `*` **OR** Source code: ZIP Upload > `python-gcp.zip` > Deploy  
  - in IAM, add *Cloud Functions Service Agent* and *Service Account User* Roles to the Member  
#### Test
- Actions > Test function > Test the function
#### Automate
- Cloud Scheduler > Create Job > Select a region: ... > Name ... > Frequency: `0 7 * * *` > Timezone ... > Target: Pub/Sub > Topic ... > Payload ... > Create
#### Update
- Automated with GitHub Actions using the [`update-cloud-functions`](/.github/workflows/update-cloud-functions.yml) workflow

```
{
  "name": "projects/product-availability-checker/locations/us-west2/functions/product-availability-checker",
  "sourceRepository": {
    "url": "https://source.developers.google.com/projects/product-availability-checker/repos/github_gdmoney_product-availability-checker/moveable-aliases/master/paths/GCP",
    "deployedUrl": "https://source.developers.google.com/projects/product-availability-checker/repos/github_gdmoney_product-availability-checker/revisions/f4f0acb61bf498b4f6b18e450bee0e8fef39f79b/paths/GCP"
  },
  "eventTrigger": {
    "eventType": "google.pubsub.topic.publish",
    "resource": "projects/product-availability-checker/topics/pac-topic",
    "service": "pubsub.googleapis.com",
    "failurePolicy": {
    }
  },
  "status": "ACTIVE",
  "entryPoint": "hello_pubsub",
  "timeout": "60s",
  "availableMemoryMb": 256,
  "serviceAccountEmail": "product-availability-checker@appspot.gserviceaccount.com",
  "updateTime": "2021-12-17T20:23:12.847Z",
  "versionId": "57",
  "labels": {
    "deployment-tool": "cli-gcloud"
  },
  "runtime": "python38",
  "ingressSettings": "ALLOW_ALL",
  "buildId": "9cb2ba19-bb7d-49ed-9118-df829bea7aa1",
  "buildName": "projects/917625258949/locations/us-west2/builds/9cb2ba19-bb7d-49ed-9118-df829bea7aa1"
}
```


### GitHub Actions Usage Instructions
- GitHub > Settings > Secrets >  
  - New repository secret > Name: `AWS_ACCESS_KEY_ID`, Value: ... > Add secret  
  - New repository secret > Name: `AWS_SECRET_ACCESS_KEY`, Value: ... > Add secret
  - New repository secret > Name: `AWS_REGION`, Value: ... > Add secret
- GitHub > Actions > New workflow > set up a workflow yourself > ...
  - copy & paste the output below in the editor

```
name: run-on-gh-actions

on:
  push:
    branches:
    - master
    paths:
    - '__main__.py'
    - 'urls.py'
    - '.github/workflows/run-on-gh-actions.yml'
  pull_request:
    branches:
    - master
  schedule:
  # every Monday at 5am PST
  - cron: '0 13 * * 1'
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout source code
      uses: actions/checkout@v2
        
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install beautifulsoup4
        pip install boto3
        pip install requests
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: ${{ secrets.AWS_REGION }}

    - name: Run
      run: python __main__.py
```

#### Test
- Actions > Workflows: `run-on-gh-actions` > Re-run jobs


## Build
### AWS Build Instructions
- create a new folder
- copy all the required Python packages from `C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python38-32\Lib\site-packages` to this new folder
- put the `lambda_function.py` file there
- archive all of the packages and the `lambda_functions.py` file into a **zip** file called `python-aws.zip`

### GCP Build Instructions
- create a new folder
- copy all the required Python packages from `C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python38-32\Lib\site-packages` to this new folder
- put the `main.py` and the `requirements.txt` files there (`pip freeze > requirements.txt`)
- archive all of the packages, the `main.py` and the `requirements.txt` files into a **zip** file called `python-gcp.zip`
  - **zip** file is not required if syncing repos and using Cloud Source Repository as function source


## Possible Improvements
- [x] automate to run daily or weekly
- [x] email only if status =/= Out of Stock
- [ ] email only the products that are available or on backorder
- [x] run it on AWS Lambda
- [x] sync GitHub and AWS CodePipeline
- [x] sync GitHub and GCP Cloud Source Repositories
- [x] run it on GCP Functions
- [x] add price
- [x] run it on GitHub Actions
- [ ] insert info in the email body (instead of the attachment)
- [ ] hyperlink product webpage URLs to the product names
- [x] use AWS SNS, SQS, or SES to send email instead of YagMail (using SES)
- [ ] containerize it
- [x] run new code in Lambda
- [x] run new code in GCP
- [x] run new code in GitHub Actions
- [x] update documentation
- [x] AWS Lambda auto deploy on repo changes using GitHub Actions
- [x] separate the URL list from the code
- [x] GCP Cloud Functions auto deploy on repo changes using GitHub Actions
- [x] add URL error handling 
