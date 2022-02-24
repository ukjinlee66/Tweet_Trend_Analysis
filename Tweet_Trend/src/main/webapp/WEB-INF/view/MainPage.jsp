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
<link href="navbar.css" rel="stylesheet">
</head>
<body>
	<main>
		<nav class="navbar navbar-dark bg-dark"
			aria-label="First navbar example">
			<div class="container-fluid">
				<a class="navbar-brand" href="#">Never expand</a>
				<div class="d-grid gap-2 d-md-flex justify-content-md-end">
					<button class="btn btn-primary me-md-2" type="button">Button</button>
					<button class="btn btn-primary" type="button">Button</button>
					<button type="button" class="btn btn-primary">Primary</button>
					<button type="button" class="btn btn-secondary">Secondary</button>
					<button type="button" class="btn btn-success">Success</button>
					<button type="button" class="btn btn-danger">Danger</button>
					<button type="button" class="btn btn-warning">Warning</button>
					<button type="button" class="btn btn-info">Info</button>
					<button type="button" class="btn btn-light">Light</button>
					<button type="button" class="btn btn-dark">Dark</button>
					<button type="button" class="btn btn-sm btn-outline-secondary">Share</button>
					<button type="button" class="btn btn-sm btn-outline-secondary">Export</button>
				</div>
			</div>
		</nav>
		<div id="jb-main"
			class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
			<h1 class="h2">Dashboard</h1>
			<div id="positive" align="center">긍정 :</div>
			<div id="neutrality" align="center">중립 :</div>
			<div id="negative" align="center">부정 :</div>
			<div id="total" align="center">총 데이터 :</div>
			<div class="btn-toolbar mb-2 mb-md-0"></div>
		</div>

		<figure class="highcharts-figure">
			<div id="container"></div>
		</figure>

		<div
			class="d-flex align-items-center p-3 my-3 text-white bg-purple rounded shadow-sm">
			<div class="lh-1">
				<h1 class="h6 mb-0 text-white lh-1">Bootstrap</h1>
				<small>Since 2011</small>
			</div>
		</div>

		<div class="my-3 p-3 bg-body rounded shadow-sm">
			<h6 class="border-bottom pb-2 mb-0">Recent updates</h6>
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="32" height="32" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 32x32"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>Placeholder</title><rect width="100%" height="100%"
						fill="#007bff" />
					<text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>

				<p class="pb-3 mb-0 small lh-sm border-bottom">
					<strong class="d-block text-gray-dark">@username</strong> Some
					representative placeholder content, with some information about
					this user. Imagine this being some sort of status update, perhaps?
				</p>
			</div>
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="32" height="32" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 32x32"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>Placeholder</title><rect width="100%" height="100%"
						fill="#e83e8c" />
					<text x="50%" y="50%" fill="#e83e8c" dy=".3em">32x32</text></svg>

				<p class="pb-3 mb-0 small lh-sm border-bottom">
					<strong class="d-block text-gray-dark">@username</strong> Some more
					representative placeholder content, related to this other user.
					Another status update, perhaps.
				</p>
			</div>
			<div class="d-flex text-muted pt-3">
				<svg class="bd-placeholder-img flex-shrink-0 me-2 rounded"
					width="32" height="32" xmlns="http://www.w3.org/2000/svg"
					role="img" aria-label="Placeholder: 32x32"
					preserveAspectRatio="xMidYMid slice" focusable="false">
					<title>Placeholder</title><rect width="100%" height="100%"
						fill="#6f42c1" />
					<text x="50%" y="50%" fill="#6f42c1" dy=".3em">32x32</text></svg>

				<p class="pb-3 mb-0 small lh-sm border-bottom">
					<strong class="d-block text-gray-dark">@username</strong> This user
					also gets some representative placeholder content. Maybe they did
					something interesting, and you really want to highlight this in the
					recent updates.
				</p>
			</div>
		</div>
		<script src="${path}/sources/js/bootstrap.bundle.min.js"></script>
		<script src="${path}/resources/js/customize_chart.js"></script>
		<script src="${path}/resources/js/statistic_count.js"></script>
		<script src="${path}/resources/js/original_content.js"></script>
		<script src="${path}/resources/js/controlSpark.js"></script>
</body>
</html>




