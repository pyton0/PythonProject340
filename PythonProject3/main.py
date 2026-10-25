
from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta property="og:title" content="Фотография">
    <meta property="og:description" content="Посмотри фотографию">
    <title>Фотография</title>

    <style>
        body {
            background: #181818;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 30px 12px;
        }

        #photo {
            width: min(90%, 650px);
            cursor: pointer;
            border-radius: 8px;
        }

        #scare {
            display: none;
            position: fixed;
            inset: 0;
            background: black;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }

        #scare img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }

        #close {
            position: absolute;
            right: 15px;
            top: 15px;
            z-index: 11;
        }
    </style>
</head>

<body>
    <h2>Фотография</h2>
    <p>Нажми на фото, чтобы открыть его.</p>

    <img id="photo"
         src="/static/images.jpg"
         alt="Фотография"
         onclick="showScare()">

    <div id="scare">
        <img src="/static/images (1).jpg" alt="Изображение">
        <button id="close" onclick="closeScare()">Закрыть</button>
    </div>

    <audio id="sound" src="/static/gdfgdgf.mp3" preload="auto"></audio>

    <script>
        function showScare() {
            document.getElementById("scare").style.display = "flex";

            const sound = document.getElementById("sound");
            sound.currentTime = 0;
            sound.play().catch(error => {
                console.log("Звук не запустился:", error);
            });
        }

        function closeScare() {
            document.getElementById("scare").style.display = "none";

            const sound = document.getElementById("sound");
            sound.pause();
            sound.currentTime = 0;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(debug=True)
