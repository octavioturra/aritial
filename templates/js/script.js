var loadPage = function(){
    var page = location.hash.replace("#","")||"home"
    var ajax = new Request.HTML({
        url: page,
        update: 'main',
        evalScripts: true,
        evalResponse: true
    })
    ajax.send();

}

window.addEvent('domready',function(){
    loadPage();
    window.onhashchange = function(){
        loadPage();
    }
})
