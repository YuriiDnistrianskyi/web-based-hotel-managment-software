const checkin = document.getElementById("checkin");
const checkout = document.getElementById("checkout");

const today = new Date().toISOString().split("T")[0];
checkin.min = today;

checkin.addEventListener("change", () => {
  const next = new Date(checkin.value);
  next.setDate(next.getDate() + 1);
  checkout.min = next.toISOString().split("T")[0];

  if (checkout.value && checkout.value < checkout.min) {
    checkout.value = "";
  }
});