function httpGET(url) {
		var xmlHttp = new XMLHttpRequest();
		xmlHttp.open("GET", url, true);	// false: wait respond
		xmlHttp.send(null);
		return url+" "+xmlHttp.responseText;
}
function saveSettings() {
		var url = "./cgi-bin/saveAuthConfig.cgi?" + document.getElementById('username').value + "\\" + document.getElementById('password').value;
		document.getElementById('info-div').innerHTML = httpGET(url);
}
