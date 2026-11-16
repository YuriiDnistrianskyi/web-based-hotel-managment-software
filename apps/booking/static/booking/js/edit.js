const checkin = document.getElementById("id_check_in");
const checkout = document.getElementById("id_check_out");

const today = new Date()

const tomorrow = new Date()
tomorrow.setDate(today.getDate() + 1)

const todayStr = today.toISOString().split("T")[0];
const tomorrowStr = tomorrow.toISOString().split("T")[0];

checkin.min = todayStr;
checkout.min = tomorrowStr;

checkin.addEventListener("change", () => {
  const next = new Date(checkin.value);
  next.setDate(next.getDate() + 1);
  checkout.min = next.toISOString().split("T")[0];

  if (checkout.value && checkout.value < checkout.min) {
    checkout.value = checkout.min;
  }
});


