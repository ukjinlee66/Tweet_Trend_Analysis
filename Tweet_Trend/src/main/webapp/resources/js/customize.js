var chart = Highcharts.chart('container', {
	chart: {
		type: 'column',
		events: {
			load: function() {
				// set up the updating of the chart each second

				setInterval(function() {
					var a = loadDoc();
					//var x = (new Date()).getTime(), // current time
					chart.series[0].setData([Math.random(), Math.random(), Math.random(), Math.random(), Math.random()], true, true);
					chart.series[1].setData([Math.random(), Math.random(), Math.random(), Math.random(), Math.random()], true, true);
					chart.series[2].setData([Math.random(), Math.random(), Math.random(), Math.random(), Math.random()], true, true);
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
		data: [1, 3, 4, 7, 2]
	}, {
		name: '중립',
		data: [2, 2, 3, 2, 1]
	}, {
		name: '부정',
		data: [3, 4, 4, 2, 5]
	}]
});

function loadDoc() {
	const xhttp = new XMLHttpRequest(); //매우 중요
	xhttp.onload = function() {   //매우 중요
		//f12 로 브라우저의 개발자 tool 실행후 콘솔창에서 확인 가능한 명령어
		//server 가 응답한 데이터는 순수 문자열로 받음
		//key(name)로 value값 활용하기 위해서는 문자열 -> JSON 객체로 변환		

		var data = this.responseText; //매우중요

		console.log(data);

		/* document : html 문서 자체를 제어하는 상위 객체
			getEleme	ntById("tag의 고유한 id(key)") : id값으로 해당 tag(element) 검색
			innerHTML : div와 p 라는 tag 내부에 html 형식을 추가 할수 있는 속성
			innerText : div와 p 라는 tag 내부 일반 text 추가 할수 있는 속성 */
		document.getElementById("increase").innerHTML = Math.random();
	}
	xhttp.open("GET", "hello", true); //매우 중요
	xhttp.send();  //매우 중요
}