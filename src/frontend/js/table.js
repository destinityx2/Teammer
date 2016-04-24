
function GenericTable ()
{
    var table = new String(/*"<table class = users>"*/);

    table +="<thead><tr><th>#</th><th>Nickname</th><th>Completed projects</th><th>Abondonned projects</th></tr></thead><tbody>";
    for(var i = 1; i < 50 + 1; ++i)
    {
        table += ("<tr><td class='number'>" + i + "</td><td class='uname'>" +
        "<a href='Profile.html' class='person'>Username</a></td><td class='amount'>m</td>" +
        "<td class='amount'>k</td></tr>");
    }
    table += "</tbody>";
    document.write(table);
   /* document.all.tab.innerHTML = table;*/
}


function NavigationBar(n) {
    var page = [], space = "<p>...</p>", num = 10;

    var pNext = "<p  onclick='tab(" + (n + 1) + ")'>></p>";
    var pPrev = "<p  id = first onclick='tab(" + (n - 1) + ")'><</p>";
    var NaNpPrev = "<p  id = first style='visibility:hidden'; onclick='tab(" + (n - 1) + ")'><</p>";

    var nav_bar = new String();

    for (var i = 1; i <= num; ++i) {
        if(i == n){
            page[i] = "<p class = active onclick='tab(" + i + ")'>" + i + "</p>";
        }
        else {
            page[i] = "<p onclick='tab(" + i + ")'>" + i + "</p>";
        }
    }

    if (n > 0 && n <= num)
    {
        if (n < 3) {
            if(n == 2){
                nav_bar = pPrev + page[1] + page[2] + page[3] + space + page[num] + pNext;
            }
            else {
                nav_bar = NaNpPrev + page[1] + page[2] + page[3] + space + page[num] + pNext;
            }
            document.all.navigation.innerHTML = nav_bar;
        }
        else if (n > num - 2) {
            if(n == num-1){
                nav_bar = pPrev + page[1] + space + page[num - 2] + page[num - 1] + page[num] + pNext;
            }
            else {
                nav_bar = pPrev + page[1] + space + page[num - 2] + page[num - 1] + page[num];
            }

            document.all.navigation.innerHTML = nav_bar;
        }
        else {
            nav_bar = pPrev + page[1];
            if (n == 3) {
                nav_bar += page[2] + page[3] + page[4] + space + page[num] + pNext;
            }
            else if(n >= num-2){
                nav_bar += space + page[n-1] + page[n] + page[n+1] + page[num] + pNext;
            }
            else{
                nav_bar += space + page[n-1] + page[n] + page[n+1] + space + page[num] + pNext;
            }

            document.all.navigation.innerHTML = nav_bar;
        }
    }
}


function tab(n)
{
    var table = new String("<table class = users>");

    table +="<tr><th>#</th><th>Nickname</th><th>Completed projects</th><th>Abondonned projects</th></tr>";
    for(var i = (n * 50 - 49); i < (n * 50 + 1); ++i)
    {
        table += ("<tr><td class='number'>" + i + "</td><td class='uname'>" +
            "<a href='Profile.html' class='person'>Username</a></td><td class='amount'>m</td>" +
            "<td class='amount'>k</td></tr>");
    }
    table += "</table>";

    document.all.tab.innerHTML = table;

   NavigationBar(n);
}