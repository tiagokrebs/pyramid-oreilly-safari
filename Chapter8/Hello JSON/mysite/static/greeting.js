$(document).ready(function () {
    $("#name").change(function () {
        var newValue = $("#name").val();
        $.ajax({
            method: "POST",
            url: "/greeting",
            data: JSON.stringify({name: newValue}),
            contentType: 'application/json; charset=utf-8'
        }).done(
            function (data) {
                $('#greeting').text(data.greeting);
            }
        );
    });
})
;
