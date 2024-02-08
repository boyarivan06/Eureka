function delete_idea(id) {
    confirm('Вы уверены? Это нельзя отменить');
    $.ajax({
        url: "/delete_idea/" + id.toString() + '/',
        success: function(){
            $('#idea'+id).remove();
        },

    });
}