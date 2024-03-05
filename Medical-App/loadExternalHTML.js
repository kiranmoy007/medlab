// loadExternalHTML.js
document.addEventListener("DOMContentLoaded", function () {
    var container = document.getElementById("external-content");
    var xhr = new XMLHttpRequest();
    
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
         
            container.innerHTML = xhr.responseText;
        }
    };
    
    xhr.open("GET", "about.html", true);
    xhr.send();
});



