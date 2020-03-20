from sqlalchemy import create_engine

#db_uri = "sqlite:///db.sqlite"
db_uri = "mysql+mysqlconnector://root:@localhost/mycrud"
engine = create_engine(db_uri)


# Create Table
engine.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")



# insert a raw
## two parameters vs 3  for AUTO_INCREMENT
mytuple=("john", "Abidjan Koumassi")
engine.execute("insert into customers(name,address)  values (%s,%s)",mytuple)

# select *
result = engine.execute('SELECT * FROM customers')

print(result.fetchall())