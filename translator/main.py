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




# ******************************* Manual Tests ******************************* #
# example1 = "db.user.find({name:'julio'});"
# example2 = "db.user.find({_id:23113},{name:1,age:1});"
# example3 = "db.user.find({age:{$gte:21}},{name:1,_id:1});"
# example4 = "db.user.find({age:{$gte:21,$lte:50}});"
# example5 = "db.user.find({age:{$gte:21,$lte:50},name:'julio'});"
# example6 = "db.user.find({age:20,name:'julio'});"
# example7 = "db.user.find({},{name:1,age:1});"
# example8 = "db.user.find({},{name:1,age:1,_id:0});"
# example9 = "db.user.find({$or:[{status:'A'},{age:50}]})"
# example10 = "db.user.find({$or:[{status:'A'},{age:50}],name:'julio'},{name:1,age:1})" # -> SELECT name, age FROM user WHERE (status = 'A' OR age = 50) AND name = 'julio';
# example11 = "db.user.find({age:{$in:[20,25]}})" # -> SELECT * FROM user WHERE age IN (20, 25);
# example12 = "db.user.find({$or:[{status:'A'},{age:50}],$and:[{name:'julio'},{status:'active'}]})" # -> SELECT * FROM user WHERE (status = 'A' OR age = 50) AND (name = 'julio' AND status = 'active');
# example13 = "db.user.watch({},{name:1,age:1});" # -> Raises method error

# print(translate(example1))
# print(translate(example2))
# print(translate(example3))
# print(translate(example4))
# print(translate(example5))
# print(translate(example6))
# print(translate(example7))
# print(translate(example8))
# print(translate(example9))
# print(translate(example10))
# print(translate(example11))
# print(translate(example12))
# print(translate(example13)) -> error, not find
# print(translate({"table": "user", "method": "find"})) -> error, not string
