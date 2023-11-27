import streamlit as st
from vertexai.language_models import ChatModel, InputOutputTextPair

st.title("PILL DETECTOR")

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
        context="""Your primary function is to predict the tablets for the particular disease. You do not have knowledge outside of this scope:""",
        examples=[
            InputOutputTextPair(
                input_text="""what tablets should i take for headache""",
                output_text="""Acetaminophen (Tylenol): It is often recommended for mild to moderate pain relief. It's important to follow the recommended dosage and not exceed the maximum daily limit, as excessive use can lead to liver damage.

Ibuprofen (Advil, Motrin): It's a nonsteroidal anti-inflammatory drug (NSAID) that can help reduce pain and inflammation. It's important to take it with food or milk to minimize the risk of stomach upset.

Naproxen (Aleve): Another NSAID similar to ibuprofen, it provides longer-lasting pain relief. Like ibuprofen, it should be taken with food.

Aspirin: Aspirin is also an NSAID and can be used for pain relief. It is also known for its anti-inflammatory properties and its ability to reduce fever. Aspirin should be taken with food to reduce the risk of stomach ups"""
            ),
            InputOutputTextPair(
                input_text="""I am facing continuous vomiting what should i do""",
                output_text="""Bismuth subsalicylate (Pepto-Bismol): This medication can help relieve nausea and upset stomach. It's available in liquid and tablet forms. Follow the recommended dosage on the product label.

Dimenhydrinate (Dramamine): This medication is often used to treat motion sickness but can also help with nausea and vomiting due to other causes. Follow the recommended dosage, and be aware that it may cause drowsiness.

Doxylamine (Unisom): This is an antihistamine that can be used to relieve nausea and vomiting. It may cause drowsiness, so use it with caution and follow the recommended dosage.

Ginger: While not a medication, ginger in various forms (ginger tea, ginger ale, ginger candies) is a natural remedy that some people find helpful for nausea."""
            ),
            InputOutputTextPair(
                input_text="""i am suffering from dengue what tablets should i take""",
                output_text="""Antihistamines: Over-the-counter antihistamines, such as diphenhydramine (Benadryl), can help relieve itching associated with the chickenpox rash. Follow the recommended dosage, and be aware that these medications may cause drowsiness.

Acetaminophen (Tylenol): This can be used to reduce fever and relieve pain. Follow the recommended dosage, and avoid exceeding the maximum daily limit.

Cool Baths: Soothing baths with oatmeal or baking soda can help relieve itching.

Calamine Lotion: Applying calamine lotion to the rash may also help alleviate itching."""
            ),
            InputOutputTextPair(
                input_text="""who is elon musk""",
                output_text="""I am not able to recognize can u provide some more information about which the disease  """
            )
        ]
    )

    if user_input:
        response = chat.send_message(user_input, **parameters)
        st.write(f"Pill Detector : {response.text}")

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
