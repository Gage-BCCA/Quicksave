const gameFollowApiEndpoint = "/process-follow-game/"

document.addEventListener("DOMContentLoaded", function(event){
    const gameFollowForms = document.getElementsByClassName("game-follow-form");
    for (let form of gameFollowForms){
        form.addEventListener("submit", async function(event){
            event.preventDefault();
            const userId = form.getElementsByClassName("game-form-user-id")[0].value;
            const gameId = form.getElementsByClassName("game-form-game-id")[0].value;

            let response = await fetch(gameFollowApiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    userId: userId,
                    gameId: gameId
                })
            });

            let data = await response.json();
            if ("Success" in data) {
                turnOffFollowButton()
            }
        });
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


function turnOffFollowButton() {
    let button = document.getElementById("follow-submit-btn");
    button.disabled = true;
    button.value = "Followed";
}