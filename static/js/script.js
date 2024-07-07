$(document).ready(function() {
    $('form').submit(function(e) {
        var name = $('#name').val();
        var age = $('#age').val();
        var phone = $('#phone_number').val();

        if (name.length < 1) {
            alert("Please enter a name.");
            e.preventDefault();
        } else if (age.length < 1 || isNaN(age) || parseInt(age) <= 0) {
            alert("Please enter a valid age.");
            e.preventDefault();
        } else if (phone.length < 1) {
            alert("Please enter a phone number.");
            e.preventDefault();
        }
    });
});