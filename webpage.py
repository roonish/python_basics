from flask import Flask, render_template_string

app = Flask(__name__)

# Define a simple HTML template as a string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Webpage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Webpage!</h1>
    <p>This is a basic webpage created using Python and Flask.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
