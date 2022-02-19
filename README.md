# mach-eight-challenge
==============================

The project is to write a function that searches through NBA player heights based on user input. The raw data is taken from [https://www.openintro.org/data/index.php?data=nba_heights)](https://www.openintro.org/data/index.php?data=nba_heights).  The data is served in json format by the endpoint [https://mach-eight.uc.r.appspot.com/)](https://mach-eight.uc.r.appspot.com/).

The task is to create an application that takes a single integer input. The application will download the raw data from the website above [https://mach-eight.uc.r.appspot.com)](https://mach-eight.uc.r.appspot.com) and print a list of all pairs of players whose height in inches adds up to the integer input to the application. If no matches are found, the application will print `No matches found`


### Sample output is as follows:
```
> app 139

- Brevin Knight         Nate Robinson
- Nate Robinson         Mike Wilks
```

The algorithm to find the pairs must be faster than `O(n^2)`. All edge cases
should be handled appropriately. This is _not_ a closed book test. You are
encouraged to reach out with any questions that you come across.


## Solution


```
pip install -r requirements.txt

```