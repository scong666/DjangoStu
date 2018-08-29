$(function () {
    $(".confirm").click(function () {
        var $current_btn = $(this);
        var c_id = $current_btn.parents("li").attr("c_id");
        // console.log(c_id);
        $.ajax({
            url:'/axf/cart-status',
            method:"put",
            data:{
                c_id:c_id
            },
            success:function (res) {
                console.log(res);
                if(res.code == 1){
            //    要改当前商品的选中状态
                    if (res.current_item_status){
                        $current_btn.find("span").find("span").html("√");
                    }else {
                        $current_btn.find("span").find("span").html("");
                    }
            //    改总价
                    $("#money").html(res.sum_money);
            //    全选按钮的状态
                    if(res.is_select_all){
                        $(".all_select>span>span").html("√");
                    }else {
                        $(".all_select>span>span").html("");
                    }

                }else {
                    alert(res.msg);
                }

            }
        })
    });

    $(".all_select").click(click_all_select)
})

function click_all_select() {
    $.ajax({
        url:"/axf/select_all_api",
        data:{},
        method:"put",
        success:function (res) {
            console.log(res);
            if (res.code == 1){
            //    修改全部商品的选中状态
            //    全选按钮状态
            //    总价
            }
        }
    })
}