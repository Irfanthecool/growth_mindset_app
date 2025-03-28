import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Growth Mindset App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #F8F9FA;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
    .stTextArea>div>div>textarea {
        border-radius: 8px;
    }
    .stProgress>div>div>div>div {
        background-color: #4CAF50;
    }
    .mindset-card {
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        padding: 20px;
        margin: 10px 0;
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.title("🧠 Growth Mindset Challenge")
st.subheader("Develop your abilities through dedication and hard work")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Mindset Assessment", "Progress Tracker", "Daily Challenge"])

# Home Page
if page == "Home":
    st.header("Welcome to Your Growth Mindset Journey")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60", 
                caption="Learning is a continuous journey")
    
    with col2:
        st.markdown("""
        <div class="mindset-card">
            <h3>What is Growth Mindset?</h3>
            <p>A growth mindset is the belief that your abilities and intelligence can be developed through hard work, 
            perseverance, and learning from your mistakes.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="mindset-card">
            <h3>Why Adopt It?</h3>
            <ul>
                <li>Embrace challenges as opportunities</li>
                <li>Learn from mistakes and feedback</li>
                <li>Persist through difficulties</li>
                <li>Celebrate effort, not just results</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Get Started")
    st.write("Use the navigation menu to explore different sections of this app and begin your growth mindset journey!")

# Mindset Assessment Page
elif page == "Mindset Assessment":
    st.header("Mindset Assessment")
    st.write("Rate how much you agree with each statement (1 = Strongly Disagree, 5 = Strongly Agree)")
    
    questions = [
        "I believe my intelligence can be developed.",
        "I view challenges as opportunities to grow.",
        "When I fail, I learn from my mistakes.",
        "I feel inspired by the success of others.",
        "Effort is the path to mastery."
    ]
    
    responses = []
    for i, question in enumerate(questions):
        response = st.slider(f"{i+1}. {question}", 1, 5, 3)
        responses.append(response)
    
    if st.button("Calculate My Mindset Score"):
        total_score = sum(responses)
        st.subheader(f"Your Growth Mindset Score: {total_score}/25")
        
        if total_score <= 10:
            st.warning("You may have a fixed mindset. Keep working on embracing challenges!")
        elif total_score <= 20:
            st.info("You're developing a growth mindset. Keep going!")
        else:
            st.success("You have a strong growth mindset! Keep nurturing it.")
        
        # Progress visualization
        progress = total_score / 25
        st.progress(progress)
        
        st.write("Track your progress over time to see your mindset grow!")

# Progress Tracker Page
elif page == "Progress Tracker":
    st.header("Progress Tracker")
    st.write("Track your growth mindset journey over time")
    
    # Initialize session state for storing entries
    if 'entries' not in st.session_state:
        st.session_state.entries = []
    
    with st.form("progress_form"):
        date = st.date_input("Date", datetime.now())
        challenge = st.text_input("What challenge did you face today?")
        response = st.text_area("How did you respond with a growth mindset?")
        rating = st.slider("Rate your mindset today (1-10)", 1, 10, 5)
        
        submitted = st.form_submit_button("Add Entry")
        if submitted:
            new_entry = {
                "date": date,
                "challenge": challenge,
                "response": response,
                "rating": rating
            }
            st.session_state.entries.append(new_entry)
            st.success("Entry added successfully!")
    
    if st.session_state.entries:
        st.subheader("Your Progress History")
        df = pd.DataFrame(st.session_state.entries)
        st.dataframe(df)
        
        # Plot progress over time
        st.subheader("Mindset Progress Over Time")
        st.line_chart(df.set_index('date')['rating'])

# Daily Challenge Page
elif page == "Daily Challenge":
    st.header("Daily Growth Mindset Challenge")
    
    challenges = [
        "Learn something new outside your comfort zone today.",
        "Reflect on a recent mistake and identify what you learned from it.",
        "Ask for constructive feedback from someone you trust.",
        "Encourage someone else in their learning journey.",
        "Try a different approach to a problem you've been stuck on."
    ]
    
    if 'current_challenge' not in st.session_state:
        st.session_state.current_challenge = np.random.choice(challenges)
    
    st.markdown(f"""
    <div class="mindset-card">
        <h3>Today's Challenge</h3>
        <p>{st.session_state.current_challenge}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Get a New Challenge"):
        st.session_state.current_challenge = np.random.choice(challenges)
        st.experimental_rerun()
    
    st.markdown("---")
    st.subheader("Complete the Challenge")
    
    with st.form("challenge_form"):
        reflection = st.text_area("How did you approach this challenge?")
        learned = st.text_area("What did you learn from this experience?")
        submitted = st.form_submit_button("Submit Reflection")
        
        if submitted:
            st.success("Thank you for your reflection! This helps reinforce your growth mindset.")
            # Store the reflection (in a real app, you'd save to a database)