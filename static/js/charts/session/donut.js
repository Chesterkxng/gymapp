var donutChart = document.getElementById('donutChartChartist');
var data_labels = donutChart.getAttribute('data-labels');
var data_series = donutChart.getAttribute('data-series');

var dlabels = JSON.parse(data_labels.replace(/'/g, '"'));
var dseries = JSON.parse(data_series.replace(/'/g, '"'));

var options = {
  chart: {
      type: 'donut',
      height: 350
  },
  series: dseries,
  labels: dlabels,
  legend: {
      position: 'bottom'
  },
  plotOptions: {
    pie: {
      donut: {
        size: '70%'
      }
    }
  },
};

var chart = new ApexCharts(document.querySelector("#donutChartChartist"), options);
chart.render();