var stackedBarChart = document.getElementById('stackedBarChart');
var data_series = stackedBarChart.getAttribute('data-series');

// Replace single quotes with double quotes to make it a valid JSON string
var dseries = JSON.parse(data_series.replace(/'/g, '"'));


var options = {
    chart: {
        type: 'bar',
        height: 350,
        stacked: true,
    },
    series: dseries,
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    legend: {
        position: 'bottom',
        horizontalAlign: 'center',
    },
    plotOptions: {
        bar: {
            horizontal: false,
        },
    },
    fill: {
        opacity: 1,
    },
    dataLabels: {
        enabled: false,
    },
};

var chart = new ApexCharts(document.querySelector("#stackedBarChart"), options);
chart.render();

var stackedBarChart2 = document.getElementById('stackedBarChartFinance');
var data_series2 = stackedBarChart2.getAttribute('data-series');

// Replace single quotes with double quotes to make it a valid JSON string
var dseries2 = JSON.parse(data_series2.replace(/'/g, '"'));


var options2 = {
    chart: {
        type: 'bar',
        height: 350,
        stacked: true,
    },
    series: dseries2,
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    legend: {
        position: 'bottom',
        horizontalAlign: 'center',
    },
    plotOptions: {
        bar: {
            horizontal: false,
        },
    },
    fill: {
        opacity: 1,
    },
    dataLabels: {
        enabled: false,
    },
};

var chart = new ApexCharts(document.querySelector("#stackedBarChartFinance"), options2);
chart.render();