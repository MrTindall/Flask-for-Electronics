function sendEventToServer(event, number = null) {
    fetch("/capture_event", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
            event: event,
            number: number
        }),
    })
    .then(response => response.json())
    .catch(error => console.error("Error:", error))
}


document.addEventListener("DOMContentLoaded", function(){
    const startButton = document.getElementById("startButton");
    const stopButton = document.getElementById("stopButton");
    const resetButton = document.getElementById("resetButton");
    const numberControl = document.getElementById("numberControl");
    
    startButton.addEventListener("click", function (e) {
        e.preventDefault();
        sendEventToServer("start");
    })

    stopButton.addEventListener("click", function (e) {
        e.preventDefault();
        sendEventToServer("stop");
    })

    resetButton.addEventListener("click", function(e) {
        e.preventDefault();
        sendEventToServer("reset", $("#numberControl").val());
        if (numberControl.value != "") {
            numberControl.value = "0";
        }
    })

    document.addEventListener("keydown", function (e) {
        if (e.key.toLowerCase() == "a") {
            sendEventToServer("left");
        }
        else if (e.key.toLowerCase() == "d") {
            sendEventToServer("right");
        }
        else if (e.key.toLowerCase() == "w") {
            sendEventToServer("up");
        }
        else if (e.key.toLowerCase() == "s") {
            sendEventToServer("down");
        }
    });
    document.addEventListener("keyup", function(e){
        if (e.key.toLowerCase() == "a" || e.key.toLowerCase() == "d" || e.key.toLowerCase() == "w" || e.key.toLowerCase() == "s") {
            sendEventToServer("stop");
        }
    })
})

$(function () {

    // Gets the cursor x and y position
    $("body").on("mouseover", function (e) {
        e.preventDefault();
        x = e.pageX;
        y = e.pageY;
    })

    // Button to submit IP address 
    // TODO get regex implemented
    $("#ipSubmitButton").on("click", function (e) {
            alert("IP Address is " + $("#ipInput").val())
    })

    // Toggle between light and dark mode
    $("#theme").on("change", function (e) {
        e.preventDefault();

        if ($(this).is(":checked") === false) {
            $("body").css("background-color", "rgb(220, 220, 220)");
            $(":root").css("--text-color", "rgb(50, 50, 50)");
            $("input").css("background-color", "white");
        }
        else {
            $("body").css("background-color", "#262626");
            $(":root").css("--text-color", "rgb(255, 255, 255)");
            $("input").css("background-color", "rgb(100, 100, 100)");
        }
    })

    // Increase and decrease button for the numeric input 
    $("#increaseButton").on("click", function (e) {
        let increaseNumVal = $("#numberControl").val();
        increaseNumVal++;
        $("#numberControl").val(increaseNumVal)
    })

    $("#decreaseButton").on("click", function (e) {
        let decreaseNumVal = $("#numberControl").val();
        decreaseNumVal--;
        $("#numberControl").val(decreaseNumVal)
    })





















    


})