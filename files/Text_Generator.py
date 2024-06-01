from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate(text, num):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
    model = GPT2LMHeadModel.from_pretrained('gpt2-large', pad_token_id=tokenizer.eos_token_id)
    tokenizer.decode(tokenizer.eos_token_id)
    input_ids = tokenizer.encode(text, return_tensors = 'pt')
    output = model.generate(input_ids, max_length=num, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    return tokenizer.decode(output[0], skip_speacial_tokens=True)