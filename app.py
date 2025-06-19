# import speech_recognition as sr 
# import pyttsx3 

# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Speak something...")
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio)
#             print("You said:", text)
#             return text
#         except:
#             return "Sorry, I didn't catch that."

# def ai_response(user_input):
#     if "your name" in user_input:
#         return "my name is Bot ai assistant."
#     else:
#         return "im in learning face"


# while True:
#     user_input = listen()
#     response = ai_response(user_input)
#     print("AI:", response)
#     speak(response)










# import openai
# client = openai.OpenAI(api_key = "api key")

# def ai_response(prompt):
#     res = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role":"user", "content": prompt}]
#     )
#     return res.choices[0].message.content


# while True:
#     user_input = listen()
#     response = ai_response(user_input)
#     print("AI:", response)
#     speak(response)






from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['text'].lower()
    if "your name" in user_input:
        response = "my name is  Bot AI."
    else:
        response = "Im learning"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
