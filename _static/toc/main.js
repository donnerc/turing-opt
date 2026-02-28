$(document).ready(function () {
    var headers = $(".contents.topic > ul > li > ul")[0];
    $(".contents.topic > ul").hide();
    $(".contents.topic").append(headers);
});
