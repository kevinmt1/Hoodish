function add_to_cart(productId){
    var title = "radio_" + productId
    var size = document.querySelector('input[name="' + title + '"]:checked');
    var qty = document.getElementById("amount_" + productId).value;
    if (size == null)
    {
        alert("Choose a size!")
    }
    else
    {
        fetch('/add_to_cart', {
            method: 'POST',
            body: JSON.stringify({ productId: productId, size: size.value, qty: qty })
        }).then((_res) => {
            window.location.href = ""
        });
    }

}

function confirm_transaction(total_price){
    fetch('/confirm_transaction', {
        method: 'POST',
        body: JSON.stringify({ total_price: total_price })
    }).then((_res) => {
        window.location.href = ""
    });
}