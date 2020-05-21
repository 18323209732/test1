function statistical(s,f,e,t,c) {
    var myChart = echarts.init(document.getElementById('picture'));
    var option = {
    backgroundColor: '#F5F5F5',
    title : {
        text: '结果统计分析',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['成功','失败','错误','超时','跳过']
    },
    color: ['#867EFE', '#FE780A', '#FF3C0D','#38CBFE','#C4CC3B'],
    series : [
        {
            name: '用例占比',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:s, name:'成功'},
                {value:e, name:'错误'},
                {value:f, name:'失败'},
                {value:t, name:'跳过'},
                {value:c, name:'超时'}
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
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


option = {
    title : {
        text: '饼图程序调用高亮示例',
        x: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
    },
    series : [
        {
            name: '访问来源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:335, name:'直接访问'},
                {value:310, name:'邮件营销'},
                {value:234, name:'联盟广告'},
                {value:135, name:'视频广告'},
                {value:1548, name:'搜索引擎'}
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};

app.currentIndex = -1;

setInterval(function () {
    var dataLen = option.series[0].data.length;
    // 取消之前高亮的图形
    myChart.dispatchAction({
        type: 'downplay',
        seriesIndex: 0,
        dataIndex: app.currentIndex
    });
    app.currentIndex = (app.currentIndex + 1) % dataLen;
    // 高亮当前图形
    myChart.dispatchAction({
        type: 'highlight',
        seriesIndex: 0,
        dataIndex: app.currentIndex
    });
    // 显示 tooltip
    myChart.dispatchAction({
        type: 'showTip',
        seriesIndex: 0,
        dataIndex: app.currentIndex
    });
}, 1000);