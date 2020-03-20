# Example Python Flask Crud

 Simple example python flask crud app for sqlite.
 
## Screenshots


![image](screenshots.png)  
 
 
### Installing (for linux)

open the terminal and follow the white rabbit.


```
git clone https://github.com/gurkanakdeniz/example-flask-crud.git
```
```
cd example-flask-crud/
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=crudapp.py
```
```
flask db init

```After creating a migration, either manually or as --autogenerate, you must apply it with alembic upgrade head. If you used db.create_all() from a shell, you can use alembic stamp head to indicate that the current state of the database represents the application of all migrations.
https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date
```
$ flask db stamp head

flask db migrate -m "entries table"
```
```
flask db upgrade
```
```
flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
