// Timetabling System application control logic
// Neeraj Chatlani and D.S. Myers, 2016


// Creates new course sections
//
// Called when:
//   the Save button in the create course modal dialog is pressed.
//
// Effects:
//   Reads the appropriate fields from the modal dialog
//   Creates new list entries for each section (lecture and lab)
//   Inserts those list entries into the course listing
//   Sends information on the new sections to the server, which adds
//     entries for them to its data store
//   
// Inputs:
//   None
//
// Returns:
//   Nothing
function createCourseSections() {
  var coursePrefix = $("#dialog_course_prefix").val().toUpperCase();
  var courseNumber = $("#dialog_course_number").val();
  var numLectures = $("#dialog_num_lectures").val();
  var numLabs = $("#dialog_num_labs").val();
  
  // List of new section names
  var sectionNames = [];

  // Get a reference to the list of courses
  var sectionList = $("#list_of_created_courses");
    
  // Create <li> items for the lecture sections
  for (var i = 0; i < numLectures; i++) {    
    var sectionName = coursePrefix + " " + courseNumber + " - Lecture " + (i + 1);
    sectionNames.push(sectionName);
    
    var newListNode = document.createElement("li");
    newListNode.classList.add("list-group-item");
    var newTextNode = document.createTextNode(sectionName)
    
    newListNode.appendChild(newTextNode);
    sectionList.append(newListNode);
  }
  
  // Create <li> items for the lab sections
  for (var i = 0; i < numLabs; i++) {    
    var sectionName = coursePrefix + " " + courseNumber + " - Lab " + (i + 1);
    sectionNames.push(sectionName);
    
    var newListNode = document.createElement("li");
    newListNode.classList.add("list-group-item");
    var newTextNode = document.createTextNode(sectionName)
    
    newListNode.appendChild(newTextNode);
    sectionList.append(newListNode);
  }
  
  // Create an object with section names as its fields
  var courseSections = {"names" : sectionNames};
  
  // Send an update to the server with the new section names
  $.ajax({
    url: '/create_course_sections',
    type: 'POST',
    contentType:'application/json',
    data: JSON.stringify(courseSections),
    dataType:'json',
    success: function() {
      alert('Done!');
    },
    error: function() {
      alert("Error!");
    }
  });
  
}