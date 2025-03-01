import torch
from transformers import MarianMTModel, MarianTokenizer
from hugging_face import load_model
from llama_translation import llama_translate 




'''def translate(text, source_lang, target_lang, model_choice="Hugging Face"):
    if model_choice == "Hugging Face":
        model, tokenizer = load_model(source_lang, target_lang)
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            translated_tokens = model.generate(**inputs)
        return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    elif model_choice == "Llama 3.2":
        return llama_translate(text, source_lang, target_lang)
    else:
        return "Unsupported model selected."  '''
        
        
def translate(text, source_lang, target_lang, model_choice="Hugging Face"):
    if source_lang == target_lang:
        return text  # Return the input text directly if source and target languages are the same

    if model_choice == "Hugging Face":
        model, tokenizer = load_model(source_lang, target_lang)
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            translated_tokens = model.generate(**inputs)
        return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    elif model_choice == "Llama 3.2":
        return llama_translate(text, source_lang, target_lang)
    else:
        return "Unsupported model selected."