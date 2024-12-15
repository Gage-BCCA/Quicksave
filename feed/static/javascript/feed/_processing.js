const likeApiEndpoint = "/process-post-like/"
const dislikeApiEndpoint = "/process-post-dislike/"
const csrftoken = getCookie('csrftoken');

const messageBox = document.getElementById("message-box")

document.addEventListener("DOMContentLoaded", () => {
    const postLikeForms = document.getElementsByClassName("post-like-form")
    const postDislikeForms = document.getElementsByClassName("post-dislike-form")
    
    for (let form of postLikeForms){
        form.addEventListener("submit", async function (event) {

            // Stop the form
            event.preventDefault();

            // Gather the User ID and Post ID
            userId = form.getElementsByClassName("post-like-user-id")[0].value;
            postId = form.getElementsByClassName("post-like-post-id")[0].value;

            // Send request to the like endpoint
            let response = await fetch(likeApiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    'userId': userId,
                    'postId': postId
                })
            });

            let data = await response.json()
        });
    }

    for (let form of postDislikeForms){
        form.addEventListener("submit", async function (event) {

            // Stop the form
            event.preventDefault();

            // Gather the User ID and Post ID
            userId = form.getElementsByClassName("post-dislike-user-id")[0].value;
            postId = form.getElementsByClassName("post-dislike-post-id")[0].value;

            // Send request to the like endpoint
            let response = await fetch(likeApiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    'userId': userId,
                    'postId': postId
                })
            });

            let data = await response.json()
            console.log(data);
        })
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}