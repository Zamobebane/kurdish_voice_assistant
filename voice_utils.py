# voice_utils.py
def kurdish_chat_response(text):
    text = text.lower()
    if "slaw" in text:
        return "Slaw! Chonî?"
    elif "navê te" in text or "nave te" in text:
        return "Navê min RêbazBot e."
    elif "tu çawa yî" in text or "tu chawa yi" in text:
        return "Ez baş im, spas!"
    else:
        return "Bibore, ez fam nakim. Ji kerema xwe daxwazêkî din bide."
