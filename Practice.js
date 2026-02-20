// Creates a variable that references the button named "practiceButton" in the HTML file.
const pButton = document.getElementById("practiceButton");

// Will be set to false when background is black
let current_color = true;

// This function will change the color of the button after it's pressed.
function bColor_Change() {
    pButton.style.color = "purple";
};

// This function will alternate the color for background of the page
function background_color() {
    if (current_color) {

        // When the function is first called, the current_color variable will be true,
        // so the background is changed to black. Then the variable is changed to false
        // so that the next time the button is pressed, the background will be changed to white.
        document.body.style.background = "black";
        current_color = !current_color;

    }
    else {

        document.body.style.background = "white";
        current_color = !current_color

    }
};