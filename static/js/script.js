// 1. Form Submit ayye mundu alert chupinchadaniki
document.addEventListener('DOMContentLoaded', function() {
    const orderForm = document.querySelector('form');
    
    if (orderForm) {
        orderForm.addEventListener('submit', function(event) {
            // User ni confirm cheyamani aduguthunnam
            let confirmOrder = confirm("Mee order details anni correct ena? Submit cheyala?");
            
            if (!confirmOrder) {
                // User 'Cancel' nokkithe, form submit avvadu
                event.preventDefault();
            }
        });
    }
});

// 2. Simple Welcome Message in Console
console.log("Paper Business Website Loaded Successfully!");