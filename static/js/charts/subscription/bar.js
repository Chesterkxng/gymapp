//===========Overlapping Bars===========================//
var barChat = document.getElementById("overlapBarchartChartist");
var data_series = barChat.getAttribute("data-series");
var dseries = JSON.parse(data_series.replace(/'/g, '"'));

console.log(dseries);   

if ($("#overlapBarchartChartist").length) {
  var data = {
    labels: [
      "Jan",
      "Fev",
      "Mar",
      "Avr",
      "Mai",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
    series: [dseries],
  };

  var options = {
    seriesBarDistance: 10,
    axisY: {
        onlyInteger: true, // Ensure only integer values are displayed
        low: 0, // Set the minimum value for the Y-axis
        scaleMinSpace: 30, // Minimum space between grid lines
        // Label interpolation function to customize the steps
        labelInterpolationFnc: function(value) {
          return value % 1 === 0 ? value : null; // Display values that are multiples of 10
        }
      }
  };

  var responsiveOptions = [
    [
      "screen and (max-width: 640px)",
      {
        seriesBarDistance: 5,
        axisX: {
          labelInterpolationFnc: function (value) {
            return value[0];
          },
        },
      },
    ],
  ];

  new Chartist.Bar(
    "#overlapBarchartChartist",
    data,
    options,
    responsiveOptions
  );
}
