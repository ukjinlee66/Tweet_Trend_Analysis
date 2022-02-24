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
	newDiv.innerHTML = content+","+sentiment;
	newDiv.setAttribute("id", "myDiv"); // 새롭게 만들어지는 div 태그에 id 값 저장
	newDiv.style.backgroundColor = "grey";

	child_len = obj.childElementCount
	if(child_len>5){
		obj.removeChild(obj.childNodes[5]);
	}
	obj.insertBefore(newDiv,obj.childNodes[0]);
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