import streamlit as st
import re
import random

# List of weak/common passwords
common_passwords = ["password", "123456", "123456789", "qwerty", "password123", "admin", "letmein"]

# Generate a strong password
def generate_strong_password(length=12):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*"

    all_chars = upper + lower + digits + special
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special),
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

# Check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in common_passwords:
        feedback.append("🚫 Too common. Avoid using easily guessed passwords.")
        return 1, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both UPPERCASE and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0–9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add a special character (!@#$%^&*).")

    if len(password) >= 12:
        score += 1

    return score, feedback

# 🎨 Streamlit App UI
st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")

st.markdown("Check how strong your password is and get suggestions to improve it.")

# User input
password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    st.subheader("🔍 Strength Evaluation:")
    if score >= 5:
        st.success("✅ Strong Password!")
    elif score >= 3:
        st.warning("⚠️ Moderate Password - Could be stronger.")
    else:
        st.error("❌ Weak Password - Needs improvement.")

    if feedback:
        st.markdown("### 💡 Suggestions:")
        for tip in feedback:
            st.write("- " + tip)

# Password Generator
st.markdown("---")
st.markdown("### 🚀 Generate a Strong Password")
if st.button("Generate Strong Password"):
    generated = generate_strong_password()
    st.success(f"🔐 `{generated}`")
