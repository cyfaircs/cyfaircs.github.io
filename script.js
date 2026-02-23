// grab the ID for ease of use
const tabStart = document.getElementById("tab-start");
const tabProjects = document.getElementById("tab-projects");
const tabMembers = document.getElementById("tab-members");

// grab the pages for ease of use
const pageStart = document.getElementById("page-start");
const pageProjects = document.getElementById("page-projects");
const pageMembers = document.getElementById("page-members");

// dont know if we need these, just have them here in case
const tabs = [tabStart, tabProjects, tabMembers];
const pages = [pageStart, pageProjects, pageMembers]; 

// event Listeners
tabStart.addEventListener("click", function() {
  window.location.href = "index.html"
});

tabProjects.addEventListener("click", function() {
  window.location.href = "projects.html"
});

tabMembers.addEventListener("click", function() {
  window.location.href = "members.html"
});