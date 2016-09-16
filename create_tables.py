from timetabling_server import db
from timetabling_server import Section, Instructor, Room, AcceptableRoom, Timeslot, AcceptableTimeslot, Conflict

def populate_tables():
    db.create_all()
    print db

    db.session.add(Instructor('Myers, Daniel S.'))
    db.session.add(Instructor('Anderson, Mark'))
    db.session.add(Instructor('Carrington, Julie'))
    db.session.add(Instructor('Anderson, Julie A.'))
    db.session.add(Instructor('Summet, Valerie'))
    db.session.add(Instructor('Vitray, Rick'))
    db.session.add(Instructor('Yellen, Jay'))
    db.session.add(Instructor('Teymuroglu, Zeynep'))
    db.session.add(Instructor('Rejniak, Gabriel'))
    db.session.add(Instructor('Boyd, Sheri'))

    db.session.add(Room('BUSH', '123'))
    db.session.add(Room('BUSH', '202'))
    db.session.add(Room('BUSH', '206'))
    db.session.add(Room('BUSH', '301'))
    db.session.add(Room('BUSH', '310'))
    db.session.add(Room('CSS', '100'))
    db.session.add(Room('KEENE', '101'))
    
    # On-matrix timeslots
    
    # MWF 50 minutes
    db.session.add(Timeslot('MWF 8:00 - 8:50', 'MWF for 50 minutes', '8:00', '8:50',
                            '', '', '8:00', '8:50', '', '', '8:00', '8:50'))
    db.session.add(Timeslot('MWF 10:00 - 10:50', 'MWF for 50 minutes', '10:00', '10:50',
                            '', '', '10:00', '10:50', '', '', '10:00', '10:50'))
    db.session.add(Timeslot('MWF 11:00 - 11:50', 'MWF for 50 minutes', '11:00', '11:50',
                            '', '', '11:00', '11:50', '', '', '11:00', '11:50'))
                            
    # TR 75 minutes
    db.session.add(Timeslot('TR 11:00 - 12:15', 'TR for 75 minutes', '', '',
                            '11:00', '12:15', '', '', '11:00', '12:15', '', ''))
    db.session.add(Timeslot('TR 14:00 - 15:15', 'TR for 75 minutes', '', '',
                            '14:00', '15:15', '', '', '14:00', '15:15', '', ''))
    db.session.add(Timeslot('TR 15:30 - 16:45', 'TR for 75 minutes', '', '',
                            '15:30', '16:45', '', '', '15:30', '16:45', '', ''))
                            
    # MW 75 minutes
    db.session.add(Timeslot('MW 13:00 - 14:15', 'MW for 75 minutes', '13:00', '14:15',
                            '', '', '13:00', '14:15', '', '', '', ''))
    db.session.add(Timeslot('MW 14:30 - 15:45', 'MW for 75 minutes', '14:30', '15:45',
                            '', '', '14:30', '15:45', '', '', '', ''))


    db.session.commit()
    
    teachers = Instructor.query.all()
    print teachers
    places = Room.query.all()
    print places
    
if __name__ == '__main__':
    populate_tables()