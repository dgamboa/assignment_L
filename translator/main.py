from . import helpers

def translate(mongoQuery):
  if type(mongoQuery) != str:
    raise Exception("The MongoDB query must be entered as a string")

  # Separate the query by stripping the db, the table name, and the method call (including method and arguments)
  db, table, methodCall = helpers.destructureQuery(mongoQuery)

  # Separate the method from its arguments
  method, combinedArguments = helpers.destructureMethod(methodCall)
  
  if method != "find":
    raise Exception("Only the MongoDB method *find* is supported at this time")

  # Separate the field components for SELECT from the where clauses for filtering
  separatedArguments = helpers.whereAndFieldsSeparator(combinedArguments)

  # Isolate the arguments associated with the where clauses
  whereArguments = separatedArguments[0]

  # Create query strings for the field component and where clauses
  fieldsSQL = "*" if separatedArguments[1] == "" else helpers.stringifyFields(separatedArguments[1])
  whereSQL = "" if whereArguments.replace(" ","") == '{}' else helpers.stringifyWhere(whereArguments)

  # Return the combined string for the translated SQL query
  return f'SELECT {fieldsSQL} FROM {table}{whereSQL};'
