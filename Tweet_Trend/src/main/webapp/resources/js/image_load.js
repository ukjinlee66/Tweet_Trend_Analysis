window.addEventListener('load', function() {
	setInterval(function() {
		changeImage();
	}, 1000);
});

function changeImage(){
	document.getElementById("wordcloud").src = "img/wordcloud.png";
}