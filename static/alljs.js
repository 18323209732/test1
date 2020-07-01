function statistical(s,f,e,t,o) {
    var myChart = echarts.init(document.getElementById('picture'));
    var option = {
    backgroundColor: '#F5F5F5',
    title : {
        text: '结果统计分析',
        x:'center',
        y:"left"
    },
    tooltip : {
        position: "right",
        extraCssText:'width:150px;height:60px;',
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['成功','失败','错误','超时','跳过']
    },
    color: ['#22bd26', '#FE780A', '#FF3C0D','#38CBFE','#C4CC3B'],
    series : [
        {
            name: '用例占比 : ',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:s, name:'成功'},
                {value:f, name:'失败'},
                {value:e, name:'错误'},
                {value:t, name:'跳过'},
                {value:o, name:'超时'}
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 10,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
return myChart.setOption(option);
}

function showClassDetail(detail_id, hiddenRow_id, class_type) {

    if ('详细' ==  document.getElementById(detail_id).innerText) {
        if ('all' == class_type) {
            document.getElementById(hiddenRow_id).className = 'all';
        }
        else if ('success' == class_type) {
            document.getElementById(hiddenRow_id).className = 'success';
        }
        else if ('error' == class_type) {
            document.getElementById(hiddenRow_id).className = 'error';
        }
        else if ('fail' == class_type) {
            document.getElementById(hiddenRow_id).className = 'fail';
        }
        else{
            document.getElementById(hiddenRow_id).className = 'timeout';
        }
        document.getElementById(detail_id).innerText = "收起"
    }
    else {
        document.getElementById(detail_id).innerText = "详细";
        document.getElementById(hiddenRow_id).className = 'hiddenRow';
    }
}

var isHide=true;
function hideTab(tab){
    var elment=document.getElementById(tab);
    var rows=elment.rows;
    var len=elment.rows.length;
    for(var i=1;i < len;i++){
        if (isHide) {
            rows[i].style.display='block';
        }else{
            rows[i].style.display='none';
        }
    }
    isHide=!isHide
}
