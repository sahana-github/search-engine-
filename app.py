from flask import Flask, request, render_template, jsonify
import pandas as pd
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Load your dataset from an Excel file
df = pd.read_excel('Book1.xlsx')  # Replace 'Book1.xlsx' with your file path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_matching_support_groups', methods=['GET'])
def get_matching_support_groups():
    query = request.args.get('query', '').strip().lower()

    # Initialize a list to store matching Support Group Names
    matching_support_groups = []

    for index, row in df.iterrows():
        for col in df.columns:
            value = str(row[col]).strip().lower()
            if fuzz.partial_ratio(query, value) >= 80:
                matching_support_groups.append(row['Support Group Name'])

    return jsonify(matching_support_groups)

if __name__ == '__main__':
    app.run(debug=True)
