from models import model


def gemini_ai(prompt):
    prompt = prompt
    try:
        response = model.generate_content(contents=[prompt])
        return response.text
    except Exception as ex:
        print(ex)
