window.onload = function() {
	setInterval(async function() {
		var list_data = await loadList();
		var idx = list_data.length-1;
		console.log(list_data);
		createDIV(list_data[idx]["content"],list_data[idx]["sentiment"],idx);
	}, 1000);
};

function createDIV(content, sentiment) {
	obj = document.getElementById("parent");
	newDiv = document.createElement("div");
	console.log(sentiment);
	back_color = "#007bff";
	if(sentiment==="중립"){
		back_color = "#adb5bd";
	}
	else if(sentiment==="부정"){
		back_color = "#dc3545";
	}
	newDiv.innerHTML = `<div class="d-flex text-muted pt-3">
								<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
									width="32" height="32" xmlns="http://www.w3.org/2000/svg"
									role="img" aria-label="Placeholder: 32x32"
									preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%"
										fill="${back_color}"/></svg>
								<p class="pb-3 mb-0 small lh-sm border-bottom">
									<strong class="d-block text-gray-dark">@username</strong>${content}
								</p>
							</div>`
	child_len = obj.childElementCount
	if(child_len>10){
		obj.removeChild(obj.childNodes[9]);
	}
	if(obj.childNodes[0]!=undefined){
		if(obj.childNodes[0].innerHTML!==content){
			console.log(obj.childNodes[0].innerHTML);
			console.log(content);
			obj.insertBefore(newDiv,obj.childNodes[0]);
		}
	}
	else{
		obj.insertBefore(newDiv,obj.childNodes[0]);
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
