var chart = Highcharts.chart('container', {
	chart: {
		type: 'column',
		events: {
			load: function() {
				// set up the updating of the chart each second
				setInterval(async function() {
					var graph_data = await loadDoc();
					console.log(graph_data);
					for(var i=0; i<graph_data.length; i++){
						chart.series[i].setData([graph_data[i]["ljmcnt"], graph_data[i]["ysycnt"], graph_data[i]["acscnt"], graph_data[i]["ssjcnt"], graph_data[i]["hgycnt"]], true, true);
					}
				}, 1000);
			}
		}
	},
	title: {
		text: '대선 후보들에 대한 SNS 반응'
	},
	xAxis: {
		categories: ['이재명', '윤석열', '안철수', '심상정', '허경영']
	},
	yAxis: {
		min: 0,
		title: {
			text: '감정 분석'
		}
	},
	tooltip: {
		pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
		shared: true
	},
	plotOptions: {
		column: {
			stacking: 'percent'
		}
	},
	series: [{
		name: '긍정',
		data: [0, 0, 0, 0, 0]
	}, {
		name: '중립',
		data: [0, 0, 0, 0, 0]
	}, {
		name: '부정',
		data: [0, 0, 0, 0, 0]
	}]
});

loadDoc = () => {
	return new Promise((resolve,reject) => {
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
		xhttp.open("GET", "v1/canditbl", true);
		xhttp.send();
	});
}

/*
function loadDoc() {
	const xhttp = new XMLHttpRequest(); //매우 중요
	xhttp.onload = function() {   //매우 중요å
		var data = this.responseText; //매우중요
		return data;
	}
	xhttp.open("GET", "hello", true); //매우 중요
	xhttp.send();  //매우 중요
}
*/
