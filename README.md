🛡️ PIXEL: Phishing URL Detector
Team Name: Pixel

Domain: Cyber Security

Project Objective: To detect and classify malicious URLs using Generative AI and Machine Learning to prevent social engineering attacks.

📌 Project Description
Pixel PhishGuard is a web-based security tool designed to identify if a website is safe or dangerous before a user clicks on it. Unlike traditional databases that only store known "bad" links, Pixel uses Google Gemini AI to "read" and analyze the structure of a URL to catch new, unreported threats.

🔍 How it Works
Input: A user pastes a suspicious URL into the Pixel dashboard.

AI Analysis: The backend sends this URL to the Gemini 2.5 Flash model.

Heuristic Check: The AI looks for red flags like:

Typosquatting: (e.g., g00gle.com instead of google.com).

Suspicious TLDs: (e.g., .xyz, .top used for banking).

Subdomain Masking: (e.g., paypal.secure.com.co).

Verdict: The system returns a result: Benign (Safe), Phishing, or Malware.

Logging: All results are saved in Firebase Firestore for future security audits.

🛠️ Technical Stack
Language: Python 3.x.

Web Framework: Flask.

AI Engine: Google Generative AI (Gemini SDK).

Database: Firebase Firestore.

Frontend: HTML5, CSS3 (Custom Dark Theme), and JavaScript.

🚀 Key Features
Real-time Analysis: Get results in under 2 seconds.

Zero-Day Detection: Identifies fake websites even if they were created minutes ago.

Cloud History: Team Pixel can monitor all detected threats via the Firebase console.

User-Friendly UI: Simple, dark-themed dashboard for high visibility.
