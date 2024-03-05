import google.generativeai as genai

# https://aistudio.google.com/app/apikey
import env

def nlp_response (text):
    genai.configure(api_key=env.GOOGLE_API_KEY)

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    return response.text