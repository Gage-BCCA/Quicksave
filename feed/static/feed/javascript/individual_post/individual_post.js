const addCommentForms = document.getElementsByClassName("add-comment-form");
const addCommentButtons = document.getElementsByClassName("post-footer__add-comment-container__button")


document.addEventListener("DOMContentLoaded", function (event){

    for (let button of addCommentButtons){
        button.addEventListener("click", function(event){
            console.log(this.dataset.referredPostId)
            for (let form of addCommentForms){
                if (form.dataset.referredPostId.localeCompare(this.dataset.referredPostId) == 0){
                    form.classList.toggle("add-comment-form--hidden");
                    break;
                }

            }
        });
    }
});