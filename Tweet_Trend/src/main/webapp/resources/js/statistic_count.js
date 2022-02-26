window.addEventListener('load', function() {
	setInterval(async function() {
		var cnt = await loadCount();
		console.log(cnt);
		changeDIV(cnt[0]["count"],cnt[1]["count"],cnt[2]["count"]);
	}, 1000);
});

function changeDIV(positive, negative, neutrality) {
	pos = document.getElementById("positive");
	neg = document.getElementById("negative");
	neutral = document.getElementById("neutrality");
	total = document.getElementById("total");
	
	pos.innerHTML = "긍정 : " + positive;
	neg.innerHTML = "부정 : " + negative;
	neutral.innerHTML = "중립 : " + neutrality;
	total.innerHTML = "총 데이터 수 : " + String(0+positive+negative+neutrality);
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

