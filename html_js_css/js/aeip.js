/**
 * Created by lenovo on 2017/10/7.
 */

function selectAllFromDb(db_name){
    var xhr = new XMLHttpRequest();
    xhr.open('POST','ip',false);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send('method=query_ip');
    if (4 == xhr.readyState && 200 == xhr.status)
    {
        return eval(xhr.responseText);
    }
    else
    {
        return [[]];
    }
}

function initTable(){
    var tbl_left = window.innerWidth * 0.2;
    var tbl_top = window.innerHeight * 0.1;
    var ip_tbl = $('#ip_tbl');
    ip_tbl.css('left',tbl_left);
    ip_tbl.css('top',tbl_top);
    var ip_tr = $('#ipt tr');
    for (var i = 0,len = ip_tr.length;i < len;i++)
    {
        ip_tr[i].className = i % 2 == 0 ?  'evenrowcolor' : 'oddrowcolor';
    }
    var ip_form = $('#ip_form');
    // ip_form.css('top',tbl_top + '10px');
    ip_form.css('left',ip_tbl.width() + tbl_left)
}

function addTblData(data){
    newTrElement = $('<tr></tr>').appendTo($('#ipt'));
    for (var i = 0;i < data.length;i++)
    {
        newTdElement = $('<td>{0}</td>'.format(data[i]));
        newTdElement.innerText = '1';
        newTdElement.appendTo(newTrElement);
    }
}

function assembleData(data){
    var out_time = parseInt(data[3]);
    var current_time = new Date().getTime();
    console.log(current_time,out_time)
    out_time = (current_time - out_time) >= 0 ? '' : new Date(out_time).toLocaleString();
    var status = data[4];
    status_map = {'0':'可申请','1':'正在使用','2':'故障','3':'其它'};
    return [data[0],data[1],data[2],out_time,status_map[status],data[5],data[6]];
}

function main(){
    String.prototype.format = function(args) {
        var result = this;
        if (arguments.length > 0) {
            if (arguments.length == 1 && typeof (args) == "object") {
                for (var key in args) {
                    if(args[key]!=undefined){
                        var reg = new RegExp("({" + key + "})", "g");
                        result = result.replace(reg, args[key]);
                    }
                }
            }
            else {
                for (var i = 0; i < arguments.length; i++) {
                    if (arguments[i] != undefined) {
                        var reg= new RegExp("({)" + i + "(})", "g");
                        result = result.replace(reg, arguments[i]);
                    }
                }
            }
        }
        return result;
    };
    var rlt = selectAllFromDb('ae_ip');
    for (var i = 0;i < rlt.length;i++)
    {
        var data_lst = assembleData(rlt[i]);
        addTblData(data_lst);
    }
    initTable();

}

$(document).ready(main);