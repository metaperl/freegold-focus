var bookmarkurl="http://ben.kbgoldintro.com/"
var bookmarktitle="KaratBars Intro"
function bookmark(){if(document.all)
window.external.AddFavorite(bookmarkurl,bookmarktitle)}
netscapeuser="First push OK and then hit CTRL+D to add a bookmark to this site."
if((navigator.appName=="Microsoft Internet Explorer")&&(parseInt(navigator.appVersion)>=4))
{document.write('<a href="javascript:bookmark()">Bookmark KaratBars Intro!</a>');}
else
document.write('&nbsp;<a href="javascript:alert(netscapeuser);">Bookmark This Page!</a>');