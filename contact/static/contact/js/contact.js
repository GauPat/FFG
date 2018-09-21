/* exported initContatLocationAndApproach */

///**
// * Initializes a regular google map.
// */
//function regularMap() {
//    var varLocation = new google.maps.LatLng(50.9780463, 6.8841171);
//
//    var varMapoptions = {
//        center: varLocation,
//        zoom: 14
//    };
//
//    var varMap = new google.maps.Map(document.getElementById("map-container-5"),
//        varMapoptions);
//
//    var varMarker = new google.maps.Marker({
//        position: varLocation,
//        map: varMap,
//        title: "Butzweilerhof"
//    });
//}
//
///**
// * init functionn to set up the google map.
// */
//function initContatLocationAndApproach() {
//	google.maps.event.addDomListener(window, 'load', regularMap);
//}

function initMap() {
  varMap = new google.maps.Map(document.getElementById('google-map'), {
    center: {lat: 50.9780463, lng: 6.8841171},
    zoom: 12,
  });
  
  var varMarker = new google.maps.Marker({
	position: varLocation,
	map: varMap,
	title: "Butzweilerhof"
  });
}

/**
* init functionn to set up the google map.
*/
function initContatLocationAndApproach() {
  initMap();
}