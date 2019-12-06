
function fileSelected() {
    let file = document.getElementById('fileselete').files[0];
    if (file) {
        console.log('select a file. ' + file)
        let fileSize = 0;
        if (file.size > 1024 * 1024)
            fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';
        else
            fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';

        console.log('select a file. ' + file.name + " " + fileSize + " " + file.type)
    }
}

function uploadFile() {
    var fd = new FormData();
    fd.append("fileToUpload", document.getElementById('fileToUpload').files[0]);
    var xhr = new XMLHttpRequest();
    xhr.upload.addEventListener("progress", uploadProgress, false);
    xhr.addEventListener("load", uploadComplete, false);
    xhr.addEventListener("error", uploadFailed, false);
    xhr.addEventListener("abort", uploadCanceled, false);
    xhr.open("POST", "../../api/test");
    xhr.send(fd);
}

function uploadProgress(evt) {
    if (evt.lengthComputable) {
      var percentComplete = Math.round(evt.loaded * 100 / evt.total);
      document.getElementById('progressNumber').innerHTML = percentComplete.toString() + '%';
    }
    else {
      document.getElementById('progressNumber').innerHTML = 'unable to compute';
    }
}

function uploadComplete(evt) {
/* 服务器端返回响应时候触发event事件*/
alert(evt.target.responseText);
}

function uploadFailed(evt) {
alert("There was an error attempting to upload the file.");
}

function uploadCanceled(evt) {
alert("The upload has been canceled by the user or the browser dropped the connection.");
}


$(document).ready(function () {

    console.log('document ready')

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

    function formatBytes(a, b) {
        if (0 == a) return "0 Bytes";
        let c = 1e3, d = b || 2, e = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
            f = Math.floor(Math.log(a) / Math.log(c));
        return parseFloat((a / Math.pow(c, f)).toFixed(d)) + " " + e[f]
    };

    let file_change = function (files) {
        $.each(files, function (k, v) {
            if (!v.type.match(/^image\/*/)) return;

            var pid = 'pic' + parseInt(Math.random() * 999999999);
            let pic = new Image()
            pic.onload=function(){
                $("#" + pid + ' .pic_desc').text(pic.naturalWidth + '*' + pic.naturalHeight + 'px | ' + $("#" + pid + ' .pic_desc').text());
            };
            pic.onerror=function(){alert("error!")};
            pic.src = URL.createObjectURL(v)

            let tmp = $('<div class="row w_content_ai_marketing" id="' + pid + '">\
                            <div class="col-lg-2  col-sm-2 col-xs-4">\
                                <div class="w_content_ai_pic_preview" style="background-image: url(' + pic.src + ')"></div>\
                            </div>\
                            <div class="col-lg-10 col-sm-10 col-xs-8">\
                                <div class="progress progress-striped active w_content_ai_pic_progress">\
                                    <div class="progress-bar progress-bar-primary" style="width: 0%"></div>\
                                </div>\
                                <div class="well well-sm w_content_ai_pic_desc">' + formatBytes(v.size) + ' | ' + v.name + '</div>\
                                <button class="btn btn-sm btn-primary big_begin" data-pid="' + pid + '">开始</button>\
                                <button class="btn btn-sm btn-danger big_del">删除</button>\
                            </div>\
                        </div>\
                        <hr>');
            tmp.find('.big_begin').click(function () {

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
            });
            $("#files").append(tmp);
        })
        $('#fileupload').val('');
    }

    $('#fileupload').change(function () {
        file_change(this.files);
    });

    $('#test').click(function () {

        let form_data = new FormData();
        form_data.append('username', 'admin')
        $.ajax({
            url: 'index/',
            type: 'POST',
            cache: false,
            data: form_data,
            processData: false,
            contentType: false,
            success: function (req) {
                alert('ajax success')
            },
            error: function () {
                alert('ajax error')
            }
        })
    });

    $('#login').click(function () {
        $('#modal_login').modal('show');
    });

    $('#register').click(function () {
        $('#modal_register').modal('show');
    });

    $('#authentication').click(function () {
        console.log("zzz")
        window.alert("zxj")
    });

    $('#submit_register').click(function () {

        let username = $.trim($('#username').val());
        let password = $.trim($('#password').val());
        let re_password = $.trim($('#re_password').val());

        console.log('username : ' + username);
        console.log('password : ' + password);
        console.log('re_password : ' + re_password);

        if(username.length > 2 &&
            password.length > 2 &&
            password == re_password) {

            let form_data = new FormData();
            let request_data = $("#form_register").serializeArray();
            $.each(request_data, function (index, data) {
                form_data.append(data.name, data.value)
            });

            $.ajax({
                url: 'register/',
                type: 'POST',
                cache: false,
                data: form_data,
                dataType:'json',
                processData: false,
                contentType: false,
                success: function (data) {
                    console.log('ajax success');
                    console.log(data);
                    $('#modal_register').modal('hide');
                    alert("注册成功，请使用账户名 " + data.username +" 登录")
                },
                error: function (data) {
                    console.log('ajax error');
                    console.log(data);
                    alert("注册失败")
                },
                complete: function (data) {
                    console.log('ajax register complete');
                }
            })
        } else alert('用户信息填写错误')


        // let form_data = $("#form_register").serialize();
        // console.log(form_data)
        // alert($("#form_register").serializeArray())

    });


})




