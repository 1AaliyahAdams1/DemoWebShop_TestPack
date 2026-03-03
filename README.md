Setup steps -
Install packages from requirements folder

Run command(s) -
pytest

Assumptions -
Assumed that for the checkout process you would only need to successfully check out 1 Digital SLR Camera with no other additional requirements to the test case
Assumed for register i didn't have to fill in the following fields : Fax and Address line 2
Assumed order of test cases is register, login and then checkout

Tradeoffs -
The loop for CounterWaitClick function hard codes a value for the number of continue buttons present on the page
For the checkout test case, only filled in the billing details and left default options for the rest of the checkout process

Improvements if given more time -
Would of created the CounterWaitClick function to be more dynamic with the loop duration and take the amount of continue buttons on the page
Would of made the checkout test case more fleshed out by adding card payment to the process
Would of done negative testing for all 3 test cases 
Checkout function breaks if you reuse same login details because the test assumes that the user starts with an empty cart, if had more time, would make this more dynamic as clear cart if full prior to adding the required item
Checkout function additionally breaks when reusing same login details after a successful checkout because it saves the previous billing details, if had more time would of made that part more dynamic to check if the user had previous billing details saved before trying to fill in billing details
