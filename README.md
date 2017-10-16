# Prototype Class Course Scheduling Application
This project was a prototype application designed for creating a college course list with course details and full schedules that avoid as much conflict as possible. Avoiding 'conflict' refers to avoiding situations such as assigning courses taught by the same instructor to the same timeslot, assigning two courses to the same room at the same time, or assigning courses with high-student overlap at the same time.

Constructing course timetables for universities and colleges is a challenging problem that requires balancing instructor and student preferences while avoiding conflicts. Previous work by Dr. Jay Yellen at Rollins College resulted in a time-tabling approach that is based on a weighted-graph model, where each graph edge has a two-component weight corresponding to the two objectives— minimizing conflict and creating compact schedules. 

Our goal was to create a web application with a user-friendly interface for implementation of the time-tabling system. The system was designed with 3 major goals in mind:

* Input courses into the system and add each course section’s information. Each course has its own number of sections or labs, each of which have separate timeslots and possible rooms, instructors, and possible course conflicts. We allow for each of these per section and store all the course information in the database.

* Schedule the courses quickly and easily once course information is input.

* Allow for post-scheduling editing in order to handle any significant conflicts that arise from the use of the time-tabling algorithm. This is also useful in case any changes arise depending on instructor preferences or other similar external circumstances.

## Implementation
This application is a full web application written using Flask, a Python microframework. The database of courses and schedules is maintained using SQLAlchemy, a Flask SQL plugin. The front-end interface is written in HTML and JavaScript. The Bootstrap framework is used for the application layout and styling.

## Authors
This application was created by Neeraj Chatlani and [Dan Myers](http://dansmyers.github.io) at [Rollins College](http://www.rollins.edu) as part of the Rollins College Student-Faculty Collaborative Research Program.
