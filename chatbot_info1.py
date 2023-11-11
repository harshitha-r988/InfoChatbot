import wikipedia

def get_wikipedia_summary(query, sentences=2):
    try:
        result = wikipedia.summary(query, sentences=sentences)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation by returning suggestions
        suggestions = ", ".join(e.options)
        return f"Multiple matches found. Did you mean: {suggestions}?"
    except wikipedia.exceptions.PageError:
        return "No information found on Wikipedia for the given query."

# Example usage
search_query = input("Enter your Wikipedia search query: ")
summary = get_wikipedia_summary(search_query)
print(summary)
