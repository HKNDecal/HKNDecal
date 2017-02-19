$(document).ready(function(){
  var update_todo_list = function(){
    $.get('api/todos', function(data){
      $('#todo_list_view').html('');
      data.forEach(function(item_name){
        $('#todo_list_view').append('<li>' + item_name + '</li>');
      });
    })
  };

  // Adding a new todo item
  $('#add').click(function(){
    var item_name = $('#input_item_name').val();
    $.get('api/todos_insert?name=' + item_name);
    update_todo_list();
  });

  // Removing an exiting todo item
  $('#delete').click(function(){
    var item_name = $('#input_item_name').val();
    $.get('api/todos_delete?name=' + item_name);
    update_todo_list();
  });

  update_todo_list();
})
