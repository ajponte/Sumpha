/** Functions to get RESTful API data.
 *  @author Alan Ponte
 */

$(document).ready(function() {
	$('#randoBtn').on('click', function() {
		var query = ($('#search').val());
		var data = getDataFromQuery("san+francisco", "ca", query);
	});
	$('#eventsDiv').text("test");

});


/** Given a String QUERY, parsers the QUERY 
 *  and searches the different REST APIs
 *  to get JSON data representations of 
 *  events in the CITY and STATE. */
 function getDataFromQuery(city, state, query) {
 	var meetupData = getMeetupData(city, state, query);
 	//var eventBriteData = getEventBriteData(city, state, query);

 }

/** Given the QUERY, searches the RESTful API
 *  for meetup.com for a QUERY which matches 
 *  in the CITY and STATE. */ 
 function getMeetupData(city, state, query) {
 	var jsonData = null;
 	var url = "http://api.meetup.com/2/open_events?status=upcoming&radius=25.0&state=" + 
 		state + "&and_text=False&limited_events=False&text=" +
 		query + "&desc=False&city=" + city + 
 		"&offset=0&photo-host=public&format=json&page=20&country=us&sig_id=14329201&sig=e31eef1653769211053be6849d5285b63f0593f6";
 	$.getJSON(url, function(data) {
 		jsonData = data;
 		console.log(data);
 	});
 	//alert(jsonData);
 }

 function writeToFile(d1, d2){
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    var fh = fso.OpenTextFile("data.txt", 8, false, 0);
    fh.WriteLine(d1 + ',' + d2);
    fh.Close();
}
var submit = document.getElementById("submit");
submit.onclick = function () {
    var id      = document.getElementById("id").value;
    var content = document.getElementById("content").value;
    writeToFile(id, content);
}
