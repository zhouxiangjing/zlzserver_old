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

                let comment_api = event.data.comment_api

                let article = parseInt(event.data.article_id)
                let user = parseInt(event.data.user_id)
                let comment_content = $('#comment_content').val()
                let comment_level = 1
                let comment_parent_id = 0

                let form_data = new FormData();
                form_data.append('article', article)
                form_data.append('user', user)
                form_data.append('content', comment_content)
                form_data.append('level', comment_level)
                form_data.append('parent_id', comment_parent_id)

                for (let value of form_data.values()) {
                    console.log(value);
                }

                $.ajax({
                    url: comment_api,
                    type: 'POST',
                    cache: false,
                    data: form_data,
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

