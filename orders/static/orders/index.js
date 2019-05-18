document.addEventListener('DOMContentLoaded', () => {

    //when users wants to add menu item to cart
    document.querySelector('#order').onsubmit = () => {

        //To do pick proper item
        var listitem = "pizza"
        const li = document.createElement('li');
        li.innerHTML = listitem;
        document.querySelector('#cartitemlist').append(li);
        return false;

    };
});