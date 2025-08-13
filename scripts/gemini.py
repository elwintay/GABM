import time
import json

from google import genai
from dotenv import load_dotenv
from google.genai import types
import requests
import os
import glob
load_dotenv()

class Gemini:
    def __init__(self, agent):
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        self.agent = agent

    def get_response(self):
        if self.agent.vision:
            image_files = glob.glob(os.path.join(self.agent.vision, "*.[jp][pn]g"))
            content = image_files + [str(self.agent.user_prompt)]
        else:
            content = str(self.agent.user_prompt)
        
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=self.agent.system_prompt),
            contents=content
        )

        # Clean the response text
        cleaned_text = self.agent.clean_prompt(response.text)

        # Calculate the next index
        existing_files = glob.glob(os.path.join(self.agent.prompt_path, f"{self.agent.name}_gemini_response_*.json"))
        next_index = len(existing_files) + 1

        # Save the response
        output_path = os.path.join(self.agent.prompt_path, f"{self.agent.name}_gemini_response_{next_index}.json")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
        return cleaned_text
    
if __name__ == "__main__":
    # Example usage
    from agent import Agent

    agent_name = "john"
    new_agent = Agent(agent_name)
    new_agent.set_agent()
    print(new_agent.prompt_path)
    
    gemini_instance = Gemini(new_agent)
    response = gemini_instance.get_response()
    
    print("Generated Response:", response)