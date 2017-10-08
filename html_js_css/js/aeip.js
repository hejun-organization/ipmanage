/**
 * Created by lenovo on 2017/10/7.
 */

function selectAllFromDb(db_name){
    var xhr = new XMLHttpRequest();
    xhr.open('POST','ip',false);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send('method=query_ip');
    //4 == xhr.readyState && 200 == xhr.status ? console.log(xhr.responseText) : console.log('hejun send http error');
    if (4 == xhr.readyState && 200 == xhr.status)
    {
        console.log(xhr.responseText);
        return eval(xhr.responseText);
    }
    else
    {
        return [];
    }

    //fr.readAsArrayBuffer(file);



//    var xhr = new XMLHttpRequest();
//    xhr.open('GET', 'ae.db', false);
//    xhr.responseType = 'arraybuffer';
//
//    xhr.onload = function(e) {
//
//        var uInt8Array = new Uint8Array(this.response);
//        var db = new SQL.Database(uInt8Array);
//        var res = db.exec("SELECT * FROM " + db_name);
//        console.log(res);
//        console.log('hejun');
//        for( i= 0;i < res[0].values.length;i++)
//        {//query values
//            console.log(res[0].values[i]);
//            rlt.push(res[0].values[i]);
//
//        }
//        db.close();
//    };
//    xhr.send();
//    console.log(rlt);
}

function initTable(){
    var tbl_left = window.innerWidth * 0.2;
    var tbl_top = window.innerHeight * 0.1;
    var ip_tbl = $('#ip_tbl');
    ip_tbl.css('left',tbl_left);
    ip_tbl.css('top',tbl_top);
    var ip_tr = $('#ip tr');
    for (var i = 0,len = ip_tr.length;i < len;i++)
    {
        ip_tr[i].className = i % 2 == 0 ?  'evenrowcolor' : 'oddrowcolor';
    }
    var ip_form = $('#ip_form');
    // ip_form.css('top',tbl_top + '10px');
    ip_form.css('left',ip_tbl.width() + tbl_left)
}

function addTblData(data){
    console.log(data);
    newTrElement = $('<tr></tr>').appendTo($('#ipt'));
    for (var i = 0;i < data.length;i++)
    {
        newTdElement = $('<td>{0}</td>'.format(data[i]));
        newTdElement.innerText = '1';
        newTdElement.appendTo(newTrElement);
    }
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
    console.log(rlt);
    for (var i = 0;i < rlt.length;i++)
    {
        addTblData(rlt[i]);
    }
    initTable();

}

$(document).ready(main);