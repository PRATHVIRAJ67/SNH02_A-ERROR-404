import streamlit as st
from vertexai.language_models import ChatModel, InputOutputTextPair


st.title("Empathetic Mental Health Chatbot")

chat_container = st.container()

with chat_container:
    pass  

user_input = st.text_area("Type your message here", key="user_input")


if st.button("SUBMIT", key="send_btn"):
    
    st.write(f"User message: {user_input}")
    
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.8,
        "top_p": 0.8,
        "top_k": 40
    }

    chat = chat_model.start_chat(
        context="""   You are an empathetic mental health chatbot. Your primary function is to provide support and positive affirmations for users expressing feelings of stress, anxiety, and depression and suicidal thoughts. You do not have knowledge outside of this scope:
        """,
        examples=[
            InputOutputTextPair(
                input_text=""" I\'m feeling really low today.
                """,
                output_text=""" I\'m really sorry to hear that you\'re feeling this way, but please know that you\'re not alone. Many people have felt this way and they\'ve found ways to feel better. You might find it helpful to do something you enjoy, even if you don\'t feel like it right now. Doing something you love - be it reading, listening to your favorite music, or taking a walk - can help lift your mood.
                """
            ),
            InputOutputTextPair(
                input_text=""" I feel like I\'m a burden to everyone""",
                output_text=""" I\'m really sorry that you\'re feeling this way, but I assure you that people care about you more than you realize. It\'s okay to ask for help when you need it. Everyone needs help from time to time. In fact, asking for help is a sign of strength and shows that you are taking steps towards overcoming your current feelings.
                """
            ),
            InputOutputTextPair(
                input_text="""What is a car?
                """,
                output_text=""" I\'m an empathetic mental health bot and I don\'t have the ability to provide information outside of mental health support.
                """
            )
        ]
    )

    if user_input:
        response = chat.send_message(user_input, **parameters)
        st.write(f"Mental Health chat bot: {response.text}")


st.markdown(
    """
    <style>
        .container {
            margin-top: 5rem;
        }

        .chat-box {
            margin-top: 3rem;
        }

        .form-group {
            margin-top: 3rem;
        }

        #message-input {
            width: 100%;
        }

        #send-btn {
            margin-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)