function initMap() {
    // The location of Uluru
      var San_Marcos = {lat: 29.8884, lng: -97.9384};
      // The map, centered at Uluru
      var map = new google.maps.Map(
          document.getElementById('google_map'), {zoom: 15, center: San_Marcos});
      // The marker, positioned at Uluru
      var marker = new google.maps.Marker({position: San_Marcos, map: map});
}

// Funtion to Update Map to New Location Based on User Input.
function alterMap() {
    
}

$(document).ready(function () {
        $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});