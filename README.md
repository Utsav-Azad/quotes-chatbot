# 📌 Quotes Recommendation Chatbot (Rasa + Python)

An AI-powered conversational chatbot that recommends inspirational quotes based on user intent such as motivation, love, success, and humor. The chatbot is built using the **Rasa framework** for Natural Language Understanding (NLU) and dialogue management, with a **Flask-based web interface** for real-time user interaction.

---

# 🚀 Features

- 🤖 AI-powered chatbot using **Rasa NLU**
- 💬 Intent detection for different quote categories
- 🧠 Dynamic quote generation using **custom Python action**
- 📂 JSON-based quote database
- 🌐 Web-based chat interface using **Flask**
- 🔌 REST API communication between frontend and chatbot backend
- 🧪 Automated chatbot testing using **Rasa test stories**
- 📊 Conversation accuracy validation

---

# 🧠 Technologies Used

- Python  
- Rasa (NLU + Core)  
- Flask  
- REST API  
- JSON  
- HTML / CSS / JavaScript  

---

# 🏗 System Architecture

User → Web Interface → Flask Backend → Rasa REST API →  
NLU Intent Detection → Dialogue Policy → Custom Action → Quote Database → Response

---

# 📂 Project Structure

```
quotes_bot
│
├── actions/
│   └── actions.py
│
├── data/
│   ├── nlu.yml
│   ├── stories.yml
│   └── rules.yml
│
├── models/
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_stories.yml
│
├── app.py
├── quotes.json
├── domain.yml
├── config.yml
├── endpoints.yml
├── credentials.yml
└── requirements.txt
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/Utsav-Azad/quotes-chatbot.git
cd quotes-chatbot
```

Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Chatbot

Start the action server:

```bash
rasa run actions
```

Start the Rasa server:

```bash
rasa run --enable-api --cors "*"
```

Run the Flask web application:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# 🧪 Testing the Chatbot

Automated testing can be performed using test stories:

```bash
rasa test core
```

This validates conversation flows and ensures the chatbot behaves as expected.

---

# 🌍 Deployment

The chatbot backend can be deployed using platforms such as:

- Render  
- Railway  
- Docker containers  
- Cloud servers  

Deployment enables real-time interaction through a web interface instead of command-line usage.

---

# 🔮 Future Enhancements

- Sentiment analysis integration  
- Database integration for scalable quote storage  
- Voice-based chatbot interaction  
- Mobile application integration  
- Multi-language support  
- User profile personalization  

---

# 👨‍💻 Author

**Utsav Azad**

GitHub:  
https://github.com/Utsav-Azad

---

# ⭐ If you found this project useful

Give it a **star ⭐ on GitHub**