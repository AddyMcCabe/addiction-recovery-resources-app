from src import app
from src import db

if __name__ == "__main__":
    db.create_all()
    app.env = "development"
    app.run(debug=True)