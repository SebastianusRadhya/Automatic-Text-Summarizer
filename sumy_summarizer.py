import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer 
import heapq

def generate_sumy(raw_text):
    parser = PlaintextParser.from_string(raw_text,Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, 5)
    summary_results = " ".join(map(str, summary))
    return summary_results