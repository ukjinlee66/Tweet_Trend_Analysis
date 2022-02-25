<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<c:set var="path" value="${pageContext.request.contextPath}" />
<%--

<!DOCTYPE html>
<html lang="ko">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tweet_Trend</title>
<script src="https://code.highcharts.com/highcharts.js"></script>
<link href="${path}/resources/css/customize.css" rel="stylesheet" />
</head>
<body>
	<div id="jb-container">
		<img src="img/logo2.png" width="10%" height="10%">
		<button onclick="tweetOn()">서버 ON</button>
		<button onclick="tweetOff()">서버 OFF</button>
		<div id="jb-header">
			<div class="mybox" align="center">
				<font size="5">대선</font>
				<span></span>
			</div>
			<div class="mybox" align="center">
				<font size="5">긍정</font>
				<span id="positive"></span>
			</div>
			<div class="mybox" align="center">
				<font size="5">중립</font>
				<span id="neutrality"></span>
			</div>
			<div class="mybox" align="center">
				<font size="5">부정</font>
				<span id="negative"></span>
			</div>
			<div class="mybox" align="center">
				<font size="5">총 데이터 수</font>
				<span id="total"></span>
			</div>
		</div>
		<div id="jb-content">
			<h3>List</h3>
			<hr>
			<div id="parent">
			</div>
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
		<div id="jb-content">
			<figure class="highcharts-figure">
				<div id="container"></div>
			</figure>
		</div>
		<div id="jb-footer">
			<p>Copyright 2022. (IlDa.)</p>
		</div>
		<!-- <button id="create" onClick="loadDoc()">new</button>
		<div id="increase"></div> -->
	</div>
	<script src="${path}/resources/js/statistic_count.js"></script>
	<script src="${path}/resources/js/customize_chart.js"></script>
	<script src="${path}/resources/js/original_content.js"></script>
	<script src="${path}/resources/js/controlSpark.js"></script>
</body> --%>


<!doctype html>
<html lang="ko">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://code.highcharts.com/highcharts.js"></script>
<link href="${path}/resources/css/customize.css" rel="stylesheet" />
<link href="${path}/resources/css/offcanvas.css" rel="stylesheet" />
<link href="${path}/resources/css/navbar.css" rel="stylesheet" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tweet_Trend</title>

<link rel="canonical"
	href="https://getbootstrap.com/docs/5.1/examples/navbars/">

<!-- Bootstrap core CSS -->
<link href="${path}/resources/css/bootstrap.min.css" rel="stylesheet">

<style>
.bd-placeholder-img {
	font-size: 1.125rem;
	text-anchor: middle;
	-webkit-user-select: none;
	-moz-user-select: none;
	user-select: none;
}

@media ( min-width : 768px) {
	.bd-placeholder-img-lg {
		font-size: 3.5rem;
	}
}
</style>

<!-- Custom styles for this template -->
</head>
<body>
	<main>
		<nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark"
			aria-label="First navbar example">
			<div class="container-fluid">
				<a class="navbar-brand" href="#"> <img src="img/logo2.png"
					width="5%" height="5%">
					<div
						class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
						<h1 class="h2">Dashboard</h1>
						<div
							class="d-flex align-items-center p-3 my-3 text-white rounded shadow-sm"
							id="positive" align="center" style="background-color: #0d6efd;"></div>
						<div
							class="d-flex align-items-center p-3 my-3 text-white rounded shadow-sm"
							id="neutrality" align="center" style="background-color: #adb5bd;"></div>
						<div
							class="d-flex align-items-center p-3 my-3 text-white rounded shadow-sm"
							id="negative" align="center" style="background-color: #dc3545;">
							</span>
						</div>
						<div
							class="d-flex align-items-center p-3 my-3 text-white rounded shadow-sm"
							id="total" align="center" style="background-color: #ffc107;"></div>
						<div class="btn-toolbar mb-2 mb-md-0"></div>
					</div>
				</a>
				<div class="d-grid gap-2 d-md-flex justify-content-md-end">
					<button type="button" class="btn btn-sm btn-outline-secondary">서버
						ON</button>
					<button type="button" class="btn btn-sm btn-outline-secondary">서버
						OFF</button>
				</div>
			</div>
		</nav>
		<div id="main">

			<div class="row mb-2">
				<div class="col-md-6">
					<div
						class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
						<div id="twitter_table" class="my-3 p-3 bg-body rounded shadow-sm"
							style="width: 100%">
							<div
								class="d-flex align-items-center p-3 my-3 text-white rounded shadow-sm"
								style="background-color: #1da1f2">
								<img class="me-3" src="img/twitter.png" alt="" width="48"
									height="38">
								<div class="lh-1">
									<h1 class="h6 mb-0 text-white lh-1">Twitter</h1>
								</div>
							</div>
							<h6 class="border-bottom pb-2 mb-0">Recent updates</h6>
							<div id="parent"></div>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div
						class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
						<figure class="highcharts-figure" style="width: 100%">
							<div id="container"></div>
						</figure>
					</div>
					<div
						class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
						<img id="wordcloud" src="img/wordcloud.png"
							style="width: 100%; height: 500px">
					</div>
				</div>
			</div>
		</div>
	</main>
	<div class="container">
		<footer class="py-3 my-4">
			<ul class="nav justify-content-center border-bottom pb-3 mb-3">
			</ul>
			<p class="text-center text-muted">&copy; 2022 Playdata, Illda</p>
		</footer>
	</div>
	<script src="${path}/resources/js/customize_chart.js"></script>
	<script src="${path}/resources/js/statistic_count.js"></script>
	<script src="${path}/resources/js/original_content.js"></script>
	<script src="${path}/resources/js/controlSpark.js"></script>
</body>
</html>




