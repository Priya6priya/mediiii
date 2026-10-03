from flask import Flask, render_template, request, redirect, session
from utils.fetch_data import get_real_time_data
from model.predictor import predict_outbreak
import os
from utils.fetch_data import get_live_outbreaks_from_newsapi
from flask import Flask, jsonify
app = Flask(__name__)
from flask import jsonify
from flask import jsonify
from utils.fetch_data import get_live_outbreaks_from_newsapi
from notifications.email_alert import send_email_alert

@app.route('/send-alert', methods=["POST"])
def send_alert():
    email = request.form.get("email")
    disease = request.form.get("disease")
    region = request.form.get("region")

    subject = f"⚠️ Alert: {disease} outbreak in {region}"
    body = f"""
    Dear User,

    There's an active {disease} outbreak reported in your area: {region}.
    Stay safe and follow preventive measures provided in the MedGuardian dashboard.

    Regards,
    MedGuardian AI
    """
    success = send_email_alert(email, subject, body)
    return jsonify({"status": "sent" if success else "failed"})

@app.route("/live-outbreaks")
def live_outbreaks():
    api_key = "ACTUAL_NEWSAPI_KEY"  # Replace with your real NewsAPI key
    data = get_live_outbreaks_from_newsapi(api_key)
    return jsonify(data)

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    data = get_real_time_data()
    prediction = predict_outbreak(data)
    return render_template("dashboard.html", data=data, prediction=prediction)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session['user'] = user
        return redirect('/dashboard')
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    # test_app.py

import unittest
from app import app

class MedGuardianTest(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MedGuardian', response.data)

    def test_dashboard_data(self):
        response = self.app.get('/dashboard-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'disease', response.data)

    def test_send_alert_invalid(self):
        response = self.app.post('/send-alert', data={
            'email': 'test@example.com',
            'disease': 'Dengue',
            'region': 'Nowhere'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'status', response.data)

if __name__ == '__main__':
    unittest.main()
