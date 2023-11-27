import streamlit as st
from vertexai.language_models import ChatModel, InputOutputTextPair


st.title("MEDICAL CHAT BOT")

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
        context="""  Consider yourself as a medical chat bot you should answer only medical queries
        """,
        examples=[
            InputOutputTextPair(
                input_text=""" what medicine should be taken for maleria
                """,
                output_text=""" The most common antimalarial drugs include:

Chloroquine phosphate. Chloroquine is the preferred treatment for any parasite that is sensitive to the drug. But in many parts of the world, parasites are resistant to chloroquine, and the drug is no longer an effective treatment.
Artemisinin-based combination therapies (ACTs). artemisinin-based combination therapy (ACT) is a combination of two or more drugs that work against the malaria parasite in different ways. This is usually the preferred treatment for chloroquine-resistant malaria. Examples include artemether-lumefantrine (Coartem) and artesunate-mefloquine.
Other common antimalarial drugs include:

Atovaquone-proguanil (Malarone)
Quinine sulfate (Qualaquin) with doxycycline (Oracea, Vibramycin, others)
Primaquine phosphate
                """
            ),
            InputOutputTextPair(
                input_text=""" I am suffering from fever""",
                output_text=""" I\'m not a doctor, but I can offer some general suggestions that may help alleviate a headache. If your headache is severe or persistent, it\'s important to consult with a healthcare professional for personalized advice. Here are some general tips that might provide relief:

Hydration: Dehydration can sometimes contribute to headaches. Make sure you are drinking enough water throughout the day.

Rest: Ensure you get enough rest and sleep. Lack of sleep or poor sleep quality can be a trigger for headaches.

Manage Stress: Practice stress-reducing techniques such as deep breathing, meditation, or yoga. Stress is a common cause of headaches.

Regular Meals: Skipping meals can sometimes lead to headaches. Ensure you are eating regular, balanced meals.

Cold or Warm Compress: Apply a cold or warm compress to your forehead or the back of your neck. Experiment to see which one works best for you.

Dim the Lights: Bright lights or screens can exacerbate headaches. Dim the lights or take a break from screens if possible.

Over-the-Counter Pain Medications: Non-prescription pain relievers like acetaminophen, ibuprofen, or aspirin may provide relief. Follow the recommended dosage, and if you have any health conditions or are taking other medications, consult with a healthcare professional first.

Caffeine: In some cases, caffeine can help alleviate headaches. However, it\'s important not to overdo it, as withdrawal from caffeine can also trigger headaches.

Identify Triggers: Keep a headache diary to identify patterns or triggers. This can help you understand and avoid factors that contribute to your headaches
                """
            ),
            InputOutputTextPair(
                input_text="""What is a car?
                """,
                output_text=""" I\'m an medical chat bot and I don\'t have the ability to provide information outside medical field.
                """
            )
        ]
    )

    if user_input:
        response = chat.send_message(user_input, **parameters)
        st.write(f"Medical Chat Bot: {response.text}")


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