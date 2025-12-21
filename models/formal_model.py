from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_id_f = "rajistics/informal_formal_style_transfer"
tokenizer_f = AutoTokenizer.from_pretrained(model_id_f)
model_f = AutoModelForSeq2SeqLM.from_pretrained(model_id_f).to(
    "cuda" if torch.cuda.is_available() else "cpu"
)

def to_formal(text: str, max_new_tokens: int = 64, num_beams: int = 4):
    inputs = tokenizer_f(text, return_tensors="pt").to(model_f.device)
    outputs = model_f.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        num_beams=num_beams,
        early_stopping=True,
        no_repeat_ngram_size=2,
    )
    return tokenizer_f.decode(outputs[0], skip_special_tokens=True).strip()
