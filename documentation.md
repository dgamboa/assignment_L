# MongoDB to SQL Translator
The purpose of the translator is to take in a MongoDB query as input, and return the same query in SQL as the output.

## Engineering Specs
- The translator supports the following MongoDB methods:
```
db.find()
```
- The translator returns a simple error message with all other MongoDB methods
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
- 
