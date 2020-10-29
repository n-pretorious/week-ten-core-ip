new Chart(document.getElementById("horizontalBar"), {
    "type": "horizontalBar",
    "data": {
        "labels": ["Design", "Usability", "Content", ],
        "datasets": [{
            "label": "Average rating",
            "data": [8, 5, 7],
            "fill": false,
            "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(255, 159, 64, 0.2)",
                "rgba(255, 205, 86, 0.2)", "rgba(75, 192, 192, 0.2)", "rgba(54, 162, 235, 0.2)",
                "rgba(153, 102, 255, 0.2)", "rgba(201, 203, 207, 0.2)"
            ],
            "borderColor": ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)",
                "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"
            ],
            "borderWidth": 1
        }]
    },
    "options": {
        "scales": {
            "xAxes": [{
                "ticks": {
                    "beginAtZero": true,
                    stepSize: 1,
                    suggestedMax: 10
                }
            }]
        }
    }
});

function toggleForm() {
    $("#ratingForm").toggleClass('rateForm')
};

function submitRating() {
    $('#ratingForm').submit(function(event) {
            event.preventDefault()
            form = $("#ratingForm")

            $.ajax({
                    'path': '/project/<int:id>',
                    'type': 'POST',
                    'data': form.serialize(),
                    'dataType': 'json',
                    'success': function(data) {
                        alert(data['success'])
                    },
                }) // END of Ajax method
            $('#design').val('')
            $("#usability").val('')
            $("#content").val('')
        }) // End of submit event
}