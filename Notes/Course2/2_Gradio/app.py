from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    return model(prompt)[0]['summary_text']

with gr.Blocks() as demo:
    textbox = gr.Textbox(lines=5, placeholder="Enter text to summarize here...")
    gr.Interface(predict, textbox, "text")
    demo.launch()
