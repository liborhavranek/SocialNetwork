
    $("#add-post-form").submit(function(event) {
        event.preventDefault();
        // make ajax request here
        $.ajax({
            url: '', // put your url here
            type: 'POST',
            data: $("#add-post-form").serialize(),
            success: function(response) {
                var newPost = "<div class='row justify-content-center mt-5'>" +
                "<div class='col-md-5 col-sm-12 text-start border-bottom position-relative'>"+
                "<p><strong>" + response.post_author+ "</strong>" + ' now' +"</p>" +
                                  "<p>"+response.new_post+"</p>"+
                                  "<a class='stretched-link' href='#'></a>"+
                              "</div>" + "</div>";
                $('.post-list').prepend(newPost);
                $("#add-post-form").trigger("reset");
            }
        });
    });


