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


var donutChart2 = document.getElementById('donutChartChartistFinance');
var data_labels2 = donutChart2.getAttribute('data-labels');
var data_series2 = donutChart2.getAttribute('data-series');

var dlabels2 = JSON.parse(data_labels2.replace(/'/g, '"'));
var dseries2 = JSON.parse(data_series2.replace(/'/g, '"'));

var options2 = {
  chart: {
      type: 'donut',
      height: 350
  },
  series: dseries2,
  labels: dlabels2,
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

var chart = new ApexCharts(document.querySelector("#donutChartChartistFinance"), options2);
chart.render();