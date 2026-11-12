const checkin = document.getElementById("checkin");
const checkout = document.getElementById("checkout");

const today = new Date()

const tomorrow = new Date()
tomorrow.setDate(today.getDate() + 1)

const todayStr = today.toISOString().split("T")[0];
const tomorrowStr = tomorrow.toISOString().split("T")[0];

checkin.min = todayStr;
checkout.min = todayStr;
checkin.value = todayStr;
checkout.value = tomorrowStr;

checkin.addEventListener("change", () => {
  const next = new Date(checkin.value);
  next.setDate(next.getDate() + 1);
  checkout.min = next.toISOString().split("T")[0];

  if (checkout.value && checkout.value < checkout.min) {
    checkout.value = "";
  }
});