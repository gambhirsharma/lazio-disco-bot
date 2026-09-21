// Eventi dei campi
// campi Date
$('.dateInput').keypress(function (e) {
    if ($(this).val().length <= 9)
        return isDateKey(e, $(this));
    return false;
});

// Fine eventi dei campi


















// Controlli sui dati
function DateValidation(date) {
    var dateRegex = /^(?=\d)(?:(?:31(?!.(?:0?[2469]|11))|(?:30|29)(?!.0?2)|29(?=.0?2.(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(?:\x20|$))|(?:2[0-8]|1\d|0?[1-9]))([-.\/])(?:1[012]|0?[1-9])\1(?:1[6-9]|[2-9]\d)?\d\d(?:(?=\x20\d)\x20|$))?(((0?[1-9]|1[012])(:[0-5]\d){0,2}(\x20[AP]M))|([01]\d|2[0-3])(:[0-5]\d){1,2})?$/;
    console.log(dateRegex.test(date));
    return dateRegex.test(date);
}

function isNumberKey(evt) {
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode != 46 && charCode > 31 &&
        (charCode < 48 || charCode > 57))
        return false;
    return true;
}

function isDateKey(evt, element) {
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    var txt = element.val();
    console.log(txt);
    var count = 1;
    console.log(txt.length);
    for (let index = 0; index < txt.length; index++) {
        const char = txt[index];
        if (char == "/") {
            count++;
        }
    }
    if (charCode == 47) {
        if (count > 2 || (txt.length != 2 && txt.length != 5)) {
            return false;
        }
    } else if ((txt.length == 2 || txt.length == 5) && charCode != 47) {
        element.val(element.val() + "/");
        return;
    }
    if (charCode != 46 && charCode != 47 && charCode > 31 &&
        (charCode < 48 || charCode > 57))
        return false;
    return true;
}
// Fine controlli sui dati