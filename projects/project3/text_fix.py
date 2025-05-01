

def text_fix(text: str):
    """used to convert text into a format where only the first letter of each word is capitalized"""
    """will remove any underscores as well. primarily used for drinks formatted 'DRINK_NAME' """
    text = [word[0].upper() + word[1:].lower() for word in text.replace("_", " ").split()]
    return_text = ""
    for word in text:
        return_text += f"{word} "
    return return_text.strip()