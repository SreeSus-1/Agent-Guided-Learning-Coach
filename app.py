import streamlit as st

from agents.explainer_agent import ExplainerAgent
from agents.quiz_agent import QuizAgent
from agents.motivation_agent import MotivationAgent
from memory.progress_db import save_progress, get_progress

st.title("Agent Guided Learning Coach")

explainer = ExplainerAgent()
quiz = QuizAgent()
motivation = MotivationAgent()

menu = st.sidebar.selectbox(
    "Menu",
    ["Learn Topic", "View Progress"]
)

if menu == "Learn Topic":

    topic = st.text_input("Enter a topic to learn")

    if st.button("Explain Concept"):

        with st.spinner("Explaining..."):
            explanation = explainer.explain(topic)

        st.subheader("Concept Explanation")
        st.write(explanation)

        with st.spinner("Generating Quiz..."):
            questions = quiz.generate_quiz(topic)

        st.subheader("Quiz Questions")
        st.write(questions)

        score = st.slider("How well did you understand? (self score)", 1, 10)

        if st.button("Submit Progress"):

            save_progress(topic, score)

            feedback = motivation.motivate(topic)

            st.success("Progress Saved")

            st.subheader("Motivation Coach")
            st.write(feedback)

elif menu == "View Progress":

    progress = get_progress()

    for p in progress:

        st.write(
            f"Topic: {p['topic']} | Score: {p['score']} | Time: {p['timestamp']}"
        )