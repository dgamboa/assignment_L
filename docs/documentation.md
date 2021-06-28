# MongoDB to SQL Translator
The purpose of the translator is to take in a MongoDB query as input, and return the same query in SQL as the output.

## Running the Tests
From the root directory in the terminal, run `python -m unittest tests/tests.py`.

## Running the Translator
Create a sample file on the project's root directory. From the sample file, import main with `from translator import main`, and call the `main.translate` function passing in a string containing a MongoDB query: `main.translate(query -> str): -> str`. The function will return a string with the MongoDB query translated to SQL.

Alternatively, import main in the REPL with `from translator import main` and run the function directly from the terminal.

## Engineering Specs
- The translator supports the following MongoDB methods:
```
db.find()
```
- The translator returns a simple error message if passed any MongoDB methods not supported.
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
  - Queries consist of unicode characters best represented as strings.
- File structure and testing
  - After researching a few projects, I followed the most common structuring guidelines.
  - The file was original an executable script than I refactored into modules to incorporate testing.
- Data structures and algorithms
  - General approach:
    - My primary focus was to build a working translator.
    - The intent was to get a functional MVP that could be later refactored for algorithmic efficiency.
    - I chose to prioritize the delivery guideline (3-4 hours) and simplicity over more sophisticated algorithms that might take more time than intended.
  - Specific choices:
    - The most time-intensive operations are performed by the helper functions that search for characters by looping through strings, or build strings based on a subset of characters specified by indexed locations.
    - The majority of these utilize native functions that search for characters in O(n) time (e.g. `find`, `split`, and `replace`).
    - There are a few instances of custom character-by-character search where necessary (mainly, for instances where arguments need to be split but depend on the sequence of braces or brackets).
    - Some of these may be optimized by incorporating more performant search algorithms.
- Opportunities for future improvement:
  - The logic in several of the helper functions overlaps. This logic should be abstracted into a separate function and leveraged to achieve a DRYer module (e.g. The `whereList` and `whereAndFieldsSeparator` functions both use brace counting functionality).
  - It would be useful to implement unit tests for all the helper functions before refactoring them to automate testing for bugs that might be introduced from the changes.
  - My experience building Python packages is limited, so I would want to check with a more experienced developer to incorporate best practices and make imports more robust.
