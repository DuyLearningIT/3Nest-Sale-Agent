from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from app.model import VirtualAssistant

ollama_model = OpenAIModel(model_name='llama3.2', base_url = '')

knowledge_agent = Agent(
    ollama_model,
    result_type = VirtualAssistant,
    result_retries = 3,
    system_prompt = 'You are a knowledgable personal assistant. Use the provided context to answer the questions.'
)