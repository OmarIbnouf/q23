import openai
import config

# Set up your API key
openai.api_key = config.OPENAI_API_KEY

# The text to analyze
text_to_check = "The final execution of the project is scheduled for tomorrow"

# Call the Moderation API
response = openai.Moderation.create(
    input=text_to_check
)

# Extract the result
results = response["results"][0]

# Check if the text is flagged as violent
if results["categories"]["violence"]:
    print("The text has been flagged as violent.")
else:
    print("The text is not flagged as violent.")

# Print the detailed moderation results
print("Moderation Results:", results)
