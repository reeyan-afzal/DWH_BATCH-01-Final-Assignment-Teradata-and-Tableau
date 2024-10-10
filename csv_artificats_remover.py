import pandas as pd
import re

# Function to clean text by removing specific artifacts
def clean_text(text):
    # Check if the value is a string
    if isinstance(text, str):
        # Fix known encoding issues (like â„¢, Â®, etc.)
        encoding_artifacts = {
            'â„¢': '',
            'â€™': "'",
            'â€œ': '"',
            'â€': '"',
            'Â®': '',
            'Â©': '',
            'â€˜': "'",
            'Ã©': 'e',
            'Ã': 'A'
            # Add more mappings for common artifacts if needed
        }

        # Replace known artifacts
        for artifact, replacement in encoding_artifacts.items():
            text = text.replace(artifact, replacement)

        # Remove remaining non-ASCII characters
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text  # Return the text unchanged if it's not a string (i.e., a float or NaN)

# Load your CSV file into a pandas DataFrame
df = pd.read_csv('tableau_games.csv', encoding='utf-8')

# Apply the clean_text function to the entire 'short_description' column (or any other column)
df['Game_Name'] = df['Game_Name'].apply(clean_text)
df['Short_Description'] = df['Short_Description'].apply(clean_text)

# Save the cleaned data to a new CSV file
df.to_csv('tableau_games1.csv', index=False)

print("Short descriptions cleaned by removing encoding artifacts and non-ASCII characters.")
