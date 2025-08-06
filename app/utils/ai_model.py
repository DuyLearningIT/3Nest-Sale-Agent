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
    Based on the given information about document A and document B

    **Document A:**
    ---
    {document_A}
    ---

    **Document B:**
    ---
    {document_B}
    ---

    Analysis Tasks:
    - You just need to give me the answer is YES or NO, and then give me all the information of this company 
    including CEO, email, phone, ... of company B if haved
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)
