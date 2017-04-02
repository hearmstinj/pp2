jQuery(document).ready(function(){
    var voted=0;
    $('.single-toplist button').click(function(){
        var button=$(this);
        var url=$(this).data('link');
        var id=$(this).data('id');
        $(this).button('loading');
        window.open(url);
        checkVoteStatus(id,button);
    });
    function checkVoteStatus(id,button){
        $.ajax({
            url:'/vote/check-voted',
            method:'POST',
            data:{id:id},
            error:function(data){},
            success:function(data){
                console.log(data);
                if(data.voted==false){
                    setTimeout(function(){
                        checkVoteStatus(id,button);
                    },3000);
                }
                else if(data.voted==true){
                    button.html(button.data('done-text'));
                    voted++;
                }
            }
        });
    }
    $('#claim-form').submit(function(){
        var username=$('#vote-username').val();
        $.ajax({
            url:'/vote/claim',
            method:'POST',
            data:{username:username},
            success:function(data){
                console.log(data);
                triggerNotification(data.message)
            }
        });
        return false;
    });
    function triggerNotification(message){
        $('#modal-message').html(message);$('#notification-modal').modal('show');
    }
});
