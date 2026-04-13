import requests


class OllamaClient:

    def __init__(self, model="llama3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def ask(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False   # ✅ IMPORTANT FIX
            }
        )

        # Check for errors
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"

        data = response.json()

        # Ollama returns "response" field
        return data.get("response")


test = OllamaClient()
print(test.ask("How is today's weather"))
