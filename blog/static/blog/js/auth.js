$(document).ready(function () {

    console.log('authentication document ready')

    let countdown = 60;
    let is_mobile = navigator.userAgent.toLowerCase().match(/(ipod|ipad|iphone|android|coolpad|mmp|smartphone|midp|wap|xoom|symbian|j2me|blackberry|wince)/i) != null;

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

    $("#auth_form").ajaxForm(function (data) {
        console.log(data)
        if(is_mobile) {
            AndroidFunction.login(JSON.stringify(data));
        } else {
            if (1000 == data.code) {
                window.location.href = "/"
            } else {
                window.alert("登录失败")
            }
        }
    });

    get_captcha = function (obj) {

        if (countdown == 60) {

            let phone =  $('#phone').val()
            if(phone.length != 11) {
                window.alert("手机号格式错误！")
                return;
            }
            let form_data = new FormData();
            form_data.append('phone', phone)
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