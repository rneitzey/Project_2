// var myMap = L.map("map", {
//   center: [38.563891, -94.878246],
//   zoom: 8
// });

// L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//   attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
//   maxZoom: 8,
//   id: "mapbox.streets",
//   accessToken: API_KEY
// }).addTo(myMap);

d3.json('/data').then(response => {

  console.log(response);
});

//   var tornadoArray = [];

//   for (var i = 0; i < response.length; i++) {
//     var location = response[i];

//     if (location) {
//         tornadoArray.push([Start_Lat, Start_Lon]);
//     }
//   }

//   var heat = L.heatLayer(tornadoArray, {
//     radius: 20,
//     blur: 35
//   }).addTo(myMap);  

// });