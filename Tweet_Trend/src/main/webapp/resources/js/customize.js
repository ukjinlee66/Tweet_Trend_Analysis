Highcharts.chart('container', {
	chart: {
		type: 'column'
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
		data: [5, 3, 4, 7, 2]
	}, {
		name: '중립',
		data: [2, 2, 3, 2, 1]
	}, {
		name: '부정',
		data: [3, 4, 4, 2, 5]
	}]
});