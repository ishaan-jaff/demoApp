import os
from flask import Flask, render_template, request
from litellm import completion

app = Flask(__name__)

# Set your API keys here
os.environ["OPENAI_API_KEY"] = "your_openai_key"
os.environ["COHERE_API_KEY"] = "your_cohere_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        model = request.form["model"]

        # Construct a message for the model
        messages = [{"content": user_input, "role": "user"}]

        # Make a completion call based on the selected model
        response = completion(model, messages)

        bot_response = response['choices'][0]['message']['content']

        return render_template("index.html", bot_response=bot_response)

    return render_template("index.html", bot_response=None)

if __name__ == "__main__":
    app.run(debug=True)
