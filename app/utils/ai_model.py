import google.generativeai as genai 

GOOGLE_API_KEY = 'AIzaSyARU5sXd2fesrBz6fuCcEdXJ8OFWgv7KTw'
genai.configure(api_key=GOOGLE_API_KEY)

document_A = """
3Nest Investment and Trading Company
Research and develop about AI solutions to automate in factory
This means we will use hardware to collect information and then give them AI to handle,
and also, we make softwares to visualize information that AI handled
"""

async def matching_information(document_A: str, document_B: str):
    model = genai.GenerativeModel('gemini-2.5-pro')

    prompt = f"""
    You are an AI assistant specializing in document analysis.
    Based on the given information about document A and document B, 
    We're company A, please check for us whether my company can become a partner of company B or not, 
    if the answer is YES, talk about the fields of B that I can involve in, 
    if the answer is NO, just give me the reason.

    **Document A:**
    ---
    {document_A}
    ---

    **Document B:**
    ---
    {document_B}
    ---

    **Analysis Tasks:**
    1.  Answer: Do my company can become the partner of B company or not? Answer with "Yes" or "No".
    2.  Details: Briefly explain your reasoning for the answer above in one sentence.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
