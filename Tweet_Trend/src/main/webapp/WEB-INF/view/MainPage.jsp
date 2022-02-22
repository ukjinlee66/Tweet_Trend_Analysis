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
	<button onclick="loadDoc()">실행</button>
	<div id="books"></div>
	
	<script type="text/javascript">
	
		function loadDoc() {
			//요청 객체 생성
			//기능 : 비동기로 요청하고 응답된 데이터 받을 수 있는 객체
			//특징 : 요청중이니? 응답중인지? 응답완료? 다 파악 가능
		  	const xhttp = new XMLHttpRequest(); // 매우중요
			
		  //응답이 오면 자동 실행되는 함수
			/*	개발 형식 - 응답을 감지하는 속성에 익명함수 등록
			*	응답이 되기는 하나 언제 정확히 몇시 몇분에 응답에 대한보장은 불가
			*	개발 코드는 응답 오면을 기준으로 실행될수 있게 등록
			*		- 콜백함수
			*/
			
		  xhttp.onload = function() {//매우 중요
			//f12 로 브라우저의 개발자 tool 실행후 콘솔창에서 확인 가능한 명령어
			//server 가 응답한 데이터는 순수 문자열로 받음
			//key(name)로 value값 활용하기 위해서는 문자열 -> JSON 객체로 변환 ()
			
			var data = this.reponseText; //매우 중요
			console.log(data);
			console.log(data[0]);
			console.log(data[1]);
			console.log(data[2]);
			
			data = JSON.parse(data);
			console.log(data[0]);
			console.log(data[0].title);
			
			/* document : html 문서 자체를 제어하는 상위 객체
			* getElementById("tag의 고유한 id(key)") : id 값으로 해당 tag(element)검색
			* innerHTML : div와 p 라는 tag 내부에 html 형식을 추가 할 수 있는 속성
			* innerTEXT : div와 p 라는 tag 내부 일반 text 추가 할 수 있는 속성
			*/
			
		    //document.getElementById("books").innerHTML = data[1].title;
		    }
		  
			//server의 어떤 프로그램(url, 요청 방식, true(비동기의미))
			//http://ip:port/getname 로 요청이라 간주
			//자원 설정
		  	xhttp.open("GET", "books", true);//매우 중요
			
			//실제 요청
		  	xhttp.send();
			
			
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