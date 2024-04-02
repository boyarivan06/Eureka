function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const appendAlert = (message, type, id) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    '<div class="alert alert-' + type + ' alert-dismissible" role="alert">',
    '   <div>'+message+'</div>',
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
    ].join('')
    var alertPlaceholder = document.getElementById('liveAlertPlaceholder'+id)
    alertPlaceholder.append(wrapper)
    sleep(5000).then(() => {alertPlaceholder.innerHTML = "";})
}
