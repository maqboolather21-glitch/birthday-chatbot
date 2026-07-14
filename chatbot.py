import streamlit as st

st.title(" College Help Chatbot")

# User input
user_input = st.text_input("Ask your question:")

# Function for chatbot response
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "timetable" in user_input:
        return "Your timetable is available on the college website."

    elif "lab" in user_input:
        return "Labs are on the 2nd floor."

    elif "assignment" in user_input:
        return "You can submit assignments through the student portal."

    elif "fees" in user_input:
        return "Fees can be paid online or at the admin office."

    elif "exam" in user_input:
        return "Exam schedule will be announced soon."

    elif "library" in user_input:
        return "Library is open from 9 AM to 5 PM."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand. Please ask something else."

# Show response
if user_input:
    response = get_response(user_input)
    st.write(" Bot:", response)