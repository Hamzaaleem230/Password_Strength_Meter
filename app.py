import re
import streamlit as st

# Title
st.title("🔒 Password Strength Meter")

# Description
st.markdown("""
            ### Welcome to the **Password Strength Meter!**
            Ensure that your passwords are strong and secure by checking the following statistics:
            - 📏 Length: The length of the password should be at least 8 characters.
            - 🔡 Complexity: The password should contain uppercase and lowercase letter.
            - 🔢 Digits: The password should contain at least one digit (0-9).
            - 💥 Special characters: The password should contain at least one special character (!@#$%^&*).
            
            **💡 Improve your password strength by adding these criteria to your password.**
            """)

# Input field
password = st.text_input("Enter your password", type="password")

# Password strength meter
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        st.warning("❌ Password length should be at least 8 characters.")
        feedback.append("📏 Use at least 8 characters.")

    # Complexity check    
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    else:
        st.warning("❌ Password should contain both uppercase and lowercase letters.")
        feedback.append("🔡 Add uppercase and lowercase letters (e.g. Aᵇ Cᵈ).")

    # Digits check
    if re.search("[0-9]", password):
        score += 1
    else:
        st.warning("❌ Password should contain at least one digit (0-9).")
        feedback.append("🔢 Add digits (e.g. 1 2 3).")

    # Special characters check
    if re.search("[!@#$%^&*]", password):
        score += 1
    else:
        st.warning("❌ Password should contain at least one special character (!@#$%^&*).")
        feedback.append("💥 Add special characters (e.g. ! @ # $).")

    return score, feedback

# Button
if st.button("🔍 Check Password"):
    if password:
        score, feedback = check_password_strength(password)
        
        st.subheader("🔒 Password Strength Result:")
        
        if score == 3:
            st.warning("⚠️ Password is moderate. Add more security features to improve its strength.")
        elif score == 4:
            st.success("✅ Password is strong and secure.")
        else:
            st.error("🚨 Weak password - Improve it using the suggestions below.")
            
        if feedback:
            st.info("📝 Suggestions:")
            for tip in feedback:
                st.write(tip)
    else:
        st.error("🚨 Please enter a password to check its strength.")

# Footer
st.markdown("""
            ---
        ***Made by Hamza Syed~***
            """)
