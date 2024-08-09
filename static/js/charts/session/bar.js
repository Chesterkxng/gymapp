var BarChart = document.getElementById('barChart');
var data_hours = BarChart.getAttribute('data-hours');
var data_series = BarChart.getAttribute('data-series');

// Replace single quotes with double quotes to make it a valid JSON string
var dhours = JSON.parse(data_hours.replace(/'/g, '"'))
var dseries = JSON.parse(data_series.replace(/'/g, '"'));

var options = {
  chart: {
    type: "bar",
    height: 350,
  },
  series: [
    {
      name: "Sessions",
      data: dseries,
    },
  ],
  xaxis: {
    categories: dhours,
  },
  yaxis: {
    title: {
      text: "Nombre de sessions",
    },
  },
  legend: {
    position: "bottom",
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: "50%",
    },
  },
  dataLabels: {
    enabled: false,
  },
};

var chart = new ApexCharts(document.querySelector("#barChart"), options);
chart.render();
