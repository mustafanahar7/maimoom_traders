// document.addEventListener("DOMContentLoaded", () => {
//   const quantityInputs = document.querySelectorAll(".quantity-input");
//   const grandTotalElement = document.getElementById("grand-total");

//   function updateTotalPrice() {
//     let grandTotal = 0;

//     quantityInputs.forEach((input) => {
//       const price = parseFloat(input.getAttribute("data-price"));
//       const quantity = parseFloat(input.value);
//       const itemTotalPrice = price * quantity;
//       input
//         .closest(".cart-item")
//         .querySelector(
//           ".item-total-price"
//         ).textContent = `$${itemTotalPrice.toFixed(2)}`;
//       grandTotal += itemTotalPrice;
//     });

//     grandTotalElement.textContent = grandTotal.toFixed(2);
//   }

//   quantityInputs.forEach((input) => {
//     input.addEventListener("input", updateTotalPrice);
//   });

//   updateTotalPrice(); // Initialize total price on page load
// });

