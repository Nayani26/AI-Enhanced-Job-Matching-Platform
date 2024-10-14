import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import base64

# Load the datasets
resumes_path = "resumes_large.csv"
job_descriptions_path = "job_descriptions_large.csv"
resumes_df = pd.read_csv(resumes_path)
job_descriptions_df = pd.read_csv(job_descriptions_path)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("AI-Enhanced Job Matching Platform"),
    
    # Resume Upload
    dcc.Upload(
        id='upload-resume',
        children=html.Div(['Drag and Drop or ', html.A('Select a Resume')]),
        style={
            'width': '100%', 'height': '60px', 'lineHeight': '60px',
            'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
            'textAlign': 'center', 'margin': '10px'
        }
    ),
    
    # Extracted Skills Section
    html.Div(id='output-data-upload'),
    
    # Job Recommendations
    html.H2("Recommended Jobs"),
    html.Div(id='job-recommendations'),
    
    # Skill Match Visualizations
    dcc.Graph(id='skill-match-graph')
])

# Function to parse uploaded resume
def parse_resume(contents):
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    return decoded.decode('utf-8')

# Callback to handle resume upload and display extracted skills
@app.callback(
    Output('output-data-upload', 'children'),
    Output('job-recommendations', 'children'),
    Output('skill-match-graph', 'figure'),
    Input('upload-resume', 'contents')
)
def update_output(contents):
    if contents is None:
        return "", "", {}
    
    # Parse the uploaded resume
    resume_text = parse_resume(contents)
    
    # Extract skills from resume (simple example using regex)
    skills = ['Python', 'Machine Learning', 'SQL']  # Placeholder for actual skill extraction
    
    # Matching with job descriptions (Placeholder logic)
    matched_jobs = ['Data Scientist', 'ML Engineer']  # Placeholder for actual job matching
    
    # Visualize the skill matching with bar chart (example)
    skill_counts = {skill: skills.count(skill) for skill in set(skills)}
    fig = {
        'data': [{'x': list(skill_counts.keys()), 'y': list(skill_counts.values()), 'type': 'bar'}],
        'layout': {'title': 'Skill Match Count'}
    }
    
    return (
        f"Extracted Skills: {', '.join(skills)}",
        html.Ul([html.Li(job) for job in matched_jobs]),
        fig
    )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
