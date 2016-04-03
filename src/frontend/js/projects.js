
function GenericTable ()
{
    var table = new String("<table class = 'projects'>");

    table += "<tr><th>Projects</th><th>Publication date</th><th>Participants</th></tr>";

    for(var i = 0; i < 5; ++i)
    {
        table += ("<tr><td  class='project_name'><h3><a href='Project.html'>Build a Simple Website</a></h3>" +
        "<p class='description'>Create a simple website using the design of an existing WordPress template website. " +
        "(Download it here: http://sh.st/UwwqS) This will be a new and nearly static website and will require copying " +
        "the WordPress template and modifying the layout and graphics to create a new and unique website.</p>" +
        "<p class='skills'>Skills: HTML, PHP</p></td>" +
        "<td class='date'><p>12.03.16</p></td><td class='members'><p>3/4</p></td></tr>");

        table += ("<tr><td class='project_name'><h3><a href='Project.html'>Online Mapping app project</a></h3>" +
        "<p class='description'>A mapping software application is needed. Preferred a web based application. " +
        "The application will show each tracking device on Google map and their progress. The program can be done in C++," +
        " .net(C#) or nodewebkit or any other windows oriented program. The program will show the moving device progress on map." +
        "The PC application will update a mobile app (on iOS & Android) about each device's location via the internet/network. " +
        "The mobile app will simply show the mobile device on the PC application all tracking devices can be observed including " +
        "their progress.</p><p class='skills'>Skills: .NET, iPhone, Objective C, VB.NET, Windows Mobile</p></td>" +
        "<td class='date'><p>1.04.16</p></td><td class='members'><p>1/4</p></td></tr>");

        table += ("<tr><td class='project_name'><h3><a href='Project.html'>Write an iPhone application</a></h3>" +
        "<p class='description'>Marketplace. My app is simply for users who makes things at home and would like to sell it." +
        " Plus, those looking to buy things homemade.Specific required features are available and will be sent on request.</p>" +
        "<p class='skills'>Skills: Android, iPhone, Java</p></td>" +
        "<td class='date'><p>25.03.16</p></td><td class='members'><p>2/4</p></td></tr>");
    }
    table += "<tr><td colspan='3'><p id='left_arrow'><a href='#'><img class='arrow' src='img/left_arrow.png' width='15px' height='15px' alt=''>  Previos page</a></p>" +
             "<p id='right_arrow'><a href='#'>Next page  <img class='arrow' src='img/right_arrow.png' width='15px' height='15px' alt=''></a></p></td></tr>";

    table += "</table>";

    document.all.projects.innerHTML = table;
}