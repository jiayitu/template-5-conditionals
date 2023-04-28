# Assignment 5 - Conditionals

This program is going to calculate someone's BMI and give feedback on their health (based on the somewhat limited view of just the BMI). 
My (Dutch) source for the calculation and subsequent evaluation is: https://www.voedingscentrum.nl/bmi.

Your file should be called: bmi.py

Write a function calculate_bmi(length, weight) that takes the length (in m) and weight (in kg) for a person, calculates the bmi and returns that value. 
The formula for bmi is weight divided by length squared.

Write another function bmi_to_category(bmi) that takes a bmi and returns a corresponding string. The strings are:

* for bmi lower than 18.5: "underweight";
* for bmi between 18.5 and 25: "healthy weight";
* for bmi between 25 and 30: "overweight";
* for bmi over 30: "obese".

Use your main function to write code that asks the user for their length and weight, use the functions above and gives the user their bmi and category. 
The output should look something like this:

```
C:\Users\vevr\PycharmProjects\conditionals\Scripts\python.exe C:\Users\vevr\PycharmProjects\LCfPC\conditionals\bmi.py 
What is your length (in m)? 1.83
What is your weight (in kg)? 83
With your length and weight your bmi is: 24.78425751739377 which means you are healthy weight

Process finished with exit code 0
```
