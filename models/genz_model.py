from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch, random

model_id = "universalgamingfen1/genz-slang-t5-small"
tokenizer_g = AutoTokenizer.from_pretrained(model_id)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # Changed to torch.device for type safety
model_g = AutoModelForSeq2SeqLM.from_pretrained(model_id)
model_g = model_g.to(device)

fallback_emojis = ["😭", "🔥", "💀", "🤯", "✨", "😍", "🥳", "😡", "💔"]

def ensure_emoji(text: str) -> str:
    if any(ch in text for ch in "😭🔥💀🤯✨😍🥳😡💔"):
        return text.strip()
    return text.strip() + " " + random.choice(fallback_emojis)

def to_genz(text: str, max_new_tokens: int = 100):
    # yahan tumhara prefix / style hint daal dena
    inp = text
    inputs = tokenizer_g(inp, return_tensors="pt").to(model_g.device)
    output_ids = model_g.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=1.0,
        top_k=50,
        top_p=0.9,
    )
    out = tokenizer_g.decode(output_ids[0], skip_special_tokens=True)
    return ensure_emoji(out)
