// Plotting Codes are here

var url = "/data";

function buildPlot(){
    Plotly.d3.json(url, function(error, response){
        console.log(response);

        var trace = {
            type: "scatter",
            mode: "lines", 
            name: "Bigfoot Sightings",
            y: response.map(data => data.sightings),
            x: response.map(data => data.months),
            line: {
                color: "#17BECF"
            }
        };

        var data = [trace]

        var layout = {
            title: "Bigfoot Sightings Per Year",
            xaxis: {
                type: "date"
            },
            yaxis: {
                autorange: true,
                type: "linear"
            }
        };

        Plotly.newPlot("plot", data, layout)
    })
}

buildPlot();

