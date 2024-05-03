import gradio as gr
from transformers import pipeline
import redis
from deep_translator import GoogleTranslator

sentiment_model = pipeline("sentiment-analysis")

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def sentiment_analysis(text):
    if not text:
        return "Nenhum texto", "N/A", "N/A"

    translated_text = GoogleTranslator(source="pt", target="en").translate(text=text)

    cached_result = redis_client.get(translated_text)
    if cached_result:
        sentiment, score = cached_result.split(":")
        return text, sentiment, float(score)

    try:
        result = sentiment_model(translated_text)[0]
        sentiment = result["label"]
        score = result["score"]

        redis_client.setex(translated_text, 600, f"{sentiment}:{score}")

        return text, sentiment, score
    except Exception as e:
        return f"Error: {str(e)}", "N/A", "N/A"


css = """
body { font-family: 'Arial', sans-serif; }
textarea, input { border: 2px solid #007BFF; border-radius: 5px; }
button { background-color: #007BFF; color: white; border-radius: 5px; padding: 10px; }
button:hover { background-color: #0056b3; }
"""
print("Starting the application...")
iface = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(
        lines=2, placeholder="Digite o texto em português aqui...", label="Texto"
    ),
    outputs=[
        gr.Textbox(label="Texto Original"),
        gr.Textbox(label="Sentimento"),
        gr.Textbox(label="Confiança"),
    ],
    title="Análise de sentimento 🧐😮",
    description="Digite o texto em português e veja o sentimento associado a ele.",
    css=css,
    allow_flagging="never",
)
print("Interface created, launching...")

if __name__ == "__main__":
    iface.launch()
    print("Interface launched.")
