import gradio as gr
import os
import google.generativeai as genai

# Set Google API key 
os.environ['GOOGLE_API_KEY'] = "AIzaSyBS1pqU2FvyW9mIViPVc7swf-1Yqtu1-f8"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Create the Model
txt_model = genai.GenerativeModel('gemini-pro')

# Custom function to handle specific queries about ownership or creation
def custom_response(text):
    if "owner" in text.lower() or "created" in text.lower() or "developer" in text.lower() or "developed" in text.lower():
        return "I am a AI chatbot created by Yashwanth Kapa of Amrita Vishwa Vidyapeeetham , Nagercoil campus for his python mini project"
    else:
        return txt_model.generate_content(text).text

# Function that takes User Inputs and displays it on ChatUI
def query_message(history, txt):
    history.append((txt, None))
    return history

# Function that takes User Inputs, generates Response and displays on Chat UI
def llm_response(history, text):
    response_text = custom_response(text)
    history.append((None, response_text))
    return history

# Interface Code
with gr.Blocks(css="""
    .input-textbox { 
        border: 2px solid #4A90E2; 
        border-radius: 10px; 
        padding: 10px; 
    } 
    .submit-button { 
        background-color: #4A90E2; 
        color: white; 
        border-radius: 10px; 
        padding: 10px 20px; 
        border: none; 
    } 
    .submit-button:hover { 
        background-color: #357ABD; 
    } 
    .chatbot-box { 
        border: 2px solid #4A90E2; 
        border-radius: 10px; 
        padding: 10px; 
        height: 500px; 
    } 
    .credit { 
        text-align: center; 
        margin-top: 20px; 
        font-size: 14px; 
        color: #666; 
    }
    body {
        overflow: hidden; /* Prevents scrolling */
    }
    """) as app:
    
    with gr.Row():
        chatbot = gr.Chatbot(height=500, elem_classes="chatbot-box")
    
    with gr.Row():
        text_box = gr.Textbox(
            placeholder="Enter text and press enter",
            container=False,
            elem_classes="input-textbox",
        )
        btn = gr.Button("Submit", elem_classes="submit-button")
    
    with gr.Row():
        gr.HTML("<div class='credit'>Made by Yashwanth Kapa CSE-C</div>")

    btn.click(query_message, [chatbot, text_box], chatbot) \
       .then(llm_response, [chatbot, text_box], chatbot)

app.queue()
app.launch(debug=True, share=True)
