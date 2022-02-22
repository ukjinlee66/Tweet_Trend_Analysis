<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8">
    <title>Tweet_Trend</title>
    <meta name="viewport" content="width=device-width, initial-scale=0.5">
    <style>
      #jb-container {
        width: 940px;
        margin: 10px auto;
        padding: 20px;
        border: 1px solid #bcbcbc;
      }
      #jb-header {
        padding: 10px;
        margin-bottom: 10px;
        vertical-align: middle;
    	text-align: center;
        border: 1px solid #bcbcbc;
      }
      #jb-content {
        width: 580px;
        padding: 10px;
        margin-bottom: 10px;
        float: left;
        border: 1px solid #bcbcbc;
      }
      #jb-sidebar {
        width: 260px;
        padding: 10px;
        margin-bottom: 10px;
        float: right;
        border: 1px solid #bcbcbc;
      }
      #jb-footer {
        clear: both;
        padding: 10px;
        border: 1px solid #bcbcbc;
      }
      @media ( max-width: 480px ) 
      {
        #jb-container {
          width: auto;
        }
        #jb-content {
          float: none;
          width: auto;
        }
        #jb-sidebar {
          float: none;
          width: auto;
        }
      }
    </style>
    <style type="text/css">
    .mybox {
    	border:1.5px solid;
    	padding:10px;
    	border-radius : 5px;
    	width : 170px;
    	height : 60px;
    	background-color: #EBEBEB;
    	font-family:Nanum Gothic;
		display: inline-block;
    	width : 20%;
    }
	@import url(//fonts.googleapis.com/earlyaccess/jejumyeongjo.css);

	.jm-font{
		font-family: 'Jeju Myeongjo', serif;
		color: orange;
	}
    </style>
  </head>
  <body>
  
    <div id="jb-container">
      <img src="img/logo2.png" width="10%" height="10%">
      <div id="jb-header">
        	<div class="mybox" align="center" >
        		<font size="6" >
        			대선
        		</font>
        	</div>
        	<div class="mybox" align="center">
        	<font size="6" >
        		긍정 / 부정
        		</font>
        	</div>
        	<div class="mybox" align="center">
        	<font size="6" >
        		총 데이터 수 : 
        		</font>
        	</div>
      </div>
      <div id="jb-content">
        <h2>List</h2>
        List1<br>List2<br>List3<br>
	<button onclick="tweetOn()">서버 ON</button>
	<button onclick="tweetOff()">서버 OFF</button>
	<div id="books"></div>
	
	<script type="text/javascript">
	var workerId1="";
	var workerId2="";
	
	function tweetOn(){
		
		var params1 = { "appResource": "file:/home/hadoop/python3/tweet.py",
				  "sparkProperties": {
				    "spark.executor.memory": "1g",
				    "spark.master": "spark://192.168.56.100:7077",
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
				  "appArgs": [ "/home/hadoop/python3/tweet.py",  "80" ]}
		
		var params2 = { "appResource": "file:/home/hadoop/python3/senti.py",
				  "sparkProperties": {
				    "spark.executor.memory": "1g",
				    "spark.master": "spark://192.168.56.100:7077",
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
				  "appArgs": [ "/home/hadoop/python3/senti.py",  "80" ]}
				  		  
		
		var myParam1 = JSON.stringify(params1);
		var myParam2 = JSON.stringify(params2);
		
		const xhttp = new XMLHttpRequest(); 
		xhttp.onload = function() {
			
			
			var data = this.responseText;
			console.log(data);
			
			data = JSON.parse(data);
			console.log(data.submissionId+"실행");
			
			
			if(workerId1 ==""){
				workerId1 = data.submissionId;
			}
			else{
				workerId2 = data.submissionId;
			}
															
		}
		
		console.log(myParam1);
		
		xhttp.open("Post", "http://192.168.56.100:6066/v1/submissions/create", true); 
		xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
	    xhttp.send(myParam1); 
	
	    
	    setTimeout(function(){
			xhttp.open("Post", "http://192.168.56.100:6066/v1/submissions/create", true); 
			xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
		    xhttp.send(myParam2);
			console.log('works~!');
	    },5000);
	    //5초 후 함수 실행

	   // xhttp.open("Get", "http://34.64.240.227:6066/v1/submissions/status/driver-20220218024614-0000", true); 
		//xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
	   // xhttp.send(); 
		}
		
		function tweetOff(){
			const xhttp = new XMLHttpRequest(); 
			xhttp.onload = function() {
				var data = this.responseText;
				console.log(data);
			}
				
			xhttp.open("Post", "http://192.168.56.100:6066/v1/submissions/kill/"+workerId1, true); 
			xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
		    xhttp.send();
		    console.log(workerId1+"종료"); 
		    
		    setTimeout(function(){
				xhttp.open("Post", "http://192.168.56.100:6066/v1/submissions/kill/"+workerId2, true); 
				xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
			    xhttp.send();
				console.log(workerId2+"종료");
		    },3000);														
		}
	
		
	
	</script>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec mollis nulla. Phasellus lacinia tempus mauris eu laoreet. Proin gravida velit dictum dui consequat malesuada. Aenean et nibh eu purus scelerisque aliquet nec non justo. Aliquam vitae aliquet ipsum. Etiam condimentum varius purus ut ultricies. Mauris id odio pretium, sollicitudin sapien eget, adipiscing risus.</p>
      </div>
      <div id="jb-sidebar">
        <h2>ìë í´ë¼ì°ë ìëasdasd¦¬</h2>
        <ul>
          <li>Lorem</li>
          <li>Ipsum</li>
          <li>Dolor</li>
        </ul>
      </div>
      <div id="jb-sidebar">
        <h2>ë§ë ìë¦¬</h2>
        <ul>
          <li>Lorem</li>
          <li>Ipsum</li>
          <li>Dolor</li>
        </ul>
      </div>
      <div id="jb-footer">
        <p>Copyright 2022. (IlDa.)</p>
      </div>
    </div>
  </body>
</html>