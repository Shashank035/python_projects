from transformers import pipeline


summarizer = pipeline("summarization")

def summarize_text(text, max_length=100, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


if __name__ == "__main__":
    text = """
    Artificial Intelligence (AI) is revolutionizing many industries, from healthcare to finance. 
    AI models can process vast amounts of data and make intelligent decisions, improving efficiency and accuracy. 
    With advancements in deep learning, AI systems have become more powerful, enabling applications like self-driving cars, 
    medical diagnostics, and virtual assistants. However, ethical concerns such as bias, privacy, and job displacement remain important challenges. 
    Researchers continue to develop solutions to make AI more responsible and beneficial for society.
    """
    
    summary = summarize_text(text)
    print("Summary:")
    print(summary)
