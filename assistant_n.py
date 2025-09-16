import speech_recognition as sr
import google.generativeai as genai

# Function to convert speech to text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

genai.configure(api_key="AIzaSyD8tceqfzNCUBpa7QybPsSvTkUetmNcDOY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Convert speech to text
text = speech_to_text()
print("Converted Text: ", text)

prompt_parts = [
  "(On January 16, 2024, at 08:30 AM, a critical alert was triggered by the Server Monitoring system. The alert message stated, \"Alert! High server CPU usage detected.\"\nLater, at 12:45 PM, the Security System issued a warning, \"Attention! Unusual login activity detected.\"\nAround 3:20 PM, the Backup System sent an informational notification, \"Notification: Daily backup completed successfully.\"\nThe next day, on January 17, 2024, at 09:10 AM, the Network Monitoring system reported a critical alert, \"Alert! Network connectivity issue reported.\"\nAt 2:55 PM the same day, the Server Monitoring system issued a warning, \"Warning! Disk space running low on server.\"\nLooking ahead to January 18, 2024, at 10:00 AM, the System Maintenance system provided an informational update, \"Info: System update scheduled for tomorrow.\"\n)\n" + text,
]

response = model.generate_content(prompt_parts)
print(response.text)
