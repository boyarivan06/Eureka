$(document).ready(function () {
          // отслеживаем событие отправки формы
          $('.req').submit(function () {
              // создаем AJAX-вызов
              $.ajax({
                  data: $(this).serialize(), // получаем данные формы
                  type: $(this).attr('method'), // GET или POST
                  url: "/add_request/",
                  // если успешно, то
                  success: function (response) {
                      appendAlert("Запрос на сотрудничество отправлен", 'success', response.id);
                  },
                  // если ошибка, то
                  error: function (response) {
                      // предупредим об ошибке
                      alert(response.responseJSON.errors);
                      console.log(response.responseJSON.errors)
                  }
              });
              return false;
          });
      })