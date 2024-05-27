document.addEventListener('DOMContentLoaded', function() {
    var phoneInput = document.querySelector('#id_phone_number');

    phoneInput.addEventListener('input', function(e) {
        var value = phoneInput.value;

        // Remove all non-digit characters except +
        value = value.replace(/[^\d\+]/g, '');

        // Add formatting
        if (!value.startsWith('+7(')) {
            value = '+7(' + value.replace('+7', '').replace('(', '');
        }

        if (value.length > 6) {
            value = value.slice(0, 6) + ')-' + value.slice(6);
        }
        if (value.length > 11) {
            value = value.slice(0, 11) + '-' + value.slice(11);
        }
        if (value.length > 14) {
            value = value.slice(0, 14) + '-' + value.slice(14);
        }
        if (value.length > 17) {
            value = value.slice(0, 17);
        }

        phoneInput.value = value;
    });

    phoneInput.addEventListener('keydown', function(e) {
        var key = e.key;
        var pos = phoneInput.selectionStart;

        // Prevent deletion of initial part
        if ((key === 'Backspace' && pos <= 3) ||
            (key === 'Delete' && pos <= 4)) {
            e.preventDefault();
        }
    });

    // Set initial value if empty
    if (phoneInput.value === '') {
        phoneInput.value = '+7(';
    }
});
