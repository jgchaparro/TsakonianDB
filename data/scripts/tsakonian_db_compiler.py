# Data wrangling
import pandas as pd

# Read main table
main = pd.read_excel('tables/main.xlsx')

# Join `types` table
types = pd.read_excel('tables/types.xlsx')

# Join main and types by type
main_dict = pd.merge(main, types, on='type', how='left')

# Fill NaN values with empty string
main_dict = main_dict.fillna('')

# Reorder columns for easier usage
order = ['tsakonian', 'greek', 'notes'] # NOTE: excluding additional info columns
main_dict = main_dict[order]

# Save the dictionary to a Markdown file
dictionary_name = 'Tsakonian - Greek Dictionary.md'
dictionary_path = 'exports/' + dictionary_name
main_dict.to_markdown(dictionary_path, index=False)