import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_recommendation(insight):
    """Send product insights to LLM and get smart recommendations."""
    prompt = f"""
    You’re a business advisor helping small and medium-sized businesses make better product decisions.
    Based on the following product insight, provide a clear and actionable recommendation:

    Insight: {insight}

    Recommendation:
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You’re an expert business advisor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()

    except Exception as e:
        print(f"Error generating recommendation: {e}")
        return "Could not generate recommendation at this time."
