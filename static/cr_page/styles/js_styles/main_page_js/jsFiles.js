//PRIORITY COLOR//
$(document).ready(function () {
    var $priorityTd = $('.priority');
    for (let i = 0; i < $priorityTd.length; i++) {
        if ($priorityTd[i].innerText === 'Low') {
            $($priorityTd[i]).css('color', '#427705');
        } else if ($priorityTd[i].innerText === 'Medium') {
            $($priorityTd[i]).css('color', '#985c11');
        } else if ($priorityTd[i].innerText === 'High') {
            $($priorityTd[i]).css('color', '#e21606');
        }
    }

});
//End PRIORITY COLOR//


var implementer_row = document.getElementsByClassName('td_implementer');
for (let i = 0; i < implementer_row.length; i++) {
    if (implementer_row[i].textContent == '') {
        implementer_row[i].style.border = '1px solid #3b2121';
    };
}


//file uploading Section
$('#id_file').bind('change', function () {
    var filename = $('#id_file').val();
    if (/^\s*$/.test(filename)) {
        $('.file_upload').removeClass('active');
        $('#no_file').text('No file chosen...');
    } else {
        $('.file_upload').addClass('active');
        $('#no_file').text(filename.replace('C:\\fakepath\\', ''));
    }
});


//end of file uploading Section


//add Table inputs//
$('.mat_div').children('input').focus(function () {
    $(this).parent().addClass('is_active is_completed');
});
$('.mat_div').children('input').focusout(function () {
    if ($(this).val() === '')
        $(this).parent().removeClass('is_completed');
    $(this).parent().removeClass('is_active');
})
//End add Table inputs//


//Current date time//
function time_now() {
    let input = $(".mat_div").children("#id_initated_date"),
        date = new Date(),
        month = date.getMonth() + 1,
        day = date.getDate(),
        year = date.getFullYear(),
        hour = (date.getHours() < 10 ? '0' : '') + date.getHours(),
        minute = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
    input.value = ''
    if (day < 10) {
        day = '0' + day
    }

    if (month < 10) {
        month = '0' + month
    }
    input.val(year + '-' + month + '-' + day + ' ' + hour + ':' + minute);

}

function time_now_finished() {
    let input = $(".mat_div").children("#id_finished_date"),
        date = new Date(),
        month = date.getMonth() + 1,
        day = date.getDate(),
        year = date.getFullYear(),
        hour = (date.getHours() < 10 ? '0' : '') + date.getHours(),
        minute = (date.getMinutes() < 10 ? '0' : '') + date.getMinutes();
    if (day < 10) {
        day = '0' + day
    }

    if (month < 10) {
        month = '0' + month
    }
    input.val(year + '-' + month + '-' + day + ' ' + hour + ':' + minute);

}
//End Current date time//



//modal opening//
var modal = document.getElementById('my_modal'),
    plusButton = document.getElementById('column_plus'),
    btn = document.getElementById('add_row_submit'),
    span = document.getElementsByClassName('close')[1];
//btn.onclick = function() {
//    modal.style.display = 'flex';
//}
btn.onclick = function () {
    modal.style.display = 'flex';
}
span.onclick = function () {
    modal.style.display = 'none';
}
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
//end modal opening//




//set requiret to add page inputs//
$('.mat_div').children('input').not('#id_done_by, #id_finished_date, #id_online, #id_offline, #id_remark ').attr('required', true);
$('.mat_div').children('select').attr('required', true);
$('.fields_container').find('input').attr('required', true);
//end set requiret to add page inputs//



//loading first .5 sec//
var load;

function loader_function() {
    load = setTimeout(show_page, 1);
}

function show_page() {
    document.getElementById('main').style.opacity = '1';
    document.getElementById('loader').style.display = 'none';
}
//end loading first .5 sec//



//add new row popup//
function waiting_request_add_button() {
    var modal = document.getElementById('my_modal'),
        plus_button = document.getElementById('column_plus'),
        btn = document.getElementById('add_row_submit'),
        span = document.getElementsByClassName('close')[1];
    btn.onclick = function () {
        modal.style.display = 'flex';
    }
    span.onclick = function () {
        modal.style.display = 'none';
    }
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
}
//endadd new row popup//


//make add new row modal//
var addRow = document.getElementById('add_row_modal'),
    plusButton = document.getElementById('column_plus'),
    button = document.getElementById('add_new_row_button'),
    span = document.getElementsByClassName('close')[0];
button.onclick = function () {
    addRow.style.display = 'flex';
}
span.onclick = function () {
    addRow.style.display = 'none';
}
//end make add new row modal//
