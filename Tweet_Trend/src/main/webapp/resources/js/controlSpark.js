var workerId1 = "";
var workerId2 = "";

function tweetOn() {
	btn = document.getElementById("button");
	btn.innerHTML = "서버 OFF";
	btn.setAttribute("onclick","tweetOff();");
	
	var params1 = {
		"appResource": "file:/home/hadoop/python/tweetServer.py",
		"sparkProperties": {
			"spark.executor.memory": "1g",
			"spark.master": "spark://34.64.240.227:7077",
			"spark.driver.memory": "1g",
			"spark.driver.cores": "1",
			"spark.eventLog.enabled": "false",
			"spark.app.name": "Spark REST API - PI",
			"spark.submit.deployMode": "cluster",
			"spark.driver.supervise": "true"
		},
		"clientSparkVersion": "3.1.2",
		"mainClass": "org.apache.spark.deploy.SparkSubmit",
		"environmentVariables": {
			"SPARK_ENV_LOADED": "1"
		},
		"action": "CreateSubmissionRequest",
		"appArgs": ["/home/hadoop/python/tweetServer.py", "80"]
	}

	var params2 = {
		"appResource": "file:/home/hadoop/python/sentiment_analysis.py",
		"sparkProperties": {
			"spark.executor.memory": "1g",
			"spark.master": "spark://34.64.240.227:7077",
			"spark.driver.memory": "1g",
			"spark.driver.cores": "1",
			"spark.eventLog.enabled": "false",
			"spark.app.name": "Spark REST API - PI",
			"spark.submit.deployMode": "cluster",
			"spark.driver.supervise": "true"
		},
		"clientSparkVersion": "3.1.2",
		"mainClass": "org.apache.spark.deploy.SparkSubmit",
		"environmentVariables": {
			"SPARK_ENV_LOADED": "1"
		},
		"action": "CreateSubmissionRequest",
		"appArgs": ["/home/hadoop/python/sentiment_analysis.py", "80"]
	}

	var myParam1 = JSON.stringify(params1);
	var myParam2 = JSON.stringify(params2);

	const xhttp = new XMLHttpRequest();
	xhttp.onload = function() {

		var data = this.responseText;
		console.log(data);

		data = JSON.parse(data);
		console.log(data.submissionId + "실행");

		if (workerId1 == "") {
			workerId1 = data.submissionId;
		} else {
			workerId2 = data.submissionId;
		}

	}

	console.log(myParam1);

	xhttp.open("Post",
		"http://34.64.240.227:6066/v1/submissions/create",
		true);
	xhttp.setRequestHeader("Content-type",
		"application/json;charset=UTF-8");
	xhttp.send(myParam1);

	setTimeout(
		function() {
			xhttp
				.open(
					"Post",
					"http://34.64.240.227:6066/v1/submissions/create",
					true);
			xhttp.setRequestHeader("Content-type",
				"application/json;charset=UTF-8");
			xhttp.send(myParam2);
		}, 10000);
	//10초 후 함수 실행
 
}

function tweetOff() {
	btn = document.getElementById("button");
	btn.innerHTML = "서버 On";
	btn.setAttribute("onclick","tweetOn();");

	const xhttp = new XMLHttpRequest();
	xhttp.onload = function() {
		var data = this.responseText;
		console.log(data);
	}

	xhttp.open("Post",
		"http://34.64.240.227:6066/v1/submissions/kill/"
		+ workerId1, true);
	xhttp.setRequestHeader("Content-type",
		"application/json;charset=UTF-8");
	xhttp.send();
	console.log(workerId1 + "종료");

	setTimeout(function() {
		xhttp.open("Post",
			"http://34.64.240.227:6066/v1/submissions/kill/"
			+ workerId2, true);
		xhttp.setRequestHeader("Content-type",
			"application/json;charset=UTF-8");
		xhttp.send();
		console.log(workerId2 + "종료");
	}, 3000);

}
