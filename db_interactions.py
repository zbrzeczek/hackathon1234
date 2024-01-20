from app import db, user, app

app.app_context().push()
# Add a new user
new_user = user(imie='Adam', nazwisko='YourSurname', punkty=10)
db.session.add(new_user)
db.session.commit()
# Query all users
users = user.query.all()
print(users)