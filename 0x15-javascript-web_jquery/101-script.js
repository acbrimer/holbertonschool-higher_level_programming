// Simple add, remove, clear <ul> triggered from click events
$('document').ready(() => {
    const my_list = $('UL.my_list');
    // Handler functions for div clicks/list operations
  const handleAddItem = () => my_list.append(`<li>Item</li>`);
  const handleRemoveItem = () => $('li', my_list).last().remove();
  const handleClearList = () => my_list.html('');
  // Wire handler functions to div click actions
  $('DIV#add_item').click(handleAddItem);
  $('DIV#remove_item').click(handleRemoveItem);
  $('DIV#clear_list').click(handleClearList);
});
