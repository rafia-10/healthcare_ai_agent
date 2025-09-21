from nlu import call_groq
from utils import add_appointment, log_faq

def handle_user_input(user_input):
    
    result = call_groq(user_input)
    if not result:
        return {"error": "AI parsing failed"}

    intent, entities, confidence = result

    patient_name = entities.get("patient_name") if entities else None
    doctor = entities.get("doctor") if entities else None
    datetime_ = entities.get("datetime") if entities else None
    email = entities.get("email") if entities else None

    if intent == "book_appointment":
        add_appointment(patient_name, doctor, datetime_, email)
        return f"Appointment booked for {entities['patient_name']}."
    elif intent == "faq":
        answer = "placeholder FAQ answer"
        log_faq(user_input, answer)
        return answer
    else:
        return "Escalation: staff notified."
