/**
	JS
*/
hljs.initHighlightingOnLoad();

// var elements = []
// elements.push("devops")
// elements.push("jenkins")
// elements.push("nexus")
// elements.push("bitbucket")
// elements.push("sonarqube")
// elements.push("sonatype")
// elements.push("veracode")
// elements.push("linux")
// elements.push("windows")
// elements.push("sharepoint")
// elements.push("aboutme")
// elements.push("kubernetes")

// function show_only_this_elem(param) {
//     for (i in elements) {
//     	$("div[id^='"+elements[i]+"']").hide()
//     }
//     $("div[id^='"+param+"']").show()
// }


/**
	LINKEDIN
*/

// var liLogin = function() { // Setup an event listener to make an API call once auth is complete
//     IN.UI.Authorize().params({"scope":["r_basicprofile", "r_emailaddress"]}).place();
//     IN.Event.on(IN, 'auth', getProfileData);
// }

// function send_get_request(url) {
// 	$.get(url, function(data, status) {
// 		console.log(data)
// 	})
// }

// function send_post_request(url, body) {
// 	$.post(url, body, function(data, status) {
// 		console.log(data)
// 	})
// }

// function onLinkedInLoad() {
// 	console.log("onLinkedInLoad called")
// 	IN.Event.on(IN, "auth", getProfileData)
// 	IN.Event.on(IN, "logout", sendGoodByeMessage)
// }

// function get() {
// 	IN.Event.on(IN, "auth", getProfileData)
// }

// function getProfileData() {
// 	console.log("inside getProfileData")
// 	if (IN.User.isAuthorized()) {
// 		IN.API.Raw("/people/~").result(onSuccess).error(onError)
// 	} else {
// 		console.log("user is not authorized")
// 	}
// }

// function onSuccess(data) {
// 	console.log(data)
// }

// function onError(error) {
// 	console.log(error)
// }

// send_get_request("https://api.linkedin.com/v2/me")


// var body = {
// 	headers: {

// 	},
// 	body: request_body,
// 	method: "POST"
// }

// function send_request(url, body) {
// 	fetch(url, body).then(data=>{return data.json()}).then(res=>{console.log(res)}).catch(error=>console.log(error))
// }