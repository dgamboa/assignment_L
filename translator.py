def translator(mongoQuery):
  
  return mongoQuery




# db.user.find({name:'julio'}); -> SELECT * FROM user WHERE name = 'julio';
# db.user.find({_id:23113},{name:1,age:1}); -> SELECT name, age FROM user WHERE _id = 23113;
# db.user.find({age:{$gte:21}},{name:1,_id:1}); -> SELECT name, _id FROM user WHERE age >= 21;
example1 = "db.user.find({name:'julio'});"
example2 = "db.user.find({_id:23113},{name:1,age:1});"
example3 = "db.user.find({age:{$gte:21}},{name:1,_id:1});"

print(translator(example1))
