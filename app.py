import gradio as gr
from transformers import pipeline
from prompts import MEDICAL_PROMPT
from risk_engine import detect_risk

print("Loading model...")

pipe = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct",
    trust_remote_code=True
)

print("Model loaded!")


def analyze(symptoms):

    risk = detect_risk(symptoms)

    prompt = MEDICAL_PROMPT.format(
        symptoms=symptoms
    )

    result = pipe(
        prompt,
        max_new_tokens=250,
        do_sample=True,
        temperature=0.7
    )

    answer = result[0]["generated_text"]

    return risk, answer


with gr.Blocks(title="MediGuide AI") as demo:

    gr.Markdown("""
    # 🩺 MediGuide AI

    Offline Medical Reasoning Assistant
    for Underserved Communities
    """)

    symptoms = gr.Textbox(
        lines=5,
        label="Describe Your Symptoms"
    )

    submit = gr.Button("Analyze")

    risk_box = gr.Textbox(
        label="Risk Level"
    )

    output = gr.Textbox(
        label="Medical Guidance",
        lines=15
    )

    submit.click(
        analyze,
        inputs=symptoms,
        outputs=[risk_box, output]
    )

demo.launch()
