var model = null;
/*
function getvalues() {
    
    if (model != null) {
        var tensor = tf.tensor1d([parseInt('12')]);
        var prediction = model.predict(tensor).dataSync();
        console.log(prediction)
    } else {
        console.log("No Data")
    }
} */

$(function() {    
    $('#button').click(function() {
        console.log('print algo')
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

/*
function predictData(){
    
}

(async () => {
    console.log("Cargando modelo")
    model = tf.loadLayersModel("cliport.json")
    console.log("Modelo cargado")
});*/
