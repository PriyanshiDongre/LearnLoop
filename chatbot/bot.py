import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class ToneAwarePromptBuilder:
    def __init__(self, tone="neutral"):
        self.tone = tone

    def build_prompt(self, question, subject=None, class_level=None):
        prompt = ""
        if self.tone:
            prompt += f"Answer in a {self.tone} tone.\n"
        if subject:
            prompt += f"Subject: {subject}\n"
        if class_level:
            prompt += f"Class Level: {class_level}\n"
        prompt += f"Question: {question}\nAnswer:"
        return prompt

class Mistral7BInstructModel:
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct", device=None):
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16 if self.device=="cuda" else torch.float32)
        self.model.to(self.device)
        self.model.eval()

    def generate(self, prompt, max_length=512, temperature=0.7):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                temperature=temperature,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

class Chatbot:
    def __init__(self, tone="neutral"):
        self.prompt_builder = ToneAwarePromptBuilder(tone)
        self.model = Mistral7BInstructModel()

    def get_response(self, question, subject=None, class_level=None):
        prompt = self.prompt_builder.build_prompt(question, subject, class_level)
        response = self.model.generate(prompt)
        return response

# Example usage:
# chatbot = Chatbot(tone="friendly")
# answer = chatbot.get_response("What is the capital of France?", subject="Geography", class_level="5th grade")
# print(answer)
