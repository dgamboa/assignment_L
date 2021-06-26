# Helper function to parse list of fields to select
def fieldsList(fieldsString):
  fields = fieldsString.split(',')
  fieldNames = []

  for field in fields:
    colon = field.find(":")
    if field[colon + 1:] == '1':
      fieldNames.append(field[:colon])
  
  return fieldNames

# Helper function to stringify fields for appending to SQL query
def stringifyFields(fieldsString):
  fields = fieldsList(fieldsString)
  return ",".join(fields)

# Helper function to separate WHERE and FIELDS arguments
def whereAndFieldsSeparator(arguments):
  arguments = arguments.replace("(","").replace(")","").replace(";","").replace(" ","")
  return arguments[1:-1].split("},{")

# Helper function to destructure method from arguments
def destructureMethod(call):
  argumentStart_index = call.find('(')
  method = call[:argumentStart_index]
  arguments = call[argumentStart_index:]

  return [method, arguments]

# Helper function to destructure db, table and method call
def destructureQuery(query):
  return query.split('.')

# Main function to translate MongoDB to SQL
def translator(mongoQuery):
  db, table, methodCall = destructureQuery(mongoQuery)

  method, combinedArguments = destructureMethod(methodCall)

  separatedArguments = whereAndFieldsSeparator(combinedArguments)

  whereArguments = separatedArguments[0]

  fieldsSQL = "*" if len(separatedArguments) == 1 else stringifyFields(separatedArguments[1])

  print(whereArguments)
  print(fieldsSQL)

  # whereClause = ""

  # return f'SELECT {fieldsSQL} FROM {table}' + whereClause




# db.user.find({name:'julio'}); -> SELECT * FROM user WHERE name = 'julio';
# db.user.find({_id:23113},{name:1,age:1}); -> SELECT name, age FROM user WHERE _id = 23113;
# db.user.find({age:{$gte:21}},{name:1,_id:1}); -> SELECT name, _id FROM user WHERE age >= 21;
example1 = "db.user.find({name:'julio'});"
example2 = "db.user.find({_id:23113},{name:1,age:1});"
example3 = "db.user.find({age:{$gte:21}},{name:1,_id:1});"
example4 = "db.user.find({age:{$gte:21,$lte:50}});"

translator(example1)
