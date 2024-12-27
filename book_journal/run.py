#The entry point, This is the main file to run the Flask app

import sys
import os

#add project root to python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from app import create_app



app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
