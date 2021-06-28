# MongoDB to SQL Translator
The purpose of the translator is to take in a MongoDB query as input, and return the same query in SQL as the output.

## Running the Tests
From the main directory in the terminal, run `python -m unittest tests/tests.py`.

## Running the Translator
Create a sample file on the project's root directory. From the sample file, import main with `from translator import main`, and call the `main.translate` function passing in a string containing a MongoDB query: `main.translate(query -> str): -> str`. The function will return a string with the MongoDB query translated to SQL.

Alternatively, import main in the REPL with `from translator import main` and run the function directly from the terminal.

## Engineering Specs
- The translator supports the following MongoDB methods:
```
db.find()
```
- The translator returns a simple error message if passed any MongoDB methods not supported
- The translator supports the following MongoDB operators:
```
$or
$and
$lt
$lte
$gt
$gte
$ne
$in
```

## Design Decisions
- String as the input / output data structure
  - Queries consist of unicode characters best represented as strings
- File structure and testing
  - After researching, I followed basic project guidelines from the Python community
  - For simplicity, I have kept the file as an executable script rather than a full package
  - To add test functionality, I would invest additional time researching how to turn the translator into a package and incorporate functional tests
  - With additional time to invest, I would also want to write unit tests for the helper functions 
- Data structures and algorithms
  - General approach:
    - My primary focus was to build a working translator
    - The intent was to get a functional MVP that could be refactored for algorithmic efficiency
    - I chose to prioritize the delivery guideline (3-4 hours) over algorithmic performance
  - Specific choices:
    - []
