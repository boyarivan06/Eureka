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
                      alert("Запрос на сотрудничество отправлен");
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