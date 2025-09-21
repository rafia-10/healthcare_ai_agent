
# Healthcare Customer Support Agent — Solution Design Doc



### 1. Introduction


Role Chosen: Healthcare Customer Support Agent
Industry: Healthcare / Clinics
Why this role?
The role focuses on repetitive, high-value tasks like booking appointments and answering FAQs. Automating this reduces staff workload, improves patient satisfaction, and provides measurable business value. It’s specific, easy to demo in 1 day, and aligns with the assessment rubric.


### 2. Role Responsibilities
A clinic receptionist normally:
    1. Answers patient questions (clinic hours, services, insurance).
    2. Books, reschedules, or cancels appointments.
    3. Sends confirmations and reminders.
    4. Escalates complex queries to staff.
    5. Maintains appointment logs.


### 3. AI Agent Tasks
The AI agent automates:
    • Appointment Booking / Rescheduling / Cancellation: Detect intent, collect details (name, doctor, date/time), save to DB, sync to Google Calendar.
    • FAQ Handling: Responds to common questions (hours, insurance, services).
    • Confirmations / Reminders: Sends confirmation emails via SendGrid.
    • Escalation: If AI cannot answer or low confidence, notify staff via email.
Prioritization:
    1. Booking/rescheduling → High impact
    2. FAQ → Medium impact
    3. Confirmations/reminders → High impact

### 4. High-Level Architecture
User (web UI)  ⇄  Flask Backend  ⇄  Gemini AI API
                                ⇄  SQLite Database
                                ⇄  Google Calendar API
                                ⇄  SendGrid API

Flow Example (Booking):
    1. User types: “Book an appointment with Dr. Aisha tomorrow 2 PM.”
    2. Backend calls Gemini API → extracts intent & entities.
    3. Backend saves booking in SQLite.
    4. Backend creates Google Calendar event.
    5. Backend triggers SendGrid email confirmation.
    6. Frontend displays success message.
Flow Example (FAQ):
    1. User types question: “What time do you open on Sundays?”
    2. Backend calls Gemini API → identifies intent/question type.
    3. Backend retrieves answer from predefined FAQ table.
    4. Frontend displays answer.
       
### 5. Tech Stack


Layer
Technology / Tool
Frontend
Flask + HTML + Bootstrap (simple UI for input/output)
Backend
Python Flask
AI / NLP
Gemini AI API (free tier)
Database
SQLite
APIs
Google Calendar API, SendGrid API
Scheduler
Cloud Scheduler / simple cron for reminders




### 6. Data Model
Booking Table (SQLite)


Column         Type        Description
id             Integer     Primary key
patient_name   Text        Patient’s name
doctor         Text        Doctor name
datetime_iso   Text        Appointment date & time (ISO)
email          Text        Patient email
status         Text        booked / cancelled / completed



### 7. Automation Actions
    • Booking: Slot filling → DB → Google Calendar → SendGrid email.
    • Reminders: Scan DB for next-day bookings → send email reminders.
    • FAQ: AI interprets question → fetch answer → display.
    • Escalation: Low confidence → email staff with details.
### 8. Frontend Design
    • Single-page interface:
        ◦ Input box for free-text commands
        ◦ Chat-style response area
        ◦ Booking list (table)
    • Shows status of bookings and escalations

### 9. Future Extensions
    • Two-way Google Calendar sync for staff
    • SMS reminders via Twilio free tier
    • Authentication for staff and patients
    • Voice interface for hands-free booking
    • Multilingual support
      
### 10. Running the Project
    1. Backend:
            python -m venv venv
	source venv/bin/activate  # Linux/Mac
	venv\Scripts\activate     # Windows
	pip install -r requirements.txt
	python app.py

    2. Frontend: Open browser → http://localhost:5000
    3. Demo example: “Book appointment with Dr. Aisha tomorrow 2 PM”
    4. Confirmations: Check email inbox for SendGrid notification
       
### 11. Free Tier Compliance
    • Groq AI: free API key 
    • Google Calendar: free-tier events
    • SendGrid: free tier for transactional email
    • Cloud Scheduler: optional, Always Free Tier


### 12. Summary
    • Automates high-value clinic receptionist tasks.
    • End-to-end full-stack implementation: UI → Backend → AI → APIs → DB.
    • Demonstrates practical problem-solving, API integration, and rapid development under time constraints.
