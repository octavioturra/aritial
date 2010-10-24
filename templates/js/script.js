var loadPage = function(){
    var page = location.hash.replace("#","")||"home"
    var ajax = new Request.HTML({
        url: page,
        update: 'main',
        evalScripts: true,
        evalResponse: true,
        encoding: 'utf-8'
    })
    ajax.send();

}

window.addEvent('domready',function(){
    if(navigator.vendor!="Google Inc.")
    {
        document.write("ESTE É UM EXPERIMENTO GOOGLE CHROME.")
        document.write("<a href='http://chrome.google.com'>Google Chrome</a>")
    }
    loadPage();
    window.onhashchange = function(){
        loadPage();
    }
})
