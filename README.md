## Check product availability


### Description
Queries each website, checks product availability, and send an email if one of the products is available.

Can be run on a computer using '__main.py__' or on **AWS Lambda** using 'lambda_function.py'


### Things to add
- automate to run daily - **DONE** - using Windows Task Scheduler
- email only if status =/= Out of Stock - **DONE**
- email only the products that are available


### Issues
 - ~~when the email code is inside the for loop, it emails 6 separate messages~~
 - ~~when it's outside of the loop, it emails once with the status of the first item only~~
