import json
import os


# Let's assume 'llm_output' is a string containing JSON data from the LLM
# This is where you would capture the output from the LLM
llm_output = """
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "website": "www.johndoeportfolio.com",
    "location": "New York, USA",
    "professional_profile": "Description and interests go here...",
    "academic_background": "<li>MSc in Computer Science - XYZ University, 2018-2020 - New York Campus</li><li>BSc in Information Technology - ABC Institute, 2014-2018</li>",
    "professional_experience": "<article><h3>Senior Developer at TechCorp</h3><p>Area: Software Development | Position: Senior Developer | Jan 2021 - Present</p><p>Detailed description of experience and achievements...</p></article>",
    "projects": "<article><h3>Automated Testing System</h3><p> May 2022</p><p>A comprehensive testing suite</p><p>Details about the project...</p></article>",
    "competences_skills": "<li>Advanced proficiency in Java and Python</li><li>Project management and team leadership</li>",
    "technical_knowledge": "<li>Database Management: SQL, MongoDB</li><li>Cloud Services: AWS, Azure</li>",
    "courses": "<li>Advanced Web Development - Coursera</li><li>Machine Learning Basics - Udemy</li>",
    "languages": "<li>English - Native</li><li>Spanish - Intermediate (Ongoing)</li>"
}
"""

# Define the path to your JSON file
json_file_path = os.path.join('code', 'variables.json')

# Convert the JSON string from the LLM into a Python dictionary
cv_data = json.loads(llm_output)

# Write the data to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(cv_data, json_file, indent=4)

print(f"JSON file updated successfully at {json_file_path}")

# Define your HTML template as a string with placeholders for the variables
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CV of {name}</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>{name}</h1>
        <p>Email: {email} | Tel: {phone}</p>
        <p> {website} | {location}</p>
    </header>

    <!-- Professional Profile -->
    <section id="professional-profile">
        <h2>Professional Profile</h2>
        <p>{professional_profile}</p>
    </section>

    <!-- Academic Background -->
    <section id="academic-background">
        <h2>Academic Background</h2>
        <ul>{academic_background}</ul>
    </section>

    <!-- Professional Experience -->
    <section id="professional-experience">
        <h2>Professional Experience</h2>
        {professional_experience}
    </section>

    <!-- Projects -->
    <section id="projects">
        <h2>Projects</h2>
        {projects}
    </section>

    <!-- Competences and Skills -->
    <section id="competences-skills">
        <h2>Competences and Skills</h2>
        <ul>{competences_skills}</ul>
    </section>

    <!-- Technical Knowledge -->
    <section id="technical-knowledge">
        <h2>Technical Knowledge</h2>
        <ul>{technical_knowledge}</ul>
    </section>

    <!-- Courses -->
    <section id="courses">
        <h2>Courses</h2>
        <ul>{courses}</ul>
    </section>

    <!-- Languages -->
    <section id="languages">
        <h2>Languages</h2>
        <ul>{languages}</ul>
    </section>

</body>
</html>"""

output_file_path = 'HTML/cv_template.html'

# Use the format method to insert the variables into the template
html_content = html_template.format(**cv_data)

# Write the HTML content to the file in the specified directory
with open(output_file_path, 'w') as file:
    file.write(html_content)

print(f"HTML file created successfully at {output_file_path}")