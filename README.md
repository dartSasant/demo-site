School Management System

A lightweight, responsive, and modern school website built using Flask for the backend and Tailwind CSS for a custom, utility-first UI.
Features

    Responsive Design: Fully optimized for mobile, tablet, and desktop views.

    Dynamic Routing: Flask-driven pages for Admissions, Academics, and Faculty.

    Tailwind UI: Clean, modern aesthetics without the heavy overhead of traditional CSS frameworks.

    Contact Forms: Integrated handling for parent and student inquiries.

Tech Stack
Component	Technology
Backend	Flask (Python)
Frontend	HTML5, Tailwind CSS
Templating	Jinja2


File Structure
├── app.py              # Main Flask application
├── static/             # Assets
│   ├── css/            # Compiled Tailwind CSS
│   └── images/         # School media and logos
├── templates/          # HTML files (Jinja2)
│   ├── base.html       # Main layout template
│   ├── index.html      # Homepage
│   └── about.html      # School history and vision
└── requirements.txt    # Python dependencies


1. Installation and Setup

Follow these steps to get the project running locally:


git clone https://github.com/dartSasant/demo-site.git
cd demo-site

2. Create a Virtual Environment
  python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. Install dependencies
pip install flask

4. Setup Tailwind CSS
If you are using the Tailwind CLI to compile your styles, use the following command to watch for changes:
npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --watch

5. Run the Application
python app.py

