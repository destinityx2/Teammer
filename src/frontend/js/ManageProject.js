function AddPeople(n) {
    var member_list = String();
    var curr_table = document.getElementById("team");
    var trList= curr_table.getElementsByTagName('tr');
    var num_col;
    var max_col = 4;
    var num_member = n + 1;

    for (var i = 0;i < trList.length; i++)
    {
        tdList = trList[i].getElementsByTagName('td');
        member_list += "<tr>";
        num_col = tdList.length;
        if(i == trList.length - 1){
            num_col = tdList.length - 1;
        }
        for (var j = 0;j < num_col; j++)
        {
            member_list += "<td>" + tdList[j].innerHTML + "</td>";
        }
        if(num_col == tdList.length - 1){
            member_list += "<td id = 'default'><p onclick='DeletePeople(" + num_member + ")' class ='profile' alt=''> </p><br>" +
                "<img class='ava'  onclick='DeletePeople(" + num_member + ")' src='img/delete_people.png' alt=''></td>";
        }
        if(tdList.length == max_col) {
            member_list += "</tr>";
        }
    }
    if(tdList.length == max_col)
    {
        member_list += "<tr><td id = 'default'><p onclick='AddPeople(" + num_member + ")' class ='profile' alt=''></p><br>" +
            "<img class='ava' onclick='AddPeople(" + num_member + ")' src='img/add_people.png' alt=''></td></tr>";
    }else{
        member_list += "<td id = 'default'><p onclick='AddPeople(" + num_member + ")' class ='profile' alt=''></p><br>" +
            "<img class='ava' onclick='AddPeople(" + num_member + ")' src='img/add_people.png' alt=''></td></tr>";
    }
    document.all.team.innerHTML = member_list;
    fun(n);

}

function DeletePeople(n) {
    var member_list = String();
    var curr_table = document.getElementById("team");
    var trList= curr_table.getElementsByTagName('tr');
    var num_col;
    var num_member = n - 1;

    for (var i = 0;i < trList.length; i++)
    {
        tdList = trList[i].getElementsByTagName('td');
        member_list += "<tr>";
        num_col = tdList.length;
        if(i == trList.length - 1){
            num_col = tdList.length - 2;
        }else if(trList[i + 1].getElementsByTagName('td').length == 1){
            num_col = tdList.length - 1;
        }
        for (var j = 0;j < num_col; j++)
        {
            member_list += "<td>" + tdList[j].innerHTML + "</td>";
        }
        if((num_col == tdList.length - 2) || (num_col == tdList.length - 1)){
            member_list += "<td id = 'default'><p onclick='AddPeople(" + num_member + ")' class ='profile' alt=''></p><br>" +
                "<img class='ava'  onclick='AddPeople(" + num_member + ")' src='img/add_people.png' alt=''></td>";
            break;
        }
        member_list += "</tr>";
    }

    member_list += "</tr>";
    document.all.team.innerHTML = member_list;
    fun(n);
}

function fun (n){
    var curr_table = document.getElementById("team");
    var trList= curr_table.getElementsByTagName('tr');
    var num_col;
    var num_member = 0;
    var input = String();

    for (var i = 0;i < trList.length; i++)
    {
        tdList = trList[i].getElementsByTagName('td');
        num_col = tdList.length;
        for (var j = 0;j < num_col; j++)
        {
            ++num_member;
        }
    }
    --num_member;
    input = "<tr><td><input id='num_members' name='num_members' form='manage_project' " +
        "type='hidden' value="+ num_member +"></td></tr>";
    document.all.Members.innerHTML = input;
}