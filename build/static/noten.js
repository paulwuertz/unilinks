//ließt URL Param
function gup( name, url ) {
    if (!url) url = location.href;
    name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+name+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( url );
    return results == null ? null : results[1];
}

//ließt url-Parameter um Session für den Nutzer zu wiederherzustellen
$(document).ready(function functionName() {
    //dekodiert die URL
    var noten=gup('noten', window.location.href)

    if(noten){
      noten=decodeURIComponent(noten)
      noten=noten.split(",")
      //setzt die Werte ein
      for (var i = 0; i < notenrows ; i++) {
          $("input#slider"+i).slider('setValue',parseFloat(noten[i]));
      }
    }
    //init usrURL input
    $("#usrURL").val(window.location.href)
});

//wenn eine Note geändert wird aktualisiere alle Reihen und Spalten
$("input.slider").on("change",function(){
  var sum=0,sumC=0;
  //url zum wiederherstellen
  var url=location.protocol + '//' + location.host + location.pathname+"?noten="
  var arr=[]

  //für alle Note
  for (var i = 0; i < notenrows ; i++) {
      //hohle Noten und Credits
      var note=$("input#slider"+i).slider('getValue');;
      var credits=parseInt($(".credits"+i).html());
      arr.push(note)
      if (note>4 || isNaN(note) || isNaN(credits)) {
          $("#mul"+i).val("")
      }
      //wenn das Fach gültig ist, also kleiner gleich 4
      else {
          sum+=note*credits
          sumC+=credits
          $("#mul"+i).val(note*credits)
      }
  }
  //aktualisiert die URL
  url+=encodeURIComponent(arr.toString())
  //setze Ergebnisse
  $("#usrURL").val(url)
  $("#sum").val(sum);
  $("#sumC").val(sumC)
  $("#res").val(sum/sumC)
});
