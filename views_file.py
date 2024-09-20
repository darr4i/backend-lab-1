from backend_lab_1 import app  # Імпортуємо існуючий об'єкт app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
