var changePage = function()
{
    var page = location.hash.replace("#","");
    var ajax = new Request.HTML({
        url: "/page?p="+page;
        update: "main"
    }).send();

}

window.addEvent('load',function(){
    
})
