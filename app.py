import gradio as gr
from models.genz_model import to_genz
from models.formal_model import to_formal

def style_transfer(text, mode):
    if mode == "Gen Z":
        return to_genz(text)
    else:
        return to_formal(text)

# Enhanced UI with Gradio Blocks
with gr.Blocks(theme=gr.themes.Soft(), title="Text Style Transfer") as demo:
    gr.Markdown("# 🎨 Text Style Transfer\nTransform your text into Gen Z slang or formal style using AI models.")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                lines=4, 
                label="Input Text", 
                placeholder="Enter your text here...",
                info="Type the text you want to transform."
            )
            style_choice = gr.Radio(
                choices=["Gen Z", "Formal"], 
                value="Gen Z", 
                label="Target Style",
                info="Choose the style to convert to."
            )
            submit_btn = gr.Button("Transform", variant="primary")
        
        with gr.Column(scale=1):
            output_text = gr.Textbox(
                lines=4, 
                label="Transformed Text", 
                interactive=False,
                info="The result will appear here."
            )
    
    gr.Examples(
        examples=[
            ["Hello, how are you?", "Gen Z"],
            ["I am fine, thank you.", "Formal"],
            ["What's up?", "Gen Z"],
            ["This is a test message.", "Formal"]
        ],
        inputs=[input_text, style_choice],
        outputs=output_text,
        fn=style_transfer,
        cache_examples=True
    )
    
    submit_btn.click(fn=style_transfer, inputs=[input_text, style_choice], outputs=output_text)
    
    gr.Markdown("---\n*Powered by Hugging Face Transformers and Gradio.*")

if __name__ == "__main__":
    demo.launch()
