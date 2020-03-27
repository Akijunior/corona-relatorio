var selected = $('#selected-country');
const countries_div = $('#country-historical');
const endpoint = '/historico/';
const delay_by_in_ms = 700;
let scheduled_function = false;


selected[0].addEventListener("change", showCountryHistoric, false);

function showCountryHistoric() {

    $.ajax({
        url: '/historico/',
        method: 'GET',
        data: {sortBy: selected.val()},
        success: function (response) {

            countries_div.html(response);
            countries_div.fadeTo('slow', 0).promise().then(() => {
                countries_div.html(response['html_from_view']);
                countries_div.fadeTo('slow', 1);
            })
        },
        error: function (e) {
            alert('error');
        }
    });
}

let ajax_call = function (endpoint, request_parameters) {
    console.log("OI");
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            countries_div.fadeTo('slow', 0).promise().then(() => {
                countries_div.html(response['html_from_view']);
                countries_div.fadeTo('slow', 1);
            })
        })
};


selected.on('keyup', function () {

    const request_parameters = {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    };

    // start animating the search icon with the CSS class
    search_icon.addClass('blink');

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
});