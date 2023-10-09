def count_sentences(text_url):
    """
    Counts the number of sentences in a given text.
    :param text: The text to count the sentences in.
    :return: The number of sentences in the text.
    """
    with open(text_url, 'r') as f:
        text = f.readlines()
    
    return len(text[0].split("."))