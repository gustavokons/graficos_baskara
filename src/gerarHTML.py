#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Dec 17, 2012

@author: gustavokons
'''

import os
import function

def gerarGrafico(a,b,c,x):
    valores = ''
    x = x.split(',')
    for i in range(len(x)):
        valores += '['+x[i]+','+str(function.getYFuncao(a,b,c,int(x[i])))+'],'
          
    html = open("chart.html","w")
    html.write('''<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Grafico Bascara</title>    
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['X', 'Y'],
          '''+valores[0:(len(valores)-1)]+'''
        ]);

        var options = {
          title: 'Equação de 2º Grau',
          hAxis: {title: 'X', minValue: -15, maxValue: 15},
          vAxis: {title: 'Y', minValue: -15, maxValue: 15},
          legend: 'none'
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 1350px; height: 750px;"></div>
  </body>
</html>''')
    html.close()
    os.system("firefox chart.html")

