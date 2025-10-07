from flask import Flask, render_template_string

app = Flask(__name__)

# Reemplaza con el ID de tu bot y los permisos que quieras
BOT_ID = "TU_BOT_ID_AQUI"
PERMISSIONS = "8"  # 8 = Admin, puedes cambiar
INVITE_LINK = f"https://discord.com/oauth2/authorize?client_id=1425158409128251505&permissions=8&integration_type=0&scope=bot+applications.commands"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lyvion Bot</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            color: white;
        }
        .container {
            text-align: center;
            animation: fadeIn 2s ease;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(0,0,0,0.3);
            animation: slideDown 1s ease forwards;
        }
        p {
            font-size: 1.2rem;
            margin-bottom: 40px;
            animation: slideUp 1s ease forwards;
        }
        .btn {
            padding: 15px 30px;
            background: #ff5f6d;
            background: linear-gradient(to right, #ff5f6d, #ffc371);
            border: none;
            border-radius: 50px;
            color: white;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            text-decoration: none;
        }
        .btn:hover {
            transform: scale(1.1);
            box-shadow: 0 0 20px rgba(255,255,255,0.5);
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        @keyframes slideDown {
            from {opacity: 0; transform: translateY(-50px);}
            to {opacity: 1; transform: translateY(0);}
        }
        @keyframes slideUp {
            from {opacity: 0; transform: translateY(50px);}
            to {opacity: 1; transform: translateY(0);}
        }
        /* Animación de fondo */
        body::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at center, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: rotateBG 20s linear infinite;
            z-index: 0;
        }
        @keyframes rotateBG {
            0% {transform: rotate(0deg);}
            100% {transform: rotate(360deg);}
        }
        .container * {
            position: relative;
            z-index: 1;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bienvenido a Lyvion Bot</h1>
        <p>Tu bot favorito de Discord, ahora más fácil de agregar a tu servidor.</p>
        <a href="{{ invite_link }}" class="btn" target="_blank">Agregar Bot a Discord</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, invite_link=INVITE_LINK)

if __name__ == "__main__":
    app.run(debug=True)
