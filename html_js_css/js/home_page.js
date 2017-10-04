/**
 * Created by lenovo on 2017/9/13.
 */


function initNav(){
    var nav_li_a = $('#home_page_nav li a');
    for (var i = 0,len = nav_li_a.length; i < len; i++)
    {
        var a = nav_li_a[i];
        a.className = 'nav_li';
        a.style.fontSize = '20px';
    }
}
function font2Max(e){
    if ('nav_li' === e.target.className)
    {
        e.target.style.fontSize = '50px';
    }
}

function font2Min(e){
    if ('nav_li' === e.target.className)
    {
        e.target.style.fontSize = '20px';
    }
}

function main(){
    initNav();
    document.addEventListener('mouseover',font2Max);
    document.addEventListener('mouseout',font2Min);
}
$(document).ready(main);