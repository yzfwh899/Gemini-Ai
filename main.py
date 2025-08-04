import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import GenerativeModel
from google.generativeai.types import Content, Part

# Load environment variables dari file .env
load_dotenv()

# Konfigurasi API key Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Inisialisasi model, contoh: 'gemini-pro' atau 'gemini-1.5-flash'
model = genai.GenerativeModel('models/gemini-2.5-flash')
chat = model.start_chat(history=[
    Content(role="user", parts=[Part(text="Hello, I have a question about Gemini.")]),
    Content(role="model", parts=[Part(text="Certainly, what would you like to know?")]),
])

def main():
    """Fungsi utama untuk menjalankan chatbot interaktif."""
    print("🤖 Gemini AI Chat Bot")
    print("Ketik 'exit' untuk keluar\\n")
    
    while True:
        user_input = input("Anda: ")
        
        if user_input.lower() == 'exit':
            print("Terima kasih! Sampai jumpa!")
            break
            
        try:
            # Mengirim input ke model dan mendapatkan respons
            response = model.generate_content(user_input)
            print(f"Gemini: {response.text}\\n")
        except Exception as e:
            print(f"Terjadi error: {e}\\n")

if __name__ == "__main__":
    main() 