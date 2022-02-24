window.addEventListener = function() {
	setInterval(async function() {
		var cnt = await loadCount();
		console.log(cnt);
		changeDIV(cnt[0]["count"],cnt[1]["count"],cnt[1]["count"]);
	}, 1000);
};

function changeDIV(positive, negative, neutrality ) {
	pos = document.getElementById("positive");
	neg = document.getElementById("negative");
	neutral = document.getElementById("neutrality");
	
	pos.innerHTML = positive;
	neg.innerHTML = negative;
	neutral.innerHTML = neutrality;
	
}

loadCount = () => {
	return new Promise((resolve, reject) => {
		const xhttp = new XMLHttpRequest();
		xhttp.onload = () => {
			if (xhttp.status === 200) {
				data = xhttp.responseText;
				data = JSON.parse(data);
				resolve(data);
			}
			else {
				reject("Error");
			}
		};
		xhttp.open("GET", "v1/sentimenttbl", true);
		xhttp.send();
	});
}