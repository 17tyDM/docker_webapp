function change_table() {
    table_obj = document.getElementById('table_id');
    if (table_obj.style.backgroundColor == "blue") {
        table_obj.style.backgroundColor = "red";
    } else {
        table_obj.style.backgroundColor = "blue";
    }
}
function change_by_select() {
    select_obj = document.getElementById('select_id');
    table_obj = document.getElementById('table_id');
    if (select_obj.value == "red") {
        table_obj.style.backgroundColor = "red";
    } else if (select_obj.value == "blue") {
        table_obj.style.backgroundColor = "blue";
    } else {
        table_obj.style.backgroundColor = "";
    }
}
