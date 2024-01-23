function rating(n, id) {
    $.post("/set_like/{id}", {like:n});
}