var output=document.getElementById('chat');
var form=document.getElementById('form');
var Auser=document.getElementById('loginuser').innerHTML;
function scrolls(){
    document.getElementById('chat').scrollTop+=document.getElementById('chat').scrollHeight;
};
function setusers(users){
    for(var i=0;i<users.length;i++){
        $('.online_users_box').append('<div class="onlineuser" style="padding:4px;" name="'+users[i]+'"><div style="padding:5px;text-transform:capitalize;" class="bg-danger">'+users[i]+'</div></div>');
    }    
}
function remuser(user){
    $('.onlineuser[name="'+user+'"]').hide();
}

                try{
			            var host='ws://'+window.location.hostname+":9000/Chat/";
                        console.log("Host:",host);
                        var s=new WebSocket(host);
                        s.onopen=function(e){
                                $('#logs').html("You Are Connected !");
                                s.send(Auser);
                                scrolls();
                        };
                        s.onclose=function(e){
                            $('#logs').html("You are offline !");
                        };

                        s.onmessage=function(e){
                                data = JSON.parse(e.data)
                                if(data.type == 'onlineusers'){
                                    setusers(data.users);
                                }
                                else if(data.type == 'remuser'){
                                    remuser(data.user);
                                }
                                else if(data.type == 'status'){
                                    document.getElementById('status').innerHTML=e.status; 
                                       
                                }
                                else if(data.type == 'othermsg'){
                                    $('#chat').append('<div class="chatbox bounceInUp" style="padding: 10px;width: 80%;position: relative;float: left;" name = "'+data.chatid+'">\
                                        <div class="" style="text-transform: capitalize;padding: 4px;background-color: black;color: white;border-radius:  2px 2px 0 0;font-weight: bold;">'+data.username+'</div>\
                                        <i class="fa fa-trash delete_chat" style="position: absolute;right: 15px;font-size: 24px;cursor: pointer;"  chatid="'+data.chatid+'"></i>\
                                        <div style="background-color: #fff;border-radius: 0 0 2px 2px;padding: 8px;"><span style="font-size: 150%;">'+data.message+'</span><div style="text-align:right;font-size:80%">'+Date().substr(0,25)+'</div></div>\
                                    </div>');    
                                    scrolls();
                                }
                                else if(data.type == 'minemsg'){
                                    $('#chat').append('<div class="chatbox bounceInUp" style="padding: 10px;width: 80%;float: right;position: relative;" name="'+data.chatid+'">\
                                            <i class="fa fa-trash delete_chat" style="position: absolute;right: 15px;font-size: 24px;cursor: pointer;" chatid="'+data.chatid+'"></i>\
                                        <div style="background-color: #25D366;border-radius: 2px;padding: 8px;"><span style="font-size: 150%;">'+data.message+'</span><div style="text-align:right;font-size:80%">'+Date().substr(0,25)+'</div></div>\
                                    </div>');
                                    scrolls();    
                                }
                        };
                        s.error=function(e){
                                console.log('Socket Error: ',e);
                        };
                       
                }
                catch(ex){
                        console.log('Socket Exception:',ex);
                }

                form.addEventListener('submit',function(e){
                        e.preventDefault();
                        if($('.msg_input').val()!=""){
                                s.send(
                                    JSON.stringify({
                                        'username':Auser,
                                        'message':$('.msg_input').val()
                                }));
                                $('.msg_input').val("");
                        }
                },false);
                 function status(id){ 
                         if(id){
                               s.send(JSON.stringify({
                                    'type':'status',
                                    'status': Auser+' is Typing message .....',
                                }));
                        }
                };

$('#chat').on('click', '.delete_chat', function(){
    if(confirm("Are you sure?")){
        var chatid = $(this).attr('chatid');
        $.ajax({
            url:'/delete_chat/',
            method:'POST',
            data:{
                'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
                'chatid': chatid,
            },
        }).done(function(){
            $('.chatbox[name="'+chatid+'"]').hide();
        }).fail(function(){
            console.log('ERROR 45784547');
        });
    }
});
