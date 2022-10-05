import transformers
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

if torch.cuda.is_available():
   device = torch.device("cuda")
else:
   device = torch.device("cuda")

def generate_bart(raw_text):
    bart_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn").to(device)
    bart_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    
    input_text = ' '.join(raw_text.split())
    input_tokenized = bart_tokenizer.encode(input_text, return_tensors='pt').to(device)
    
    summary_ids = bart_model.generate(input_tokenized,
                                    num_beams = 4,
                                    num_return_sequences = 1,
                                    no_repeat_ngram_size = 2,
                                    length_penalty = 1,
                                    min_length = 0,
                                    max_length = 128,
                                    early_stopping = True)
    
    output = [bart_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
    return "".join(output)