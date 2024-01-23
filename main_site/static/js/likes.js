function add_like(id) {
    $.ajax({
        url: "/add_like/" + id.toString() + '/',
        success: function(){
            $('#likes').innerHTML = (parseInt(($('#likes').text))+1).toString();
            location.reload();
        },
        
    });
}

function add_dislike(id) {
    $.ajax({
        url: "/add_dislike/" + id.toString() + '/',
        success: function(){
            $('#dislikes').innerHTML = parseInt(($('#dislikes').text))+1;
            location.reload();
        },
        
    });
}
