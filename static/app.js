function getBHKValue() {
    var bhkRadios = document.getElementsByName("uiBHK");
    for (var i = 0; i < bhkRadios.length; i++) {
        if (bhkRadios[i].checked) {
            return parseInt(bhkRadios[i].value);
        }
    }
    return 1; // Default value
}

function getBathValue() {
    var bathRadios = document.getElementsByName("uiBathrooms");
    for (var i = 0; i < bathRadios.length; i++) {
        if (bathRadios[i].checked) {
            return parseInt(bathRadios[i].value);
        }
    }
    return 1; // Default value
}

function onClickedEstimatePrice() {
    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    // Use relative URL (works locally + on Render)
    var url = "/predict_home_price";

    $.ajax({
        url: url,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            location: location,
            sqft: parseFloat(sqft),
            bhk: bhk,
            bath: bathrooms
        }),
        success: function(data) {
            if (data.estimated_price) {
                estPrice.innerHTML = `<h2>Estimated Price: ${data.estimated_price} Lakh</h2>`;
            } else {
                estPrice.innerHTML = "<h2 style='color: red;'>Error fetching price</h2>";
                console.error("Invalid response from server:", data);
            }
        },
        error: function(xhr, status, error) {
            estPrice.innerHTML = "<h2 style='color: red;'>Error fetching price</h2>";
            console.error("Error fetching price:", error);
            console.error("Server Response:", xhr.responseText);
        }
    });
}

function loadLocations() {
    // Use relative URL
    var url = "/get_location_names";

    $.get(url, function(data, status) {
        if (data && data.locations) {
            var locationSelect = document.getElementById("uiLocations");
            locationSelect.innerHTML = "";

            data.locations.forEach(function(location) {
                var option = document.createElement("option");
                option.text = location;
                locationSelect.add(option);
            });
        } else {
            console.error("Error loading location names:", data);
        }
    }).fail(function(xhr, status, error) {
        console.error("Failed to load locations:", error);
    });
}

// Load locations on page load
window.onload = loadLocations;
