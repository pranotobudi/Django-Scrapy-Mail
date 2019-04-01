$(document).ready(function() {
    $(".message").html("BISMILLAH");
});
$('#my-form').submit(function(e){
    $.post('/scraping-process/', $(this).serialize(), function(data){
        alert(data)
        var json = JSON.parse(data);
       $('.message').html(json.message);
       $('#id_website_lists').val(json.message);

       var bar = document.getElementById("progress-bar");
       var barMessage = document.getElementById("progress-bar-message");
   
       for (var i = 0; i < 11; i++) {
        setTimeout(updateProgress_basic, 500 * i, bar, barMessage, {
        percent: 10 * i,
        current: 10 * i,
        total: 100
        })
    }
       
       // of course you can do something more fancy with your respone
    });
    e.preventDefault();
});

function updateProgress_basic(progressBarElement, progressBarMessageElement, progress) {
    progressBarElement.style.width = progress.percent + "%";
    progressBarMessageElement.innerHTML = progress.current + ' of ' + progress.total + ' processed.';
  }
  
// var trigger = document.getElementById('progress-bar-trigger');
// trigger.addEventListener('click', function(e) {
//     var bar = document.getElementById("progress-bar");
//     var barMessage = document.getElementById("progress-bar-message");
//     for (var i = 0; i < 11; i++) {
//         setTimeout(updateProgress_basic, 500 * i, bar, barMessage, {
//         percent: 10 * i,
//         current: 10 * i,
//         total: 100
//         })
//     }
// })


