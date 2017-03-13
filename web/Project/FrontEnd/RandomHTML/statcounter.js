$(document).ready(function() {

    //Date slicing
    var date = new Date();
    var dateString = date.toString();
    dateString = dateString.substr(4, 11);

    //New thing, trying browser info stuff
    var queryString = "?touch=" + navigator.maxTouchPoints + "&os=" + navigator.appVersion + "&ref=" + document.referrer + "&host=" + document.location.host + "&path=" + document.location.pathname + "&width=" + window.screen.width + "&height=" + window.screen.height + "&date=" + dateString;

    var xhr1 = new XMLHttpRequest();
    xhr1.open("GET", "../../phpstuff/statcounterinfo.php" + queryString, true);

    xhr1.onreadystatechange = function() {
        if (xhr1.readyState == 4) {
            //document.write(xhr.responseText);
        }
    }

    xhr1.send();

    //onbeforeunload testing
    window.onbeforeunload = function() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "../../phpstuff/endtime.php", false);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                // do nothing
                alert("lol");
            }
        }
        alert("lol");
        xhr.send();
    }

})
