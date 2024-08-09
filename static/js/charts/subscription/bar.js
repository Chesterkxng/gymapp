var barChat = document.getElementById("barChart");
var data_series = barChat.getAttribute("data-series");
var dseries = JSON.parse(data_series.replace(/'/g, '"'));

var options = {
    chart: {
        type: 'bar',
        height: 350,
    },
    series: [{
        name: 'subscriptions',
        data: dseries
    }],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    plotOptions: {
        bar: {
            horizontal: false,
        },
    },
    dataLabels: {
        enabled: false,
    },
    fill: {
        opacity: 1,
    },
    legend: {
        position: 'bottom',
        horizontalAlign: 'center',
    },
};

var chart = new ApexCharts(document.querySelector("#barChart"), options);
chart.render();
