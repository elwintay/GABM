import glob
import os
import json

class Agent:
    def __init__(self, name):
        
        self.system_prompt = None
        self.user_prompt = None
        self.name = name
        self.personality = None
        self.vision = f"../images/user/{name}/"
        self.prompt_path = f"../prompts/user/{name}/"

    def get_system_prompt(self):
        return self.system_prompt
    
    def get_user_prompt(self):
        return self.user_prompt
    
    def get_personality(self):
        return self.personality
    
    def get_vision(self):
        return self.vision
    
    def get_prompt_path(self):
        return self.prompt_path
    
    def set_agent(self):
        # Read system prompt from file
        with open("../prompts/system/systemprompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.user_prompt = self.set_user_prompt()
        self.personality = self.user_prompt['personality']
    
    def set_user_prompt(self):
        files = glob.glob(os.path.join(self.prompt_path, f"{self.name}_gemini_response_*.json"))
        if not files:
            # Fallback to initial json if no outputs yet
            with open(f"../prompts/user/{self.name}/{self.name}_gemini_response_1.json", "r", encoding="utf-8") as f:
                prompt_str = f.read()
                prompt_str = self.clean_prompt(prompt_str)
                prompt_dict = json.loads(prompt_str)
                return prompt_dict
        files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
        with open(files[-1], "r", encoding="utf-8") as f:
            self.user_prompt = f.read()
            self.user_prompt = self.clean_prompt(self.user_prompt)
            self.user_prompt = json.loads(self.user_prompt)
            return self.user_prompt

    def clean_prompt(self, prompt):
        cleaned_text = prompt.strip()
        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text[7:].strip()
        if cleaned_text.startswith("```"):
            cleaned_text = cleaned_text[3:].strip()
        if cleaned_text.endswith("```"):
            cleaned_text = cleaned_text[:-3].strip()
        return cleaned_text
    
if __name__ == "__main__":
    agent = Agent("maria")
    agent.set_agent()
    print(agent.get_user_prompt())
    print(agent.get_system_prompt())
    print(agent.get_personality())
    print(agent.get_vision())
    print(agent.get_prompt_path())