function add_like(id) {
    $.ajax({
        url: "/add_like/" + id.toString() + '/',
        success: function(){
            var n = parseInt($('#likes'+id).text())+1;
            $('#likes'+id).text(n);

        },
        
    });
}

function add_dislike(id) {
    $.ajax({
        url: "/add_dislike/" + id.toString() + '/',
        success: function(){
            //alert($('#dislikes'+id).text());
            var n = parseInt($('#dislikes'+id).text())+1;
            $('#dislikes'+id).text(n);

        },
        
    });
}
