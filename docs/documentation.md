# MongoDB to SQL Translator
The purpose of the translator is to take in a MongoDB query as input, and return the same query in SQL as the output.

## Running the Translator


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
- File structure
  - [followed guidelines from other projects]
- Data structures and algorithms
  - General approach:
    - My primary focus was to build a working translator
    - The intent was to get a functional MVP that could be refactored for algorithmic efficiency
    - I chose to prioritize the delivery guideline (3-4 hours) over algorithmic performance
  - Specific choices:
    - 
