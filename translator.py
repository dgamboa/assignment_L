# Library mapping MongoDB operators to SQL operators
operatorLibrary = {
  "or": "OR",
  "and": "AND",
  "lt": "<",
  "lte": "<=",
  "gt": ">",
  "gte": ">=",
  "ne": "<>",
  "in": "IN"
}

# Helper function to parse list of where clauses
def whereList(whereString):
  clauses = []
  tracker = ""
  brace_counter = 1
  bracket_counter = 0

  for c in whereString[1:]:
    if brace_counter == 1 and bracket_counter == 0 and (c == "," or c == "}"):
      clauses.append(tracker)
      tracker = ""
      continue
    
    if c == "{":
      brace_counter += 1
    elif c == "}":
      brace_counter -= 1
    
    if c == "[":
      brace_counter += 1
    elif c == "]":
      brace_counter -= 1
    
    tracker += c

  print(f'clauses: {clauses}')

  return clauses

# Helper function to parse where clause with AND/OR operators
def operatorsClause(clauseWithOperators):
  queryString = ""
  
  splitClauses = clauseWithOperators.split("$")
  
  field = splitClauses[0].replace(":","")

  for i in range(1, len(splitClauses)):
    if i > 1:
      queryString += " AND"

    clause = splitClauses[i].replace(",","").replace("}","")
    colon = clause.find(":")
    operatorSQL = operatorLibrary[clause[:colon]]
    queryString += f' {field} {operatorSQL} {clause[colon + 1:]}'

  return queryString

# Helper function to stringify where clauses for append to SQL query
def stringifyWhere(whereString):
  clauses = whereList(whereString)

  whereSQL = " WHERE"

  for i, clause in enumerate(clauses):
    if i > 0:
      whereSQL += " AND"

    if clause.find("$") == -1:
      colon = clause.find(":")
      whereSQL += f' {clause[:colon]} = {clause[colon + 1:]}'
    else:
      whereSQL += operatorsClause(clause)
  
  return whereSQL

# Helper function to parse list of fields to select
def fieldsList(fieldsString):
  fields = fieldsString.replace("{","").replace("}","").split(',')
  fieldNames = []

  for field in fields:
    colon = field.find(":")
    if field[colon + 1:] == '1':
      fieldNames.append(field[:colon])
  
  return fieldNames

# Helper function to stringify fields for appending to SQL query
def stringifyFields(fieldsString):
  fields = fieldsList(fieldsString)
  return ", ".join(fields)

# Helper function to separate WHERE and FIELDS arguments
def whereAndFieldsSeparator(arguments):
  parenthesis_counter = 1
  brace_counter = 0
  whereStr = []
  fieldStr = []
  i = 1
  toUpdate = whereStr

  while parenthesis_counter > 0:
    c = arguments[i]
    i += 1

    if c == "{":
      brace_counter += 1
    elif c == "}":
      brace_counter -= 1
    
    toUpdate.append(c)

    if arguments[i] == "(":
      parenthesis_counter += 1
    elif arguments[i] == ")":
      parenthesis_counter -= 1
    
    if brace_counter == 0:
      toUpdate = fieldStr
      i += 1
    
  return ["".join(whereStr), "".join(fieldStr)]

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
  # print(f'whereA: {separatedArguments[0]}')

  fieldsSQL = "*" if separatedArguments[1] == "" else stringifyFields(separatedArguments[1])

  whereSQL = "" if whereArguments.replace(" ","") == '{}' else stringifyWhere(whereArguments)

  return f'SELECT {fieldsSQL} FROM {table}' + whereSQL + ";"




# db.user.find({name:'julio'}); -> SELECT * FROM user WHERE name = 'julio';
# db.user.find({_id:23113},{name:1,age:1}); -> SELECT name, age FROM user WHERE _id = 23113;
# db.user.find({age:{$gte:21}},{name:1,_id:1}); -> SELECT name, _id FROM user WHERE age >= 21;
example1 = "db.user.find({name:'julio'});"
example2 = "db.user.find({_id:23113},{name:1,age:1});"
example3 = "db.user.find({age:{$gte:21}},{name:1,_id:1});"
example4 = "db.user.find({age:{$gte:21,$lte:50}});"
example5 = "db.user.find({age:{$gte:21,$lte:50},name:'julio'});"
example6 = "db.user.find({age:20,name:'julio'});"
example7 = "db.user.find({},{name:1,age:1});"
example8 = "db.user.find({},{name:1,age:1,_id:0});"
example9 = "db.user.find({$or:[{status:'A'},{age:50}]})"
example10 = "db.user.find({$or:[{status:'A'},{age:50}],name:'julio'},{name:1,age:1})" 
# -> SELECT name, age FROM user WHERE (status = 'A' OR age = 50) AND (name = 'julio');
example11 = "db.user.find({age:{$in:[20,25]}})"
# -> SELECT * FROM user WHERE age IN (20, 25);

translator(example1)
translator(example2)
translator(example3)
translator(example4)
translator(example5)
# print(translator(example6))
# print(translator(example7))
translator(example8)
# print(translator(example9))
translator(example10)

# print(stringifyWhere("name:'julio',age:20"))
# print(stringifyWhere("age:{$gte:21,$lte:50},name:'julio'"))
# print(operatorsClause('age:$gte:21'))
