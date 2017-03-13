$(document).ready(function(){

    //New thing, trying browser info stuff
    var queryString = "?touch=" + navigator.maxTouchPoints + "&os=" + navigator.appVersion + "&ref=" + document.referrer + "&host=" + document.location.host + "&path=" + document.location.pathname ;

    var xhr1 = new XMLHttpRequest();
    xhr1.open("GET", "../../phpstuff/info.php" + queryString, true);

    xhr1.onreadystatechange = function(){
        if(xhr1.readyState==4){
            //document.write(xhr.responseText);
        }
    }

    xhr1.send();
})
