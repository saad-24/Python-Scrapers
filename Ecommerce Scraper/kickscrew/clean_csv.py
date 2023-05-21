# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv('product_sample.csv')

# # Remove single quotes from all columns
# df = df.apply(lambda x: x.str.replace("'", "").str.replace('"', ''))
# df = df.apply(lambda x: x.str.replace("[", "").str.replace("]", ""))

# # Save the cleaned data back to a new CSV file
# df.to_csv('products_sample.csv', index=False)

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('products_clean.csv')

# Convert all columns to string data type
df = df.astype(str)

# Remove single quotes from all columns
df = df.apply(lambda x: x.str.replace("'", "").str.replace('"', ''))

# Remove square brackets from all columns
df = df.apply(lambda x: x.str.replace("[", "").str.replace("]", ""))

# Save the cleaned data back to a new CSV file
df.to_csv('products_final.csv', index=False)
