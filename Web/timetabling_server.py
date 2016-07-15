# Timetabling System Server
# Neeraj Chatlani and D.S. Myers, 2016

from flask import Flask
from flask import jsonify, request
import json

app = Flask(__name__)

# Global dictionary of course information
course_information = {}

@app.route('/')
def index():
    return app.send_static_file('timetabling_system.html')
    

# Creates new object entries for new course sections entered by a user
#
# Inputs from client:
#   A JSON string containing a list of new course names
#
# Effects;
#   Creates a new object to store information on each new course
#
# Returns:
#   Nothing
@app.route('/create_course_sections', methods = ['POST'])
def create_course_sections():
    
    # Unpack the name list from the request's JSON content
    content = request.get_json()
    sectionNames = content['names']
    
    # Create a new entry in the course_information for each new section name
    for name in sectionNames:
        name = name.encode('utf-8')
        if name not in course_information:
          course_information[name] = {}
          
    print course_information
          
    # The calling AJAX function expects valid JSON as message contents
    # Return null, which is parsed as valid JSON by the client
    return 'null'    

app.debug = True

if __name__ == '__main__':
    app.run()