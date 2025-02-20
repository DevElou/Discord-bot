from openai import OpenAI

class OpenAIIntegration():
    def __init__(self, key):
        self.client = OpenAI(api_key=key)


    def get_chatgpt_response(self, prompt):
        response = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            },
        ],
        temperature=0.3,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=0.1,)
        return response.choices[0].message.content

    def format_code(self,language, prompt):
        code_prompt = f"Provide only the code in {language} for the following request, without any explanation or additional text: {prompt}"
        return self.get_chatgpt_response(code_prompt)
    

    def translate(self, language, prompt):
        translation_prompt = f"Translate the following text into {language}: {prompt}"
        return self.get_chatgpt_response(translation_prompt)

    

