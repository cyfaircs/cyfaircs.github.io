function toWhereToStart() {
  window.location.href = "wheretostart.html";
};

function toProjects() {
  window.location.href = "projects.html";
};

function toMembers() {
  window.location.href = "members.html";
};

function toHome() {
  window.location.href = "index.html";
};

function goBack() {
  if (window.history.length > 1) {
    window.history.back();
  } else {
    alert("No history found.");
  }
}

/* Code for a theme button:

let currentBackgroundColor = "black";

function changeBackground() {
  if (currentBackgroundColor === "black") {
    document.body.style.background = "white";
    currentBackgroundColor = "white";

  } else {
    document.body.style.background = "black";
    currentBackgroundColor = "black";
  }
} */