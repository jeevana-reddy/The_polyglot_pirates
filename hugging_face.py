from transformers import MarianMTModel, MarianTokenizer

def load_model(source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    try:
        model = MarianMTModel.from_pretrained(model_name)
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        raise ValueError(f"Error loading model {model_name}: {e}")
    
    
    