$(document).ready(function () {

    console.log('authentication document ready')

    let countdown = 60;

    let csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
            //alert('ajax beforeSend')
        }
    });


    get_captcha = function (obj) {

        if (countdown == 60) {
            console.log('zzz 1')
            let phone =  $('#phone').val()
            console.log('zzz 2' + phone)
            let form_data = new FormData();
            form_data.append('phone', phone)
            console.log(form_data)
            $.ajax({
                url: '/sendsms/',
                type: 'POST',
                cache: false,
                data: form_data,
                processData: false,
                contentType: false
            }).done(function (res) {
                console.log(res)
            })
        }

        if (countdown == 0) {
            obj.removeAttribute("disabled");
            obj.innerHTML = "获取验证码";
            countdown = 60;
            return;
        } else {
            obj.setAttribute("disabled", true);
            obj.innerHTML = "重新发送(" + countdown + ")";
            countdown--;
        }
        setTimeout(function () {
                get_captcha(obj)
            }
            , 1000)
    }

})