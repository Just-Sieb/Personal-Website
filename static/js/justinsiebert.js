$("#home").click(function(){
    $("#submenu").children().remove();
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> test 1</i></a>');
})

$("#messages").click(function(){
    $("#submenu").children().remove();
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> View Messages</i></a>');
})

$("#lego").click(function(){
    $("#submenu").children().remove();
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> View Builds</i></a>');
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> Add Build</i></a>');
})

$("#programs").click(function(){
    $("#submenu").children().remove();
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> View Programs</i></a>');
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> Add Program</i></a>');
})

$("#stats").click(function(){
    $("#submenu").children().remove();
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> Visitors</i></a>');
})

$("#blog").click(function(){
    $("#submenu").children().remove();
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> View Articles</i></a>');
    $("#submenu").append('<a href="#" class="list-group-item" id="home"><i class="fa fa-home fa-lg"> New Article</i></a>');
})