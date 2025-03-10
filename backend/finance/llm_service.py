from google import genai

def generate_recommendation(insight):
    """Generate business recommendations using the Gemini API."""
    client = genai.Client(api_key="AIzaSyBz0ZNqaOgAEt1bXz4WjPjnvcwHv-OOg58")

    prompt = f"""
    You’re a business advisor helping small and medium-sized businesses make better product decisions.
    Based on the following product insight, provide a clear and actionable recommendation:
    And I don't want big answer just convert these insights into words and tell me that pointwise i want to show them on the dashboard on my website. 
    Insight: {insight}

    Recommendation:
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # You can change this to an available model like "gemini-2.0-pro" or "gemini-2.0-flash"
            contents=prompt
        )
        # print("I am here")
        recommendation = response.candidates[0].content.parts[0].text.strip()
        print(recommendation)

        # print(response)
        # Extract the generated recommendation
        return response.candidates[0].content.parts[0].text.strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Could not generate recommendation at this time."
