import streamlit as st
import re

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="GENAI Bike Chatbot",
    page_icon="🚴",
    layout="centered"
)

# -------------------------------
# Custom Styling (UI Upgrade)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0d1117;
}
.stChatMessage {
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Chatbot Logic
# -------------------------------
def generate_reply(message: str) -> str:
    text = message.lower().strip()

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", text):
        return "Hello 👋 Welcome to GENAI Bike Support!"

    # -------------------------------
    # GT 650
    # -------------------------------
    if "gt 650 mileage" in text:
        return "GT 650 mileage is around 22-25 km/l"

    if "gt 650 price" in text:
        return "GT 650 price starts at ₹3.2 Lakhs"

    if "gt 650 engine" in text:
        return "648cc engine producing 47 bhp"

    if "gt 650" in text:
        return "GT 650 is a powerful café racer 🔥"

    # -------------------------------
    # Himalayan 450
    # -------------------------------
    if "himalayan 450 mileage" in text:
        return "Mileage is around 28-30 km/l"

    if "himalayan 450 price" in text:
        return "Price starts at ₹2.85 Lakhs"

    if "himalayan 450 features" in text:
        return "TFT display, navigation, ABS, riding modes"

    if "himalayan 450" in text:
        return "Himalayan 450 is perfect for off-road 🏔️"

    # -------------------------------
    # Yamaha R15
    # -------------------------------
    if "r15 mileage" in text:
        return "R15 gives 40-45 km/l mileage"

    if "r15 price" in text:
        return "R15 price starts at ₹1.8 Lakhs"

    if "r15 engine" in text:
        return "155cc engine with VVA technology"

    if "r15" in text:
        return "Yamaha R15 is a stylish sports bike 🏍️"

    # -------------------------------
    # Duke 390
    # -------------------------------
    if "duke 390 mileage" in text:
        return "Mileage is around 25-30 km/l"

    if "duke 390 price" in text:
        return "Price starts at ₹3.1 Lakhs"

    if "duke 390 engine" in text:
        return "373cc engine producing 43 bhp"

    if "duke 390" in text:
        return "Duke 390 is a powerful street bike ⚡"
    # -------------------------------
    # RC 390
    # -------------------------------
    if "rc 390 mileage" in text:
        return "Mileage is around 25-28 km/l"

    if "rc 390 price" in text:
        return "Price starts at ₹3.2 Lakhs"

    if "rc 390 engine" in text:
        return "373cc engine producing 43 bhp"

    if "rc 390" in text:
        return "RC 390 is a racing-focused bike 🏁"

    # -------------------------------
    # Comparison
    # -------------------------------
    if "best bike" in text:
        return """Choose based on your need:

R15 → Best mileage 💰  
Duke 390 → Street performance ⚡  
RC 390 → Racing 🏁  
GT 650 → Power 🔥  
Himalayan 450 → Adventure 🏔️"""

    if "which bike for mileage" in text:
        return "Best mileage bike is Yamaha R15 💰"

    if "which bike for racing" in text:
        return "RC 390 is best for racing 🏁"

    if "which bike for off road" in text:
        return "Himalayan 450 is best for off-road 🏔️"

    # -------------------------------
    # Customer Support
    # -------------------------------
    if "emi" in text:
        return "EMI starts from ₹5000/month (approx)"

    if "insurance" in text:
        return "Insurance cost is around ₹15k-₹25k yearly"

    if "booking" in text:
        return "You can book from showroom or online"

    if "delivery" in text:
        return "Delivery time is 2-6 weeks"

    if "warranty" in text:
        return "Standard warranty is 3 years"

    # -------------------------------
    # Fun
    # -------------------------------
    if "joke" in text:
        return "Why do bikes love roads? Because they hate traffic 😂"

    # Fallback
    return "Ask me about GT 650, Himalayan 450, R15, Duke 390 or RC 390 😊"


# -------------------------------
# UI
# -------------------------------
st.title("🚴 GENAI Bike Support Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask your bike question...")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot reply
    reply = generate_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)