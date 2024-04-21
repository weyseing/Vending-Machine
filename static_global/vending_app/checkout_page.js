var paymentMethodDropdown = document.getElementById("payment_method");
var cashAmtInput = document.getElementById("container_cash_amt");

paymentMethodDropdown.addEventListener("change", function() {
    if (paymentMethodDropdown.value === "cash") {
        cashAmtInput.style.display = "block";
    } else {
        cashAmtInput.style.display = "none";
    }
});