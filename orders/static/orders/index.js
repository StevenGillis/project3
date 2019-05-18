document.addEventListener('DOMContentLoaded', () => {
var cartlist = [];
    //when users wants to add menu item to cart
    document.querySelector('#order').onsubmit = () => {

        //To do pick proper item
        var listitem = "pizza";
        cartlist.push(listitem);
        console.log(cartlist);
        const li = document.createElement('li');
        li.innerHTML = listitem;
        document.querySelector('#cartitemlist').append(li);
        return false;
    };
    // Get the modal
        var modal = document.getElementById("myModal");

        // Get the button that opens the modal
        var btn = document.getElementById("myBtn");

        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks on the button, open the modal and show requested items
        btn.onclick = function() {
            modal.style.display = "block";
            const li = document.createElement('li');
            li.innerHTML = cartlist;
            document.querySelector('#itemoverviewconfirm').append(li);
        }


        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            //Clearn itenoverview
            //document.getElementById("#itemoverviewconfirm").innerHTML = "";
            modal.style.display = "none";
        }

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
          if (event.target == modal) {

            modal.style.display = "none";
          }
        }
});