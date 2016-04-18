window.fbAsyncInit = function() {
    FB.init({
        appId      : '809439472501449',
        xfbml      : true,
        version    : 'v2.5'
    });
};

/*FB.init({ appId: '809439472501449', status: true, cookie: true, xfbml : true });*/

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


function doLogin()
{
    FB.login
    (
        function(response)
        {
            if (response.session)
            {
                FB.api('/me',
                    function(response)
                    {
                        alert('Welcome ' + response.name);
                        alert('Full details: ' + JSON.stringify(response));
                    }
                );
            }
        } ,

        {perms:''}

    );
}