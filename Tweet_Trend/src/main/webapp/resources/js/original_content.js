window.onload = function() {
	setInterval(async function() {
		var list_data = await loadList();
		var idx = list_data.length - 1;
		createDIV(list_data[idx]["content"], list_data[idx]["sentiment"], idx);
	}, 1000);
};

function createDIV(content, sentiment) {
	obj = document.getElementById("parent");
	newDiv = document.createElement("div");
	back_color = "#007bff";
	if (sentiment === "중립") {
		back_color = "#808080";
	}
	else if (sentiment === "부정") {
		back_color = "#dc3545";
	}
	newDiv.innerHTML = `<div id="abc" class="d-flex text-muted pt-3" data-aos="fade-right">
							<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
									width="32" height="32" xmlns="http://www.w3.org/2000/svg"
									role="img" aria-label="Placeholder: 32x32"
									preserveAspectRatio="xMidYMid slice" focusable="false">
									<rect width="100%" height="100%" fill="${back_color}"/></svg>
							<p class="pb-3 mb-0 small lh-sm border-bottom">${content}</p>
						</div>`
						
	child_len = obj.childElementCount
	if (child_len > 10) {
		obj.removeChild(obj.childNodes[10]);
	}
	if (obj.childNodes[0] !== undefined) {
		var c1 = content.replace(/(\s*)/g,"");
		var c2 = document.getElementsByClassName("pb-3 mb-0 small lh-sm border-bottom")[0].innerText.replace(/(\s*)/g, "");
		if (c1 !== c2) {
			obj.insertBefore(newDiv, obj.childNodes[0]);
			AOS.init({
				easing: 'ease-out-back',
				duration: 1000
			});
			hljs.initHighlightingOnLoad();
			$('.hero__scroll').on('click', function(e) {
				$('html, body').animate({
					scrollTop: $(window).height()
				}, 500);
			});
		}
	}
	else {
		obj.insertBefore(newDiv, obj.childNodes[0]);
		AOS.init({
			easing: 'ease-out-back',
			duration: 1000
		});
		hljs.initHighlightingOnLoad();
		$('.hero__scroll').on('click', function(e) {
			$('html, body').animate({
				scrollTop: $(window).height()
			}, 500);
		});
	}
}

loadList = () => {
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
		xhttp.open("GET", "v1/oricrawltbl", true);
		xhttp.send();
	});
}
