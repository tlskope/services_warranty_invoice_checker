from flask import Flask, request, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    num_lines = int(request.form['num_lines'])
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            return "Invalid file format", 400

        # Sort by 'Total' column
        df = df.sort_values(by='Total', ascending=False)

        # Select the top 'num_lines' jobs
        top_jobs = df.head(num_lines)

        # Columns to include in the report
        columns = [
            'Job Number', 'Serial Number', 'Finished Date', 'Model', 
            'Location Name', 'Notes', 'Line Items', 'Line Items Per Unit Ex. Gst', 'Total'
        ]
        report = top_jobs[columns]

        # Save the report to an Excel file
        output_path = os.path.join('outputs', 'top_jobs_report.xlsx')
        report.to_excel(output_path, index=False)

        # Render the table on the webpage
        table_html = report.to_html(index=False)

        return render_template('index.html', table=table_html, download=True)

    return "No file uploaded", 400

@app.route('/download', methods=['POST'])
def download_file():
    output_path = os.path.join('outputs', 'top_jobs_report.xlsx')
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    app.run(debug=True)
