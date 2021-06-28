from translator import main

import unittest

class TestTranslate(unittest.TestCase):
  def test_sanity_check(self):
    assert True

  def test_simple_where_query(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({name:'julio'});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT * FROM user WHERE name = 'julio';")
  
  def test_where_with_fields_1(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({_id:23113},{name:1,age:1});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT id, name, age FROM user WHERE _id = 23113;")
  
  def test_where_with_gte_and_fields(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({age:{$gte:21}},{name:1,_id:1});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT id, name, age FROM user WHERE age >= 21;")
  
  def test_where_with_gte_and_lte(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({age:{$gte:21,$lte:50}});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT * FROM user WHERE age >= 21 AND age <= 50;")
  
  def test__two_wheres_1(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({age:{$gte:21,$lte:50},name:'julio'});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT * FROM user WHERE age >= 21 AND age <= 50 AND name = 'julio';")

  def test_two_wheres_2(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({age:20,name:'julio'});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT * FROM user WHERE age = 20 AND name = 'julio';")
  
  def test_no_wheres_1(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({},{name:1,age:1});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT id, name, age FROM user;")

  def test_no_wheres_2(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({},{name:1,age:1,_id:0});"
    result = main.translate(query)
    self.assertEqual(result, "SELECT name, age FROM user;")

  def test_where_or(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({$or:[{status:'A'},{age:50}]})"
    result = main.translate(query)
    self.assertEqual(result, "SELECT * FROM user WHERE (status = 'A' OR age = 50);")

  def test_where_or_and_1(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({$or:[{status:'A'},{age:50}],name:'julio'},{name:1,age:1})"
    result = main.translate(query)
    self.assertEqual(result, "SELECT id, name, age FROM user WHERE (status = 'A' OR age = 50) AND name = 'julio';")

  def test_where_in(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({age:{$in:[20,25]}})"
    result = main.translate(query)
    self.assertEqual(result, "SELECT * FROM user WHERE age IN (20, 25);")

  def test_where_or_and_2(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.find({$or:[{status:'A'},{age:50}],$and:[{name:'julio'},{status:'active'}]})"
    result = main.translate(query)
    self.assertEqual(result, "SELECT * FROM user WHERE (status = 'A' OR age = 50) AND (name = 'julio' AND status = 'active');")

  def test_not_find_method(self):
    """
    Test that it outputs correct query for a record where name is 'julio'
    """
    query = "db.user.watch({},{name:1,age:1});"
    self.assertRaises(Exception, main.translate, query)

if __name__ == '__main__':
  unittest.main()
