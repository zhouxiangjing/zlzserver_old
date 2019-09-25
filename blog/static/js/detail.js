function comment_edit_focusin() {

    let height = $('#comment_content').outerHeight();
    if (height == 38) {
        $('#comment_content').css('height', '80')
        $('#comment_submit').css('display', 'flex')
    }

}

function comment_edit_focusout() {

    let width = $('#comment_content').outerHeight();
    if (width == 80) {
        $('#comment_content').css('height', '38')
        $('#comment_submit').css('display', 'none')
    }

}

$(document).ready(function () {

    console.log('document ready')
    let csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });



    function jumpLogin() {
        window.location.href="/login/";
    }


    $('#btn_comment_submit').click(data, function (event) {

        if(event.data.is_logined) {
            let comment_content =  $('#comment_content').val()
            if ($.trim(comment_content) == '') {
                alert('请输入评论');

            } else {
                console.log("comment_content : " + comment_content)

                let formData = new FormData();
                formData.append('file', v)

                $.ajax({
                    url: '/media/',
                    type: 'POST',
                    cache: false,
                    data: formData,
                    processData: false,
                    contentType: false
                }).done(function (res) {
                    alert('上传完成。')
                })
            }

        } else {
            jumpLogin()
        }
    })

})

