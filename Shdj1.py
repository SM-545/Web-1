from flask import Flask
import os
app = Flask(__name__)
@app.route('/H')
def home():
    return """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="view port" content="width=device-width, initial-scale=1.0"
    <title>My First Page</title>
</head>
<body>
    <h1>Hello Reza</h1>
    <p>This is my first page.</p>
</body>
</html>"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT' , 5000))
    app.run(host='0.0.0.0' , port = port)